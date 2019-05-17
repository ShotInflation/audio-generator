import itertools
import os
from collections import namedtuple
from itertools import chain
from math import pi

import audiogen
import numpy as np
from audiogen import tone
from audiogen.sampler import FRAME_RATE
from audiogen.util import envelope, constant
from numpy.ma import sin

AudioFile = namedtuple("AudioFile", ["filename", "seconds", "stream"])


def repeatlist(it, count):
    """
    Repeat volume stream
    :param it: original stream (will be enumerated)
    :param count: how many cycles to repeat
    :return: new volume stream
    """
    cache = []
    for value in it:
        yield value
        cache.append(value)
    for i in range(0, count - 1):
        for value in cache:
            yield value


def linear(start, end, seconds):
    """
    Generate volume based on a linear function
    :param start: start volume
    :param end: end volume
    :param seconds: length in seconds
    :return: volume stream
    """
    def f(t):
        x1 = 0.0
        y1 = float(start)
        x2 = float(seconds * FRAME_RATE)
        y2 = float(end)
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        return m * t + b
    xs = np.linspace(0, float(seconds) * FRAME_RATE, seconds * FRAME_RATE)
    return itertools.imap(f, xs)


def flat(value, seconds):
    """
    Generate a linear stream with same start and end volumes
    :param value: volume
    :param seconds: length in seconds
    :return: volume stream
    """
    return itertools.repeat(value, int(seconds * FRAME_RATE))


def sound():
    """
    base sound to use
    :return: sine wave at 150Hz
    """
    return tone(150)


def invert(point, stream):
    """
    Mirror stream vertically
    :param point: the mirror line
    :param stream: original volume
    :return: new volume stream
    """
    return itertools.imap(lambda y: point * 2 - y, stream)


def sine_wave(cycle_count, cycle_length, top, bottom):
    """
    Generate a volume stream based on a sine wave. length is cycle_count * cycle_length
    :param cycle_count: stream length in periods
    :param cycle_length: period length in seconds
    :param top: highest volume
    :param bottom: lowest volume
    :return: volume stream
    """
    return complex_sine_wave(0, cycle_count, cycle_length, top, bottom)


def complex_sine_wave(start, cycle_count, cycle_length, top, bottom):
    """
    Generate a volume stream based on a sine wave. length is cycle_count * cycle_length
    :param start: how many periods to delay. 0.5 delay produces a cosine wave.
    :param cycle_count: stream length in periods
    :param cycle_length: period length in seconds
    :param top: highest volume
    :param bottom: lowest volume
    :return: volume stream
    """
    length = cycle_count * cycle_length
    freq = 1.0 / cycle_length
    x_offset = start * cycle_length * FRAME_RATE
    xs = np.linspace(x_offset, x_offset + float(length) * FRAME_RATE, length * FRAME_RATE)
    amp = (top - bottom) / 2.0
    bump = bottom + amp

    def f(x):
        return float(bump + amp * sin(2 * pi * x * freq / FRAME_RATE))

    return itertools.imap(f, xs)


def dip(length, top, bottom):
    """
    Downward slope and rise. Half of a sine wave.
    :param length: length in seconds
    :param top: start and end
    :param bottom: lowest point
    :return: volume stream
    """
    dip_amount = top - bottom
    return invert(top, sine_wave(0.5, length * 2, top + dip_amount, bottom))


def pulse(top, bottom, length, times):
    """
    Square wave
    :param top: high point
    :param bottom: low point
    :param length: cycle length in seconds, including one top and one bottom
    :param times: cycle count
    :return: volume stream
    """
    return repeatlist(chain(
        flat(top, length / 2.0),
        flat(bottom, length / 2.0),
    ), times)


def pause(sec):
    """
    helper to generate silence
    :param sec: length in seconds
    :return: volume stream
    """
    return flat(0, sec)


def common_main(script_name, files, argv):
    assert len(argv) >= 2, "Usage: python {} folder [filename1] [filename2]...".format(script_name)
    folder = argv[1]
    if len(argv) == 3:
        filenames = argv[2:]
    else:
        filenames = None
    if not os.path.exists(folder):
        os.mkdir(folder)

    for name, value in files.items():
        if value.stream is not None and (filenames is None or name in filenames):
            print "Writing " + value.filename
            with open(os.path.join(folder, value.filename), 'wb') as f:
                audiogen.sampler.write_wav(f, envelope(envelope(sound(), value.stream), constant(0.01)))
            print "Done"
        else:
            print "Skipping " + value.filename

    return 0
