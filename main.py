

class OnlineShop_ChatBot:
    def __init__ (self, user_name, order_number):
        self.user_name = user_name
        self.order_number = order_number
        
    def welcome(self):
        print(f'\nHello {self.user_name}, welcome to our AI Customer Service!')
        print("I'm here to assist you with any issues related to our products or services.")
        print("Let\'s get started by choosing what you need help with.\n")
        print("-----------------------------") 

        
            
    def get_user_choices(self):
        user_choices = [
        "1: return item",
        "2: request refund", 
        "3: change shipping address",
        "4: track my order",
        "5: ask about product details",
    ]
        while True:
            try:
                for choices in user_choices:
                    print(choices)
                
                user_choice = input("Choose your complaint")
                if user_choice == "1":
                    print("You selected: Return item")
                    break  
                elif user_choice == "2":
                    print("You selected: Request refund")
                    print("-----------------------------") 
                    print("please ship the item back at your local usps to start the refund process")
                    break 
                elif user_choice == "3":
                    print("You selected: Change shipping address")
                    newShippingAddress =input("ENTER NEW SHIPPING ADDRESS") 
                elif user_choice == "4":
                    print("You selected: Track my order")
                    print("-----------------------------") 
                    print("Your order in currecnt in china")
                elif user_choice == "5":
                    print("You selected: Ask about product details")
                    questionAked = input("ENTER YOUR QUESTION") 
            except ValueError:
                print("Invalide input. Please choose from options 1 to num")
        
        
        
 
def main():
     name = True
     chatbot = OnlineShop_ChatBot()
     while name:  
        user_name = input("ENTER USERNAME: ").strip()
        if user_name == " ":
            print("Username is blank. Please try again.")
        else:
            while True:
                order_number = input("ENTER ORDER NUMBER (must start with 'NO' and have 8 digits after it): ").strip()
                if order_number[:2] == "NO" and order_number[2:].isdigit() and len(order_number[2:]) == 8:
                    break
                else:
                    print("Invalid order number. It must start with 'NO' and has 8 numbers.")
            chatbot = OnlineShop_ChatBot(user_name, order_number) 
            name = False   
            chatbot.welcome()
            chatbot.get_user_choices()