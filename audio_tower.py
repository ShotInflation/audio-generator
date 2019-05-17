import itertools
import sys
from itertools import chain

from audio_utils import AudioFile, linear, flat, repeatlist, sine_wave, dip, complex_sine_wave, common_main, pulse, \
    pause


def calibration():
    return itertools.chain(
        linear(0, 100, 10),
        flat(100, 50)
    )


def a10a():
    return repeatlist(chain(
        flat(30, 4),
        flat(0, 1)
    ), 6)


def a11a():
    return sine_wave(8, 4, 50, 10)


def a12b():
    return repeatlist(chain(
        flat(30, 2),
        flat(0, 1),
        flat(30, 3),
        flat(0, 1),
    ), 5)


def a13b():
    return repeatlist(chain(
        repeatlist(chain(
            flat(70, 0.5),
            flat(0, 0.5),
        ), 3),
        flat(0, 5)
    ), 7)


def a14b():
    return repeatlist(chain(
        repeatlist(chain(
            flat(70, 0.5),
            flat(0, 0.5),
        ), 2),
        flat(0, 5)
    ), 7)


def a15b():
    return flat(50, 27)


def a16b():
    return repeatlist(chain(
        flat(50, 4),
        flat(0, 0.5)
    ), 8)


def a17b():
    return sine_wave(2, 15, 50, 10)


def a18a():
    return linear(10, 100, 30)


def a19a():
    return flat(40, 29)


def a20a():
    return chain(
        flat(100, 2),
        flat(0, 28)
    )


def a100a():
    return chain(
        sine_wave(2.5, 3, 50, 30),
        dip(4, 40, 15),
        sine_wave(2.5, 3, 50, 30),
        dip(4, 40, 15),
    )


def a101a():
    return chain(
        sine_wave(2.5, 3, 60, 30),
        dip(4, 45, 15),
        sine_wave(2.5, 3, 60, 30),
        dip(4, 45, 15),
    )


def a102a():
    return repeatlist(itertools.chain(
        sine_wave(3.5, 2, 60, 30),
        dip(3, 45, 15),
    ), 8)


def a103a():
    return repeatlist(itertools.chain(
        sine_wave(3.5, 1.5, 60, 30),
        dip(3, 45, 15),
    ), 8)


def a104a():
    return repeatlist(chain(
        flat(80, 1),
        flat(10, 5)
    ), 5)


def a105a():
    return repeatlist(chain(
        flat(80, 1.5),
        flat(10, 6)
    ), 5)


def a200a():
    return sine_wave(10, 3, 40, 0)


def a201a():
    return sine_wave(10, 3, 60, 20)


def a202a():
    return sine_wave(10, 3, 80, 20)


def a203a():
    return repeatlist(chain(
        sine_wave(0.5, 2, 70, 0),
        sine_wave(0.5, 2, 70, 0),
        flat(0, 3)
    ), 6)


def a204a():
    return repeatlist(chain(
        sine_wave(0.5, 3, 70, 0),
        sine_wave(0.5, 3, 70, 0),
        flat(0, 3)
    ), 6)


def a205a():
    return repeatlist(chain(
        repeatlist(sine_wave(0.5, 2, 70, 0), 3),
        flat(0, 3)
    ), 5)


def a206a():
    return repeatlist(chain(
        linear(0, 80, 2),
        flat(0, 3)
    ), 8)


def a207a():
    return repeatlist(chain(
        flat(80, 2),
        flat(0, 3)
    ), 8)


def a208a():
    return repeatlist(chain(
        linear(0, 80, 2),
        flat(0, 2)
    ), 8)


def a209a():
    return repeatlist(chain(
        linear(0, 80, 2),
        flat(80, 2),
    ), 8)


def a210a():
    return repeatlist(chain(
        linear(0, 80, 2),
        flat(80, 2),
        flat(0, 2)
    ), 5)


def a211a():
    return repeatlist(chain(
        linear(0, 80, 2),
        flat(80, 2),
        flat(0, 4)
    ), 4)


def a212a():
    return flat(25, 30)


def a213a():
    return repeatlist(chain(
        flat(25, 5),
        flat(0, 3)
    ), 4)


def a214a():
    return repeatlist(chain(
        flat(35, 5),
        flat(0, 1.5)
    ), 5)


def a215a():
    return repeatlist(chain(
        flat(25, 4),
        flat(80, 0.7)
    ), 8)


def a216a():
    return repeatlist(chain(
        linear(20, 50, 1),
        flat(50, 3),
        linear(50, 20, 1),
        flat(20, 3),
    ), 4)


def a217a():
    return repeatlist(chain(
        linear(20, 90, 1),
        flat(90, 3),
        flat(0, 4)
    ), 4)


def a218a():
    return repeatlist(chain(
        linear(20, 80, 4),
        flat(0, 4)
    ), 4)


def a219a():
    return repeatlist(linear(20, 80, 4), 8)


def a220a():
    return repeatlist(chain(
        linear(20, 80, 4),
        flat(20, 4)
    ), 4)


def a221a():
    return repeatlist(chain(
        linear(20, 80, 4),
        flat(80, 2),
        flat(0, 2)
    ), 4)


def a222a():
    return repeatlist(chain(
        linear(20, 90, 4),
        flat(0, 4)
    ), 4)


def a223a():
    return repeatlist(chain(
        linear(20, 90, 4),
        flat(0, 6)
    ), 3)


def a300a():
    return repeatlist(chain(
        flat(20, 5),
        flat(0, 1)
    ), 5)


def a301a():
    return repeatlist(chain(
        flat(20, 3),
        flat(0, 1)
    ), 8)


def a302a():
    return repeatlist(chain(
        flat(20, 5),
        flat(0, 3)
    ), 4)


def a303a():
    return repeatlist(chain(
        flat(50, 5),
        flat(0, 3)
    ), 4)


def a304a():
    return repeatlist(chain(
        flat(50, 5),
        flat(0, 1)
    ), 5)


def a305a():
    return flat(50, 30)


def a306a():
    return repeatlist(chain(
        flat(50, 3),
        flat(0, 1)
    ), 8)


def a307a():
    return repeatlist(chain(
        flat(0, 4),
        linear(0, 100, 1),
    ), 6)


def a308a():
    return repeatlist(chain(
        flat(0, 4),
        linear(0, 100, 1),
        flat(0, 0.5),
        linear(0, 100, 1),
    ), 5)


def a309a():
    return chain(
        flat(0, 4),
        linear(0, 100, 1),
    )


def a310a():
    return chain(
        flat(0, 4),
        linear(0, 100, 1),
        flat(100, 10)
    )


def a311a():
    return repeatlist(chain(
        linear(0, 100, 1),
        flat(0, 0.5),
    ), 18)


def a312a():
    return chain(
        flat(0, 4),
        linear(0, 100, 1),
        flat(100, 22)
    )


def a318a():
    return flat(40, 29)


def a319a():
    return repeatlist(chain(
        flat(40, 4),
        flat(70, 4),
    ), 4)


def a320a():
    return repeatlist(linear(40, 70, 4), 8)


def a321a():
    return flat(70, 30)


def a322a():
    return repeatlist(chain(
        flat(70, 4),
        flat(90, 4),
    ), 4)


def a323a():
    return repeatlist(linear(30, 90, 4), 8)


def a324a():
    return sine_wave(10, 3, 70, 10)


def a325a():
    return repeatlist(chain(
        sine_wave(2.75, 3, 70, 10),
        flat(0, 2)
    ), 4)


def a326a():
    return sine_wave(15, 2, 70, 10)


def a327a():
    return repeatlist(chain(
        sine_wave(2.75, 2, 70, 10),
        flat(0, 2)
    ), 5)


