#!/usr/bin/env python
#-*- coding: utf-8 -*-

import subprocess
import platform

def sendmessage(message, title):
	if (platform.system() == 'Linux'):
		subprocess.Popen(['notify-send', title, message, '--icon=dialog-information'])
	elif (platform.system() == 'Darwin'):
		subprocess.Popen(['terminal-notifier', "-message", message, "-title", title])

