ac=float(input("pleas enter the actual product price"))
sa=float(input("pleas enter the sale amount"))
if (sa>ac):
    amt=sa-ac
    print("total profit ={0}".format(amt))
else:
    print("no profit ")