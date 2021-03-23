import os, praw, emoji, random, pyimgur, webbrowser

def delete(file):
    os.remove(file)
    return 'success'

def download(url,file_name):
    downsyndrome.download(url=submission.url, file_name=file)
    return 'success'

def unemoji(string):
    return str(emoji.demojize(string))

def upload(token_file,imgur_id,file, title):
    try:
        with open(token_file) as f:
            access_token, refresh_token = f.read().strip().split()
        im = pyimgur.Imgur(imgur_id, access_token=access_token, refresh_token=refresh_token)
    except FileNotFoundError:
        im = pyimgur.Imgur(imgur_id)
        webbrowser.open(im.authorization_url('pin'))
        pin = input('Gimme the pin: ')
        access_token, refresh_token = im.exchange_pin(pin)
        with open('tokens.txt', 'w') as f:
            f.write(f'{access_token} {refresh_token}')
        img = im.upload_image(file)
        img.submit_to_gallery(title=title)
    return 'success'

def reddit(client_id,client_secret,user_agent,sub_list):
    reddit = praw.Reddit(client_id=client_id,client_secret=client_secret,user_agent=user_agent)
    subreddit = reddit.subreddit(random.choice(sub_list))
    submissions = list(subreddit.top('all', limit=1000))
    submission = random.choice(submissions)
    return submission
