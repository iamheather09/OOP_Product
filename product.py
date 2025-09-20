class product:

    inventory = []      
    product_counter = 0          

    def __init__(self,product_id, name, category, quantity, price, supplier): 
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    @classmethod
    def add_product(cls, name, category, price, supplier):
        product_id = (product.product_counter) + 1
        new_product = product(product_id, name, category, 0, price, supplier)
        product.inventory.append(new_product)
        product.product_counter += 1
        return ("Product added succesfully")


                                 
    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
       for prd in product.inventory:
           if prd.product_id == product_id:
                if quantity is not None:
                    prd.quantity = quantity
                if price is not None:
                    prd.price = price
                if supplier is not None:
                    prd.supplier = supplier
                return ("Product information updated successfuly")
           return("Product not found")

    @classmethod
    def delete_product(cls, product_id):
        for prd in product.inventory:
            if prd.product_id == product_id:
                product.inventory.remove(prd)
                return "Product deleted successfully" 
            
            
    
class order:
     order_list = []
     order_counter = 0
     def __init__(self, order_id, product_id, quantity):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

     def place_order(self):
        
        return f"Order placed successfuly. Order ID: {self.order_id}"
        
                  
p1 = product.add_product("Laptop", "Electronics", 50, 1000)
print(p1)
p2 = product.add_product("Laptop", "Electronics", 50, "Supplier A")
print(p2) 
p3 = product.update_product(1, quantity=45, price=950)
print(p3)
p4 = product.delete_product(2)
print(p4)
order1 = order(order_id=1, product_id=1, quantity=2)
print(order1.place_order())   



        
        

