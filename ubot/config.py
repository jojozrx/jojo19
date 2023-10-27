import os

from dotenv import load_dotenv

load_dotenv(".env")

DEVS = [
    1054295664, # keenan
    2104193674, # joo
    482945686, # keenan
    1373744866, # gutama
]

KYNAN = list(map(int, os.getenv("KYNAN", "2104193674").split()))

API_ID = int(os.getenv("API_ID", "22922722"))

API_HASH = os.getenv("API_HASH", "ca54b24ac46dae3da2bfc2ac1a65e507")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6492826894:AAFKwMqU4IztDyWJNrJgS-H_lXvZKl1kZHw")

OWNER_ID = int(os.getenv("OWNER_ID", "2104193674"))

USER_ID = list(map(int, os.getenv("USER_ID", "2104193674").split()))

LOG_UBOT = int(os.getenv("LOG_UBOT", "-4018158982"))

LOG_SELLER = int(os.getenv("LOG_SELLER", "-4082776190"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001608847572 -1001538826310 -1001876092598 -1001864253073 -1001451642443 -1001825363971 -1001797285258 -1001927904459 -1001287188817 -1001812143750 -1001608701614 -1001473548283 -1001861414061").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "25"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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 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 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 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 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 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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://jojo:jojo@cluster0.kkrdltk.mongodb.net/?retryWrites=true&w=majority",
)
