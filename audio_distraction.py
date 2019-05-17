import itertools
import sys
from itertools import chain

from audio_utils import AudioFile, linear, flat, repeatlist, sine_wave, dip, common_main, pulse, pause


def calibration():
    return itertools.chain(
        linear(0, 100, 10),
        flat(100, 50)
    )


def pain1():
    return repeatlist(chain(
        flat(80, 1),
        pause(3),
    ), 5)


def pain2():
    return repeatlist(chain(
        pulse(80, 0, 1, 2),
        pause(4),
    ), 10)


def pain3():
    return repeatlist(chain(
        pulse(80, 0, 1, 3),
        pause(7),
    ), 18)


def a00():
    return pause(30)


def a01():
    return repeatlist(chain(
        pause(4),
        flat(100, 1)
    ), 4)


def a02():
    return repeatlist(chain(
        pause(3),
        flat(100, 0.5)
    ), 7)


def a03():
    return repeatlist(chain(
        pause(3),
        flat(40, 2)
    ), 4)


def a04():
    return repeatlist(chain(
        pause(6),
        flat(20, 4)
    ), 2)


def a10():
    return repeatlist(chain(
        pause(2),
        flat(40, 2)
    ), 5)


def a11():
    return repeatlist(chain(
        pause(5),
        flat(20, 5)
    ), 2)


def a12():
    return repeatlist(chain(
        pause(2),
        pulse(100, 0, 1, 2)
    ), 5)


def a13():
    return flat(20, 20)


def a14():
    return repeatlist(chain(
        pause(2),
        pulse(100, 0, 1, 3)
    ), 4)


def a20():
    return chain(
        sine_wave(2.5, 3, 50, 30),
        dip(4, 40, 15),
        sine_wave(2.5, 3, 50, 30),
        dip(4, 40, 15),
    )


def a21():
    return chain(
        sine_wave(2.5, 3, 60, 30),
        dip(4, 45, 15),
        sine_wave(2.5, 3, 60, 30),
        dip(4, 45, 15),
    )


def a22():
    return repeatlist(itertools.chain(
        sine_wave(3.5, 2, 60, 30),
        dip(3, 45, 15),
    ), 8)


def a23():
    return repeatlist(itertools.chain(
        sine_wave(3.5, 1.5, 60, 30),
        dip(3, 45, 15),
    ), 8)


def a24():
    return repeatlist(chain(
        flat(80, 1),
        flat(10, 5)
    ), 5)


def a30():
    return sine_wave(7, 3, 60, 20)


def a31():
    return sine_wave(5, 4, 60, 20)


def a32():
    return sine_wave(10, 2, 60, 20)


def a33():
    return sine_wave(10, 2, 70, 10)


def a34():
    return sine_wave(15, 1.5, 70, 10)


def a40():
    return repeatlist(chain(
        flat(70, 2),
        flat(20, 2),
    ), 5)


def a41():
    return sine_wave(20, 1, 80, 20)


def a42():
    return repeatlist(chain(
        flat(80, 3),
        flat(0, 2),
    ), 4)


def a43():
    return repeatlist(chain(
        flat(80, 2),
        flat(0, 1),
    ), 7)


def a44():
    return flat(50, 20)


def a50():
    return flat(70, 20)


def a51():
    return sine_wave(20, 1, 100, 40)


def a52():
    return repeatlist(chain(
        linear(20, 80, 1),
        flat(0, 1),
    ), 10)


def a53():
    return repeatlist(chain(
        linear(20, 80, 1),
        flat(20, 1),
    ), 10)


def a54():
    return repeatlist(chain(
        linear(80, 20, 2),
    ), 10)


def a60():
    return repeatlist(chain(
        linear(100, 0, 2),
        pause(1),
    ), 7)


def a61():
    return flat(70, 20)


def a62():
    return pulse(80, 20, 2, 10)


def a63():
    return pulse(100, 0, 4, 5)


def a64():
    return sine_wave(5, 4, 100, 20)


def a70():
    return flat(70, 20)


def a71():
    return sine_wave(10, 2, 100, 20)


def a72():
    return repeatlist(chain(
        sine_wave(0.5, 6, 60, 0),
        flat(30, 2)
    ), 4)


def a73():
    return repeatlist(chain(
        flat(80, 3),
        flat(0, 2),
        flat(90, 1),
        flat(0, 2)
    ), 3)


def a74():
    return sine_wave(20, 1, 100, 20)


def a80():
    return repeatlist(chain(
        linear(40, 90, 3),
        flat(90, 2)
    ), 4)


def a81():
    return repeatlist(chain(
        flat(90, 2),
        linear(90, 40, 3),
    ), 4)


def a82():
    return flat(90, 20)


def a83():
    return pulse(90, 0, 1, 20)


def a84():
    return pulse(90, 0, 2, 10)


def a85():
    return flat(80, 20)


def a86():
    return sine_wave(10, 2, 100, 0)


def a87():
    return sine_wave(5, 4, 100, 0)


def a88():
    return repeatlist(linear(100, 50, 1), 20)


