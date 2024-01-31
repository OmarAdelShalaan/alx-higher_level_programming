#!/usr/bin/python3
for i in range(0, 80):
        if i % 10 == i / 10:
                continue
        print(f'{i:02d},', end = ' ')
print(f'{99}')