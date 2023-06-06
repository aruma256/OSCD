import flet as ft


from header import Header
from receiver_container import ReceiverContainer
from transmitter_container import TransmitterContainer

APP_TITLE = "OSCDuplicator"


class App:
    def main(self, page: ft.Page):
        page.title = APP_TITLE
        page.horizontal_alignment = "center"
        page.window_width, page.window_height = 600, 800

        self.header = Header()
        self.receiver_container = ReceiverContainer()
        self.transmitter_container = TransmitterContainer()

        page.add(self.header)
        page.add(self.receiver_container)
        page.add(self.transmitter_container)


def start():
    ft.app(target=App().main)


if __name__ == "__main__":
    start()
