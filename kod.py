ålder = int(input("Hur gammal är du?"))

if(ålder > 18):
    print("Du är myndig")
elif(ålder < 12):
    print("Du är ett barn")
else:
    print("Jag har inget att säga om din ålder")