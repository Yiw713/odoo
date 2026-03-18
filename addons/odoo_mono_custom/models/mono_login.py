from odoo import models, fields
from odoo.exceptions import UserError
import requests
import logging

_logger = logging.getLogger(__name__)


class MonoLoginWizard(models.TransientModel):
    _name = 'mono.login.wizard'
    _description = 'Mono API Login Wizard'

    username = fields.Char(required=True)
    password = fields.Char(required=True)

    def action_login(self):
        url = "http://ops.monogps.com/api/signin"

        try:
            payload = {
                "username": self.username,
                "password": self.password
            }

            response = requests.post(
                url,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=20
            )

            _logger.warning("MONO STATUS: %s", response.status_code)
            _logger.warning("MONO RESPONSE TEXT: %s", response.text)

            if response.status_code != 200:
                raise UserError(
                    f"Login Failed\n"
                    f"Status: {response.status_code}\n"
                    f"Response: {response.text}"
                )

            result = response.json()

            if result.get("success") != "success":
                raise UserError(f"Login Failed.\nResponse: {result}")

            user_data = result.get("user", {})

            self.env.user.write({
                'mono_user_id': user_data.get("id"),
                'mono_user_name': user_data.get("name"),
            })

            return {
    'type': 'ir.actions.act_window',
    'name': 'Mono System',
    'res_model': 'mono.api.data',   # 👈 model หน้า mono ของคุณ
    'view_mode': 'tree,form',
    'target': 'current',
}

        except requests.exceptions.RequestException as e:
            raise UserError(f"Connection Error: {str(e)}")

        except Exception as e:
            raise UserError(f"Unexpected Error: {str(e)}")