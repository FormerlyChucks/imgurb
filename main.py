import os, praw, time, yaml, emoji, random, pyimgur, webbrowser, halo

spinner = halo.Halo(text='Starting Up...',spinner={'interval': 100,'frames': ['-','+','*', '+', '-']})
spinner.start()

with open("config.yaml") as c:
    config = yaml.safe_load(c)
    client_id = config["client_id"]
    client_secret = config["client_secret"]
    user_agent = config["user_agenr"]
    imgur_id = config["imgur_id"]
    subs = config["subs"]
    domains = config["domains"]
    spinner.succed(text='Loaded Configuration File')
    
reddit = praw.Reddit(client_id=client_id,client_secret=client_secret,user_agent=user_agent)

def upload(file,title):
    try:
        with open('tokens.txt') as f:
            access_token, refresh_token = f.read().strip().split()
        im = pyimgur.Imgur(imgur_id, access_token=access_token, refresh_token=refresh_token)
    except FileNotFoundError:
        im = pyimgur.Imgur(imgur_id)
        webbrowser.open(im.authorization_url('pin'))
        pin = input('Enter Your Pin: ')
        access_token, refresh_token = im.exchange_pin(pin)
        with open('tokens.txt', 'w') as f:
            f.write(f'{access_token} {refresh_token}')
    img = im.upload_image(file)
    img.submit_to_gallery(title=title)
    return 'Uploaded To Gallery'
    
while True:
    try:
        subreddit = reddit.subreddit(random.choice(subs))
        submissions = list(subreddit.top('all', limit=1000))
        submission = random.choice(submissions)
        if submission.domain in domains and '.gifv' not in submission.url:
            spinner.info(text='Imgur/Reddit Image Found')
            fileName = submission.url.replace('https://i.imgur.com/','').replace('https://i.redd.it/','')
            downsyndrome.download(url=submission.url, file_name=fileName)
            spinner.info(text=f'Downloaded {submission.url}')
            tit = str(emoji.demojize(submission.title))
            submit = upload(file=fileName,title=tit)
            spinner.succeed(text='Uploaded To Gallery')
            os.remove(fileName)
            spinner.succeed(text=f'Deleted {fileName}')
            time.sleep(300)
        else:
            spinner.info(text='URL Not Actionable')
            time.sleep(60)
    except Exception as e:
        spinner.fail(text=str(e))
        time.sleep(60)
    except KeyboardInterrupt:
        spinner.warn(text='Shutting Down :(')
        quit()
