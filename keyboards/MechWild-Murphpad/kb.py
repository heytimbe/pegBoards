import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.D9, board.D6, board.D5, board.D4, board.D10)
    row_pins = (board.A2, board.MOSI, board.MISO, board.SCK, board.A0, board.A1)
    diode_orientation = DiodeOrientation.COL2ROW
    encoder_pin_0 = board.D7
    encoder_pin_1 = board.D1