#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time


def say_hello(name):
    print("Hello, " + name)


if __name__ == "__main__":
    name = input("What's your name：")
    say_hello(name)
    time.sleep(10)