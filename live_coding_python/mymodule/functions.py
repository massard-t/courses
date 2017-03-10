#!/usr/bin/env python3
# coding: utf-8
# Module de gestion des commandes
import os
import datetime
import socket
import requests

# TODO ADD Try/Catch

def get_hour(arg=None):
    now = datetime.datetime.now()
    now_month = now.month
    now_day = now.day
    now_hour = now.hour
    now_minutes = now.minute
    now_seconds = now.second
    print("%i/%i  %i:%i:%i" % (now_month, now_day, now_hour, now_minutes,
        now_seconds))


def get_ip(arg=None):
    local_ip = socket.gethostbyname(socket.gethostname())
    print("private ip:", local_ip)
    public_ip = requests.get("http://www.icanhazip.com/")
    print("public ip: ", public_ip.text)


def get_weather(arg=None):
    response = requests.get("http://wttr.in/")
    current_weather = response.text
    print(current_weather)


def get_env(var_to_find=None):
    variable_content = os.environ.get(var_to_find, 'Unknown')
    print(var_to_find, ":", variable_content)


