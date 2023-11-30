from flet import (
    Page,
    app,
    Text,
    TextField,
    Column,
    Row,
    ThemeMode,
    MainAxisAlignment,
    TextAlign,
)


class Input(TextField):
    def __init__(self, label, on_change=None, on_submit=None):
        super().__init__()
        self.text_align = "center"
        self.counter_text = " "
        self.label = label
        self.getlenWi(label)
        self.on_change = on_change
        self.on_submit = on_submit

    def getlenWi(self, label):
        if label == "Day":
            self.max_length = 2
            self.width = 60
            self.autofocus = True
        elif label == "Month":
            self.max_length = 2
            self.width = 80
        else:
            self.max_length = 4
            self.width = 70


def main(page: Page):
    def edit(e):
        if input_day.value[0].isnumeric() == False:
            input_day.value = None
            page.update()
        if input_day.value[1].isnumeric() == False:
            input_day.value = None
            page.update()
        if int(input_day.value) > 31:
            input_day.value = None
            page.update()

    def calcule_age(e):
        output.value = f"{input_day.value}/{input_month.value}/{input_year.value}"
        page.update()

    page.title = "Find Age"
    page.theme_mode = ThemeMode.LIGHT
    page.horizontal_alignment = MainAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER

    input_day = Input(label="Day", on_change=edit)
    input_month = Input(label="Month", on_change=edit)
    input_year = Input(label="Year", on_change=edit, on_submit=calcule_age)
    output = Text()

    page.add(
        Column(
            [
                Text("Admin:Aitnour", size=30),
                Row(
                    [
                        input_day,
                        input_month,
                        input_year,
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                output,
            ],
            horizontal_alignment="center",
        ),
    )
    page.update()


if __name__ == "__main__":
    app(target=main)
