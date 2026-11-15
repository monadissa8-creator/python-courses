sn=random.randint(1,50)
a=0
ma=5
while a<ma:
    num=int(input("enter a number:"))
    a+=1
    if num ==sn:
        print("you wine when you gess the secrot number")
        break
    else:
        d=abs(sn-num)
        if d>=20:
            print("hint ice cold")
        elif d>=10:
            print("hint  cold")
        elif d>=5:
            print("hint warm")
        else:
            print("hint hot")