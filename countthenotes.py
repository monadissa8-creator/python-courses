amount=int(input("pleas enter amount for withdraw:"))
note1=amount//100
note2=(amount % 100)//50
note3=((amount%100)%50)//10
print("notes of 100 Rs",note1)
print("note of 50 Rs",note2)
print("note of 10 Rs",note3)