def a89():
    return repeatlist(linear(50, 100, 1), 20)


def a90():
    return flat(100, 20)


def a91():
    return repeatlist(chain(
        flat(100, 3),
        dip(3, 100, 30)
    ), 4)


def a92():
    return pulse(100, 20, 4, 5)


def a93():
    return repeatlist(chain(
        flat(100, 3),
        pause(0.5)
    ), 7)


def a94():
    return repeatlist(chain(
        flat(100, 2),
        pause(0.5)
    ), 10)


def a95():
    return repeatlist(chain(
        flat(100, 1.5),
        pause(0.5)
    ), 10)


def a96():
    return repeatlist(chain(
        flat(100, 4),
        pause(1)
    ), 4)


def a97():
    return repeatlist(chain(
        flat(100, 4),
        flat(20, 2)
    ), 4)


def a98():
    return sine_wave(5, 4, 100, 30)


def a99():
    return repeatlist(chain(
        flat(100, 4),
        pause(0.5)
    ), 4)


FILES = {
    "00a": AudioFile("00a.wav", 20, a00()),
    "01a": AudioFile("01a.wav", 20, a01()),
    "02a": AudioFile("02a.wav", 20, a02()),
    "03a": AudioFile("03a.wav", 20, a03()),
    "04a": AudioFile("04a.wav", 20, a04()),
    "10a": AudioFile("10a.wav", 20, a10()),
    "11a": AudioFile("11a.wav", 20, a11()),
    "12a": AudioFile("12a.wav", 20, a12()),
    "13a": AudioFile("13a.wav", 20, a13()),
    "14a": AudioFile("14a.wav", 20, a14()),
    "20a": AudioFile("20a.wav", 20, a20()),
    "21a": AudioFile("21a.wav", 20, a21()),
    "22a": AudioFile("22a.wav", 20, a22()),
    "23a": AudioFile("23a.wav", 20, a23()),
    "24a": AudioFile("24a.wav", 20, a24()),
    "30a": AudioFile("30a.wav", 20, a30()),
    "31a": AudioFile("31a.wav", 20, a31()),
    "32a": AudioFile("32a.wav", 20, a32()),
    "33a": AudioFile("33a.wav", 20, a33()),
    "34a": AudioFile("34a.wav", 20, a34()),
    "40a": AudioFile("40a.wav", 20, a40()),
    "41a": AudioFile("41a.wav", 20, a41()),
    "42a": AudioFile("42a.wav", 20, a42()),
    "43a": AudioFile("43a.wav", 20, a43()),
    "44a": AudioFile("44a.wav", 20, a44()),
    "50a": AudioFile("50a.wav", 20, a50()),
    "51a": AudioFile("51a.wav", 20, a51()),
    "52a": AudioFile("52a.wav", 20, a52()),
    "53a": AudioFile("53a.wav", 20, a53()),
    "54a": AudioFile("54a.wav", 20, a54()),
    "60a": AudioFile("60a.wav", 20, a60()),
    "61a": AudioFile("61a.wav", 20, a61()),
    "62a": AudioFile("62a.wav", 20, a62()),
    "63a": AudioFile("63a.wav", 20, a63()),
    "64a": AudioFile("64a.wav", 20, a64()),
    "70a": AudioFile("70a.wav", 20, a70()),
    "71a": AudioFile("71a.wav", 20, a71()),
    "72a": AudioFile("72a.wav", 20, a72()),
    "73a": AudioFile("73a.wav", 20, a73()),
    "74a": AudioFile("74a.wav", 20, a74()),
    "80a": AudioFile("80a.wav", 20, a80()),
    "81a": AudioFile("81a.wav", 20, a81()),
    "82a": AudioFile("82a.wav", 20, a82()),
    "83a": AudioFile("83a.wav", 20, a83()),
    "84a": AudioFile("84a.wav", 20, a84()),
    "85a": AudioFile("85a.wav", 20, a85()),
    "86a": AudioFile("86a.wav", 20, a86()),
    "87a": AudioFile("87a.wav", 20, a87()),
    "88a": AudioFile("88a.wav", 20, a88()),
    "89a": AudioFile("89a.wav", 20, a89()),
    "90a": AudioFile("90a.wav", 20, a90()),
    "91a": AudioFile("91a.wav", 20, a91()),
    "92a": AudioFile("92a.wav", 20, a92()),
    "93a": AudioFile("93a.wav", 20, a93()),
    "94a": AudioFile("94a.wav", 20, a94()),
    "95a": AudioFile("95a.wav", 20, a95()),
    "96a": AudioFile("96a.wav", 20, a96()),
    "97a": AudioFile("97a.wav", 20, a97()),
    "98a": AudioFile("98a.wav", 20, a98()),
    "calibrate": AudioFile("calibrate.wav", 20, calibration()),
    "pain1": AudioFile("pain1.wav", 20, pain1()),
    "pain2": AudioFile("pain2.wav", 60, pain2()),
    "pain3": AudioFile("pain3.wav", 180, pain3()),
}


if __name__ == '__main__':
    exit(common_main("audio_distraction.py", FILES, sys.argv))
