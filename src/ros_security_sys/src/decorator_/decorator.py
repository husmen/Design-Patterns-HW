class Abstract_Coffee(object):

   def get_cost(self):
      pass

   def get_ingredients(self):
      pass
   
   def get_tax(self):
      return 0.1*self.get_cost()

class Concrete_Coffee(Abstract_Coffee):
   
   def get_cost(self):
      return 1.00
   
   def get_ingredients(self):
      return 'coffee'

class Abstract_Coffee_Decorator(Abstract_Coffee):
   
   def __init__(self,decorated_coffee):
      self.decorated_coffee = decorated_coffee
   
   def get_cost(self):
      return self.decorated_coffee.get_cost()
   
   def get_ingredients(self):
      return self.decorated_coffee.get_ingredients()

class Sugar(Abstract_Coffee_Decorator):
   
   def __init__(self,decorated_coffee):
      Abstract_Coffee_Decorator.__init__(self,decorated_coffee)
   
   def get_cost(self):
      return self.decorated_coffee.get_cost()
   
   def get_ingredients(self):
	   return self.decorated_coffee.get_ingredients() + ', sugar'

class Milk(Abstract_Coffee_Decorator):
   
   def __init__(self,decorated_coffee):
      Abstract_Coffee_Decorator.__init__(self,decorated_coffee)
   
   def get_cost(self):
      return self.decorated_coffee.get_cost() + 0.25
   
   def get_ingredients(self):
      return self.decorated_coffee.get_ingredients() + ', milk'

class Vanilla(Abstract_Coffee_Decorator):
   
   def __init__(self,decorated_coffee):
      Abstract_Coffee_Decorator.__init__(self,decorated_coffee)
   
   def get_cost(self):
      return self.decorated_coffee.get_cost() + 0.75
   
   def get_ingredients(self):
      return self.decorated_coffee.get_ingredients() + ', vanilla'

if __name__ == "__main__":
    myCoffee = Concrete_Coffee()
    print('Ingredients: '+myCoffee.get_ingredients()+
    '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

    myCoffee = Milk(myCoffee)
    print('Ingredients: '+myCoffee.get_ingredients()+
    '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

    myCoffee = Vanilla(myCoffee)
    print('Ingredients: '+myCoffee.get_ingredients()+
    '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

    myCoffee = Sugar(myCoffee)
    print('Ingredients: '+myCoffee.get_ingredients()+
    '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))