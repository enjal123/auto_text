# 📬 Auto Text



Your own personal daily briefing bot — delivered straight to Telegram.

Sign up on the website with your name, the cities you care about, and the countries you want news from. Every day, Auto Text automatically checks the weather and pulls the latest headlines for you, then texts it all to you on Telegram. No apps to open, no scrolling — it just shows up in your chat.

---

## ✨ What it actually does

1. You sign up on the **website** and tell it your cities + countries.
2. Your info gets saved to a **Firebase** database.
3. A **Python script** runs once a day, loops through every signed-up user, and:
   - Grabs the weather for their chosen cities
   - Grabs the top news for their chosen countries
   - Sends it all as one neat message to their **Telegram**
4. You open Telegram and there's your daily update, waiting for you. ☀️📰

<img width="800" height="610" alt="image" src="https://github.com/user-attachments/assets/b858fb71-323b-4c63-ada8-bea32904bf24" />

---

## 🧩 What's in this repo

| File | What it does |
|---|---|
| `index.html`, `style.css`, `script.js` | The signup website — where users enter their info |
| `dashboard.html`, `dashboard.js` | The dashboard where users can view/manage their info |
| `main.py` | The main script — loops through every user in the database and sends them their update |
| `sms_handler.py` | A simpler standalone script for sending a single update to one user |
| `weather.py` | Fetches weather info for a given city |
| `news_engine.py` | Fetches news headlines for given countries |
| `requirements.txt` | Python packages you need installed |
| `.github/workflows` | Automation so `main.py` can run on a schedule (e.g. every morning) automatically |

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/enjal123/auto_text.git
cd auto_text
```

### 2. Install the Python requirements

```bash
pip install -r requirements.txt
```

### 3. Set up Firebase

This project uses **Firebase Firestore** to store users and their preferences.

1. Go to the [Firebase Console](https://console.firebase.google.com/) and create a project.
2. Enable **Firestore Database**.
3. Go to **Project Settings → Service Accounts → Generate new private key**.
4. Save the downloaded file in the root of this project as:
   ```
   serviceAccountKey.json
   ```
   > ⚠️ Never commit this file to GitHub — it's basically the password to your database. Add it to `.gitignore`.

### 4. Create your Telegram bot

Auto Text sends messages *through* a Telegram bot that you create and own.

1. Open Telegram and search for **[@BotFather](https://t.me/BotFather)**.
2. Start a chat with it and send `/newbot`.
3. Give your bot a name and a username (must end in "bot", like `MyAutoTextBot`).
4. BotFather will reply with a **bot token** — a long string of letters and numbers. That's your `TELEGRAM_API` value.

### 5. Get your Telegram User ID

To send *you* a message, the bot needs to know your personal Telegram Chat ID (not your username). Here's the easy way to find it:

1. Open Telegram and search for **[@userinfobot](https://t.me/userinfobot)**.
2. Tap **Start** (or send any message to it).
3. It'll instantly reply with your info — look for the line that says:
   ```
   Id: 123456789
   ```
4. That number is your **Telegram Chat ID**. Copy it — you'll need it when you sign up on the website (or in your `.env` file if you're testing with `sms_handler.py`).

> 💡 One important last step: go find the bot you just created in step 4 and tap **Start** on it too. Telegram bots can only message people who have started a conversation with them first — if you skip this, your updates won't come through!

### 6. Set your environment variables

Create a `.env` file (or set these in your hosting platform / GitHub Actions secrets):

```
TELEGRAM_API=your_bot_token_from_botfather
TELEGRAM=your_personal_chat_id_from_userinfobot
```

*(`main.py` pulls each user's chat ID from Firestore automatically — the `TELEGRAM` variable above is only needed if you're running the simpler `sms_handler.py` script for yourself.)*

### 7. Run it

To open the signup website, just open `index.html` in your browser (or host it wherever you like).

To manually trigger a round of updates for every signed-up user:

```bash
python main.py
```

To send yourself a quick one-off test update:

```bash
python sms_handler.py
```

### 8. Automate it (optional)

The `.github/workflows` folder is already set up so `main.py` can run automatically on a schedule using GitHub Actions — so once it's configured, everyone gets their update every morning without you lifting a finger. Just make sure your `TELEGRAM_API` and Firebase credentials are added as **repository secrets**.

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python
- **Database:** Firebase Firestore
- **Messaging:** Telegram Bot API
- **Weather:** PyOWM + Geopy
- **News:** NewsAPI / NewsData API
- **Automation:** GitHub Actions

---

## 🙋 Quick Troubleshooting

- **Not getting messages?** Make sure you tapped "Start" on your own bot in Telegram — bots can't message you first.
- **Wrong chat ID?** Double-check the number from @userinfobot matches exactly what you entered on the signup site (no spaces, no extra characters).
- **Weather/news missing?** Check that your API keys for OpenWeatherMap and your news provider are valid and set as environment variables.
