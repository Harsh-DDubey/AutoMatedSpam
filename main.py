import os
from dotenv import load_dotenv
from hydrogram import Client, filters
from hydrogram.types import Message

# Load environment variables from .env file
load_dotenv()

#Define Client
app = Client(
    "pro",
    api_hash=os.getenv("API_HASH"),
    api_id=int(os.getenv("API_ID")),
    session_string=os.getenv("SESSION_STRING")
)

TARGET_GROUP_ID = int(os.getenv("TARGET_GROUP_ID"))

@app.on_message(filters.chat(TARGET_GROUP_ID) & filters.dice)
async def send(c: Client, m: Message):
    if m.chat.id == TARGET_GROUP_ID:
        await c.send_dice(TARGET_GROUP_ID, "🎲")

if __name__ == "__main__":
    print("Bot started...")
    app.run()
