import os, time, core, yaml, traceback

with open("config.yaml") as config_file:
    config = yaml.safe_load(config_file)
    domains = config["domains"]
    imgur_id = config["imgur_id"]
    client_id = config["client_id"]
    client_secret = config["client_secret"]
    user_agent = config["user_agent"]
    subs = config["subs"]

while True:
    try:
        submission = core.reddit(client_id=client_id,client_secret=client_secret,user_agent=user_agent,sub_list=subs)
        print(submission.title)
        if submission.domain in domains and '.gifv' not in submission.url:
            with open('ids.txt') as db:
                if submission.id not in db.read():
                    print('Imgur/Reddit Domain!')
                    file = submission.url.replace('https://i.imgur.com/','').replace('https://i.redd.it/','')
                    core.download(url=submission.url,file_name=file)
                    print('Downloaded Image')
                    tit = core.unemoji(submission.title)
                    core.upload(token_file='tokens.txt',imgur_id=imgur_id,file=file, title=tit)
                    print('Uploaded To Gallery')
                    with open('ids.txt', 'a') as dbfile:
                        dbfile.write(submission.id + '\n')
                    core.delete(file)
                    print('Deleted File')
                    time.sleep(300)
                elif submission.id in db.read():
                    print('Already acted on submission :(')
        else:
            print('Submission Not Actionable :(')
            time.sleep(60)
    except Exception:
        print(traceback.format_exc())
        time.sleep(60)
    except KeyboardInterrupt:
        print('Shutting Down :(')
        quit()
