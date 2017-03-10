#!/usr/bin/env python3
# coding: utf-8
import mymodule.functions
import sys

# Function Array
FUNCS = {
    't': mymodule.functions.get_hour,
    'm': mymodule.functions.get_weather,
    'e': mymodule.functions.get_env,
    'i': mymodule.functions.get_ip
}


def main():
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
