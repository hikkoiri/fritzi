from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.Fritzi import Fritzi

router = APIRouter(prefix='/api/v1', tags=['api_v1'])
fritzi = Fritzi()

@router.get("/landevices", response_class=JSONResponse)
async def list_lan_devices(ipPrefix: str | None = None, active: bool | None = None):
    """List all LAN devices in the network, which match the optional filters."""    
    devices = await fritzi.list_devices()

    if active is not None:
        devices = [device for device in devices if device.get('active') == active]

    if ipPrefix is not None:
        devices = [device for device in devices if device.get('ip').startswith(ipPrefix)]

    return JSONResponse(content=devices)