def a328a():
    return repeatlist(chain(
        linear(60, 0, 4),
        flat(0, 3)
    ), 5)


def a329a():
    return repeatlist(chain(
        linear(60, 0, 4),
        flat(0, 1)
    ), 6)


def a330a():
    return repeatlist(chain(
        linear(60, 0, 4),
    ), 8)


def a331a():
    return repeatlist(chain(
        linear(90, 0, 4),
    ), 8)


def a332a():
    return repeatlist(chain(
        linear(90, 0, 4),
        flat(0, 3)
    ), 5)


def a333a():
    return repeatlist(chain(
        flat(90, 1),
        flat(20, 4)
    ), 6)


def a334a():
    return repeatlist(chain(
        flat(90, 1),
        flat(20, 2)
    ), 10)


def a400a():
    return repeatlist(chain(
        linear(10, 90, 5),
        flat(0, 4)
    ), 4)


def a401a():
    return repeatlist(chain(
        linear(10, 90, 5),
        flat(0, 2)
    ), 5)


def a402a():
    return repeatlist(chain(
        linear(10, 90, 5),
    ), 6)


def a403a():
    return repeatlist(chain(
        linear(10, 90, 5),
        flat(90, 3)
    ), 4)


def a404a():
    return repeatlist(chain(
        linear(10, 90, 5),
        flat(90, 3),
        flat(0, 2)
    ), 3)


def a405a():
    return repeatlist(chain(
        linear(10, 90, 6),
        flat(0, 4)
    ), 3)


def a406a():
    return repeatlist(chain(
        linear(10, 90, 6),
        flat(90, 4)
    ), 3)


def a407():
    return flat(80, 30)


def a408a():
    return repeatlist(chain(
        linear(90, 10, 3),
        linear(90, 10, 6),
    ), 4)


def a409a():
    return repeatlist(chain(
        linear(90, 10, 3),
        flat(0, 3),
    ), 5)


def a410a():
    return repeatlist(chain(
        linear(90, 10, 3),
        flat(0, 6),
    ), 4)


def a411a():
    return repeatlist(chain(
        linear(90, 10, 3),
    ), 10)


def a412a():
    return flat(20, 30)


def a413a():
    return repeatlist(chain(
        flat(20, 5),
        flat(0, 2)
    ), 5)


def a414a():
    return repeatlist(chain(
        flat(20, 3),
        flat(60, 3)
    ), 5)


def a415a():
    return repeatlist(chain(
        flat(50, 3),
        flat(90, 3)
    ), 5)


def a416a():
    return repeatlist(chain(
        flat(90, 3),
        flat(0, 3)
    ), 5)


def a417a():
    return repeatlist(chain(
        flat(90, 3),
        flat(0, 3),
        flat(90, 1),
        flat(0, 3),
    ), 3)


def a506a():
    return repeatlist(chain(
        sine_wave(3.5, 3, 70, 10),
        dip(3, 40, 10),
    ), 3)


def a507a():
    sine_wave(10, 3, 70, 10)


def a508a():
    return repeatlist(chain(
        sine_wave(3.25, 3, 70, 10),
        flat(70, 3),
        flat(0, 2)
    ), 3)


def a509a():
    return repeatlist(chain(
        sine_wave(3.25, 3, 70, 10),
        flat(70, 3),
    ), 3)


def a510a():
    sine_wave(10, 3, 100, 20)


def a511a():
    return sine_wave(8, 4, 50, 0)


def a512a():
    return sine_wave(15, 2, 50, 0)


def a513a():
    return sine_wave(8, 4, 80, 0)


def a514a():
    return sine_wave(15, 2, 80, 0)


def a515a():
    return repeatlist(chain(
        complex_sine_wave(-0.25, 0.5, 4, 100, 0),
        flat(100, 1),
        complex_sine_wave(0.25, 0.5, 4, 100, 0)
    ), 6)


def a516a():
    return repeatlist(chain(
        flat(100, 2),
        flat(0, 3)
    ), 6)


def a517a():
    return repeatlist(chain(
        flat(100, 2),
        flat(0, 1.5)
    ), 9)


def a518a():
    return repeatlist(chain(
        flat(100, 3),
        flat(0, 3)
    ), 5)


def a519a():
    return repeatlist(chain(
        flat(100, 2),
        flat(0, 1.5),
        flat(100, 2),
        flat(0, 1.5),
        flat(100, 2),
        flat(0, 1.5),
        flat(100, 4),
        flat(0, 1.5),
    ), 3)


def a520a():
    return repeatlist(chain(
        flat(100, 4),
        flat(0, 2),
    ), 5)


def a521a():
    return repeatlist(chain(
        flat(100, 0.8),
        flat(0, 0.2),
    ), 30)


def a522a():
    return repeatlist(chain(
        sine_wave(0.5, 6, 60, 0),
        flat(0, 2)
    ), 6)


def a523a():
    return repeatlist(chain(
        sine_wave(0.5, 6, 60, 0),
    ), 10)


def a524a():
    return repeatlist(chain(
        sine_wave(0.5, 6, 90, 0),
        flat(0, 4)
    ), 10)


def a525a():
    return repeatlist(chain(
        sine_wave(0.5, 8, 90, 0),
        flat(0, 2)
    ), 10)


def a526a():
    return repeatlist(chain(
        sine_wave(0.5, 6, 90, 0),
        flat(0, 1)
    ), 5)


def a527a():
    return repeatlist(chain(
        sine_wave(0.5, 8, 90, 0),
        flat(0, 6)
    ), 6)


def a528a():
    return repeatlist(chain(
        sine_wave(0.5, 8, 90, 0),
        flat(20, 6)
    ), 6)


def a529a():
    return repeatlist(chain(
        sine_wave(0.5, 4, 90, 0),
        flat(20, 4)
    ), 16)


def a530a():
    return repeatlist(chain(
        sine_wave(0.5, 4, 90, 0),
        flat(0, 4),
        sine_wave(0.5, 4, 90, 0),
        flat(0, 1),
    ), 6)


def a531a():
    return repeatlist(chain(
        sine_wave(0.5, 4, 90, 0),
        flat(20, 2)
    ), 16)


def a532a():
    return repeatlist(chain(
        sine_wave(0.5, 4, 90, 0),
    ), 15)


def a533a():
    return repeatlist(chain(
        linear(40, 0, 2),
        flat(0, 2)
    ), 8)


def a534a():
    return repeatlist(chain(
        linear(40, 0, 2),
    ), 15)


def a535a():
    return repeatlist(chain(
        linear(90, 0, 2),
    ), 15)


def a536a():
    return repeatlist(chain(
        flat(90, 1),
        linear(90, 0, 2),
    ), 10)


def a537a():
    return repeatlist(chain(
        flat(90, 1),
        linear(90, 0, 2),
        flat(0, 2)
    ), 6)


def a538a():
    return repeatlist(chain(
        flat(40, 3),
        linear(40, 90, 2),
        flat(90, 2)
    ), 5)


def a539a():
    return repeatlist(chain(
        flat(40, 3),
        linear(40, 90, 2),
        flat(90, 4)
    ), 4)


def a540a():
    return repeatlist(chain(
        flat(40, 5),
        linear(40, 90, 1),
        flat(90, 2)
    ), 4)


def a541a():
    return repeatlist(chain(
        flat(40, 5),
        linear(40, 90, 1),
        flat(90, 5)
    ), 3)


def a1400a():
    return flat(20, 29)


def a1401a():
    return repeatlist(chain(
        flat(0, 2),
        linear(0, 70, 4)
    ), 5)


