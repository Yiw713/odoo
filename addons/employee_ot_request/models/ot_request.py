from odoo import models, fields, api
from odoo.exceptions import UserError
import pytz
from datetime import datetime, timedelta

class HrOtRequest(models.Model):
    _name = 'hr.ot.request'
    _description = 'Overtime Request'
    _inherit = ['mail.thread', 'mail.activity.mixin'] # เพิ่มระบบ Tracking ด้านล่างฟอร์ม

    name = fields.Char(string='เลขที่คำขอ', required=True, copy=False, readonly=True, default='New')
    employee_id = fields.Many2one('hr.employee', string='พนักงาน', required=True, default=lambda self: self.env.user.employee_id)
    date = fields.Date(string='วันที่ต้องการทำ OT', required=True, default=fields.Date.context_today)
    hours = fields.Float(string='จำนวนชั่วโมง', required=True)
    reason = fields.Text(string='เหตุผล/งานที่ทำ')
    
    state = fields.Selection([
        ('draft', 'ร่าง'),
        ('submitted', 'รออนุมัติ'),
        ('approved', 'อนุมัติแล้ว'),
        ('rejected', 'ปฏิเสธ')
    ], string='สถานะ', default='draft', tracking=True)

    manager_id = fields.Many2one('hr.employee', string='ผู้อนุมัติ', related='employee_id.parent_id', readonly=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('hr.ot.request') or 'New'
        return super().create(vals_list)

    def action_submit(self):
        for record in self:
            # ดึง Timezone ของผู้ใช้งาน (ถ้าไม่มีให้ใช้ Asia/Bangkok)
            user_tz = pytz.timezone(self.env.user.tz or 'Asia/Bangkok')
            current_time = datetime.now(pytz.utc).astimezone(user_tz)

            # เช็คเงื่อนไข: ห้ามขอ OT ย้อนหลัง
            if record.date < current_time.date():
                raise UserError("ไม่สามารถส่งคำขอ OT ย้อนหลังได้")

            # เช็คเงื่อนไข: ถ้าขอ OT สำหรับวันนี้ ต้องส่งก่อน 14:00 น.
            if record.date == current_time.date():
                if current_time.hour >= 14:
                    raise UserError("เลยกำหนดเวลา! ไม่อนุญาตให้ส่งคำขอ OT สำหรับวันนี้หลังเวลา 14:00 น.")
            
            record.state = 'submitted'

    def action_approve(self):
        # 1. ค้นหาประเภทเวลาทำงาน (Work Entry Type) ที่ใช้รหัส 'OVERTIME'
        # *หมายเหตุ: คุณต้องไปสร้าง Work Entry Type รหัส OVERTIME ไว้ในตั้งค่าของ Odoo ก่อน
        ot_work_entry_type = self.env['hr.work.entry.type'].search([('code', '=', 'OVERTIME')], limit=1)
        
        if not ot_work_entry_type:
            raise UserError("ไม่พบประเภทเวลาทำงาน 'OVERTIME' ในระบบ! กรุณาไปตั้งค่า Work Entry Type ก่อนใช้งาน")

        # 2. สร้าง Work Entry ให้พนักงาน
        for record in self:
            # ระบบ Work Entry ของ Odoo บังคับใช้เป็นวันเวลา (Datetime) 
            # แต่ฟอร์มเรามีแค่วันที่ (Date) และจำนวนชั่วโมง (Float)
            # สมมติฐาน: ให้ OT เริ่มนับตอน 17:30 น. ของวันที่ขอ (คุณสามารถนำไปประยุกต์เปลี่ยนเป็นฟิลด์ให้พนักงานกรอกเวลาเริ่ม-จบได้ในอนาคต)
            
            user_tz = pytz.timezone(self.env.user.tz or 'Asia/Bangkok')
            
            # กำหนดเวลา 17:30 น. ใน Timezone ของผู้ใช้
            local_start_dt = user_tz.localize(datetime.combine(record.date, datetime.min.time()) + timedelta(hours=17, minutes=30))
            
            # แปลงเป็น UTC ก่อนบันทึกลง Database (Odoo เก็บเวลาเป็น UTC เสมอ)
            utc_start_dt = local_start_dt.astimezone(pytz.utc).replace(tzinfo=None)
            
            # คำนวณเวลาสิ้นสุด จากจำนวนชั่วโมงที่ขอ OT
            utc_stop_dt = utc_start_dt + timedelta(hours=record.hours)

            # สั่งสร้าง Work Entry
            self.env['hr.work.entry'].create({
                'name': f'OT Approved: {record.employee_id.name} - {record.name}',
                'employee_id': record.employee_id.id,
                'work_entry_type_id': ot_work_entry_type.id,
                'date_start': utc_start_dt,
                'date_stop': utc_stop_dt,
                'company_id': record.employee_id.company_id.id,
                'state': 'draft', # หรือจะให้เป็น 'validated' เลยก็ได้
            })
            
            # 3. เปลี่ยนสถานะเป็นอนุมัติ
            record.write({'state': 'approved'})

    def action_reject(self):
        self.write({'state': 'rejected'})

    def action_draft(self):
        self.write({'state': 'draft'})