#!/usr/bin/env python
#-*- coding: utf-8 -*-

import subprocess
import platform
import os

def sendmessage(message, title, icona):
	if (icona == 'busv'):
		if (platform.system() == 'Linux'):
			subprocess.Popen(['notify-send', title, message, '--icon=%s/bus.png' % (os.getcwd())])
		elif (platform.system() == 'Darwin'):
			subprocess.Popen(['terminal-notifier', "-message", message, "-title", title])
	elif (icona == 'busr'):
		if (platform.system() == 'Linux'):
			subprocess.Popen(['notify-send', title, message, '--icon=%s/busrosso.png' % (os.getcwd())])
		elif (platform.system() == 'Darwin'):
			subprocess.Popen(['terminal-notifier', "-message", message, "-title", title])

