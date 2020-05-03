from RPLCD.i2c import CharLCD


class LCD:
    def __init__(self):
        self.lcd = CharLCD('PCF8574', 0x27)

    def print(self, rows: list, row=0, col=0) -> None:
        self.lcd.clear()
        self.lcd.cursor_pos = (row, col)
        for i, text in enumerate(rows):
            self.lcd.write_string(text)
            self.lcd.cursor_pos = (row+i+1, col)
