#!/usr/bin/env python3

import time
import click

from rpi_ws281x import PixelStrip, Color
import argparse

# LED strip configuration:
LED_COUNT = 4        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Define functions which animate LEDs in various ways.
def colorWipe(color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    global strip
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

def setColor(color):
    """Sets the color of all pixels."""
    global strip
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

def clear():
    """Clears all pixels."""
    setColor(Color(0, 0, 0))


@click.group()
def cli():
    pass

@cli.command()
def off():
    click.echo('Turn all pixels off')
    clear()

@cli.command()
@click.argument('color', type=(int,int,int))
def color(color):
    click.echo('Set all pixels to color')
    setColor(Color(*color))


cli.add_command(off)
cli.add_command(color)

if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    global strip
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    cli()
