from notificator import sendmessage
from check import orariFermata
import time


ris = orariFermata(1724)
while True:
	for el in ris:
		if (el['orario'][0] < 10):
			sendmessage ("Mancano %s minuti per il %s" % (str(el['orario'][0]), str(el['linea'])), "Pullman")
	time.sleep (60)
