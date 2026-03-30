from odoo import http
from odoo.http import request

class DashboardController(http.Controller):

    @http.route('/crm/dashboard/data', type='jsonrpc', auth='user')
    def dashboard_data(self):
        model = request.env['crm.dashboard']

        return {
            'kpi': model.get_kpi(),
            'chart': model.get_chart(),
            'activity': model.get_sales_activity(),
            'funnel': model.get_funnel(),
        }