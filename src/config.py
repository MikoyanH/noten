# import os
# from dotenv import load_dotenv

# load_dotenv()

# BOT_TOKEN = os.getenv("BOT_TOKEN")
# ADMIN_ID = int(os.getenv("ADMIN_ID"))
# USE_REDIS = os.getenv("USE_REDIS", "False").lower() == "true"

# # Если хочешь сделать по красоте — можешь потом вынести это в pydantic.BaseSettings, но пока так проще и быстрее.


import os
from dotenv import load_dotenv


# Загружаем нужный .env
# ENV = os.getenv("ENV", "prod")
# env_file = ".env.dev" if ENV == "dev" else ".env"
# load_dotenv(env_file)

BOT_TOKEN = os.getenv("BOT_TOKEN")
