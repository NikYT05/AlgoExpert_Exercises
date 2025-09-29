import flet as ft
import praw


reddit = praw.Reddit(      # Before submission, revert all strings below to "..."
    client_id="nNxGuCvSA2SjYmnBeTZ8FA",       # Change this to your Client ID
    client_secret="edOKaP5rvVdaYFQzS-dnzcq8jUqCQQ",   # Change this to your Client Secret
    password="password123",        # Change this to your Reddit account password
    user_agent="testscript by u/rvtan1",      # Change this to "testscript by u/(your username)"
    username="rvtan1",        # Change this to your username
)


def main(page):
    def increment(_):
        nonlocal counter

        counter += 1
        text.value = str(counter)

        page.update()  # Updates the screen with any new content

    def decrement(_):
        nonlocal counter

        counter -= 1
        text.value = str(counter)

        page.update()

    def refresh(_):
        nonlocal counter

        counter -= 1
        text.value = str(counter)

        page.update()


    counter = 0

    text = ft.Text(str(counter))
    button = ft.IconButton(icon='arrow_circle_up', on_click=increment)

    page.add(text)    # Adds the counter text on screen
    page.add(button)  # Adds the increment button on screen

    button = ft.IconButton(icon='arrow_circle_down', on_click=decrement)
    page.add(button)

    button = ft.IconButton(icon="refresh", on_click=refresh)
    page.add(button)


ft.app(target=main)   # Executes `main(page)` and runs an infinite loop
                      # (event loop; out of scope for now)