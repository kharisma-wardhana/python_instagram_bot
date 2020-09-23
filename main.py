from instapy import InstaPy
from instapy import smart_run
from dotenv import load_dotenv
from pathlib import Path
import os 

load_dotenv(verbose=True)
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

insta_username = os.getenv('USERNAME')
insta_password = os.getenv('PASSWORD')

session = InstaPy(username = insta_username, password = insta_password)

with smart_run(session):
    session.set_dont_include([])

    session.set_do_follow(True, percentage=50)

    session.set_do_comment(True, percentage=100)

    session.set_comments(['hi @{}, ada product baru nih'])

    session.set_quota_supervisor(enabled = True, 
                                peak_follows_daily = 3000, 
                                peak_follows_hourly = 200, 
                                peak_likes_daily = 100)
    
    session.like_by_tags(['python3', 'javascript'], amount = 200)
session.end()

