# fritzi

- [fritzi](#fritzi)
  - [Goal](#goal)
  - [Security \& Safety](#security--safety)
  - [Development](#development)
    - [Install dependencies](#install-dependencies)
    - [Configuration](#configuration)
    - [Run](#run)
    - [Test](#test)
  - [Deployment](#deployment)
    - [systemd service](#systemd-service)
  - [References](#references)


## Goal
Provide an easy-to-use REST interfaces for FRITZ!Box routers.

## Security & Safety
> As always the same principle applies: Don't do anything stupid.

Right now only one endpoint is implemented: `ListDevices` to get more transparency about devices connected to your home network (read-only).

If you intend to further extend the scope of functionalities (especially looking at writing and destructive actions), be sure about what you are going to do and how to protect this service and network against unauthorised access.


## Development 
### Install dependencies

```bash
python3 -m venv ./venv
source ./venv/bin/activate

pip3 install -r requirements.txt
```

### Configuration
This service makes use of the [python-dotenv](https://pypi.org/project/python-dotenv/) library. On startup following configurations will be pulled from the `.env` configuration file:
```
USERNAME=fritzxyz
PASS=password123
URL=http://10.0.0.1  
```

> Remember to never checkin those credentials to git.

### Run

```bash
python3 main.py
```

### Test

Open `http://localhost:8001/docs` to Swagger interface or `http://localhost:8001/redoc` for Redocly interface.

## Deployment
### systemd service

You can simply run this as Linux service. Adapt the template file `fritzi.service` and store it in the right location:

```bash
sudo nano /etc/systemd/system/fritzi.service
#enter systemd file content
sudo systemctl --system daemon-reload
sudo systemctl enable fritzi
sudo systemctl start fritzi
sudo systemctl status fritzi
```

## References

- [AVM developer documentation](https://avm.de/service/schnittstellen/) -> Also includes the source code to get a valid SID token: `src/Auth.py`