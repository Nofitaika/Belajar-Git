Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data3 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
>>> data3
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
>>> ganjil = []
>>> for i in data3:
	if i%2 == 1;
		ganjil.append(i)
ganjil
SyntaxError: invalid syntax
>>> for i in data3:
	if i%2 == 1 :
		ganjil.append(i)

		
>>> ganjil
[1, 3, 5, 7, 9, 11, 13]
>>> genap = [ x for in data3 if x%2 == 0 ]
SyntaxError: invalid syntax
>>> genap = [ x for x in data3 if x%2 == 0 ]
>>> genap
[2, 4, 6, 8, 10, 12]
>>> # dictionary
>>> kota : {'jkt': 'Jakarta', 'bdg' : 'Bandung', 'sby' : 'Surabaya'}
>>> type(kota)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    type(kota)
NameError: name 'kota' is not defined
>>> kota : {'jkt': 'Jakarta', 'bdg' : 'Bandung', 'sby' : 'Surabaya'}
>>> kota ={'jkt': 'Jakarta', 'bdg' : 'Bandung', 'sby' : 'Surabaya'}
SyntaxError: multiple statements found while compiling a single statement
>>> kota = {'jkt': 'Jakarta', 'bdg' : 'Bandung', 'sby' : 'Surabaya'}
>>> type(kota)
<class 'dict'>
>>> for k,v in kota.items():
	print ("%s -> %s" % (k,v))

	
jkt -> Jakarta
bdg -> Bandung
sby -> Surabaya
>>> for k,v in kota.items():
	print(k,v)

	
jkt Jakarta
bdg Bandung
sby Surabaya
>>> for k,v in kota.items():
	print( k, "->" , v)

	
jkt -> Jakarta
bdg -> Bandung
sby -> Surabaya
>>> # Tuple
>>> daftar = {'butterfly' : 'kupu-kupu', 'elephant' : 'gajah', 'girrafe' : 'jerapah'}
>>> def kamus(a):
for k,v in daftar.items():
	if a = k	
	print(v)
	
SyntaxError: expected an indented block
>>> def kamus(a):
	for k,v daftar.items():
		
SyntaxError: invalid syntax
>>> def kamus(a):
	daftar = {'butterfly' : 'kupu-kupu', 'elephant' : 'gajah', 'girrafe' : 'jerapah'}
	for k,v in daftar.items():
		if a == k:
			return(v)

		
>>> kamus(butterfly)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    kamus(butterfly)
NameError: name 'butterfly' is not defined
>>> kamus('butterfly')
'kupu-kupu'
>>> def kamus():
	a=input('Kata apa yang ingin kamu tahu?')
	a = a.lower()
	daftar = {'butterfly' : 'kupu-kupu', 'elephant' : 'gajah', 'girrafe' : 'jerapah'}
	for k,v in daftar.items():
		if a == k:
			return(v)
		else:
			print('Oops maaf saya tidak bisa membantumu')

			
>>> kamus()
Kata apa yang ingin kamu tahu?Aku
Oops maaf saya tidak bisa membantumu
Oops maaf saya tidak bisa membantumu
Oops maaf saya tidak bisa membantumu
>>> def kamus():
	a=input('Kata apa yang ingin kamu tahu?')
	a = a.lower()
	daftar = {'butterfly' : 'kupu-kupu', 'elephant' : 'gajah', 'girrafe' : 'jerapah'}
	for k,v in daftar.items():
		if a == k:
			return(v)
		else:
			return('Oops maaf saya tidak bisa membantumu')

		
>>> kamus()
Kata apa yang ingin kamu tahu?Akus
'Oops maaf saya tidak bisa membantumu'
>>> kamus()
Kata apa yang ingin kamu tahu?ButTerfly
'kupu-kupu'
>>> kamus()
Kata apa yang ingin kamu tahu?butterfly 
'Oops maaf saya tidak bisa membantumu'
>>> def kamus():
	a=input('Kata apa yang ingin kamu tahu?')
	a = a.lower()
	a = a.replace(' ',)
	daftar = {'butterfly' : 'kupu-kupu', 'elephant' : 'gajah', 'girrafe' : 'jerapah'}
	for k,v in daftar.items():
		if a == k:
			return(v)
		else:
			return('Oops maaf saya tidak bisa membantumu')

		
>>> kamus()
Kata apa yang ingin kamu tahu?butterfly 
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    kamus()
  File "<pyshell#57>", line 4, in kamus
    a = a.replace(' ',)
TypeError: replace() takes at least 2 arguments (1 given)
>>> def kamus():
	a=input('Kata apa yang ingin kamu tahu?')
	a = a.lower()
	a = a.replace(' ','')
	daftar = {'butterfly' : 'kupu-kupu', 'elephant' : 'gajah', 'girrafe' : 'jerapah'}
	for k,v in daftar.items():
		if a == k:
			return(v)
		else:
			return('Oops maaf saya tidak bisa membantumu')

		
>>> kamus()
Kata apa yang ingin kamu tahu?Butterfly 
'kupu-kupu'
>>> kamus()
Kata apa yang ingin kamu tahu?
'Oops maaf saya tidak bisa membantumu'
>>> 
