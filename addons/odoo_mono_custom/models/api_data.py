from odoo import models, fields, api
import requests
from requests.auth import HTTPBasicAuth


class MonoAPIData(models.Model):
    _name = 'mono.api.data'
    _description = 'Mono API Data'
    _order = 'timestamp desc'

    vehicle_id = fields.Char()
    vehicle_name = fields.Char()
    timestamp = fields.Datetime()
    speed = fields.Float()
    status = fields.Char()
    engine_status = fields.Char()

    def fetch_api_data(self):
        url = "https://api-realtime.monogps.com/api/getrealtime/5307"

        response = requests.get(
            url,
            auth=HTTPBasicAuth("mono-realtime", "#M0ng0Realt!me%Ap!"),
            timeout=20
        )

        if response.status_code == 200:
            data = response.json()

            for item in data:
                existing = self.search(
                    [('vehicle_id', '=', item.get('vehicle_id'))],
                    limit=1
                )

                values = {
                    'vehicle_id': item.get('vehicle_id'),
                    'vehicle_name': item.get('vehicle_name'),
                    'timestamp': item.get('timestamp'),
                    'speed': item.get('speed'),
                    'status': item.get('status'),
                    'engine_status': item.get('engine_status'),
                }

                if existing:
                    existing.write(values)
                else:
                    self.create(values)

    # Smart Button action
    def action_refresh(self):
        self.fetch_api_data()

        return {
        'type': 'ir.actions.client',
        'tag': 'display_notification',
        'params': {
            'title': 'Success',
            'message': 'API Data saved successfully',
            'type': 'success',
            'sticky': False,
        }
    }