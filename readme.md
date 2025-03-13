<p align="center">
  <img src="carlo.jpg" alt="AutoMatedSpam Banner" width="500"/>
</p>

# AutoMatedSpam - A Telegram Dice Bot 🎲  

A powerful **Telegram userbot** that **automatically rolls a dice** 🎲 whenever someone sends a dice in a specific group. Built with **Hydrogram**, this bot is **fast, efficient, and easy to set up**.  

---

## 📊 GitHub Stats  

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Harsh-DDubey&show_icons=true&theme=radical" alt="GitHub Stats" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Harsh-DDubey&layout=compact&theme=radical" alt="Top Languages" />
</p>

---

## ❄️ Features  
1⃣ **Auto-detects dice rolls** in a group and instantly replies with another dice 🎲  
2⃣ **Easy setup & deployment** with simple commands  
---


---
## Session String Generator  
To run this bot, you need a **Telegram session string**. Use my **SessionString** repository to generate one easily:  

[**SessionString Repo**](https://github.com/Harsh-DDubey/StringSession)  

Follow the instructions in the repository to generate your session string and use it in the `.env` file.  

---

## ⚒️ Installation & Setup  

### Installation on PC/Linux  
First, **clone the repository** and navigate to the project directory:  
```sh
git clone https://github.com/Harsh-DDubey/AutoMatedSpam.git  
cd AutoMatedSpam  
```  

Next, **install dependencies** using:  
```sh
pip install -r requirements.txt  
```  

Now, **create a `.env` file** in the project folder and add:  
```
API_HASH=your_api_hash  
API_ID=your_api_id  
SESSION_STRING=your_session_string  
TARGET_GROUP_ID=your_target_group_id  
```  

Finally, **run the bot** with:  
```sh
python main.py  
```  
---

### Installation on Termux  
If you are using Termux, follow these steps:  

1. **Update and install dependencies:**  
```sh
pkg update && pkg upgrade -y  
pkg install python git -y  
pip install --upgrade pip  
```

2. **Clone the repository and navigate to it:**  
```sh
git clone https://github.com/Harsh-DDubey/AutoMatedSpam.git  
cd AutoMatedSpam  
```

3. **Install required Python packages:**  
```sh
pip install -r requirements.txt  
```

4. **Set up environment variables:**  
```sh
echo "API_HASH=your_api_hash" > .env  
echo "API_ID=your_api_id" >> .env  
echo "SESSION_STRING=your_session_string" >> .env  
echo "TARGET_GROUP_ID=your_target_group_id" >> .env  
```

5. **Run the bot:**  
```sh
python main.py  
```

---

## 🌿 How It Works?  
1⃣ A user **sends a 🎲 dice** in the target group.  
2⃣ The bot **detects it** and **instantly replies** with another dice.  

---

## 🍂 Built With  
- [Hydrogram](https://pypi.org/project/hydrogram/) - Asynchronous Telegram Client  
- [Python](https://www.python.org/) - Programming Language  
- [dotenv](https://pypi.org/project/python-dotenv/) - Environment Variable Loader  

---

## 📈 Contribution Graph  

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=Harsh-DDubey&theme=github" alt="GitHub Activity Graph" />
</p>

---

## 📌 License  
This project is open-source and available under the Apache License 2.0.
---

## 💬 Contact  
Have questions? Reach out to me on Telegram!  
📩 **[Harsh-DDubey](https://t.me/Dev_HarshD)**  

---

🌟 **Star the repo** if you like this bot!