def a1402a():
    return repeatlist(chain(
        flat(0, 1),
        linear(0, 70, 2)
    ), 10)


def a1403a():
    return sine_wave(30, 1, 100, 0)


def a1404a():
    return sine_wave(15, 2, 100, 0)


def a1405a():
    return repeatlist(chain(
        flat(0, 1),
        flat(40, 3)
    ), 8)


def a1406a():
    return repeatlist(chain(
        flat(0, 2),
        flat(80, 3)
    ), 6)


def a1407a():
    return repeatlist(chain(
        flat(0, 2),
        flat(80, 1)
    ), 10)


def a1408a():
    return repeatlist(chain(
        sine_wave(4, 1.5, 10, 50),
        sine_wave(4, 1.5, 0, 100),
    ), 6)


def a1409a():
    return repeatlist(chain(
        sine_wave(4, 0.8, 10, 50),
        sine_wave(4, 0.8, 0, 100),
    ), 4)


def a1410a():
    return repeatlist(chain(
        flat(100, 1),
        flat(0, 5),
    ), 5)


def a1411a():
    return repeatlist(chain(
        flat(100, 1),
        flat(0, 3),
    ), 8)


def a1412a():
    return repeatlist(chain(
        flat(100, 1),
        flat(0, 3),
        flat(100, 1),
        flat(0, 2),
    ), 5)


def a1413a():
    return repeatlist(linear(100, 40, 0.8), 40)


def a1414a():
    return repeatlist(chain(
        flat(20, 3),
        flat(80, 3),
    ), 5)


def a1415a():
    return repeatlist(chain(
        flat(40, 3),
        flat(80, 3),
    ), 5)


def a1416a():
    return repeatlist(chain(
        flat(40, 8),
        flat(100, 2),
    ), 3)


def a600a():
    return repeatlist(linear(0, 70, 10), 3)


def a601a():
    return repeatlist(chain(
        linear(0, 80, 1),
        flat(80, 3),
        flat(0, 2)
    ), 6)


def a602a():
    return repeatlist(chain(
        linear(0, 80, 1),
        flat(0, 1),
        linear(0, 80, 1),
        linear(0, 80, 1),
        flat(0, 2)
    ), 5)


def a603a():
    return repeatlist(chain(
        flat(40, 1),
        flat(80, 1),
    ), 15)


def a604a():
    return repeatlist(chain(
        linear(0, 80, 1),
        flat(80, 3),
    ), 8)


def a605a():
    return repeatlist(linear(0, 80, 1), 30)


def a606a():
    return repeatlist(chain(
        linear(0, 40, 3),
        linear(40, 0, 3)
    ), 5)


def a607a():
    return repeatlist(chain(
        flat(100, 1),
        flat(0, 2)
    ), 50)


def a608a():
    return repeatlist(chain(
        flat(100, 1),
        flat(0, 2),
        flat(100, 1),
        flat(0, 0.4),
        flat(100, 1),
    ), 12)


def a609a():
    return sine_wave(30, 2, 20, 60)


def a610a():
    return sine_wave(30, 2, 20, 90)


def a611a():
    return sine_wave(30, 1, 20, 90)


def a612a():
    return repeatlist(chain(
        sine_wave(4, 1, 20, 90),
        flat(0, 3)
    ), 5)


def a613a():
    return sine_wave(10, 3, 20, 90)


def a614a():
    return sine_wave(6, 5, 20, 90)


def a615a():
    return repeatlist(chain(
        linear(40, 80, 3),
        linear(80, 40, 3),
    ), 6)


def a616a():
    return repeatlist(chain(
        linear(40, 80, 3),
        flat(0, 3),
    ), 6)


def a617a():
    return flat(20, 30)


def a618a():
    return repeatlist(chain(
        flat(20, 3),
        flat(50, 3),
    ), 5)


def a619a():
    return repeatlist(chain(
        flat(20, 4),
        flat(0, 2),
    ), 5)


def a620a():
    return repeatlist(chain(
        flat(50, 4),
        flat(20, 2),
    ), 5)


def a621a():
    return repeatlist(chain(
        flat(50, 6),
        flat(20, 2),
    ), 4)


def a622a():
    return flat(30, 30)


def a623a():
    return repeatlist(chain(
        flat(50, 5),
        flat(0, 3)
    ), 4)


def a624a():
    return repeatlist(chain(
        flat(100, 1),
        flat(0, 5)
    ), 5)


def a625a():
    return repeatlist(chain(
        flat(100, 2),
        flat(0, 5)
    ), 5)


def a626a():
    return repeatlist(chain(
        flat(100, 2),
        flat(0, 3)
    ), 6)


def a627a():
    return repeatlist(chain(
        flat(100, 2),
        flat(0, 2),
        flat(100, 1),
        flat(0, 3),
    ), 4)


def a628a():
    return repeatlist(chain(
        flat(0, 4),
        flat(100, 2),
        flat(0, 0.5),
        flat(100, 2),
    ), 4)


def a629a():
    return repeatlist(chain(
        flat(100, 1),
        flat(0, 0.5),
        flat(100, 1),
        flat(0, 3),
        flat(100, 2),
        flat(0, 0.5),
        flat(100, 2),
        flat(0, 3),
    ), 3)


def a630a():
    return repeatlist(chain(
        flat(0, 2),
        flat(100, 4),
    ), 5)


def a631a():
    return repeatlist(chain(
        repeatlist(chain(
            flat(100, 1),
            flat(0, 0.5)
        ), 3),
        flat(0, 4),
    ), 4)


def a632a():
    return repeatlist(chain(
        repeatlist(chain(
            flat(100, 1),
            flat(0, 0.5)
        ), 2),
        flat(0, 3),
        repeatlist(chain(
            flat(100, 1),
            flat(0, 0.5)
        ), 3),
        flat(0, 3),
    ), 3)


def a700a():
    return repeatlist(chain(
        sine_wave(0.5, 8, 60, -20),
        flat(20, 2)
    ), 5)


def a701a():
    return repeatlist(chain(
        sine_wave(0.5, 8, 60, 0),
        flat(30, 2)
    ), 5)


def a702a():
    return repeatlist(chain(
        sine_wave(0.5, 8, 60, 0),
        flat(0, 2)
    ), 5)


def a703a():
    return repeatlist(chain(
        repeatlist(sine_wave(0.5, 3, 60, 0), 3),
        flat(0, 2),
    ), 5)


def a704a():
    return repeatlist(chain(
        repeatlist(sine_wave(0.5, 3, 60, 0), 2),
        flat(0, 2),
    ), 6)


def a705a():
    return repeatlist(chain(
        repeatlist(sine_wave(0.5, 3, 60, 0), 2),
        flat(0, 2),
        repeatlist(sine_wave(0.5, 3, 60, 0), 3),
        flat(0, 2),
    ), 3)


def a706a():
    return sine_wave(10, 3, 50, 0)


def a707a():
    return sine_wave(10, 3, 90, 0)


def a708a():
    return repeatlist(chain(
        flat(90, 4),
        flat(0, 4)
    ), 4)


def a709a():
    return repeatlist(chain(
        flat(90, 4),
        flat(0, 2),
        flat(90, 1),
        flat(0, 4)
    ), 3)


def a710a():
    return repeatlist(chain(
        flat(90, 3),
        flat(0, 2),
        repeatlist(chain(
            flat(90, 0.5),
            flat(0, 0.5),
        ), 4),
        flat(0, 3),
    ), 3)


def a711a():
    return repeatlist(chain(
        linear(20, 90, 3),
        flat(90, 1),
        linear(90, 20, 3),
        flat(20, 1),
    ), 4)


