# (c) @EverythingSuckz | @AbirHasan2005

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = 561279
    API_HASH = "cc3529e1a07ac281b09fdda091a7899e"
    BOT_TOKEN = "1123852269:AAHPbBr4yvlCed3VMV_BCC06kjgphx80USg"
    SESSION_NAME = "File2Link"
    SLEEP_THRESHOLD = 60
    WORKERS = 4
    BIN_CHANNEL = 552073351
    PORT = 5001
    BIND_ADRESS = '0.0.0.0'
    OWNER_ID = 512025730
    NO_PORT = False
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU else APP_NAME+'.herokuapp.com'
    DATABASE_URL = str(getenv('DATABASE_URL'))
    UPDATES_CHANNEL = "None"
    BANNED_CHANNELS = list(set(int(x) for x in str("-1001362659779").split()))
