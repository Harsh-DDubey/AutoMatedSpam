from hydrogram import Client, filters
from hydrogram.types import Message
app = Client(
    "pro",
    api_hash="",
    api_id=,
    session_string=""
)

TARGET_GROUP_ID = 
@app.on_message(filters.chat(TARGET_GROUP_ID) & filters.dice)
async def send(c: Client, m: Message):
    if m.chat.id==TARGET_GROUP_ID:
        await c.send_dice(TARGET_GROUP_ID,"🎲")
    else:
        pass

if __name__ == "__main__":
    print("Bot started...")
    app.run()