def a712a():
    return flat(60, 60)


def a713a():
    return repeatlist(chain(
        flat(80, 3),
        flat(0, 0.5)
    ), 20)


def a714a():
    return repeatlist(chain(
        flat(80, 1),
        flat(0, 0.5)
    ), 40)


def a715a():
    return repeatlist(chain(
        flat(80, 3),
        flat(0, 2)
    ), 12)


def a716a():
    return sine_wave(8, 4, 50, 10)


def a717a():
    return sine_wave(8, 4, 90, 10)


def a718a():
    return repeatlist(chain(
        flat(90, 3),
        dip(3, 90, 20)
    ), 5)


def a800a():
    return flat(20, 30)


def a801a():
    return repeatlist(chain(
        flat(20, 4),
        flat(60, 4)
    ), 4)


def a802a():
    return repeatlist(chain(
        flat(20, 4),
        flat(90, 4)
    ), 4)


def a803a():
    return flat(60, 30)


def a804a():
    return repeatlist(chain(
        sine_wave(5, 1, 100, 80),
        flat(0, 5)
    ), 3)


def a805a():
    return repeatlist(chain(
        flat(0, 1),
        linear(0, 90, 4)
    ), 6)


def a806a():
    return repeatlist(chain(
        flat(90, 5),
        flat(0, 5),
    ), 3)


def a807a():
    return repeatlist(chain(
        flat(90, 3),
        flat(0, 1),
    ), 8)


def a808a():
    return repeatlist(chain(
        flat(90, 3),
        flat(0, 1),
        flat(60, 1),
        flat(0, 1),
    ), 5)


def a809a():
    return repeatlist(chain(
        flat(90, 3),
        flat(0, 1),
        flat(90, 1),
        flat(0, 1),
    ), 5)


def a810a():
    return repeatlist(chain(
        flat(90, 3),
        flat(0, 1),
        repeatlist(chain(
            flat(90, 0.5),
            flat(0, 0.5),
        ), 2),
        flat(0, 1),
    ), 5)


def a811a():
    return sine_wave(8, 4, 100, 30)


def a812a():
    return sine_wave(15, 2, 100, 30)


def a813a():
    return repeatlist(chain(
        sine_wave(3, 2, 100, 30),
        flat(0, 3)
    ), 4)


def a814a():
    return repeatlist(chain(
        sine_wave(2, 4, 100, 30),
        flat(0, 3)
    ), 3)


def a815a():
    return repeatlist(chain(
        flat(90, 2),
        flat(0, 2),
    ), 8)


def a816a():
    return repeatlist(chain(
        linear(0, 50, 3),
        flat(50, 3),
        flat(0, 2)
    ), 4)


def a817a():
    return repeatlist(chain(
        linear(0, 50, 3),
        flat(50, 3),
    ), 5)


def a900a():
    return repeatlist(chain(
        flat(80, 4),
        flat(0, 4),
    ), 4)


def a901a():
    return repeatlist(chain(
        flat(50, 4),
        flat(0, 2),
    ), 5)


def a902a():
    return repeatlist(chain(
        flat(80, 4),
        flat(40, 4),
    ), 4)


def a903a():
    return repeatlist(chain(
        flat(40, 2),
        flat(0, 2),
    ), 8)


def a904a():
    return repeatlist(chain(
        flat(40, 4),
        flat(0, 2),
    ), 5)


def a905a():
    return repeatlist(chain(
        flat(90, 2),
        flat(0, 2),
    ), 8)


def a906a():
    return repeatlist(chain(
        flat(90, 2),
        flat(0, 1),
    ), 10)


def a907a():
    return repeatlist(chain(
        flat(90, 3),
        flat(0, 1),
    ), 8)


def a909a():
    return repeatlist(chain(
        linear(40, 90, 3),
        flat(0, 2)
    ), 6)


def a910a():
    return repeatlist(chain(
        linear(40, 90, 3),
        flat(90, 2)
    ), 6)


def a911a():
    return pulse(40, 0, 1, 30)


def a912a():
    return pulse(90, 0, 1, 30)


def a1000a():
    return flat(40, 30)


def a1001a():
    return flat(60, 30)


def a1002a():
    return pulse(90, 40, 6, 5)


def a1003a():
    return pulse(90, 20, 6, 5)


def a1004a():
    return repeatlist(chain(
        flat(90, 3),
        flat(0, 1),
        pulse(100, 0, 1, 3)
    ), 4)


def a1005a():
    return repeatlist(chain(
        flat(90, 3),
        flat(0, 1),
        pulse(100, 0, 1, 4)
    ), 4)


def a1006a():
    return repeatlist(chain(
        pulse(100, 0, 1, 4),
        pause(1),
    ), 6)


def a1007a():
    return repeatlist(chain(
        pulse(100, 0, 1, 2),
        pause(1),
    ), 10)


def a1008a():
    return linear(0, 100, 30)


def a1009a():
    return repeatlist(linear(0, 100, 15), 2)


def a1101a():
    return repeatlist(chain(
        pulse(100, 0, 2, 2),
        pause(2),
    ), 5)


def a1102a():
    return repeatlist(chain(
        pulse(100, 0, 2, 3),
        pause(2),
    ), 4)


def a1103a():
    return repeatlist(chain(
        pulse(100, 0, 2, 4),
        pause(2),
    ), 3)


def a1104a():
    return sine_wave(8, 4, 100, 10)


def a1105a():
    return sine_wave(10, 3, 100, 10)


def a1106a():
    return sine_wave(6, 5, 100, 10)


def a1107a():
    return sine_wave(4, 8, 100, 10)


def a1108a():
    return sine_wave(3, 10, 100, 10)


def a1109a():
    return sine_wave(2, 15, 100, 10)


def a1201a():
    return flat(50, 30)


def a1202a():
    return flat(90, 30)


def a1203a():
    return repeatlist(chain(
        flat(100, 4),
        pause(1)
    ), 6)


def a1204a():
    return repeatlist(chain(
        flat(100, 4),
        pause(2)
    ), 5)


def a1205a():
    return repeatlist(chain(
        repeatlist(chain(
            flat(100, 2),
            pause(0.5)
        ), 2),
        pause(2)
    ), 5)


def a1206a():
    return repeatlist(chain(
        repeatlist(chain(
            flat(100, 2),
            pause(0.5)
        ), 3),
        pause(2)
    ), 4)


def a1207a():
    return repeatlist(chain(
        repeatlist(chain(
            flat(100, 2),
            pause(0.5)
        ), 4),
        pause(2)
    ), 3)


def a1208a():
    return repeatlist(chain(
        repeatlist(chain(
            flat(100, 2),
            pause(0.5)
        ), 5),
        pause(2)
    ), 3)


def a1209a():
    return repeatlist(chain(
        repeatlist(chain(
            flat(100, 2),
            pause(0.5)
        ), 6),
        pause(2)
    ), 2)


def a1301a():
    return flat(100, 30)


def a1302a():
    return repeatlist(chain(
        linear(20, 100, 1),
        flat(100, 3),
        pause(1)
    ), 6)


def a1303a():
    return repeatlist(chain(
        linear(20, 100, 1),
        flat(100, 4),
        pause(1)
    ), 5)


def a1304a():
    return repeatlist(chain(
        flat(100, 3),
        pause(1)
    ), 8)


def a1305a():
    return repeatlist(chain(
        flat(100, 2),
        pause(1)
    ), 10)


def a1306a():
    return repeatlist(chain(
        flat(100, 2),
        dip(4, 100, 30)
    ), 5)


def a1307a():
    return repeatlist(chain(
        flat(100, 4),
        dip(4, 100, 30)
    ), 4)


