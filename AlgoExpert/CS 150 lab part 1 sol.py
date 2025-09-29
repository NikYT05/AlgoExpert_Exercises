import praw
import flet as ft

reddit = praw.Reddit(      # Before submission, revert all strings below to "..."
    client_id="nNxGuCvSA2SjYmnBeTZ8FA",       # Change this to your Client ID
    client_secret="edOKaP5rvVdaYFQzS-dnzcq8jUqCQQ",   # Change this to your Client Secret
    password="password123",        # Change this to your Reddit account password
    user_agent="testscript by u/rvtan1",      # Change this to "testscript by u/(your username)"
    username="rvtan1",        # Change this to your username
)

def main(page):
    page.title = "CS 150 23.1 Lab 1"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # For layouting; ignore

    controls = []
    
    def upvote_arrow_click(some_post):
        def appropriate_vote(_):
            print(f'Upvoting post: {some_post.title}')
            some_post.upvote()
        return appropriate_vote
        

    def downvote_arrow_click(some_post):
        def appropriate_vote(_):
            print(f'Downvoting post: {some_post.title}')
            some_post.downvote()
        return appropriate_vote

    for post in reddit.front.new():

        upvote_arrow = ft.IconButton(
            icon='arrow_upward',
            #icon_color='orange' if post.likes else 'grey',
            on_click=upvote_arrow_click(post),
        )

        score_text = ft.Text(
            str(post.score),
            color='orange' if post.likes else 'blue' if post.likes is False else 'grey',
        )

        downvote_arrow = ft.IconButton(
            icon='arrow_downward',
            #icon_color='blue' if post.likes is False else 'grey',
            on_click=downvote_arrow_click(post),
        )

        controls.append(
            ft.Card(
                ft.Row(
                    [
                        ft.Column(
                            [
                                upvote_arrow,
                                score_text,
                                downvote_arrow,
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            width=80,     # For layouting; ignore
                        ),
                        ft.Text(
                            post.title,
                            max_lines=2,  # For layouting; ignore
                            expand=1,     # For layouting; ignore
                        ),
                    ],
                ),
            ),
        )

    page.add(
        ft.ListView(
            controls,
            expand=1,    # For layouting; ignore
            spacing=10,  # For layouting; ignore
            padding=20,  # For layouting; ignore
        )
    )


ft.app(target=main)