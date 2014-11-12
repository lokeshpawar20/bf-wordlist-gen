#!/usr/bin/python -tt
from itertools import product
global len 
global charset
length=0
charset=[]
def leninput():
	""" This Function takes Length of Wordlist"""
	global length
	try:	
		length=input('Enter the length of Dictionary : ')
	except NameError:
		print 'Length should be numeric value'
		leninput()
	except SyntaxError:
		print 'Please enter apprepiate input'
		leninput()
def displaydomain():
	"""This Function Show predefined character set domain for wordlist"""
	print 'enter 1  for alpha_lowercase 		abcdefghijklmnopqrstuvwxyz'
	print 'enter 2  for ALPHA_UPPERCASE 		ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	print 'enter 3  for Numeric 	    		0123456789'
	print 'enter 4  for alphanumeric_lowecase 	abcdefghijklmnopqrstuvwxyz0123456789'
	print 'enter 5  for ALPHANUMERIC_UPPERCASE 	ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	print 'enter 6  for Alpha_Allcase		abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	print 'enter 7  for Alphanumeric_Allcase 	abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	print "enter 8  for Special_Char	 	@%+\\#/'!$^?:.(){}[]~`-_|<>"
	print "enter 9  for Numeric_Special_Char	@%+\\#/'!$^?:.(){}[]~`-_|<>0123456789"
	print "enter 10 for alpha_lower_special_char 	abcdefghijklmnopqrstuvwxyz@%+\\#/'!$^?:.(){}[]~`-_|<>"
	print "enter 11 for ALPHA_UPPER_special_char  	ABCDEFGHIJKLMNOPQRSTUVWXYZ@%+\\#/'!$^?:.(){}[]~`-_|<>"
	print "enter 12 for Alpha_Allcas_special_char	abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@%+\\#/'!$^?:.(){}[]~`-_|<>"	
	print "enter 13 for Alphanum_Allcas_spe_char 	abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@%+\\#/'!$^?:.(){}[]~`-_|<>"
	print "enter 14 for enter manually"
def chardomainput(sindex=0):
	"""This function takes input for damain set for specific position"""
	try:
		for i in range(sindex,length):
			displaydomain()
			a=input(str(i+1)+'th char: ')
			if a==1:
				charset.insert(i,['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
			elif a==2:
				charset.insert(i,['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
			elif a==3:
        	                charset.insert(i,['0','1','2','3','4','5','6','7','8','9'])
			elif a==4:
				charset.insert(i,['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'])
			elif a==5:
				charset.insert(i,['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9'])
			elif a==6:
				charset.insert(i,['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
			elif a==7:
				charset.insert(i,['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9'])
			elif a==8:
				charset.insert(i,['@','%','+',"\\",'/','\'','!','#','$','^','?',':','.','(',')','{','}','[',']','~','-','_','`'])
			elif a==9:
				charset.insert(i,['@','%','+',"\\",'/','\'','!','#','$','^','?',':','.','(',')','{','}','[',']','~','-','_','`','0','1','2','3','4','5','6','7','8','9'])
			elif a==10:
				charset.insert(i,['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','@','%','+',"\\",'/','\'','!','#','$','^','?',':','.','(',')','{','}','[',']','~','-','_','`'])
			elif a==11:
				charset.insert(i,['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','@','%','+',"\\",'/','\'','!','#','$','^','?',':','.','(',')','{','}','[',']','~','-','_','`'])
			elif a==12:
				charset.insert(i,['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','@','%','+',"\\",'/','\'','!','#','$','^','?',':','.','(',')','{','}','[',']','~','-','_','`'])
			elif a==13:
				charset.insert(i,['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','@','%','+',"\\",'/','\'','!','#','$','^','?',':','.','(',')','{','}','[',']','~','-','_','`'])
			elif a==14:
				charset.insert(i,raw_input('enter characterset saparated by space: ').split())
			else:
				print 'wrong choice'
				i-=1
        except NameError:
                print 'Choice should be numeric'
                chardomainput(i)
        except SyntaxError:
                print 'Please enter apprepiate input'
                chardomainput(i)
def printdict(fname):
	"""It generates wordlist"""
	global charset
	f=open(fname,'w')
	for i in product(*charset):
		print ''.join(i)
		f.write(''.join(i))
		f.write('\n')
	f.close()
def main():
	leninput()
	chardomainput()
	fname=raw_input("Enter the filename:")
	size=1
	for i in charset:
                size*=len(i)
	print 'File Size would be around %d Bytes, do you want to continue Y or N'%(size*(length+1))
	c=raw_input()
	if c=='Y' or 'y':
                printdict(fname)
if __name__=='__main__':
	main()
