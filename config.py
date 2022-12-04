#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = "5507245538:AAHanmyr-_aLK36wVehqHNrKjJpknq9q618"


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = 5080899
    API_HASH = "6fc7f813cf96e6692990b752b43fd9c7"


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    
