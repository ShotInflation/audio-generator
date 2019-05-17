import itertools
import sys

from audiogen.util import envelope

from audio_utils import AudioFile, repeatlist, linear, flat, sound, sine_wave, dip, common_main


def calibration():
    return envelope(sound(), itertools.chain(
        linear(0, 100, 10),
        flat(100, 50)
    ))


def a0a():
    return envelope(sound(), itertools.chain(
        linear(0, 40, 2),
        sine_wave(2.5, 3, 50, 30),
        dip(4, 40, 15),
        sine_wave(2.5, 3, 50, 30),
        dip(4, 40, 15),
    ))


def a2a():
    return envelope(sound(), itertools.chain(
        linear(0, 45, 2),
        sine_wave(2.5, 3, 60, 30),
        dip(4, 45, 15),
        sine_wave(2.5, 3, 60, 30),
        dip(4, 45, 15),
    ))


def a3a():
    return envelope(sound(), itertools.chain(
        linear(0, 45, 2),
        repeatlist(itertools.chain(
            sine_wave(3.5, 1.5, 60, 30),
            dip(3, 45, 15),
        ), 8)
    ))


def a4a():
    return envelope(sound(), itertools.chain(
        linear(0, 60, 2),
        repeatlist(itertools.chain(
            sine_wave(3.5, 1.5, 80, 40),
            dip(3, 60, 30),
        ), 5),
    ))


def a5a():
    return envelope(sound(), itertools.chain(
        linear(0, 60, 2),
        repeatlist(itertools.chain(
            sine_wave(4.5, 1.1, 80, 40),
            dip(2, 60, 40),
        ), 6),
    ))


def a6a():
    return envelope(sound(), itertools.chain(
        linear(0, 60, 2),
        repeatlist(itertools.chain(
            sine_wave(4.5, 1, 80, 40),
            dip(2, 60, 40),
        ), 7)
    ))


def a7a():
    return envelope(sound(), itertools.chain(
        linear(0, 65, 1.5),
        sine_wave(15.5, 1, 90, 40),
        dip(3, 65, 30),
        sine_wave(15.5, 1, 90, 40),
    ))


def a8a():
    return envelope(sound(), itertools.chain(
        linear(0, 65, 1),
        sine_wave(50, .9, 90, 40)
    ))


def a9a():
    return envelope(sound(), itertools.chain(
        linear(0, 65, 1),
        sine_wave(8.5, .8, 90, 40),
        flat(0, 3),
        sine_wave(8.5, .8, 90, 40),
        flat(0, 3),
        sine_wave(8.5, .8, 90, 40),
        flat(0, 3),
        sine_wave(8.5, .8, 90, 40),
        flat(0, 3),
        sine_wave(8.5, .8, 90, 40),
        flat(0, 3),
    ))


def a10aa():
    return envelope(sound(), itertools.chain(
        linear(0, 65, 1),
        sine_wave(6.25, .7, 90, 40),
        flat(90, 3),
        linear(90, 65, 0.5),
        sine_wave(6.25, .7, 90, 40),
        flat(90, 3),
        linear(90, 65, 0.5),
        sine_wave(6.25, .7, 90, 40),
        flat(90, 3),
        linear(90, 65, 0.5),
        sine_wave(6.25, .7, 90, 40),
        flat(90, 3),
        linear(90, 65, 0.5),
        sine_wave(6.25, .7, 90, 40),
        flat(90, 3),
        linear(90, 65, 0.5),
        sine_wave(6.25, .7, 90, 40),
        flat(90, 3),
        linear(90, 65, 0.5),
    ))


def a11a():
    return envelope(sound(), itertools.chain(
        linear(0, 65, 1),
        sine_wave(6.25, .7, 90, 40),
        flat(90, 3),
        flat(0, 3),
        sine_wave(6.25, .7, 90, 40),
        flat(90, 3),
        flat(0, 3),
        sine_wave(6.25, .7, 90, 40),
        flat(90, 3),
        flat(0, 3),
        sine_wave(6.25, .7, 90, 40),
        flat(90, 3),
        flat(0, 3),
        sine_wave(6.25, .7, 90, 40),
        flat(90, 3),
        flat(0, 3),
    ))


