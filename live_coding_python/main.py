#!/usr/bin/env python3
# coding: utf-8
'''
Very basic CLI program
Made in a livecoding session at school, in
order to present in a very quick course the
Python language.

Can be a base for newcoming projects for my
colleagues who want to train their python coding.
'''
import sys
from mymodule import functions

FUNCS = {
    't': functions.get_hour,
    'm': functions.get_weather,
    'e': functions.get_env,
    'i': functions.get_ip
}


def main():
    '''
    Main function of the program.
    Executes the function based on argv[1]
    '''
    try:
        arg = sys.argv[1]
        arg_func = sys.argv[2]
        FUNCS[arg](arg_func)
    except IndexError:
        print(sys.argv[0], " [-i|-t|-m|-e [to_find]]")
        sys.exit(1)
    except KeyError:
        print("Unknown arg:", arg)
        sys.exit(2)


if __name__ == "__main__":
    main()
