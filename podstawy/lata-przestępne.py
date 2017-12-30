rok = int(input("podaj rok\n"))
print(rok) 
if rok % 400 == 0:
	print("przestępny")
elif rok % 4 == 0 and rok % 100 != 0:
	print("przestępny")
else:
	print("nie jest przestępny")
	
