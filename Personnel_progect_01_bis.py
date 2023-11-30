from flet import (Page,
                  app,
                  Text,
                  TextField,
                  Column,
                  Row,
                  ThemeMode,
                  MainAxisAlignment,
                  TextAlign,
                  
                  )
def jump(e):
    if len(day.value) == 2:
        month.focus()

day = TextField(on_change=jump)
month = TextField()
def main(page: Page):
    page.add(
        day,
        month
    )
app(main)