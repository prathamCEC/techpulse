# 🚀 TechPulse

**Stay informed. Stay curious. Stay ahead.**

TechPulse is an AI-powered technology news assistant built with Python
that automatically collects, filters, and summarizes the latest
developments in the technology industry and delivers a personalized
daily briefing directly to Telegram at **7:00 PM IST**.

Instead of spending hours browsing multiple news websites, TechPulse
brings the most relevant technology updates into one convenient place.

## ✨ Features

-   📰 **Automated News Aggregation** -- Collect technology news from
    multiple sources and APIs.
-   🤖 **AI-Powered Summarization** -- Generate concise, meaningful
    summaries of important stories.
-   🧠 **Smart Filtering** -- Remove duplicate articles and prioritize
    relevant developments.
-   📂 **Topic Categorization** -- Organize news into dedicated
    categories.
-   📱 **Telegram Integration** -- Receive daily technology briefings
    directly on Telegram.
-   ⏰ **Daily Automation** -- Automatically deliver news at 7:00 PM
    IST.
-   🔗 **Source Attribution** -- Include original article links for
    further reading.

## 🗂️ News Categories

TechPulse focuses on the following technology domains:

  -----------------------------------------------------------------------
  Category                            Coverage
  ----------------------------------- -----------------------------------
  Artificial Intelligence             AI models, LLMs, AI agents and
                                      research

  Big Tech                            Google, Microsoft, Apple, Meta,
                                      NVIDIA

  Startups                            Startup launches, funding and
                                      acquisitions

  Cybersecurity                       Vulnerabilities, security research
                                      and threats

  Developer Tools                     Programming languages, frameworks
                                      and tools

  Emerging Technology                 Robotics, quantum computing and
                                      space technology
  -----------------------------------------------------------------------

## 🛠️ Tech Stack

-   **Language:** Python
-   **News Aggregation:** GNews API, RSS Feeds
-   **Bot Integration:** Telegram Bot API
-   **AI Integration:** LLM API
-   **HTTP Requests:** Requests
-   **Feed Parsing:** Feedparser
-   **Environment Management:** Python-dotenv
-   **Scheduling:** Cron
-   **Version Control:** Git and GitHub

## 🏗️ Architecture

``` text
        News APIs and RSS Feeds
                  |
                  v
          News Fetcher
                  |
                  v
        Filtering and Deduplication
                  |
                  v
         News Categorization
                  |
                  v
          AI Summarization
                  |
                  v
          Message Formatter
                  |
                  v
           Telegram Bot
                  |
                  v
       Daily Briefing at 7 PM IST
```

## 📁 Project Structure

``` text
techpulse/
│
├── bot/
│   ├── telegram_bot.py
│   └── commands.py
│
├── news/
│   ├── fetcher.py
│   ├── summarizer.py
│   └── filter.py
│
├── scheduler/
│   └── daily_scheduler.py
│
├── config.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Getting Started

### Prerequisites

-   Python 3.12+
-   Telegram account
-   Telegram Bot Token
-   GNews API Key

### 1. Clone the repository

``` bash
git clone https://github.com/YOUR_USERNAME/techpulse.git
cd techpulse
```

### 2. Create a virtual environment

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

``` env
GNEWS_API_KEY=your_gnews_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

### 5. Run the application

``` bash
python main.py
```

## 🗺️ Development Roadmap

-   [ ] Initialize project structure
-   [ ] Integrate GNews API
-   [ ] Integrate RSS news feeds
-   [ ] Implement news filtering and deduplication
-   [ ] Implement topic-based categorization
-   [ ] Integrate AI summarization
-   [ ] Develop Telegram bot commands
-   [ ] Implement daily 7 PM IST scheduling
-   [ ] Add error handling and logging
-   [ ] Deploy for continuous execution

## 🔒 Security

-   API keys and bot tokens are stored in environment variables.
-   Sensitive configuration files are excluded from version control.
-   Never commit your `.env` file or expose API credentials.

## 🎯 Project Objective

TechPulse aims to simplify technology news consumption by transforming
information from multiple sources into a structured, concise, and
intelligent daily briefing.

The long-term vision is to evolve TechPulse into a personalized
technology intelligence assistant.

## 📄 License

This project is licensed under the MIT License.

------------------------------------------------------------------------

**Built with curiosity and Python. 🚀**
