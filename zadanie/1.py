#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Подсчитайте количество гласных в строке, введенной
    # с клавиатуры с использованием множеств.
    if __name__ == "__main__":
        words = {'а', 'у', 'е', 'о', 'э', 'я', 'и', 'ю', 'ё', 'ы'}
        string = list(input('Введите строку: ').lower())
        count = 0
        for i, slov in enumerate(string):
            if slov in words:
                count += 1
        print(count)
