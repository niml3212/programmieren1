from random import Random
def calcdiscount(age):
    if (not(-1 < age < 100)):
        print("Ungültiges Alter!")
    elif (age < 30):
        d
        print(f"Du kriegst nen Discount von {age}!")
    else:
        print("Du kriegst keinen Discount!")


alter = int(input("Dein Alter:"))
calcdiscount(alter)