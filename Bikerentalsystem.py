class bikerental:
    def __init__(self,stock):
        self.stock=stock
    def displaybike(self):
        print("Available stock is:",self.stock)
    
    def rentbike(self,qty):
        if qty>self.stock:
            print("Please enter the value which is less than the stock")
        elif qty<0:
            print("Please enter the positive value or greater than 0")
        else:
            self.stock=self.stock-qty
            print("The rent of one bike is 350")
            print("Rent which you pay",qty*350)
            print("Now available bike is :",self.stock)
obj=bikerental(100)   
while True:
    n=input('''
            1 Show the available stock of bike
            2 Give me bikes for rent
            3 Thanks I want to leave
          ''')
    if n=="1":
        obj.displaybike()
    elif n=="2":
        qty=int(input("enter the quantity which you want")) 
        obj.rentbike(qty)
    elif n=="3":
        break
    else:
        print("invalid choice please cboose 1,2 or 3")
