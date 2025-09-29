import praw
import flet as ft

reddit = praw.Reddit(      # Before submission, revert all strings below to "..."
    client_id="nNxGuCvSA2SjYmnBeTZ8FA",       # Change this to your Client ID
    client_secret="edOKaP5rvVdaYFQzS-dnzcq8jUqCQQ",   # Change this to your Client Secret
    password="password123",        # Change this to your Reddit account password
    user_agent="testscript by u/rvtan1",      # Change this to "testscript by u/(your username)"
    username="rvtan1",        # Change this to your username
)

post = reddit.submission(id='16pwzzf')