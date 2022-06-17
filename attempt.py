class Cart:
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def show_cart(self):
        if not self.items:
             print('You have no items in your cart.')
        else:
            display_cart = []
            for obj in self.items:
                if obj.name not in [i ['name'] for i in display_cart]:
                    display_cart.append({
                        'name' :obj.name,
                        'price': obj.price
                        })
                           
                else:
                    for i in display_cart:
                        if i['name'] == obj.name:
                            i['price'] += obj.price
            for idx, item in enumerate(display_cart):
                print(f{idx+1}) {item['name']} @ ${item['price']} [{[obj.name for obj in self.items].count(item['name'])}
            print("=" * 60)

    def clear_cart(self):
        self.items.clear()
    
   
   
    class CartItem:
        def __init__ (self, name, price) :
            self.name = name
            self.price = price
    
class Shop:
    def run(self):
        #shopping begins by taking out a new cart
        cart = Cart()
        
           #add item to cart 
           
        item1= CartItem ("apple" , .59)
        item2= CartItem ("orange" , 1.19)  
        item3= CartItem ("banana" , 1.49)  
        item4= CartItem ("apple" , .59)  
        item5= CartItem ("snickers" , 1.59)  
        item6= CartItem ("tomatoe" , .69)  
        item7= CartItem ("yams" , .79) 
        
        cart.add_item(item1)
        cart.add_item(item2)
        cart.add_item(item3)
        cart.add_item(item4)
        cart.add_item(item5)
        cart.add_item(item6)
        cart.add_item(item7)
        
        cart.show_cart()
        
         #-remove item from cart    
        cart.remove_item("apple")
        cart.show_cart()
        
        #-remove allitem from cart 
        cart.clear_cart()
        cart.show_cart()
        
shopping_session = Shop()
shopping_session.run()
         