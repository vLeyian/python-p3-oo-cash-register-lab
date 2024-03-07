#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0):
    self.discount=discount
    self.total=0
    self.items=[]
    self.void_last_transaction_amount=0

  def add_item(self,title,price,quantity=1):
    total=price*quantity 
    self.last_transaction_amount=total 
    self.price=price
    self.total+=total 
    self.items.extend([title] * quantity)  

  def apply_discount(self):
    if self.discount>0:
      discount_amount=self.total*(self.discount/100)
      (self.total)-=int(discount_amount)
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def items_list_without_multiples(self):
        new_list=list(set(self.items))
        return new_list
  
  def void_last_transaction(self):
        if self.items:
            self.total -= self.last_transaction_amount 
        else:
            print("No transactions to void.")
     