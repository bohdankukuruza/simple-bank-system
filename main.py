import colorama
import os
import AccountManager

class App:
    def __init__(self):
        colorama.init()
        self.account_manager = AccountManager.AccountManager()

        self.user = None
        self.username = None
        self.surname = None
        self.balance = None
        self.id = None

    def authentication(self):
        login_attempts = 0  

        while True:
            print("1. Login")
            print("2. Register")
            print("3. Quit")
            choice = input("Enter your choice: ")

            if choice == "1":
                for i in range(3 - login_attempts):
                    first_name = input("Enter your first name: ")
                    last_name = input("Enter your last name: ")
                    password = input("Enter your password: ")

                    try:
                        self.user = self.account_manager.login(first_name, last_name, password)

                        self.username = self.user["first_name"]
                        self.surname = self.user["last_name"]
                        self.balance = self.user["balance"]
                        self.id = self.user["id"]

                        self.clear()
                        print(colorama.Fore.GREEN + "Logged in successfully \n" + colorama.Style.RESET_ALL)
                        break
                    except Exception as e:
                        self.clear()
                        login_attempts += 1  
                        if login_attempts == 3:
                            print(colorama.Fore.RED + f"Error: {e} \n")
                            print(colorama.Fore.RED + "You have exceeded the maximum number of attempts \n" + colorama.Style.RESET_ALL)
                            self.quit()  
                        else:
                            print(colorama.Fore.RED + f"Error: {e} \n")
                            print(colorama.Fore.RED + f"Attempt {login_attempts + 1} of 3 \n" + colorama.Style.RESET_ALL)
                    else:
                        break
            elif choice == "2":
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                self.account_manager.register_user(first_name, last_name)

                self.clear()

                print(colorama.Fore.GREEN + "User registered successfully \n")
                print(colorama.Fore.RED + "Your password is your last name" + colorama.Style.RESET_ALL)
                print(colorama.Fore.RED + "Please change your password after login" + colorama.Style.RESET_ALL)
                
                self.user = self.account_manager.login(first_name, last_name, last_name.capitalize())
                self.username = self.user["first_name"]
                self.surname = self.user["last_name"]
                self.balance = self.user["balance"]
                self.id = self.user["id"]

                break

            elif choice == "3":
                self.quit()
                break
            else:
                print("Invalid choice")
            
            if self.user:
                break

    def run(self):
        self.clear()
        self.authentication()
        self.menu()

    def menu(self):
        print(colorama.Fore.GREEN + f"Welcome to CBFET bank {self.username} {self.surname}! \n" + colorama.Style.RESET_ALL)
        while True:
            print("1. Check balance")
            print("2. Lodge funds")
            print("3. Withdraw")
            print("4. Change password")
            print("5. Calculate interest")
            print("6. Statement")
            print("7. Quit\n")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.clear()
                print(colorama.Fore.GREEN + f"Your balance is: {self.balance} Euro \n" + colorama.Style.RESET_ALL)

            elif choice == "2":
                amount = float(input("Enter the amount you want to lodge: "))
                if amount <= 0:
                    print(colorama.Fore.RED + "Invalid amount \n" + colorama.Style.RESET_ALL)
                    continue

                self.balance = self.account_manager.lodge_funds(self.id, amount)
                self.clear()

                print(colorama.Fore.GREEN + f"Successfully lodged {amount} Euro" + colorama.Style.RESET_ALL)
                print(colorama.Fore.GREEN + f"Your new balance is: {self.balance} Euro \n" + colorama.Style.RESET_ALL)
                if self.balance >= 5000:
                    print(colorama.Fore.RED + "Your interest is 4% per year\n" + colorama.Style.RESET_ALL)
                else:
                    print(colorama.Fore.RED + "Your interest is 2% per year\n" + colorama.Style.RESET_ALL)

            elif choice == "3":
                amount = float(input("Enter the amount you want to withdraw: "))

                try:
                    self.balance = self.account_manager.withdraw(self.id, amount)
                except Exception as e:
                    self.clear()
                    print(colorama.Fore.RED + f"Error: {e} \n" + colorama.Style.RESET_ALL)
                    continue
                self.clear()
                print(colorama.Fore.GREEN + f"Successfully withdrew {amount} \n")
                print(colorama.Fore.GREEN + f"Your new balance is: {self.balance} Euro \n" + colorama.Style.RESET_ALL)

                if self.balance >= 5000:
                    print(colorama.Fore.RED + "Your interest is 4% per year\n" + colorama.Style.RESET_ALL)
                else:
                    print(colorama.Fore.RED + "Your interest is 2% per year\n" + colorama.Style.RESET_ALL)

            elif choice == "4":
                for i in range(3):
                    old_password = input("Enter your old password: ")
                    new_password = input("Enter your new password: ")
                    confirm_password = input("Confirm your new password: ")

                    if new_password != confirm_password:
                            self.clear()
                            print(colorama.Fore.RED + "Passwords do not match \n" + colorama.Style.RESET_ALL)
                            break

                    try:
                        self.account_manager.change_password(self.id, old_password, new_password)

                        self.clear()
                        print(colorama.Fore.GREEN + "Password changed successfully \n" + colorama.Style.RESET_ALL)
                        break
                    except Exception as e:
                        self.clear()
                        print(colorama.Fore.RED + f"Error: {e} \n")
                        print(colorama.Fore.RED + f"Attempt {i + 1} of 3 \n" + colorama.Style.RESET_ALL)
                else:
                    self.clear()
                    print(colorama.Fore.RED + "You have exceeded the maximum number of attempts \n" + colorama.Style.RESET_ALL)
                    self.quit()

            elif choice == "5":
                self.clear()
                percents, interest = self.account_manager.calculate_interest(self.id)
                total_interest = sum(interest)
                print(colorama.Fore.GREEN + f"Your total interest is: {total_interest:.2f} Euro")
                print(colorama.Fore.GREEN + f"Your monthly interest breakdown:")
                for i, value in enumerate(interest):
                    print(colorama.Fore.RED + f"Month {i + 1}: " + colorama.Fore.GREEN + f"{value} Euro - " + f"{percents[i] * 100}%" + colorama.Style.RESET_ALL)
                print()

            elif choice == "6":
                self.clear()
                print(colorama.Fore.MAGENTA + "------- Statement -------")
                print(colorama.Fore.GREEN + f"ID: {self.id}")
                print(colorama.Fore.MAGENTA + "--------------------------" + colorama.Style.RESET_ALL)
                print(colorama.Fore.GREEN + f"Name: {self.username} {self.surname}")
                print(colorama.Fore.MAGENTA + "--------------------------" + colorama.Style.RESET_ALL)
                print(colorama.Fore.GREEN + f"Balance: {self.balance} Euro")
                print(colorama.Fore.MAGENTA + "--------------------------" + colorama.Style.RESET_ALL)
                if self.balance >= 5000:
                    print(colorama.Fore.GREEN + "Interest rate: 4%")
                else:
                    print(colorama.Fore.GREEN + "Interest rate: 2%")
                print(colorama.Fore.MAGENTA + "--------------------------\n" + colorama.Style.RESET_ALL)


            elif choice == "7":
                self.quit()

            else:
                print("Invalid choice")

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def quit(self):
        self.clear()
        print(colorama.Fore.CYAN + "Goodbye!\n")
        exit()

if __name__ == '__main__':
    app = App()
    app.run()