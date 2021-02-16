import praw
import configparser
from time import sleep
import concurrent.futures

config = configparser.ConfigParser()
config.read('config.ini')


#this is taken care of make sure you  your info to the config.ini
reddit = praw.Reddit(
    username=config['Api_keys']['username'],
    password=config['Api_keys']['password'],
    client_id=config['Api_keys']['client_id'],
    client_secret =config['Api_keys']['secret'],
    user_agent = 'Repost bot by u/Purple_scale_boi'

)

subreddits = [
    'Sub you want to take from here',
    'You can add as many as you like',
    'Just seperate with commas',
    ]

Reddit_topost = 'Your Subreddit here'

def getpost(subreddit):
    sub = reddit.subreddit(subreddit)
    for submission in sub.stream.submissions():
        img, title = submission.url, submission.title
        post(img,title)

def post(img,title ):
    if img.endswith('.jpg') or img.endswith('.png'):
        reddit.subreddit(Reddit_topost).submit(title,img,nsfw=True)
        print(f'Title: {title} , What is being posted: {img}')
        #Waitis so it dosen't hit ratelimit 
        sleep(600)
    else:
        pass


def main():
    #going to use conncurrent futures to make multithreads to listen to multiple subreddits and repost based to a spefic subreddit
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(getpost, subreddits)

main()