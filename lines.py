#open the file, read only
#s = open('lines.txt', 'r')
#This file is updated. 
datafile = file('lines.txt')
string1 = "HELO something"
for line in datafile:
	if string1 in line:
		print '250 something'
	else:
		print "500 wtf"
