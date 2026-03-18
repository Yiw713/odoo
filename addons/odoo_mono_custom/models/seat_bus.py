from odoo import models, fields
from odoo.exceptions import UserError
import pymysql


class MonoSeatBus(models.Model):
    _name = 'mono.seat.bus'
    _description = 'Seat Bus Status'
    _order = 'ts desc'

    ts = fields.Datetime("Timestamp")
    passenger = fields.Integer("Passenger")

    imei = fields.Char("IMEI")
    car_plate_number = fields.Char("Car Plate")

    # Seat 1-40
    seat1 = fields.Boolean()
    seat2 = fields.Boolean()
    seat3 = fields.Boolean()
    seat4 = fields.Boolean()
    seat5 = fields.Boolean()
    seat6 = fields.Boolean()
    seat7 = fields.Boolean()
    seat8 = fields.Boolean()
    seat9 = fields.Boolean()
    seat10 = fields.Boolean()
    seat11 = fields.Boolean()
    seat12 = fields.Boolean()
    seat13 = fields.Boolean()
    seat14 = fields.Boolean()
    seat15 = fields.Boolean()
    seat16 = fields.Boolean()
    seat17 = fields.Boolean()
    seat18 = fields.Boolean()
    seat19 = fields.Boolean()
    seat20 = fields.Boolean()
    seat21 = fields.Boolean()
    seat22 = fields.Boolean()
    seat23 = fields.Boolean()
    seat24 = fields.Boolean()
    seat25 = fields.Boolean()
    seat26 = fields.Boolean()
    seat27 = fields.Boolean()
    seat28 = fields.Boolean()
    seat29 = fields.Boolean()
    seat30 = fields.Boolean()
    seat31 = fields.Boolean()
    seat32 = fields.Boolean()
    seat33 = fields.Boolean()
    seat34 = fields.Boolean()
    seat35 = fields.Boolean()
    seat36 = fields.Boolean()
    seat37 = fields.Boolean()
    seat38 = fields.Boolean()
    seat39 = fields.Boolean()
    seat40 = fields.Boolean()

    def action_sync_seat_bus(self):

        connection = pymysql.connect(
            host='8.213.196.146',
            port=3306,
            user='dev-hw',
            password='@$!lpLHODev',
            database='db-hw',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM seat_bus_status ORDER BY ts DESC LIMIT 100")
                rows = cursor.fetchall()

                for row in rows:
                    self.create({
                        'ts': row.get('ts'),
                        'passenger': row.get('passenger'),
                        'imei': row.get('imei'),
                        'car_plate_number': row.get('car_plate_number'),

                        **{f"seat{i}": bool(row.get(f"seat{i}", 0)) for i in range(1, 41)}
                    })

        finally:
            connection.close()

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Success',
                'message': 'Seat Bus Data Synced',
                'type': 'success',
            }
        }