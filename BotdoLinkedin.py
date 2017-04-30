# Bot for getting friends in LinkedIn.
# Coded by Carlos Daniel Giovanella
# Macro made by me aswell
# Requirements: Python 3+, iMacros, and Firefox.
# Not tested on Linux/MacOS based systems

import subprocess , sys , os
def inicio():
	os.system("cls")
	print (' -----------------------------Made by--------------------------------------')
	print ('  # Carlos Daniel Giovanella (car.dangi@hotmail.com)')
	print ('  # ')
	print ('  # Facebook: www.fb.com/KiritoKirigayaKazutoKunZ')
	print ('  # Github: github.com/cardangi')
	print ('  # LinkedIn: https://www.linkedin.com/in/carlos-d-870792128/')
	print ('  # ')
	print ('  # usage: --v1 (run in normal slowly and limitated mode, add 1000 connections in like 5 hours')
	print ('  # usage: --v2 (run in the best mode, with timings, add 5000 connections in 2~3 hours')
	print ('  # usage: --help (more info about the usage)')
	print ('  # I do not take any responsibility and i are not liable for any damage caused.')
	print (' -------------------------------------------------------------------------')

try:
	if sys.argv[1] == "--v1":
		subprocess.call([r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe', '-new-tab', 'imacros://run/?m=MacroLinkedin.iim'])
	if sys.argv[1] == "--v2":
		subprocess.call([r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe', '-new-tab', 'imacros://run/?m=MacroLinkedinV2.iim'])
	if sys.argv[1] == "--help":
		print ("\n\n\n\n\n\n\n\n\n\n\n\n\n")
		print ("--v1 : Version 1, 100% working")
		print ("--v2 : Version2 , beta test, maybe 100% working (?) any issue needs to be reported.")
except IndexError:
	inicio()
