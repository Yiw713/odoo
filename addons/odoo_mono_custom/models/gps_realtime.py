from odoo import models, fields, api
import requests
from requests.auth import HTTPBasicAuth


class GpsRealtime(models.Model):
    _name = 'gps.realtime'
    _description = 'GPS Realtime Data'
    _order = 'timestamp desc'

    vehicle_id = fields.Char("Vehicle ID")
    vehicle_name = fields.Char("Vehicle Name")
    gps_id = fields.Char("GPS ID")
    province = fields.Char("Province")
    timestamp = fields.Datetime("Timestamp")
    speed = fields.Float("Speed")
    mileage = fields.Float("Mileage")
    lat = fields.Float("Latitude")
    lng = fields.Float("Longitude")
    fuel_percent = fields.Float("Fuel %")
    engine_status = fields.Char("Engine Status")
    status = fields.Char("Status")
    location_name = fields.Char("Location")

    def fetch_gps_data(self):
        url = "https://api-realtime.monogps.com/api/getrealtime/14134"

        response = requests.get(
            url,
            auth=HTTPBasicAuth("Test", "Test"),
            timeout=20
        )

        if response.status_code == 200:
            data = response.json()

            for item in data:
                self.create({
                    'vehicle_id': item.get('vehicle_id'),
                    'vehicle_name': item.get('vehicle_name'),
                    'gps_id': item.get('gps_id'),
                    'province': item.get('province_en'),
                    'timestamp': item.get('timestamp'),
                    'speed': item.get('speed'),
                    'mileage': item.get('mileage'),
                    'lat': item.get('lat'),
                    'lng': item.get('lng'),
                    'fuel_percent': item.get('fuel_percent'),
                    'engine_status': item.get('engine_status'),
                    'status': item.get('status'),
                    'location_name': item.get('location_name'),
                })