# Copyright 2025 Harsh Dhar Dubey
# Licensed under the Apache License, Version 2.0
#
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.


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
    await c.send_dice(TARGET_GROUP_ID, "🎲")

if __name__ == "__main__":
    print("Bot started...")
    app.run()
