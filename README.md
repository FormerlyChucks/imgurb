# imgurb

![](badge.png)

Repost old reddit posts to imgur for imaginary internet points 🤤

# Set-up

**Download the bot, change into the directory:**

    git clone https://github.com/IThinkImOKAY/imgurb && cd imgurb

**Install the needed packages:**

    pip3 install requests praw pyimgur

**Getting API Keys**

- You can get your Imgur credentials from [here](https://api.imgur.com/oauth2/addclient)
- Follow [James Briggs' uide](https://towardsdatascience.com/how-to-use-the-reddit-api-in-python-5e05ddfd1e5c) to get your reddit API keys

**Edit lines 3-7:**

- `client_id` is your reddit client ID
- `client_secret` is your reddit client secret
- `user_agent` should be a short description about your bot
- `subs` should be a list of subs you wish to repost from
- `imgur_id`

**Run the bot:**

    python3 main.py
