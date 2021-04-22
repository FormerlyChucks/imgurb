import os, praw, time, yaml, emoji, random, pyimgur, traceback, webbrowser

with open("config.yaml") as config_file:
    config = yaml.safe_load(config_file)
    
reddit = praw.Reddit(client_id=config["client_id"],client_secret=config["client_secret"],user_agent=config["user_agent"])

while True:
    try:
        subreddit = reddit.subreddit(random.choice(config["subs"]))
        submissions = list(subreddit.top('all', limit=1000))
        submission = random.choice(submissions)
        if submission.domain in config["domains"] and '.gifv' not in submission.url:
            print('Imgur/Reddit Domain!')
            file = submission.url.replace('https://i.imgur.com/','').replace('https://i.redd.it/','')
            downsyndrome.download(url=submission.url, file_name=file)
            print('Downloaded Image')
            tit = str(emoji.demojize(submission.title))
            try:
                with open('tokens.txt') as f:
                    access_token, refresh_token = f.read().strip().split()
                im = pyimgur.Imgur(config["imgur_id"], access_token=access_token, refresh_token=refresh_token)
            except FileNotFoundError:
                im = pyimgur.Imgur(config["imgur_id"])
                webbrowser.open(im.authorization_url('pin'))
                pin = input('Gimme the pin: ')
                access_token, refresh_token = im.exchange_pin(pin)
                with open('tokens.txt', 'w') as f:
                    f.write(f'{access_token} {refresh_token}')
                img = im.upload_image(file)
                img.submit_to_gallery(title=tit)
                print('Uploaded To Gallery')
                os.remove(file)
                print('Deleted File')
                time.sleep(300)
        else:
            print('Submission Not Actionable :(')
            time.sleep(60)
    except Exception:
        print(traceback.format_exc())
        time.sleep(60)
    except KeyboardInterrupt:
        print('Shutting Down :(')
        quit()
