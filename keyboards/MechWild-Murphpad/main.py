from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()
layers_ext = Layers()
encoder_handler = EncoderHandler()
encoder_handler.pins = ((keyboard.encoder_pin_0, keyboard.encoder_pin_1, None, False),)

keyboard.modules.append(layers_ext, encoder_handler)

# keymap
keyboard.keymap = [
    [
        KC.F1,   KC.F2,   KC.F3,   KC.F4,
        KC.COLON, KC.KP_SLASH, KC.KP_ASTERISK, KC.KP_MINUS,
        KC.KP_7,   KC.KP_8,   KC.KP_9,   KC.KP_PLUS,
        KC.MUTE,  KC.KP_4,   KC.KP_5,   KC.KP_6,
        KC.NO, KC.KP_1,   KC.KP_2,   KC.KP_3,   KC.KP_ENTER,
        KC.BSPC,  KC.KP_0,   KC.NO, KC.KP_DOT,

        KC.F5,   KC.F6,   KC.F7,
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
