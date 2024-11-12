#from nrclex import NRCLex
class OnlineShop_ChatBot:
    def __init__ (self, user_name, order_number):
        self.user_name = user_name
        self.order_number = order_number
        
    def welcome(self):
        print(f'\nHello {self.user_name}, welcome to our AI Customer Service!')
        print("I'm here to assist you with any issues related to our products or services.")
        print("Choose what you need help with.\n")
        print("----------------------------------------------------------") 

        
            
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
                
                user_choice = input("Choose your complaint ")
                if user_choice == "1":
                    print("You selected: Return item")
                    print("please ship the item back at your local usps to start the refund and returning process")

                    break  
                elif user_choice == "2":
                    print("You selected: Request refund")
                    print("----------------------------------------------------------")  
                    print("please ship the item back at your local usps to start the refund process")
                    break 
                elif user_choice == "3":
                    print("You selected: Change shipping address")
                    new_shipping_address =input("ENTER NEW SHIPPING ADDRESS") 
                    print(f"Shipping address updated to: {new_shipping_address}")
                elif user_choice == "4":
                    print("You selected: Track my order")
                    print("----------------------------------------------------------") 
                    print("Your order in currecnt in china")
                    break
                elif user_choice == "5":
                    print("You selected: Ask about product details")
                    questionAked = input("ENTER YOUR QUESTION ") 
                    print("if your expericening any issues with our product please watch a Youtube video on how to fix it.")
                    break
            except ValueError:
                print("----------------------------------------------------------")
                print("Invalide input. Please choose from options 1 to num")
    def user_rated_experience(self):
        print("----------------------------------------------------------")
        print(f'\nLastly, {self.user_name}, can you rate your experience with us?')
        
        
        while True:
            try:
                user_experience = int(input("Type in your experience from 1 to 5: "))
                if user_experience < 2:
                    print("We are sorry for the negative experience")
                elif user_experience < 4:
                    print("Thank you for your feedback. We'll try to improve.")
                elif user_experience <= 5:
                    print("Thank you for the positive feedback!")
                else:
                    print("Invalid rating. Please enter a number between 1 and 5.")
                break 
            except ValueError:
                print("Please enter a number from 1 to 5.") 
        
        #emotion = NRCLex(user_experience)
        #emotions = emotion.top_emotions
            
        #if emotions:
            #returned_emotion = emotions[0][0]
            #print(f"Your experience was {returned_emotion}")
            #if returned_emotion in ["joy", "trust", "anticipation"]:
                #print("Thank you for the positive feedback")
            #elif returned_emotion in ["anger", "fear", "sadness"]:
                #print("we are soory for the negative experince")
            #else:
                #print("thank you we'll try to improve")
        #else:
            #print(f"Thank you for your feedback.\n have a nice day")

        
        
 
def main():
     name = True
     chatbot = None
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
            chatbot.user_rated_experience()
if __name__ == "__main__":
    main()