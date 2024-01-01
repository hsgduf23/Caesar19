import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5986064594:AAGMa2CGvJr1sAIfePQJlyXUc4jpjiohXSc")

    APP_ID = int(os.environ.get("APP_ID", 11511974))

    API_HASH = os.environ.get("API_HASH", "0ab433dff1310e9728169d1f1cd1c1f2")
