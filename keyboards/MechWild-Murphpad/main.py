

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()
layers_ext = Layers()
keyboard.modules.append(layers_ext)
encoder_handler = EncoderHandler()
encoder_handler.pins = ((keyboard.encoder_pin_0, keyboard.encoder_pin_1, None, False),)
keyboard.modules.append(layers_ext, encoder_handler)

# keymap
keyboard.keymap = [
    [
        KC.RESET, KC.F1,   KC.F2,   KC.F3,   KC.F4,
        KC.F6, KC.COLON, KC.SLASH, KC.ASTERISK, KC.MINUS,
        KC.F5, KC.N7,   KC.N8,   KC.N9,   KC.PLUS,
        KC.AUDIO_MUTE,  KC.N4,   KC.N5,   KC.N6, KC.PLUS,
        KC.NO, KC.N1,   KC.N2,   KC.N3,   KC.ENTER,
        KC.BSPC, KC.N0,  KC.N0,   KC.DOT, KC.NO,
    ],

]
# keymap

encoder_handler.map = (((KC.VOLD, KC.VOLU, KC.MUTE),),
                       ((KC.DOWN, KC.UP, KC.MUTE),),
                       ((KC.VOLD, KC.VOLU, KC.N1),),
                       ((KC.VOLD, KC.VOLU, KC.N1),),
                       )

if __name__ == '__main__':
    keyboard.go()
