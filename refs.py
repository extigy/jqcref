import re
import sys

def getyear(s):
	yearline = re.findall(r'year\s*=\s*.*',s)
	if yearline:
		yearstring = re.findall(r'[0-9]+',yearline[0])[0]
		return yearstring
	else:
		return None

def cmp(a, b):
	if not getyear(a) or not getyear(b):
		return -1
	if int(float(getyear(a))) > int(float(getyear(b))):
		return 1
	elif int(float(getyear(a))) == int(float(getyear(b))):
		return 0
	else:
		return -1

#refoldfile = open('refold.bib', 'r')
entires = re.findall(r'@.*\{.*\n(?:.*=.*\n)*\}', sys.stdin.read() ,re.I)
newentries = []
for entry in entires:
	#print ("---------Found entry----------")
	label = "ERROR" # incase it all goes wrong search output for ERROR
	authorline = re.findall(r'author\s*=\s*.*',entry,re.I)
	yearstring = getyear(entry)
	if authorline:
		#print  "authorline: ", authorline[0]
		cleanauthorline = re.split(r'\s*=\s*', authorline[0])[1][1:-2] # get rid of = and the opening/closing {},
		authorstrings = re.split(r'\s+and\s+', cleanauthorline) # split by author
		authorsurnames = []
		for authorstring in authorstrings:
			#Lets find some names! 
			#first check for a ,
			surnamecommastring = re.findall(r'.*,',authorstring)
			if surnamecommastring:
				yay = surnamecommastring[0][0:-1]
				cleanname = re.sub(r"([^A-za-z]|\\|\^)", "", yay)
				authorsurnames.append(cleanname)
			else:
				#separate and take last part!
				nameparts = re.split(r'(?:\.|\s)+', authorstring)
				cleanname = re.sub(r"([^A-za-z]|\\|\^)", "", nameparts[-1])
				authorsurnames.append(cleanname)

		#print what we found
		#print "Parsed authors: ", authorsurnames
		if authorsurnames:
			label = '_'.join(authorsurnames[:2]).lower()
		if yearstring:
			label = label + "_" + yearstring
		#print "Using label: ", label
		splitcomma = re.split(r',', entry)
		splitcomma[0] = re.sub(r"(\{.*)", "{"+label, splitcomma[0])
		newentry =  ','.join(splitcomma)
		newentries.append(newentry)
	else:
		#print  "No authors found, falling back..."
		newentries.append(entry)

newentries.sort(cmp)
print '\n'.join(newentries);