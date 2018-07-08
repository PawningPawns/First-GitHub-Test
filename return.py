print("Hellow World!")

class Transaction:
  
  sales_tax = 0.1
  
  def __init__(self, total, discount_rate):
    self.total = total
    self.tax = Transaction.sales_tax * total
    self.discount = disocunt_rate 
    self.total_discount = int(total - (total * discount))
    
    
  def change_rate(self):
    self.change_rate = self.total
    return self.change_rate
  
  def output_value(self):
    self.output = self.total
    self.discount_output = self.total_discount
    
    return self.output
    return self.discount_output
  
  def print_value(self):
    
    print('{} tax, {} total, {} discounted total'.format(Transaction.sales_tax, self.output, self.discount_output))
    
sale_input = int(input())

sale_discount = int(input))

foo1 = Transaction(sale_input, sale_discount)

foo1.print_value()

print('{} total, {} discount'.format(foo1.total, foo1.discount))