def a12a():
    return envelope(sound(), itertools.chain(
        linear(0, 65, 1),
        sine_wave(6, .8, 90, 40),
        sine_wave(7, .5, 90, 40),
        flat(0, 2),
        sine_wave(6, .8, 90, 40),
        sine_wave(7, .5, 90, 40),
        flat(0, 2),
        sine_wave(6, .8, 90, 40),
        sine_wave(7, .5, 90, 40),
        flat(0, 2),
        sine_wave(6, .8, 90, 40),
        sine_wave(7, .5, 90, 40),
        flat(0, 2),
        sine_wave(6, .8, 90, 40),
        sine_wave(7, .5, 90, 40),
        flat(0, 2),
        sine_wave(6, .8, 90, 40),
        sine_wave(7, .5, 90, 40),
        flat(0, 2),
    ))


def a13a():
    return envelope(sound(), itertools.chain(
        linear(0, 65, 1),
        repeatlist(itertools.chain(
            sine_wave(5, 1, 90, 40),
            sine_wave(7, .5, 90, 40),
        ), 6)
    ))


def a14a():
    return envelope(sound(), itertools.chain(
        linear(0, 50, 1),
        sine_wave(10, 6, 90, 20),
    ))


def a15a():
    return envelope(sound(), itertools.chain(
        linear(0, 80, 1),
        sine_wave(120, 1, 100, 30),
    ))


def a16a():
    return envelope(sound(), itertools.chain(
        linear(0, 70, 1),
        repeatlist(itertools.chain(
            sine_wave(4, .7, 90, 50),
            sine_wave(3, 1.5, 90, 50),
        ), 5)
    ))


def a17a():
    return envelope(sound(), itertools.chain(
        linear(0, 70, 1),
        repeatlist(itertools.chain(
            sine_wave(4.25, .7, 90, 50),
            flat(90, 4),
        ), 6),
    ))


def a18a():
    return envelope(sound(), itertools.chain(
        linear(0, 60, 1),
        repeatlist(itertools.chain(
            sine_wave(4.75, .7, 90, 30),
            flat(0, 5),
        ), 6),
    ))


def a20a():
    return envelope(sound(), itertools.chain(
        repeatlist(itertools.chain(
            sine_wave(0.5, 8, 80, 0),
            flat(20, 4),
        ), 6),
    ))


def a21a():
    return envelope(sound(), itertools.chain(
        repeatlist(itertools.chain(
            sine_wave(0.5, 8, 80, 0),
            flat(20, 2),
        ), 6),
    ))


def a22a():
    return envelope(sound(), itertools.chain(
        repeatlist(sine_wave(0.5, 8, 80, 0), 8)
    ))


def a23a():
    return envelope(sound(), itertools.chain(
        linear(0, 80, 1),
        repeatlist(itertools.chain(
            flat(80, 0.5),
            flat(0, 0.5),
        ), 30)
    ))


def a24a():
    return envelope(sound(), itertools.chain(
        linear(0, 80, 1),
        repeatlist(itertools.chain(
            repeatlist(itertools.chain(
                flat(80, 0.5),
                flat(0, 0.5),
            ), 6),
            flat(80, 3)
        ), 4)
    ))


def a25a():
    return envelope(sound(), itertools.chain(
        linear(0, 80, 1),
        repeatlist(itertools.chain(
            repeatlist(itertools.chain(
                flat(80, 0.5),
                flat(0, 0.5),
            ), 6),
            flat(80, 5)
        ), 4)
    ))


def a26a():
    return envelope(sound(), itertools.chain(
        linear(0, 80, 1),
        repeatlist(itertools.chain(
            repeatlist(itertools.chain(
                flat(80, 0.5),
                flat(0, 0.5),
            ), 6),
            flat(90, 6),
            flat(0, 0.5),
        ), 3)
    ))


def a27a():
    return envelope(sound(), itertools.chain(
        linear(0, 50, 2),
        repeatlist(itertools.chain(
            sine_wave(5.5, .7, 80, 20),
            flat(0, 3),
        ), 7),
    ))


def a28a():
    return envelope(sound(), itertools.chain(
        linear(0, 80, 2),
        repeatlist(linear(80, 40, 2), 30)
    ))


def a29a():
    return envelope(sound(), itertools.chain(
        linear(0, 90, 2),
        repeatlist(linear(90, 40, 1.5), 50)
    ))


def a30a():
    return envelope(sound(), itertools.chain(
        linear(0, 90, 2),
        repeatlist(itertools.chain(
            repeatlist(linear(90, 40, 0.9), 4),
            flat(90, 3)
        ), 6)
    ))


