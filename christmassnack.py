userinput = int(input('ENTER NUMBER OF SUCCESSFUL DELIVERY: '))
collectionrate1 = 160
collectionrate2 = 200
collectionrate3 = 250
collectionrate4 = 500
baserate = 5000

if (userinput < 50):
	print('WAGES OF THE DAY :' , ((userinput * collectionrate1) + baserate))

if (userinput >= 50 and userinput <= 59):
	print('WAGES Of THE DAY :' , ((userinput * collectionrate2) + baserate))

if (userinput >= 60 and userinput <= 69):
	print('WAGES OF THE DAY :' , ((userinput * collectionrate3) + baserate))

if (userinput >= 70):
	print('WAGES OF THE DAY :' , ((userinput * collectionrate4) + baserate))