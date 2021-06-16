The reason you saw that post twice.

![](badge.png)

## Setup

**Download the bot, change into the directory:**

    git clone https://github.com/IThinkImOKAY/imgurb && cd imgurb

**Install the needed packages:**

    pip3 install -r requirements.txt

**Getting API Keys**

- You can get your Imgur Credentials From [Here](https://api.imgur.com/oauth2/addclient)
- Follow [James Briggs' Guide](https://towardsdatascience.com/how-to-use-the-reddit-api-in-python-5e05ddfd1e5c) To Get Your Reddit API Keys

**Edit lines 3-7:**

- "client_id" is your reddit client ID
- "client_secret" is your reddit client secret
- "user_agent" should be a short description about your bot
- For the list of subs, add some subs that you wish to repost from
- "imgur_id" will be your Imgur client id

**Run the bot:**

    python3 main.py
