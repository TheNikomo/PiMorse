#!/usr/bin/env python3

import control
from morse import morse

userinput = input("Enter a phrase: ")
for character in userinput:
    signals = morse[character.upper()]
    for signal in signals:
        control.blink(signal)