def a31a():
    return envelope(sound(), itertools.chain(
        linear(0, 90, 2),
        repeatlist(itertools.chain(
            flat(90, 3),
            linear(90, 30, 0.5),
            flat(30, 0.5),
            linear(30, 90, 0.5),
        ), 10)
    ))


def a32a():
    return envelope(sound(), itertools.chain(
        linear(0, 70, 1),
        sine_wave(40, .8, 100, 40),
    ))


def a33a():
    return envelope(sound(), itertools.chain(
        linear(0, 70, 1),
        repeatlist(itertools.chain(
            sine_wave(4.25, .7, 90, 50),
            flat(90, 3),
        ), 6)
    ))


def a34a():
    return envelope(sound(), itertools.chain(
        linear(0, 70, 1),
        sine_wave(40, 1, 95, 45),
    ))


def a35a():
    return envelope(sound(), itertools.chain(
        linear(0, 100, 1.5),
        repeatlist(linear(100, 60, 0.5), 30)
    ))


def a36a():
    return envelope(sound(), itertools.chain(
        linear(0, 80, 3),
        repeatlist(itertools.chain(
            flat(80, 2),
            linear(80, 20, 2),
            flat(20, 2),
            linear(20, 80, 2),
        ), 5)
    ))


def a37a():
    return envelope(sound(), itertools.chain(
        linear(0, 90, 3),
        repeatlist(itertools.chain(
            flat(90, 3),
            linear(90, 30, 2),
            linear(30, 90, 2),
        ), 5)
    ))


def a38a():
    return envelope(sound(), itertools.chain(
        linear(0, 90, 3),
        repeatlist(itertools.chain(
            flat(90, 4),
            linear(90, 50, 1.5),
            linear(50, 90, 1.5),
        ), 5)
    ))


def a39a():
    return envelope(sound(), itertools.chain(
        linear(0, 100, 3),
        repeatlist(itertools.chain(
            flat(100, 3),
            linear(100, 30, 2.5),
            flat(30, 0.5),
            linear(30, 100, 2.5),
        ), 5)
    ))


def a40a():
    return envelope(sound(), itertools.chain(
        linear(0, 80, 1),
        repeatlist(itertools.chain(
            flat(80, 3),
            flat(0, 2),
        ), 6)
    ))


def a41a():
    return envelope(sound(), itertools.chain.from_iterable([
        linear(0, 90, 1),
        repeatlist(itertools.chain(
            flat(90, 4),
            flat(0, 1),
        ), 6)
    ]))


def a42a():
    return envelope(sound(), itertools.chain(
        linear(0, 90, 1),
        repeatlist(itertools.chain(
            linear(90, 70, 1),
        ), 30)
    ))


def a43a():
    return envelope(sound(), itertools.chain(
        linear(0, 90, 1),
        repeatlist(itertools.chain(
            repeatlist(linear(90, 40, 1), 4),
            flat(90, 3)
        ), 5)
    ))


def a44a():
    return envelope(sound(), itertools.chain(
        linear(0, 90, 1),
        repeatlist(itertools.chain(
            repeatlist(linear(90, 40, 1), 4),
            flat(90, 4),
            flat(0, 2)
        ), 3)
    ))


def a45a():
    return envelope(sound(), itertools.chain(
        repeatlist(itertools.chain(
            flat(100, 1),
            flat(0, 3),
        ), 8)
    ))


def a46a():
    return envelope(sound(), itertools.chain(
        repeatlist(itertools.chain(
            flat(100, 1),
            flat(0, 2),
        ), 10)
    ))


def a47a():
    return envelope(sound(), itertools.chain(
        repeatlist(itertools.chain(
            flat(100, 1),
            flat(0, 1),
        ), 15)
    ))


def a48a():
    return envelope(sound(), itertools.chain(
        linear(0, 80, 1),
        sine_wave(50, 0.6, 100, 60)
    ))


def a49a():
    return envelope(sound(), itertools.chain(
        linear(0, 65, 1),
        sine_wave(15, 3, 100, 30)
    ))


def a50a():
    return envelope(sound(), itertools.chain(
        linear(0, 65, 1),
        sine_wave(20, 1.5, 100, 60)
    ))


