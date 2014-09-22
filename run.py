#!/usr/bin/env python3

import control
from morse import morse

while True:
    userinput = input("Enter a phrase, or press enter to quit: ")
    if userinput == "":
        quit()

    for character in userinput:
        signals = morse[character.upper()]
        for signal in signals:
            print(signal, end="", flush=True)
            control.blink(signal)
    print()
