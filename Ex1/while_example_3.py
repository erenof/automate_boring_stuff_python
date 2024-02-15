spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue # Hace que vuelva al while
    print("spam is " + str(spam))