def a1308a():
    return repeatlist(chain(
        flat(100, 3),
        dip(3, 100, 30)
    ), 5)


def a1309a():
    return repeatlist(chain(
        flat(100, 4),
        dip(2, 100, 30)
    ), 5)


def empty():
    return pause(30)


def tease1():
    return repeatlist(chain(
        pause(8),
        flat(100, 1)
    ), 4)


def tease2():
    return repeatlist(chain(
        pause(6),
        flat(100, 0.5)
    ), 5)


def tease3():
    return repeatlist(chain(
        pause(3),
        flat(40, 2)
    ), 6)


def tease4():
    return repeatlist(chain(
        pause(6),
        flat(20, 4)
    ), 3)


def tease5():
    return flat(15, 30)


def tease6():
    return repeatlist(chain(
        pause(10),
        flat(40, 4)
    ), 2)


def tease7():
    return repeatlist(chain(
        pause(10),
        flat(80, 2)
    ), 2)


def tease8():
    return chain(
        pause(18),
        flat(80, 4)
    )


def tease9():
    return chain(
        pause(20),
        flat(20, 10)
    )


def tease10():
    return repeatlist(chain(
        pause(13),
        flat(100, 1)
    ), 2)


def tease11():
    return repeatlist(chain(
        pause(5),
        flat(20, 5)
    ), 3)


def tease12():
    return repeatlist(chain(
        pause(4),
        pulse(100, 0, 1, 2)
    ), 5)


def tease13():
    return repeatlist(chain(
        pause(5),
        pulse(100, 0, 1, 2)
    ), 5)


def tease14():
    return repeatlist(chain(
        pause(7),
        pulse(100, 0, 1, 2)
    ), 3)


def tease15():
    return repeatlist(chain(
        pause(9),
        pulse(100, 0, 1, 3)
    ), 3)


def tease16():
    return chain(
        pause(20),
        flat(40, 5)
    )


def tease17():
    return repeatlist(chain(
        pause(4),
        flat(80, 1)
    ), 6)


def tease18():
    return repeatlist(chain(
        pause(3),
        flat(100, 0.5)
    ), 10)


def tease19():
    return repeatlist(chain(
        pause(12),
        flat(80, 2)
    ), 2)


