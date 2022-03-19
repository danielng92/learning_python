price=int(input("Enter price: "))
if price >= 300 and price >0:
    price=price-(price*30/100)
    print(price)
elif price >= 200 or price < 300 and price >0:
    price=price-(price*20/100)
    print(price)
elif price >= 100 or price < 200 and price >0:
    price=price-(price*10/100)
    print(price)
elif price < 100 and price >0:
    price=price-(price*5/100)
    print(price)
elif price < 0:
    print("No discount")