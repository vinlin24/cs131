#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""joker.py

Code for question 12.

USAGE: ./joker.py
"""

class Joker:
    joke = "I dressed as a UDP packet at the party. Nobody got it."

    def change_joke(self):
        print(f'self.joke = {self.joke}')
        print(f'Joker.joke = {Joker.joke}')
        Joker.joke = "How does an OOP coder get wealthy? Inheritance."
        self.joke = "Why do Java coders wear glasses? They can't C#."
        print(f'self.joke = {self.joke}')
        print(f'Joker.joke = {Joker.joke}')

j = Joker()
print(f'j.joke = {j.joke}')
print(f'Joker.joke = {Joker.joke}')

j.change_joke()
print(f'j.joke = {j.joke}')
print(f'Joker.joke = {Joker.joke}')
