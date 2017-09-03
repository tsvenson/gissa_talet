#!/usr/bin/env python
"""Gissa Talet

Ett enkelt spel där din utmaning är att gissa vilket nummer som slumpmässigt valts av
datorn. Enda ledtråden är att spelet säger om din gissningen är högre eller lägre.
"""
import random

target = random.randint(1, 100)

print('Välkommen till Gissa Talet spelet!')
print('==================================')

guesses = 0
guess = 0

while guess != target:
    guesses += 1
    guess = int(input(f'Gissa vilket nummer jag tänker på [{guesses}]: '))
    if guess < target:
        print('För lågt gissat!')
    elif guess > target:
        print('För högt gissa!')

print('')
print('Bra gjort!')
print(f'Mitt nummer var {target} och du lyckades gissa rätt på bara {guesses} försök.')
