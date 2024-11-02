from datetime import datetime
from dotenv import load_dotenv
import os
import httpx
from src.Auth import get_sid

class Fritzi:
    
    validity_timeout = 20 #in minutes

    def __init__(self):
        load_dotenv()
        missing_vars = [var for var in ['USERNAME', 'PASS', 'URL'] if not os.getenv(var)]
        if missing_vars:
            raise EnvironmentError(f"Required environment variables {', '.join(missing_vars)} are not set.")
        self.user = os.getenv('USERNAME')
        self.password = os.getenv('PASS')
        self.url = os.getenv('URL')
        self.get_token()
        
    
    def get_token(self):
        if not hasattr(self, 'token') or self.token is None:
            print("no token found, fetching a new one")
            self.refresh_token()

        if (datetime.now() - self.lastUpdate).total_seconds() > self.validity_timeout * 60:
            print("token expired, fetching a new one")
            self.refresh_token()
        return self.token
    
    def refresh_token(self):
        self.token = get_sid(self.url, self.user, self.password)
        self.lastUpdate = datetime.now()

    async def list_devices(self):
        async with httpx.AsyncClient() as client:
            headers = {
                'Authorization': f'AVM-SID {self.get_token()}'
            }
            external_response = await client.get(f"{self.url}/api/v0/landevice", headers=headers)
            external_response.raise_for_status() 
            return self.thin_out(external_response.json())

    def thin_out(self,input: any):
        devices = input['landevice']
        thinned_out = []
        for device in devices:
            thinned_device = {
            'uid': device.get('UID'),
            'ip': device.get('ip'),
            'active': device.get('active') == '1',
            'friendly_name': device.get('friendly_name')
            }
            thinned_out.append(thinned_device)
        return thinned_out