def a51a():
    return envelope(sound(), itertools.chain(
        linear(0, 70, 1),
        repeatlist(itertools.chain(
            sine_wave(4.5, 1, 100, 70),
            linear(70, 0, 0.5),
            flat(0, 3),
            linear(0, 70, 0.5),
        ), 4)
    ))


def a52a():
    return envelope(sound(), itertools.chain(
        linear(0, 80, 1),
        sine_wave(30, 1, 100, 60)
    ))


def a53a():
    return envelope(sound(), itertools.chain(
        flat(90, 35),
    ))


def a54a():
    return envelope(sound(), itertools.chain(
        repeatlist(itertools.chain(
            flat(90, 4),
            flat(0, 0.5)
        ), 8)
    ))


def a55a():
    return envelope(sound(), itertools.chain(
        repeatlist(itertools.chain(
            flat(90, 1.5),
            flat(0, 0.5)
        ), 16)
    ))


def a100a():
    return envelope(sound(), itertools.chain(
        sine_wave(200, 0.7, 100, 60)
    ))


def a101a():
    return envelope(sound(), itertools.chain(
        flat(0, 0.5),
        repeatlist(itertools.chain(
            flat(100, 0.5),
            flat(0, 0.3),
            flat(100, 0.8),
            flat(0, 0.3),
        ), 70)
    ))


def a102a():
    return envelope(sound(), itertools.chain(
        repeatlist(itertools.chain(
            repeatlist(itertools.chain(
                flat(100, 0.8),
                flat(0, 0.2),
            ), 5),
            flat(100, 5)
        ), 10)
    ))


def a103a():
    return envelope(sound(), itertools.chain(
        repeatlist(linear(100, 60, 0.7), 200)
    ))


