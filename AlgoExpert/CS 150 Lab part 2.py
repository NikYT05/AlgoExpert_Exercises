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
    
    def upvote_arrow_click(some_post, score, ua, da):

        def appropriate_vote(_):
            
            if some_post.likes == None:
                print(f'Upvoting post: {some_post.title}')
                some_post.likes = True
                some_post.score += 1
                score.value = str(some_post.score)
                ua.icon_color = 'orange'
                score.color = 'orange'
                some_post.upvote()
                page.update()
                print(some_post.score)
                
            elif some_post.likes:
                print("Clearing Vote")
                some_post.likes = None
                some_post.score -= 1
                score.value = str(some_post.score)
                ua.icon_color = 'grey'
                score.color = 'grey'
                some_post.clear_vote()
                page.update()
                print(some_post.score)
            else:
                print('upvoting')
                some_post.likes = True
                ua.icon_color = 'orange'
                da.icon_color = 'grey'
                some_post.score += 2
                score.value = str(some_post.score)
                score.color = 'orange'
                some_post.upvote()
                page.update()
                print(some_post.score)
        return appropriate_vote
        

    def downvote_arrow_click(some_post, score, da, ua):
        def appropriate_vote(_):

            if some_post.likes == None:
                print(f'Downvoting post: {some_post.title}')
                some_post.likes = False
                some_post.score -= 1
                score.value = str(some_post.score)
                da.icon_color = 'blue'
                score.color = 'blue'
                some_post.downvote()
                page.update()
                print(some_post.score)

            elif some_post.likes:
                print('Downvoting')
                some_post.likes = False
                some_post.score -= 2
                score.value = str(some_post.score)
                ua.icon_color = 'grey'
                da.icon_color = 'blue'
                score.color='blue'
                some_post.clear_vote()
                page.update()
                print(some_post.score)

            else:
                print('clearing vote')
                some_post.likes = None
                da.icon_color = 'grey'
                some_post.score += 1
                score.value = str(some_post.score)
                score.color = 'grey'
                some_post.downvote()
                page.update()
                print(some_post.score)
        return appropriate_vote

    for post in reddit.front.new():

        score_text = ft.Text(
            str(post.score),
            color='orange' if post.likes else 'blue' if post.likes is False else 'grey',
        )

        upvote_arrow = ft.IconButton(
            icon='arrow_upward',
            icon_color='orange' if post.likes else 'grey',
        )


        downvote_arrow = ft.IconButton(
            icon='arrow_downward',
            icon_color='blue' if post.likes is False else 'grey',
        )

        upvote_arrow.on_click = upvote_arrow_click(post, score_text, upvote_arrow, downvote_arrow)
        downvote_arrow.on_click = downvote_arrow_click(post, score_text, downvote_arrow, upvote_arrow)

        page.update()

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