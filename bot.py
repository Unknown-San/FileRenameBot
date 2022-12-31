import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
import os

if bool(os.environ.get("WEBHOOK", False)):
    from config import Config

import pyrogram



if __name__ == "__main__" :
    if not os.path.isdir(config.DOWNLOAD_LOCATION):
        os.makedirs(config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "RenameBot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    Config.AUTH_USERS.add(861055237)
    app.run()