FILES = {
    "10a": AudioFile("10a.wav", 29, a10a()),  # question low constant pauses
    "11a": AudioFile("11a.wav", 29, a11a()),  # question slow low sine
    "12b": AudioFile("12b.wav", 32, a12b()),  # question low constant pauses
    "13b": AudioFile("13b.wav", 36, a13b()),  # wrong 3 blips, pause
    "14b": AudioFile("14b.wav", 34, a14b()),  # wrong 2 blips, pause
    "15b": AudioFile("15b.wav", 27, a15b()),  # correct mid constant
    "16b": AudioFile("16b.wav", 27, a16b()),  # correct mid constant pauses
    "17b": AudioFile("17b.wav", 27, a17b()),  # correct very long sine
    "18a": AudioFile("18a.wav", 29, a18a()),  # question slow rise
    "19a": AudioFile("19a.wav", 29, a19a()),  # question mid const
    "20a": AudioFile("20a.wav", 29, a20a()),  # no answer long peak, silence
    "100a": AudioFile("100a.wav", 15, a100a()),  # intro 1
    "101a": AudioFile("101a.wav", 15, a101a()),  # intro 2
    "102a": AudioFile("102a.wav", 15, a102a()),  # easy tease
    "103a": AudioFile("103a.wav", 19, a103a()),  # faster tease
    "104a": AudioFile("104a.wav", 24, a104a()),  # short peaks with long lows
    "105a": AudioFile("105a.wav", 25, a105a()),  # short peaks with long lows
    "200a": AudioFile("200a.wav", 29, a200a()),  # long sine mid 1
    "201a": AudioFile("201a.wav", 29, a201a()),  # long sine mid 2
    "202a": AudioFile("202a.wav", 29, a202a()),  # long high sine
    "203a": AudioFile("203a.wav", 29, a203a()),  # 2 peaks, pause
    "204a": AudioFile("204a.wav", 29, a204a()),  # 2 longer peaks, pause
    "205a": AudioFile("205a.wav", 29, a205a()),  # 3 peaks, pause
    "206a": AudioFile("206a.wav", 30, a206a()),  # asc buzzsaw, pause
    "207a": AudioFile("207a.wav", 29, a207a()),  # longer peak, pause
    "208a": AudioFile("208a.wav", 29, a208a()),  # asc buzzsaw, pause shorter
    "209a": AudioFile("209a.wav", 29, a209a()),  # asc buzzsaw, peak
    "210a": AudioFile("210a.wav", 29, a210a()),  # asc buzzsaw, peak, pause
    "211a": AudioFile("211a.wav", 29, a211a()),  # asc buzzsaw, peak, pause longer
    "212a": AudioFile("212a.wav", 29, a212a()),  # low constant
    "213a": AudioFile("213a.wav", 29, a213a()),  # low constant pauses
    "214a": AudioFile("214a.wav", 29, a214a()),  # low constant shorter pauses
    "215a": AudioFile("215a.wav", 29, a215a()),  # low constant peaks
    "216a": AudioFile("216a.wav", 29, a216a()),  # low to mid 50-50
    "217a": AudioFile("217a.wav", 29, a217a()),  # low to high to pause
    "218a": AudioFile("218a.wav", 29, a218a()),  # long asc buzzsaw pauses
    "219a": AudioFile("219a.wav", 29, a219a()),  # long asc buzzsaw
    "220a": AudioFile("220a.wav", 29, a220a()),  # long asc buzzsaw, low
    "221a": AudioFile("221a.wav", 29, a221a()),  # long asc buzzsaw, peak, pause
    "222a": AudioFile("222a.wav", 29, a222a()),  # long asc buzzsaw pauses
    "223a": AudioFile("223a.wav", 29, a223a()),  # long asc buzzsaw pauses longer
    "300a": AudioFile("300a.wav", 29, a300a()),  # low constant, pauses
    "301a": AudioFile("301a.wav", 29, a301a()),  # low constant, pauses often
    "302a": AudioFile("302a.wav", 29, a302a()),  # low constant, pauses longer
    "303a": AudioFile("303a.wav", 28, a303a()),  # mid constant, pauses longer
    "304a": AudioFile("304a.wav", 28, a304a()),  # mid constant, pauses
    "305a": AudioFile("305a.wav", 29, a305a()),  # mid constant
    "306a": AudioFile("306a.wav", 29, a306a()),  # mid constant pauses often
    "307a": AudioFile("307a.wav", 20, a307a()),  # pause, rise
    "308a": AudioFile("308a.wav", 18, a308a()),  # pause, 2 rises
    "309a": AudioFile("309a.wav", 5, a309a()),  # rise, nothing
    "310a": AudioFile("310a.wav", 15, a310a()),  # rise, stay
    "311a": AudioFile("311a.wav", 18, a311a()),  # rises
    "312a": AudioFile("312a.wav", 27, a312a()),  # rise, stay
    "318a": AudioFile("318a.wav", 29, a318a()),  # mid
    "319a": AudioFile("319a.wav", 29, a319a()),  # mid / high
    "320a": AudioFile("320a.wav", 29, a320a()),  # mid to high
    "321a": AudioFile("321a.wav", 29, a321a()),  # high
    "322a": AudioFile("322a.wav", 29, a322a()),  # high / very high
    "323a": AudioFile("323a.wav", 29, a323a()),  # rise to high
    "324a": AudioFile("324a.wav", 29, a324a()),  # sine slow
    "325a": AudioFile("325a.wav", 29, a325a()),  # sine slow breaks
    "326a": AudioFile("326a.wav", 29, a326a()),  # sine faster
    "327a": AudioFile("327a.wav", 29, a327a()),  # sine faster breaks
    "328a": AudioFile("328a.wav", 29, a328a()),  # desc buzzsaw slow break
    "329a": AudioFile("329a.wav", 30, a329a()),  # desc buzzsaw slow short break
    "330a": AudioFile("330a.wav", 30, a330a()),  # desc buzzsaw slow
    "331a": AudioFile("331a.wav", 30, a331a()),  # desc buzzsaw high
    "332a": AudioFile("332a.wav", 29, a332a()),  # desc buzzsaw high pause
    "333a": AudioFile("333a.wav", 29, a333a()),  # peak to low
    "334a": AudioFile("334a.wav", 29, a334a()),  # peak to shorter low
    "400a": AudioFile("400a.wav", 29, a400a()),  # slow asc break
    "401a": AudioFile("401a.wav", 29, a401a()),  # slow asc break shorter
    "402a": AudioFile("402a.wav", 29, a402a()),  # slow asc
    "403a": AudioFile("403a.wav", 30, a403a()),  # slow asc peak
    "404a": AudioFile("404a.wav", 29, a404a()),  # slow asc peak break
    "405a": AudioFile("405a.wav", 29, a405a()),  # very slow asc, stop
    "406a": AudioFile("406a.wav", 29, a406a()),  # very slow asc, peak
    "407a": AudioFile("407a.wav", 29, a407()),  # constant high
    "408a": AudioFile("408a.wav", 29, a408a()),  # alternating long/very long dec buzzsaw
    "409a": AudioFile("409a.wav", 29, a409a()),  # long desc buzzsaw, break
    "410a": AudioFile("410a.wav", 29, a410a()),  # long desc buzzsaw, break longer
    "411a": AudioFile("411a.wav", 29, a411a()),  # long desc buzzsaw
    "412a": AudioFile("412a.wav", 29, a412a()),  # constant low
    "413a": AudioFile("413a.wav", 29, a413a()),  # low, breaks
    "414a": AudioFile("414a.wav", 29, a414a()),  # low / mid
    "415a": AudioFile("415a.wav", 29, a415a()),  # mid / high
    "416a": AudioFile("416a.wav", 29, a416a()),  # high, pause
    "417a": AudioFile("417a.wav", 30, a417a()),  # high, pause, shorter high, pause
    "506a": AudioFile("506a.wav", 29, a506a()),  # long sine mid dip
    "507a": AudioFile("507a.wav", 29, a507a()),  # long sine mid
    "508a": AudioFile("508a.wav", 59, a508a()),  # long sine high break
    "509a": AudioFile("509a.wav", 29, a509a()),  # long sine peak
    "510a": AudioFile("510a.wav", 59, a510a()),  # long sine high
    "511a": AudioFile("511a.wav", 29, a511a()),  # long 0 to mid sine
    "512a": AudioFile("512a.wav", 29, a512a()),  # faster 0 to mid sine
    "513a": AudioFile("513a.wav", 29, a513a()),  # long 0 to 80 sine
    "514a": AudioFile("514a.wav", 29, a514a()),  # faster 0 to 80 sine
    "515a": AudioFile("515a.wav", 29, a515a()),  # 0 to 100 sine, with short stay
    "516a": AudioFile("516a.wav", 29, a516a()),  # peaks with pauses
    "517a": AudioFile("517a.wav", 29, a517a()),  # peaks with shorter pauses
    "518a": AudioFile("518a.wav", 29, a518a()),  # longer peaks with longer pauses
    "519a": AudioFile("519a.wav", 29, a519a()),  # peaks with stays
    "520a": AudioFile("520a.wav", 29, a520a()),  # long peak, pause
    "521a": AudioFile("521a.wav", 29, a521a()),  # fast peaks
    "522a": AudioFile("522a.wav", 29, a522a()),  # hills with short breaks
    "523a": AudioFile("523a.wav", 29, a523a()),  # hills
    "524a": AudioFile("524a.wav", 52, a524a()),  # high hills with long breaks
    "525a": AudioFile("525a.wav", 57, a525a()),  # high longer hills with shorter breaks
    "526a": AudioFile("526a.wav", 19, a526a()),  # high hills with short breaks
    "527a": AudioFile("527a.wav", 60, a527a()),  # high longer hills with longer breaks
    "528a": AudioFile("528a.wav", 59, a528a()),  # high longer hills with lows
    "529a": AudioFile("529a.wav", 54, a529a()),  # high short hills with lows
    "530a": AudioFile("530a.wav", 49, a530a()),  # high short hills with alternating pauses
    "531a": AudioFile("531a.wav", 29, a531a()),  # high short hills with short lows
    "532a": AudioFile("532a.wav", 29, a532a()),  # high short hills
    "533a": AudioFile("533a.wav", 29, a533a()),  # mid to low pause
    "534a": AudioFile("534a.wav", 29, a534a()),  # mid to low
    "535a": AudioFile("535a.wav", 29, a535a()),  # high to low
    "536a": AudioFile("536a.wav", 29, a536a()),  # high peak to low
    "537a": AudioFile("537a.wav", 29, a537a()),  # high peak to low pause
    "538a": AudioFile("538a.wav", 29, a538a()),  # mid to short high
    "539a": AudioFile("539a.wav", 29, a539a()),  # mid to longer high
    "540a": AudioFile("540a.wav", 29, a540a()),  # long mid to short high
    "541a": AudioFile("541a.wav", 29, a541a()),  # long mid to long high
    "600a": AudioFile("600a.wav", 29, a600a()),  # very long rise
    "601a": AudioFile("601a.wav", 29, a601a()),  # fast rise, stay, pause
    "602a": AudioFile("602a.wav", 29, a602a()),  # fast rise, two fast rises, break
    "603a": AudioFile("603a.wav", 29, a603a()),  # fast alternate mid - high
    "604a": AudioFile("604a.wav", 29, a604a()),  # fast rise, stay
    "605a": AudioFile("605a.wav", 29, a605a()),  # fast rises
    "606a": AudioFile("606a.wav", 30, a606a()),  # slow to mid, slow down
    "607a": AudioFile("607a.wav", 150, a607a()),  # peak, short pause
    "608a": AudioFile("608a.wav", 59, a608a()),  # peak, two peaks
    "609a": AudioFile("609a.wav", 29, a609a()),  # med sine
    "610a": AudioFile("610a.wav", 29, a610a()),  # high sine
    "611a": AudioFile("611a.wav", 29, a611a()),  # high faster sine
    "612a": AudioFile("612a.wav", 29, a612a()),  # high faster sine breaks
    "613a": AudioFile("613a.wav", 29, a613a()),  # long high sine
    "614a": AudioFile("614a.wav", 29, a614a()),  # very long high sine
    "615a": AudioFile("615a.wav", 29, a615a()),  # slow mid to high to mid
    "616a": AudioFile("616a.wav", 29, a616a()),  # slow mid to high break
    "617a": AudioFile("617a.wav", 29, a617a()),  # low constant
    "618a": AudioFile("618a.wav", 29, a618a()),  # low to med to low
    "619a": AudioFile("619a.wav", 29, a619a()),  # low constant with breaks
    "620a": AudioFile("620a.wav", 29, a620a()),  # med constant with lows
    "621a": AudioFile("621a.wav", 29, a621a()),  # med long constant with breaks
    "622a": AudioFile("622a.wav", 29, a622a()),  # low constant
    "623a": AudioFile("623a.wav", 29, a623a()),  # medium constant breaks
    "624a": AudioFile("624a.wav", 29, a624a()),  # peak, long pause
    "625a": AudioFile("625a.wav", 29, a625a()),  # longer peak, long pause
    "626a": AudioFile("626a.wav", 29, a626a()),  # longer peak, shorter pause
    "627a": AudioFile("627a.wav", 29, a627a()),  # longer peak, short pause, shorter peak
    "628a": AudioFile("628a.wav", 27, a628a()),  # pause, two long peaks, pause
    "629a": AudioFile("629a.wav", 28, a629a()),  # two short peaks, two long peaks
    "630a": AudioFile("630a.wav", 29, a630a()),  # very long peak, short pause
    "631a": AudioFile("631a.wav", 29, a631a()),  # 3 short peaks, very long pause
    "632a": AudioFile("632a.wav", 29, a632a()),  # 2 short peaks, long pause, 3 short peaks
    "700a": AudioFile("700a.wav", 29, a700a()),  # long hills with lows
    "701a": AudioFile("701a.wav", 29, a701a()),  # long higher hills with mids
    "702a": AudioFile("702a.wav", 29, a702a()),  # long higher hills with pauses
    "703a": AudioFile("703a.wav", 29, a703a()),  # shorter 3 hills
    "704a": AudioFile("704a.wav", 29, a704a()),  # shorter 2 hills
    "705a": AudioFile("705a.wav", 29, a705a()),  # shorter 3-2 hills
    "706a": AudioFile("706a.wav", 29, a706a()),  # low sine
    "707a": AudioFile("707a.wav", 29, a707a()),  # long high sine
    "708a": AudioFile("708a.wav", 29, a708a()),  # long high with long pauses
    "709a": AudioFile("709a.wav", 29, a709a()),  # long high, med pause, short high
    "710a": AudioFile("710a.wav", 29, a710a()),  # long high, short pause, shorter highs
    "711a": AudioFile("711a.wav", 29, a711a()),  # slow high, slow low
    "712a": AudioFile("712a.wav", 59, a712a()),  # constant
    "713a": AudioFile("713a.wav", 59, a713a()),  # constant short high, very short pauses
    "714a": AudioFile("714a.wav", 59, a714a()),  # constant very short high, very short pauses
    "715a": AudioFile("715a.wav", 59, a715a()),  # constant high, med pauses
    "716a": AudioFile("716a.wav", 29, a716a()),  # med long sine
    "717a": AudioFile("717a.wav", 29, a717a()),  # high long sine
    "718a": AudioFile("718a.wav", 29, a718a()),  # long high with dips
    "800a": AudioFile("800a.wav", 29, a800a()),  # constant low
    "801a": AudioFile("801a.wav", 29, a801a()),  # constant low/constant med
    "802a": AudioFile("802a.wav", 29, a802a()),  # constant low/constant high
    "803a": AudioFile("803a.wav", 29, a803a()),  # constant med
    "804a": AudioFile("804a.wav", 29, a804a()),  # constant hard, longer breaks
    "805a": AudioFile("805a.wav", 29, a805a()),  # slow rises to high
    "806a": AudioFile("806a.wav", 29, a806a()),  # constant high, long breaks
    "807a": AudioFile("807a.wav", 29, a807a()),  # med high, pause
    "808a": AudioFile("808a.wav", 29, a808a()),  # med high, pause, short mid
    "809a": AudioFile("809a.wav", 29, a809a()),  # med high, pause, short high
    "810a": AudioFile("810a.wav", 29, a810a()),  # med high, pause, two short highs
    "811a": AudioFile("811a.wav", 29, a811a()),  # med to high long sine
    "812a": AudioFile("812a.wav", 29, a812a()),  # med to high short sine
    "813a": AudioFile("813a.wav", 29, a813a()),  # med to high short sine, break
    "814a": AudioFile("814a.wav", 29, a814a()),  # med to high long sine, break
    "815a": AudioFile("815a.wav", 29, a815a()),  # high-off, 2 sec interval
    "816a": AudioFile("816a.wav", 29, a816a()),  # slow asc to mid, stay, break
    "817a": AudioFile("817a.wav", 31, a817a()),  # slow asc to mid, stay
    "900a": AudioFile("900a.wav", 29, a900a()),  # long high, long pause
    "901a": AudioFile("901a.wav", 29, a901a()),  # long mid, shorter pause
    "902a": AudioFile("902a.wav", 29, a902a()),  # long high, long mid
    "903a": AudioFile("903a.wav", 29, a903a()),  # 2s mid, 2s break
    "904a": AudioFile("904a.wav", 29, a904a()),  # 4s mid, 2s break
    "905a": AudioFile("905a.wav", 29, a905a()),  # 2s high, 2s break
    "906a": AudioFile("906a.wav", 29, a906a()),  # 2s high, short pause
    "907a": AudioFile("907a.wav", 29, a907a()),  # 3s high, short pause
    "909a": AudioFile("909a.wav", 29, a909a()),  # slow from med to high, pause
    "910a": AudioFile("910a.wav", 29, a910a()),  # slow from med to high, stay
    "911a": AudioFile("911a.wav", 29, a911a()),  # 0.5s med, 0.5s break
    "912a": AudioFile("912a.wav", 29, a912a()),  # 0.5s high, 0.5s break
    "1000a": AudioFile("1000a.wav", 29, a1000a()),  # constant mid
    "1001a": AudioFile("1001a.wav", 29, a1001a()),  # constant mid+
    "1002a": AudioFile("1002a.wav", 29, a1002a()),  # mid-high changes
    "1003a": AudioFile("1003a.wav", 29, a1003a()),  # low-high changes
    "1004a": AudioFile("1004a.wav", 29, a1004a()),  # longer high, 3 short highs
    "1005a": AudioFile("1005a.wav", 29, a1005a()),  # long high, 4 short highs
    "1006a": AudioFile("1006a.wav", 29, a1006a()),  # 4 short highs, break
    "1007a": AudioFile("1007a.wav", 29, a1007a()),  # 2 short highs, break
    "1008a": AudioFile("1008a.wav", 29, a1008a()),  # slow rise to high over audio
    "1009a": AudioFile("1009a.wav", 29, a1009a()),  # slow two rises to high over audio
    "1101a": AudioFile("1101a.wav", 29, a1101a()),  # 2 longer highs, short pause
    "1102a": AudioFile("1102a.wav", 29, a1102a()),  # 3 longer highs, short pause
    "1103a": AudioFile("1103a.wav", 29, a1103a()),  # 4 longer highs, short pause
    "1104a": AudioFile("1104a.wav", 29, a1104a()),  # high sine, 4s period
    "1105a": AudioFile("1105a.wav", 29, a1105a()),  # high sine, 3s period
    "1106a": AudioFile("1106a.wav", 29, a1106a()),  # high sine, 5s period
    "1107a": AudioFile("1107a.wav", 29, a1107a()),  # high sine, 8s period
    "1108a": AudioFile("1108a.wav", 29, a1108a()),  # high sine, 10s period
    "1109a": AudioFile("1109a.wav", 29, a1109a()),  # high sine, 15s period
    "1201a": AudioFile("1201a.wav", 29, a1201a()),  # mid constant
    "1202a": AudioFile("1202a.wav", 29, a1202a()),  # high constant
    "1203a": AudioFile("1203a.wav", 29, a1203a()),  # high long constant, short pauses
    "1204a": AudioFile("1204a.wav", 29, a1204a()),  # high long constant, longer pauses
    "1205a": AudioFile("1205a.wav", 29, a1205a()),  # 2 long highs, short pause
    "1206a": AudioFile("1206a.wav", 29, a1206a()),  # 3 long highs, short pause
    "1207a": AudioFile("1207a.wav", 29, a1207a()),  # 4 long highs, short pause
    "1208a": AudioFile("1208a.wav", 29, a1208a()),  # 5 long highs, short pause
    "1209a": AudioFile("1209a.wav", 29, a1209a()),  # 6 long highs, short pause
    "1301a": AudioFile("1301a.wav", 29, a1301a()),  # constant high
    "1302a": AudioFile("1302a.wav", 29, a1302a()),  # rise, stay
    "1303a": AudioFile("1303a.wav", 29, a1303a()),  # rise, long stay
    "1304a": AudioFile("1304a.wav", 29, a1304a()),  # 3s high, pause
    "1305a": AudioFile("1305a.wav", 29, a1305a()),  # 2s high, pause
    "1306a": AudioFile("1306a.wav", 29, a1306a()),  # 2s high, 4s dip
    "1307a": AudioFile("1307a.wav", 29, a1307a()),  # 4s high, 4s dip
    "1308a": AudioFile("1308a.wav", 29, a1308a()),  # 3s high, 3s dip
    "1309a": AudioFile("1309a.wav", 29, a1309a()),  # 4s high, 2s dip
    "1400a": AudioFile("1400a.wav", 29, a1400a()),  # constant low
    "1401a": AudioFile("1401a.wav", 29, a1401a()),  # slow rises to 70
    "1402a": AudioFile("1402a.wav", 29, a1402a()),  # faster rises to 70
    "1403a": AudioFile("1403a.wav", 29, a1403a()),  # 1s full sine
    "1404a": AudioFile("1404a.wav", 29, a1404a()),  # 2s full sine
    "1405a": AudioFile("1405a.wav", 29, a1405a()),  # 3s med, 1s pause
    "1406a": AudioFile("1406a.wav", 29, a1406a()),  # 3s high, 2s pause
    "1407a": AudioFile("1407a.wav", 29, a1407a()),  # 1s high, 2s pause
    "1408a": AudioFile("1408a.wav", 29, a1408a()),  # low sine, high sine
    "1409a": AudioFile("1409a.wav", 29, a1409a()),  # low sine, high sine faster
    "1410a": AudioFile("1410a.wav", 30, a1410a()),  # 1s high, 5s off
    "1411a": AudioFile("1411a.wav", 30, a1411a()),  # 1s high, 3s off
    "1412a": AudioFile("1412a.wav", 29, a1412a()),  # 1s high, 3s off, 1s high, 2s off
    "1413a": AudioFile("1413a.wav", 29, a1413a()),  # desc high - med buzzsaw
    "1414a": AudioFile("1414a.wav", 29, a1414a()),  # low 3s, high 3s
    "1415a": AudioFile("1415a.wav", 29, a1415a()),  # med 3s, high 3s
    "1416a": AudioFile("1416a.wav", 29, a1416a()),  # med 8s, high 2s
    "calibrate-pain": AudioFile("calibrate-pain.wav", 59, tease18()),  # 3s pause, 0.5s high
    "calibrate": AudioFile("calibrate.wav", 59, calibration()),
    "calibrate2": AudioFile("calibrate2.wav", 59, calibration()),
    "x001a": AudioFile("x001a.wav", 28, empty()),  # empty
    "x002a": AudioFile("x002a.wav", 29, tease1()),  # 8s pause, 1s high
    "x003a": AudioFile("x003a.wav", 26, tease2()),  # 6s pause, 0.5s high
    "x004a": AudioFile("x004a.wav", 26, tease3()),  # 3s pause, 2s med
    "x005a": AudioFile("x005a.wav", 26, tease4()),  # 6s pause, 4s low
    "x006a": AudioFile("x006a.wav", 25, tease5()),  # constant 15
    "x007a": AudioFile("x007a.wav", 27, tease6()),  # pause 10s, mid 4s
    "x008a": AudioFile("x008a.wav", 26, tease7()),  # pause 10s, high 2s
    "x009a": AudioFile("x009a.wav", 28, tease8()),  # pause 18s, high 4s
    "x010a": AudioFile("x010a.wav", 29, tease9()),  # pause 20s, low 10s
    "x011a": AudioFile("x011a.wav", 29, empty()),  # empty
    "x012a": AudioFile("x012a.wav", 28, tease4()),  # 6s pause, 4s low
    "x013a": AudioFile("x013a.wav", 28, tease1()),  # 8s pause, 1s high
    "x014a": AudioFile("x014a.wav", 28, tease9()),  # pause 20s, low 10s
    "x015a": AudioFile("x015a.wav", 29, tease10()),  # pause 13s, high 1s
    "x016a": AudioFile("x016a.wav", 28, tease11()),  # pause 5s, low 5s
    "x017a": AudioFile("x017a.wav", 23, tease6()),  # pause 10s, mid 4s
    "x018a": AudioFile("x018a.wav", 27, tease9()),  # pause 20s, low 10s
    "x019a": AudioFile("x019a.wav", 27, tease5()),  # constant 15
    "x020a": AudioFile("x020a.wav", 28, tease4()),  # 6s pause, 4s low
    "x021a": AudioFile("x021a.wav", 30, tease12()),  # pause 4s, two highs
    "x022a": AudioFile("x022a.wav", 30, tease13()),  # pause 5s, two highs
    "x023a": AudioFile("x023a.wav", 28, tease14()),  # pause 7s, two highs
    "x024a": AudioFile("x024a.wav", 28, tease15()),  # pause 9s, three highs
    "x025a": AudioFile("x025a.wav", 29, tease16()),  # pause 20s, med 5s
    "x026a": AudioFile("x026a.wav", 29, tease17()),  # pause 4s, 1 high
    "x027a": AudioFile("x027a.wav", 29, tease2()),  # 6s pause, 0.5s high
    "x028a": AudioFile("x028a.wav", 28, tease1()),  # 8s pause, 1s high
    "x029a": AudioFile("x029a.wav", 29, empty()),  # empty
    "x030a": AudioFile("x030a.wav", 29, tease18()),  # 3s pause, 0.5s high
    "x031a": AudioFile("x031a.wav", 29, tease18()),  # 3s pause, 0.5s high
    "x032a": AudioFile("x032a.wav", 29, empty()),  # empty
    "x033a": AudioFile("x033a.wav", 29, tease11()),  # pause 5s, low 5s
    "x034a": AudioFile("x034a.wav", 28, tease19()),  # pause 12, high 2s
    "x035a": AudioFile("x035a.wav", 23, tease9()),  # pause 20s, low 10s
    "x036a": AudioFile("x036a.wav", 23, tease11()),  # pause 5s, low 5s
    "x037a": AudioFile("x037a.wav", 22, empty()),  # empty
    "x038a": AudioFile("x038a.wav", 29, tease12()),  # pause 4s, two highs
    "x039a": AudioFile("x039a.wav", 28, tease18()),  # 3s pause, 0.5s high
    "x040a": AudioFile("x040a.wav", 26, tease19()),  # pause 12, high 2s
    "x041a": AudioFile("x041a.wav", 29, tease18()),  # 3s pause, 0.5s high
    "x042a": AudioFile("x042a.wav", 29, tease18()),  # 3s pause, 0.5s high
    "x043a": AudioFile("x043a.wav", 26, tease12()),  # pause 4s, two highs
    "x044a": AudioFile("x044a.wav", 29, tease18()),  # 3s pause, 0.5s high
    "x045a": AudioFile("x045a.wav", 14, tease19()),  # pause 12, high 2s
}


if __name__ == '__main__':
    exit(common_main("audio_tower.py", FILES, sys.argv))
