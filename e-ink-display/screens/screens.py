import openhab


class Screen:
    """Base screen class."""

    def __init__(self) -> None:
        return

    def refresh(self) -> None:
        return

    def button_2_label(self) -> str: return None

    def button_2_handler(self) -> None:
        return

    def button_3_label(self) -> str: return None

    def button_3_handler(self) -> None:
        return

    def button_4_label(self) -> str: return None

    def button_4_handler(self) -> None:
        return


class Heos1Screen(Screen):
    """Heos 1 Screen"""
    play = None
    mute = None
    artist = None

    def __init__(self, openhab_conn: 'openhab.client.OpenHAB') -> None:
        super().__init__()
        self.openhab = openhab_conn
        self.refresh()

    def refresh(self) -> None:
        group = self.openhab.get_item("eInkHeos1Screen").members
        self.play = group.get('HEOS1Control')
        self.mute = self.openhab.get_item("HEOS1Mute")

    def button_2_label(self) -> str:
        if self.play.state == 'PLAY':
            return '\uecaa'
        else:
            return '\uec72'

    def button_2_handler(self) -> None:
        if self.play.state == 'PLAY':
            self.play.pause()
        else:
            self.play.play()

    def button_4_label(self) -> str:
        if self.mute.state == 'ON':
            return '\uecb8'
        else:
            return '\uecb7'

    def button_4_handler(self) -> None:
        self.mute.toggle()
