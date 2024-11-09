class OnlineShop_ChatBot:
    def __init__ (self, user_name):
        self.user_name = user_name
        #self.order_number = order_numer
        def welcome(self):
            print(f'\nHello {self.user_name}, welcome to our AI Customer Service!')
            print("I'm here to assist you with any issues related to our products or services.")
            print("Let’s get started by choosing what you need help with.\n")

            self.show_options()
    def get_user_choices(self):
        while True:
            try:
                print("still impelementing")
            except ValueError:
                print("Invalide input. Please choose from options 1 to num")
        
        
        
 
def main():
     name = True
     chatbot = OnlineShop_ChatBot()
     while name:  
        user_name = input("ENTER USERNAME: ").strip()
        if user_name == "":
            print("Username is blank. Please try again.")
        else:
            name = False
            chatbot.welcome(user_name)
            chatbot.get_user_choice()
if __name__ == "__main__":
    main()