FILES = {
    # sensi
    "0a": AudioFile("0a.wav", 31, a0a()),#very gentle, sine
    "1a": AudioFile("1a.wav", 31, None),#unused
    "2a": AudioFile("2a.wav", 30, a2a()),# gentle tease, sine
    "3a": AudioFile("3a.wav", 59, a3a()),# mid tease, sine
    "4a": AudioFile("4a.wav", 30, a4a()),# mid tease, sine
    "5a": AudioFile("5a.wav", 28, a5a()),# harder tease, sine
    "6a": AudioFile("6a.wav", 32, a6a()),# harder tease, sine
    "7a": AudioFile("7a.wav", 30, a7a()),# hardest tease, sine
    # end sensi
    # susana
    "8a": AudioFile("8a.wav", 29, a8a()),# mid sine
    "9a": AudioFile("9a.wav", 31, a9a()),# mid sine, with breaks
    "10a": AudioFile("10a.wav", 29, None),# unused
    "10aa": AudioFile("10aa.wav", 29, a10aa()),# sine with peaks
    "11a": AudioFile("11a.wav", 33, a11a()),# sine with peaks and breaks
    "12a": AudioFile("12a.wav", 30, a12a()),# alternate slow and fast with breaks
    "13a": AudioFile("13a.wav", 31, a13a()),# alternate slow and fast
    # end susana
    # alissiya
    "14a": AudioFile("14a.wav", 59, a14a()),# long waves
    # end alissiya
    # lilly
    "15a": AudioFile("15a.wav", 49, a15a()),# long hard
    # lilly
    # caprice
    "16aa": AudioFile("16aa.wav", 46, a16a()), # caprice easy sine
    "17a": AudioFile("17a.wav", 46, a17a()),# caprice hard sine
    # caprice end
    "18a": AudioFile("18a.wav", 28, a18a()), # harder with breaks
    "19a": AudioFile("19a.wav", 32, None), # unused
    "20a": AudioFile("20a.wav", 34, a20a()),# pulses, longer breaks
    "21a": AudioFile("21a.wav", 33, a21a()),# pulses, shorter breaks
    "22a": AudioFile("22a.wav", 32, a22a()),# pulses, no breaks
    "23a": AudioFile("23a.wav", 29, a23a()),# fast and hard
    "24a": AudioFile("24a.wav", 30, a24a()),# fast and hard with peaks
    "25a": AudioFile("25a.wav", 30, a25a()),# fast and hard with longer peaks
    "26a": AudioFile("26a.wav", 30, a26a()),# fast and hard with longer longer peaks
    "27a": AudioFile("27a.wav", 37, a27a()),# fast sine, short breaks
    "28a": AudioFile("28a.wav", 37, a28a()),# buzzsaw, easier
    "29a": AudioFile("29a.wav", 35, a29a()),# buzzsaw, harder
    "30a": AudioFile("30a.wav", 29, a30a()),# buzzsaw, harder, with peaks
    "31a": AudioFile("31a.wav", 29, a31a()),# hard peaks
    "32a": AudioFile("32a.wav", 30, a32a()),# hard sine
    "33a": AudioFile("33a.wav", 32, a33a()),# sine peaks
    "34a": AudioFile("34a.wav", 29, a34a()),# high sine, peaks
    "35a": AudioFile("35a.wav", 15, a35a()),# buzzsaw, harsh
    "36a": AudioFile("36a.wav", 30, a36a()),# jagged low
    "37a": AudioFile("37a.wav", 30, a37a()),# jagged mid
    "38a": AudioFile("38a.wav", 32, a38a()),# jagged harder
    "39a": AudioFile("39a.wav", 30, a39a()),# jagged hard
    "40a": AudioFile("40a.wav", 28, a40a()),# peaks with pauses
    "41a": AudioFile("41a.wav", 29, a41a()),# peaks with quick pauses
    "42a": AudioFile("42a.wav", 29, a42a()),# high buzzsaw
    "43a": AudioFile("43a.wav", 29, a43a()),# high buzzsaw, peaks
    "44a": AudioFile("44a.wav", 29, a44a()),# high buzzsaw, longer peaks with pauses
    "45a": AudioFile("45a.wav", 27, a45a()),# sharp peaks low
    "46a": AudioFile("46a.wav", 27, a46a()),# sharp peaks mid
    "47a": AudioFile("47a.wav", 27, a47a()),# sharp peaks hight
    "48a": AudioFile("48a.wav", 29, a48a()),# quicker upper sine
    "49a": AudioFile("49a.wav", 32, a49a()),# slow long high sine
    "50a": AudioFile("50a.wav", 30, a50a()),# quicker high sine
    "51a": AudioFile("51a.wav", 37, a51a()),# high sine breaks
    "52a": AudioFile("52a.wav", 29, a52a()),# high sine
    "53a": AudioFile("53a.wav", 32, a53a()),# constant
    "54a": AudioFile("54a.wav", 30, a54a()),# constant breaks
    "55a": AudioFile("55a.wav", 30, a55a()),# constant breaks faster
    "100a": AudioFile("100a.wav", 90, a100a()),# high sine fast
    "101a": AudioFile("101a.wav", 89, a101a()),# square peaks breaks
    "102a": AudioFile("102a.wav", 89, a102a()),# square peaks
    "103a": AudioFile("103a.wav", 89, a103a()),# buzzsaw high
    # pain start
    "200a": AudioFile("200a.wav", 19, None),
    "201a": AudioFile("201a.wav", 18, None),
    "202a": AudioFile("202a.wav", 19, None),
    "203a": AudioFile("203a.wav", 19, None),
    "204a": AudioFile("204a.wav", 18, None),
    "205a": AudioFile("205a.wav", 9, None),
    "206a": AudioFile("206a.wav", 11, None),
    "207a": AudioFile("207a.wav", 14, None),
    "208a": AudioFile("208a.wav", 17, None),
    "209a": AudioFile("209a.wav", 18, None),
    "210a": AudioFile("210a.wav", 20, None),
    "211a": AudioFile("211a.wav", 23, None),
    "212a": AudioFile("212a.wav", 25, None),
    "213a": AudioFile("213a.wav", 25, None),
    "214a": AudioFile("214a.wav", 29, None),
    "215a": AudioFile("215a.wav", 20, None),
    "216a": AudioFile("216a.wav", 20, None),
    "217a": AudioFile("217a.wav", 20, None),
    "218a": AudioFile("218a.wav", 19, None),
    "219a": AudioFile("219a.wav", 29, None),
    "220a": AudioFile("220a.wav", 28, None),
    "221a": AudioFile("221a.wav", 27, None),
    "222a": AudioFile("222a.wav", 19, None),
    "223a": AudioFile("223a.wav", 19, None),
    "224a": AudioFile("224a.wav", 19, None),
    # pain end
    "calibrate": AudioFile("calibrate.wav", 60, calibration()),
}


if __name__ == '__main__':
    exit(common_main("audio_mansion.py", FILES, sys.argv))
