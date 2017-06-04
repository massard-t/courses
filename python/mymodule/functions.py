#!/usr/bin/env python3
# coding: utf-8
'''
Functions for mymodule

Made at school, for a Python course.
'''
# Module de gestion des commandes
import os
import datetime
import socket
import requests


def get_hour(_=None):
    'Prints the date.'
    now = datetime.datetime.now()
    now_month = now.month
    now_day = now.day
    now_hour = now.hour
    now_minutes = now.minute
    now_seconds = now.second
    print("%i/%i  %i:%i:%i" % (  # Changed indentation -> Lisibility
        now_month,
        now_day,
        now_hour,
        now_minutes,
        now_seconds
        )
         )


def get_ip(_=None):
    '''
    Gets local and public IP address
    '''
    local_ip = socket.gethostbyname(socket.gethostname())
    print("private ip:", local_ip)
    public_ip = requests.get("http://www.icanhazip.com/")  # try/catch
    print("public ip: ", public_ip.text)


def get_weather(_=None):
    '''Returns the weather for the actual location'''
    response = requests.get("http://wttr.in/")  # Should try/catch every req
    current_weather = response.text
    print(current_weather)


def get_env(arg=None):
    '''
    Prints an environment variable
    '''
    variable_content = os.environ.get(arg, 'ERROR: Unknown')
    print(arg, ":", variable_content)
