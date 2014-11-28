from notificator import sendmessage
from check import orariFermata
import time



while True:
	try:
		ris = orariFermata(1724)
		for el in ris:
			if ((el['orario'][0] < 12) and (el['orario'][0] >= 10)):
				sendmessage ("Mancano %s minuti per il %s" % (str(el['orario'][0]), str(el['linea'])), "Pullman", 'busv')
			elif ((el['orario'][0] < 6) and (el['orario'][0] >= 4)):
				sendmessage ("Mancano %s minuti per il %s" % (str(el['orario'][0]), str(el['linea'])), "Pullman", 'busr')
		print ris	
	except Exception:
		print "Eccezione"
	time.sleep (60)
	
