import praw, random, webbrowser, pyimgur, os, requests, yaml

with open("config.yaml") as cf:
    config = yaml.safe_load(cf)

try:
    with open('tokens.txt') as t:
        access_token, refresh_token = t.read().strip().split()
    im = pyimgur.Imgur(imgur_id, access_token=access_token, refresh_token=refresh_token)
except FileNotFoundError:
    im = pyimgur.Imgur(cf["imgur_id"])
    webbrowser.open(im.authorization_url('pin'))
    pin = input('Enter Your Pin: ')
    access_token, refresh_token = im.exchange_pin(pin)
    with open('tokens.txt', 'w') as t:
        t.write(f'{access_token} {refresh_token}')

reddit = praw.Reddit(client_id=cf["client_id"],client_secret=cf["client_secret"],user_agent=cf["user_agent"])
subreddit = reddit.subreddit(random.choice(cf["subs"]))
submissions = list(subreddit.top('all', limit=1000))
submissions = [submission for submission in submissions if submission.domain in cf["domains"] and '.gifv' not in submission.url and submission.over_18==False and len(submission.title)<=225]
submission = random.choice(submissions)
print('Submission ID:',submission.id)
fileName = submission.url.replace('https://i.imgur.com/','').replace('https://i.redd.it/','')
print('File Name:',fileName)
with open(fileName,'wb') as f:
    response = requests.get(submission.url)
    f.write(response.content)
print('Downloaded:',submission.url)
img = im.upload_image(fileName)
submit = img.submit_to_gallery(title=submission.title)
print('Submitted To Gallery:','https://imgur.com/gallery/'+submit.id)
os.remove(fileName)
print('Deleted',fileName)
