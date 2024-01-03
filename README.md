# SiAsistenBot

A simple Fasilkom UI's SiAsisten scraper to give hourly updates on teaching assistant job vacancies.

## Deployment

Here, I assume you have set up your Discord bot, has stored its token, and chosen which Discord server you want to host the bot in. If you haven't, Google or YouTube it.

If you have, clone the repository to your local machine or virtual private server (preferred, as you can keep the bot running 24/7, even with your computer off):

```
git clone https://github.com/pwndbg/pwndbg.git
```

Or, using SSH:

```
git clone git@github.com:pwndbg/pwndbg.git
```

Then create a virtual environment using Python, also install the dependencies needed.

Linux:

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Windows:

```
python -m venv env
env/Scripts/activate
pip install -r requirements.txt
```

As the scraper and the Discord bot uses `python-dotenv` for environment variables management, you need to create a `.env` file containing the environment variables that will be used in the program. Create a `.env` file containing:

```
DISCORD_TOKEN=<your discord token>
DISCORD_GUILD=<your discord SERVER name>
DISCORD_CHANNEL=<your chosen discord text channel ID>
SSO_USN=<your UI SSO username>
SSO_PASS=<your UI SSO password, in plaintext>
```

- `docker-compose up --build -d`
- ...
- Profit!

Known issues:

- Time zones cannot be localized, will always display UTC+0 time zone
