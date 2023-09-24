'''
AUTOMATED-TELLER-MACHINE PROJECT By:

Somo, Herbenne Rey V.
Flores, Bastian Bragi B.
Rapada, Benmar

Prof: Sir Madz

'''

import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog
import datetime

fontStyle = ("Times", 14, "italic")

class Accounts:
    def __init__(self, num, name, pin, bal):
        self.num = num
        self.name = name
        self.pin = pin
        self.bal = bal


class BankApp(tk.Tk):
    #FUNCTION FOR CURRENT TIME
    def update_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S %p | %x")
        self.time_label.config(text=current_time)
        self.time_label.after(1000, self.update_time)
    def __init__(self, accounts):
        super().__init__()
        self.title("BBB Automated Teller Machine")
        self.configure(bg="skyblue3")
        #CENTER THE WINDOW
        width_of_splash = 400
        height_of_splash = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_splash/2)
        y_coordinate = (screen_height/3)-(height_of_splash/3)
        self.geometry("%dx%d+%d+%d" % (width_of_splash, height_of_splash, x_coordinate, y_coordinate))
        #THIS IS WHERE THE DATA WILL INPUT
        self.a = accounts
        #FRAME FOR TIME
        self.time_frame = tk.Frame(self)
        self.time_frame.place(relx = 0.5, rely = 0.35, anchor = 'center')
        #LABEL AND DESIGN FOR TIME
        self.time_label = tk.Label(self.time_frame, font = ('Times', 20, 'bold'),fg='black', bg='white')
        self.time_label.pack()
        #THEN CALLING THE UPDATED TIME FUNCTION
        self.update_time()
        #FRAME FOR BBB LOGO
        self.bbb_frame = tk.Frame(self)
        self.bbb_frame.place(relx = 0.5, rely = 0.2, anchor = 'center')
        self.bbb_label = tk.Label(self.bbb_frame, text = "BBB ATM", font = ('Times', 50, 'bold'),fg='black', bg='white')
        self.bbb_label.pack()
        #FRAME FOR BOTH ACC NO. AND PIN
        self.login_frame = tk.Frame(self)
        self.login_frame.place(relx = 0.5, rely = 0.6, anchor = 'center' )
        self.login_frame.config(bg="gray")
        #ACC NO. LABEL / NAME
        self.num_label = tk.Label(self.login_frame, text = "Account Number: " , font = fontStyle)
        self.num_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.num_label.config (bg = "gray")
        #ACC NO. ENTRY / INPUT
        self.num_entry = tk.Entry(self.login_frame)
        self.num_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.num_entry.config(bg = "#e5e4e2")
        #PIN LABEL / NAME
        self.pin_label = tk.Label(self.login_frame, text = "PIN: " , font = fontStyle , fg = "#C04000")
        self.pin_label.grid(row = 1, column = 0, padx = 5, pady = 5,)
        self.pin_label.config(bg = "gray")
        #FUNCTION TO LIMIT THE INPUT INTO 6 CHARACTERS
        def validate_pin1(P):
            if len(P) <= 6:
                return True
            else:
                return False
        #PIN INPUT / ENTRY
        self.pin_entry = tk.Entry(self.login_frame, show = '*', validate="key", fg = "#C04000" , validatecommand=(self.login_frame.register(validate_pin1), '%P'))
        self.pin_entry.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.pin_entry.config (bg = "#e5e4e2")
        #BUTTON FOR LOGIN TO USE LOGIN FUNCTION
        self.login_button = tk.Button(self.login_frame, text = "LOG IN", font = ('Times', 9 ), command = self.login)
        self.login_button.grid(row = 2, column = 1, padx = 10, pady = 0, sticky="W")
        self.login_button.config(bg = "#7393B3")
        #BUTTON FOR REGISTER WITH REGISTER FUNCTION
        self.login_button = tk.Button(self.login_frame, text = "REGISTER", font = ('Times', 9 ) , command = self.register)
        self.login_button.grid(row = 2, column = 1, padx = 5, pady = 5, sticky="E")
        self.login_button.config(bg = "green")
        #BUTTON FOR EXIT FUNCTION
        self.exit_button = tk.Button(self.login_frame, text = "EXIT", font = ('Times', 9, "bold" ) , command = self.quit)
        self.exit_button.grid(row = 2 , column = 0, padx = 20, pady = 3, sticky="")
        self.exit_button.config(bg = "red")
    #LOGIN FUNCTION    
    def login(self):
        #CALLING OUT OR GETTING THE ENTRY FOR ACC NO. AND PIN
        num = self.num_entry.get()
        pin = self.pin_entry.get()

        #FOR LOOP IF THE GIVEN INPUT ARE TRUE
        for a_obj in self.a:
            if a_obj.num == num and a_obj.pin == pin:
                self.current_user = a_obj
                self.login_frame.destroy()
                self.main_menu()
                return
        #IF THE GIVEN PIN AND ACC NO. ARE NOT REGISTERED OR TRUE    
        messagebox.showerror("Error", "Invalid account number or pin.")
    #REGISTER FUNCTION AND FRAMES
    def register(self):
        #FRAME FOR REGISTER
        self.reg_frame = tk.Frame(self)
        self.reg_frame.place(relx = 0.5, rely = 0.6, anchor = 'center')
        self.reg_frame.config( bg = "gray")
        #LABEL FOR NAME
        self.name_label = tk.Label(self.reg_frame, text = "Name: ",font = fontStyle)
        self.name_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.name_label.config(bg="gray")
        #ENTRY / INPUT FOR NAME
        self.name_entry = tk.Entry(self.reg_frame)
        self.name_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.name_entry.config (bg = "#e5e4e2")
        #LABEL FOR ACC NO.
        self.num_label1 = tk.Label(self.reg_frame, text = "Account Number: ", font = fontStyle)
        self.num_label1.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.num_label1.config(bg = "gray")
        #ENTRY OR INPUT FOR ACC NO.
        self.num_entry1 = tk.Entry(self.reg_frame)
        self.num_entry1.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.num_entry1.config(bg = "#e5e4e2")
        #LABEL FOR PIN
        self.pin_label1 = tk.Label(self.reg_frame, text = "PIN: ", font = fontStyle , fg = "#C04000")
        self.pin_label1.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.pin_label1.config(bg = "gray")
        #LIMITING THE PIN INTO 6 CHARACTERS ONLY
        def validate_pin(P):
            if len(P) <= 6:
                return True
            else:
                return False
        #ENTRY OR INPUT FOR PIN
        self.pin_entry1 = tk.Entry(self.reg_frame, show = '*', validate="key", fg = "#C04000", validatecommand=(self.reg_frame.register(validate_pin), '%P'))
        self.pin_entry1.grid(row = 2, column = 1, padx = 10, pady = 10)
        self.pin_entry1.config (bg = "#e5e4e2")
        #CONFIRMATION BUTTON TO REGISTER THE INPUTED DATA
        self.reg_button = tk.Button(self.reg_frame, text = "REGISTER", command = self.create_account)
        self.reg_button.grid(row = 5, column = 1, padx = 10, pady = 10, sticky="E")
        self.reg_button.config(bg = "green")
        #I ADDED BACK BUTTON FOR CONVENIENCE, IF THE USER MISCLICK THE BUTTON IN LOGIN MENU
        self.reg_button = tk.Button(self.reg_frame, text = "BACK", command = self.reg_frame.destroy)
        self.reg_button.grid(row = 5, column = 1, padx = 10, pady = 10, sticky="W")
        self.reg_button.config(bg = "gray")
    #FUNCTIONS FOR CREATING AN ACCOUNT
    def create_account(self):
        #CALLING OUT THE INPUTED DATA FROM REGISTER FUNCTION
        name = self.name_entry.get()
        num = self.num_entry1.get()
        pin = self.pin_entry1.get()
        #FOR LOOP IF THE CODE IS SUCCESS
        for a_obj in self.a:
            #CONDITIONAL STATEMENT IF THE GIVEN ACCOUNT NUMBER IS ALREADY EXIST
            if a_obj.num == num:
                messagebox.showerror("Error", "Account number already exists.")
                return
        #IF THE NAME IS EMPTY RETURN ERROR
        if name == "":
            messagebox.showerror("Error", "Name is Empty")
            return
        #IF THE ACC NO. IS EMPTY RETURN ERROR
        elif num == "":
            messagebox.showerror("Error", "Account Number is Empty")
            return
        elif not num.isdigit():
            messagebox.showerror("Error", "Account Number Contains Character")
            return
        elif len(num) != 4:
            messagebox.showerror("Error", "Account Number must be 4 DIGITS")
            return
        #IF THE PIN IS EMPTY RETURN ERROR
        elif pin == "":
            messagebox.showerror("Error", "Pin is Empty")
            return
        #IF THE PIN CONTAINS CHARACTER RETURN ERROR
        elif not pin.isdigit():
            messagebox.showerror("Error", "Pin Contains Character")
            return
        #IF THE PIN IS NOT EQUAL TO 6 CHARACTERS RETURN ERROR
        elif len(pin) != 6:
            messagebox.showerror("Error", "Pin must be 6 DIGITS")
            return
        #ELSE WHEN THE IFS HAS NOT BEEN TRUE
        else:
            self.a.append(Accounts(num, name, pin, 0))
            messagebox.showinfo("Success", "Account successfully created.")
            self.reg_frame.destroy()
    #MENU FUNCTION FOR BALANCE, WITHDRAW, DEPOSIT, ETC.
    def main_menu(self):
        button_width = 12
        button_height = 2
        fontStyle = ("Arial", 10)
        #BUTTON FOR CHECKING BALANE WITH CHECK BAL FUNTION
        self.balance_button = tk.Button(self, text = "Check Balance", command = self.check_bal, font = fontStyle, width=button_width, height=button_height)
        self.balance_button.place(relx = 0.30, rely = 0.55, anchor = 'e')
        self.balance_button.config (bg = "floral white")
        #BUTTON FOR WITHDRAW WITH WITHDRAW FUNCTION
        self.withdraw_button = tk.Button(self, text = "Withdraw", command = self.withdraw, font = fontStyle, width=button_width, height=button_height)
        self.withdraw_button.place(relx = 0.30, rely = 0.65, anchor = 'e')
        self.withdraw_button.config (bg = "light blue")
        #BUTTON FOR DEPOSIT WITH DEPOSIT FUNCTION
        self.deposit_button = tk.Button(self, text = "Deposit", command = self.deposit, font = fontStyle, width=button_width, height=button_height)
        self.deposit_button.place(relx = 0.30, rely= 0.75, anchor= 'e')
        self.deposit_button.config (bg = "green")
        #WE ADDED TRANSFER BUTTON FOR TRANFER WITH TRANSFER FUNCTION
        self.transfer_button = tk.Button(self, text = "Transfer", command = self.transfer_cash, font = fontStyle, width=button_width, height=button_height)
        self.transfer_button.place(relx = 0.7, rely = 0.55, anchor = 'w')
        self.transfer_button.config (bg = "#708090")
        #WE ADDED CHANGE PIN BUTTON WITH CHANGE PIN FUNCTION
        self.changepin_button = tk.Button(self, text = "Change Pin", command = self.change_pin,font = fontStyle, width=button_width, height=button_height)
        self.changepin_button.place(relx = 0.7, rely = 0.65, anchor = 'w')
        self.changepin_button.config (bg = "light blue")
        #LOGOUT BUTTON
        self.logout_button = tk.Button(self, text = "Logout", command = self.logout,font = fontStyle, width=button_width, height=button_height)
        self.logout_button.place(relx = 0.7, rely = 0.75, anchor = 'w')
        self.logout_button.config(bg = "red")
    #FUNCTION FOR CHECKING BALANCE
    def check_bal(self):
            messagebox.showinfo("Balance", f"Your current balance is P{self.current_user.bal:,.2f}.")
    #FUNCTION FOR WITHDRAW        
    def withdraw(self):
        if self.current_user.bal < 200:
            messagebox.showerror("Error", "Cannot withdraw. Minimum balance is P200.")
            return
        while True:
            withdraw = simpledialog.askfloat("Withdraw", "Enter amount to withdraw: ")
            if withdraw > self.current_user.bal:
                messagebox.showerror("Error", "Invalid amount. Exceeded account balance.")
            elif withdraw < 200:
                messagebox.showerror("Error", "Invalid amount. Minimum is P200.")
            elif withdraw % 100 != 0:
                messagebox.showerror("Error", "Invalid amount. Please enter an amount that is divisible by 100.")
            else:
                break
        self.current_user.bal -= withdraw
        messagebox.showinfo("Success", f"Successfully withdrawn P{withdraw:,.2f}. Current balance is P{self.current_user.bal:,.2f}.")
    #FUNCTION FOR DEPOSIT    
    def deposit(self):
        while True:
            deposit = simpledialog.askfloat("Deposit", "Enter amount to deposit: ")
            if deposit < 200:
                messagebox.showerror("Error", "Invalid amount. Minimum is P200.")
            else:
                break
        self.current_user.bal += deposit
        messagebox.showinfo("Success", f"Successfully deposited P{deposit:,.2f}. Current balance is P{self.current_user.bal:,.2f}.")
    #TRANSFERING CASH FUNCTION
    def transfer_cash(self):
        if self.current_user.bal < 200:
            messagebox.showerror("Error", "Cannot transfer. Minimum balance is P200")
            return
        while True:
            transfer = simpledialog.askfloat("Transfer", "Enter amount to transfer: ")
            if transfer > self.current_user.bal:
                messagebox.showerror("Error", "Invalid amount. Exceeded account balance.")
            elif transfer < 200:
                messagebox.showerror("Error", "Invalid amount. Minimum is P200.")
            else:
                break
        account_numbers = [obj.num for obj in self.a if obj.num != self.current_user.num]
        to_account = simpledialog.askstring("Transfer", f"Enter account number to transfer to.\nAvailable accounts: {', '.join(account_numbers)}")
        for obj in self.a:
            if obj.num == to_account:
                obj.bal += transfer
                self.current_user.bal -= transfer
                messagebox.showinfo("Success", f"Successfully transferred P{transfer:,.2f} to {obj.name}.\nCurrent balance is P{self.current_user.bal:,.2f}.")
                return
        messagebox.showerror("Error", "Invalid account number.")
    #CHANGE PIN FUNCTION
    def change_pin(self):
        while True:
            new_pin = simpledialog.askstring("Change Pin", "Enter new pin: ", show='*')
            confirm_pin = simpledialog.askstring("Change Pin", "Confirm new pin: ", show='*')
            if new_pin == "" or confirm_pin == "":
                messagebox.showerror("Error", "Please enter a valid pin.")
            elif len(new_pin) != 6:
                messagebox.showerror("Error", "Pin must be 6 digits long.")
            elif not new_pin.isdigit():
                messagebox.showerror("Error", "Pin must contain only digits.")
            elif new_pin != confirm_pin:
                messagebox.showerror("Error", "Pin did not match. Please try again.")
            else:
                self.current_user.pin = new_pin
                messagebox.showinfo("Success", "Pin successfully changed.")
                return
    #LOGOUT FUNCTION
    def logout(self):
        self.destroy()
        app = BankApp(self.a)
        app.mainloop()
        
        
a = [Accounts("1111", "PRINCE", "111111", 10000.00)]
app = BankApp(a)
app.mainloop()


