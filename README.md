```markdown
# 🧠 Bar-On Emotional Quotient (EQ) Telegram Bot

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/platform-Telegram-blue)](https://telegram.org)

An advanced, user-friendly Telegram bot designed to conduct the standard **Bar-On Emotional Quotient (EQ) Test** featuring 90 specialized questions in Persian. The bot seamlessly collects demographic data (age and gender) post-test, automatically calculates the scoring metrics, and delivers an immediate statistical interpretation to the user.

---

## 🚀 Key Features

* **Comprehensive Assessment:** Fully integrates all 90 standard Bar-On EQ test questions with precise Persian translations.
* **Interactive UX:** Core survey utilizing Telegram `Inline Keyboards` (buttons 1 to 5) for a smooth and fast user response flow.
* **State Management:** Temporarily caches answers securely during the active session, avoiding data cross-talk between concurrent users.
* **Demographic Metrics:** Dynamically requests user gender and age after test completion to structure more detailed profiling.
* **Instant Evaluation:** Automatically processes final averages and returns instant results mapped against standard psychometric scales.
* **Flow Controls:** Quick conversational commands allowing users to reset the test via `/start` or exit instantly via `/cancel`.

---

## 📊 Workflow Diagram

```text
/start ──> Test Info ──> 90 Questions (Inline) ──> Select Gender ──> Enter Age ──> Final Results & Interpretation

```

---

## 📈 Scoring & Interpretation Scales

Test outcomes are derived from the overall average score (ranging from $1.0$ to $5.0$) and classified according to the standard psychometric scale below:

| Average Score Range | EQ Level | Clinical Interpretation |
| --- | --- | --- |
| **4.5 - 5.0** | 🌟 Excellent | Outstanding capacity for managing and directing emotions |
| **3.5 - 4.4** | ✅ Good | High, efficient level of emotional intelligence |
| **2.5 - 3.4** | 📊 Average | Standard baseline; potential for growth in specific sub-scales |
| **1.5 - 2.4** | ⚠️ Below Average | Mild difficulties in personal or social emotional coping |
| **1.0 - 1.4** | 🔴 Low | Significant need for emotional intelligence development |

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

Clone this repository to your local machine using terminal or GitHub Desktop:

```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME

```

### 2. Install Dependencies

Ensure you have Python 3.8+ installed, then run the following command to install the required libraries:

```bash
pip install -r requirements.txt

```

### 3. Configure the Bot Token

For quick initialization, locate the token variable inside your main script:

1. Message **@BotFather** on Telegram to create a new bot and copy your HTTP API token.
2. Open `baron_eq_bot.py`, locate the string placeholder, and paste your token:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

```

### 4. Run the Project

Launch the polling agent to bring your bot online:

```bash
python baron_eq_bot.py

```

---

## 🔒 Security Notice

> ⚠️ **Important:** Never push your live production `BOT_TOKEN` to a public GitHub repository. It is highly recommended to strip your token before committing, or manage sensitive strings via an environment file (`.env`) utilizing the `python-dotenv` package, ensuring `.env` is listed inside your `.gitignore`.

---

## 📄 License

This project is licensed under the **MIT License** - feel free to fork, modify, and distribute as needed.

```

```