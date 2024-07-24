import tkinter as tk
from tkinter import messagebox
import pymysql

class Bank:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank")

        scrn_width = self.root.winfo_screenwidth()
        scrn_height = self.root.winfo_screenheight()
        self.root.geometry(f"{scrn_width}x{scrn_height}+0+0")

        # Label for bank management
        main_label = tk.Label(self.root, text="BANK MANAGEMENT SYSTEM", font=("Arial", 49, "bold"), bg="light green", bd=5, relief="groove")
        main_label.pack(side="top")

        # Main Frame
        mainframe = tk.Frame(self.root, bg="light grey", bd=5, relief="ridge")
        mainframe.place(x=500, y=140, width=450, height=600)

        # Open Account button
        open_account = tk.Button(mainframe, command=self.open_ac, text="Open Account", width=20, bg="light blue", bd=3, relief="raised", font=("Arial", 20, "bold"))
        open_account.grid(row=0, column=1, padx=40, pady=50)

# Deposit button
        deposit = tk.Button(mainframe,command=self.deposit, text="Deposit", width=20, bg="light blue", bd=3, relief="raised", font=("Arial", 20, "bold"))
        deposit.grid(row=1, column=1, padx=40, pady=50)

# Withdraw button
        withdraw = tk.Button(mainframe,command=self.withdraw, text="Withdraw", width=20, bg="light blue", bd=3, relief="raised", font=("Arial", 20, "bold"))
        withdraw.grid(row=2, column=1, padx=40, pady=50)

#check balance
        check_balance= tk.Button(mainframe,command=self.checkbalance, text="Check Balance", width=20, bg="light blue", bd=3, relief="raised", font=("Arial", 20, "bold"))
        check_balance.grid(row=3, column=1, padx=40, pady=50)

    def open_ac(self):
        self.open_ac_frame = tk.Frame(self.root, bg="light grey", bd=5, relief="ridge")
        self.open_ac_frame.place(x=450, y=140, width=500, height=600)

# Username
        uname = tk.Label(self.open_ac_frame, text="Username:", bg="light grey", font=("Arial", 15, "bold"))
        uname.grid(row=0, column=0, padx=20, pady=30)

        self.uname_in = tk.Entry(self.open_ac_frame, width=15, font=("Arial", 15))
        self.uname_in.grid(row=0, column=1, padx=15, pady=30)

# Password field
        password_ac = tk.Label(self.open_ac_frame, text="Password:", bg="light grey", font=("Arial", 15, "bold"))
        password_ac.grid(row=1, column=0, padx=20, pady=30)

        self.pwd_in = tk.Entry(self.open_ac_frame, show="*", width=15, font=("Arial", 15))  
        self.pwd_in.grid(row=1, column=1, padx=15, pady=30)

# Confirm password field
        cnf_pwd = tk.Label(self.open_ac_frame, text="Confirm Password:", bg="light grey", font=("Arial", 15, "bold"))
        cnf_pwd.grid(row=2, column=0, padx=20, pady=30)

# password input
        self.cpwd_in = tk.Entry(self.open_ac_frame, show="*", width=15, font=("Arial", 15)) 

        self.cpwd_in.grid(row=2, column=1, padx=15, pady=30)

 # OK button
        ok_btn = tk.Button(self.open_ac_frame, width=10, text="OK", command=self.insert, bg="light blue", bd=5, relief="raised", font=("Arial", 15, "bold"))
        ok_btn.grid(row=4, column=0, padx=40, pady=90)

# Close button
        close_btn = tk.Button(self.open_ac_frame, width=10, text="Close", bg="light blue", command=self.close_open_ac, bd=5, relief="raised", font=("Arial", 15, "bold"))
        close_btn.grid(row=4, column=1, padx=40, pady=90)

#close open account Frame function
    def close_open_ac(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to close?"):
            self.open_ac_frame.destroy()
#open account details insert in database
    def insert(self):
        username = self.uname_in.get()
        password = self.pwd_in.get()
        cnfpassword = self.cpwd_in.get()    
    
        if username != "" and password != "" and cnfpassword != "":    
            if password == cnfpassword:
            
                try:
# Using 'with' to manage database connection
                    with pymysql.connect(host="localhost", user="root", passwd="7379", database="bankdb") as con:
                        cur = con.cursor()
                        cur.execute("INSERT INTO account(username, password) VALUES(%s, %s)", (username, password))
                        con.commit()
                    messagebox.showinfo("Success", "ACCOUNT OPENED SUCCESSFULLY!")
                    self.open_ac_frame.destroy()
                except pymysql.MySQLError as e:
                    messagebox.showerror("Database Error", f"Error: {e}")
            else:
                messagebox.showerror("ERROR", "Confirm password and password did not match!")
                self.clear()
         
                
#clear in openACCount
    def clear(self):
        # self.uname_in.delete(0,tk.END)
        self.pwd_in.delete(0,tk.END)
        self.cpwd_in.delete(0,tk.END)
        
#deposit function        
    def deposit(self):
       
        self.deposit_frame= tk.Frame(self.root, bg="light grey", bd=5, relief="ridge")
        self.deposit_frame.place(x=450, y=140, width=500, height=600)
#name
        name = tk.Label(self.deposit_frame, text="Username:", bg="light grey", font=("Arial", 15, "bold"))
        name.grid(row=0, column=0, padx=20, pady=30)
#name input
        self.name_in = tk.Entry(self.deposit_frame, width=15, font=("Arial", 15))
        self.name_in.grid(row=0, column=1, padx=15, pady=30)

#Amount
        amount = tk.Label(self.deposit_frame, text="Enter Amount:", bg="light grey", font=("Arial", 15, "bold"))
        amount.grid(row=1, column=0, padx=20, pady=30)

#Amount input
        self.amt_in = tk.Entry(self.deposit_frame, width=15, font=("Arial", 15))  
        self.amt_in.grid(row=1, column=1, padx=15, pady=30)

# deposit button
        ok = tk.Button(self.deposit_frame,command=self.deposit_amount, width=10, text="Deposit",  bg="light blue", bd=5, relief="raised", font=("Arial", 15, "bold"))
        ok.grid(row=2, column=0, padx=50, pady=70)

# Close button
        close = tk.Button(self.deposit_frame, width=10, text="Close", bg="light blue", command=self.close_deposit, bd=5, relief="raised", font=("Arial", 15, "bold"))
        close.grid(row=2, column=1, padx=50, pady=70)

#close deposit window
    def close_deposit(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to close?"):
            self.deposit_frame.destroy()

#deposit amount function            
    def deposit_amount(self):   
        name=self.name_in.get()
        amount=self.amt_in.get() 


        if name != "" and amount != "":    
                try:
#database connection
                    with pymysql.connect(host="localhost", user="root", passwd="7379", database="bankdb") as con:
                        cur = con.cursor()
                        cur.execute("select balance from account where username=%s",(name))
                        data=cur.fetchone()
                        if data:
                            balance=data[0]
                            if balance is None:
                                balance=0
                            
                            updatedamount=balance +float(amount)
                            
                            if messagebox.askyesno("Confirm", "Are you sure you want to deposit?"):
                                cur.execute("update account set balance=%s where username=%s",(updatedamount,name))
                                con.commit()
                            
                                messagebox.showinfo("Success", "Amount ₹ "+amount+" deposited in "+name.upper()+" account SUCCESSFULLY!")

                            else:
                                messagebox.showinfo("Cancelled", "Deposit cancelled.")

                            self.deposit_frame.destroy()
                        else:
                            messagebox.showerror("ERROR", "INVALID USER!")
                            self.name_in.delete(0,tk.END)
                            self.amt_in.delete(0,tk.END)
                                        
                except pymysql.MySQLError as e:
                    messagebox.showerror("Database Error", f"Error: {e}")
        else:
                messagebox.showerror("ERROR", "Field Empty!")
#withdraw                
    def withdraw(self):  
         
         self.withdraw_frame= tk.Frame(self.root, bg="light grey", bd=5, relief="ridge")
         self.withdraw_frame.place(x=450, y=140, width=500, height=600)
#name
         wname = tk.Label(self.withdraw_frame, text="Username:", bg="light grey", font=("Arial", 15, "bold"))
         wname.grid(row=0, column=0, padx=20, pady=30)
#name input
         self.wname_in = tk.Entry(self.withdraw_frame, width=15, font=("Arial", 15))
         self.wname_in.grid(row=0, column=1, padx=15, pady=30)

#Amount
         wamount = tk.Label(self.withdraw_frame, text="Enter Amount:", bg="light grey", font=("Arial", 15, "bold"))
         wamount.grid(row=1, column=0, padx=20, pady=30)

#Amount input
         self.wamt_in = tk.Entry(self.withdraw_frame, width=15, font=("Arial", 15))  
         self.wamt_in.grid(row=1, column=1, padx=15, pady=30)

# deposit button
         ok = tk.Button(self.withdraw_frame,command=self.withdraw_amount, width=10, text="Withdraw",  bg="light blue", bd=5, relief="raised", font=("Arial", 15, "bold"))
         ok.grid(row=2, column=0, padx=50, pady=70)

# Close button
         wclose = tk.Button(self.withdraw_frame, width=10, text="Close", bg="light blue", command=self.close_withdraw, bd=5, relief="raised", font=("Arial", 15, "bold"))
         wclose.grid(row=2, column=1, padx=30, pady=70)

#balance check
         ok = tk.Button(self.withdraw_frame,command=self.checkbalance, width=13, text="balance check",  bg="light blue", bd=5, relief="raised", font=("Arial", 15, "bold"))
         ok.grid(row=3, column=0, padx=30, pady=50)

         

    def withdraw_amount(self):
         name=self.wname_in.get()
         amount=self.wamt_in.get()
         if name != "" and amount != "":
            try:
                amount = float(amount)  # Convert amount to float
                # Database connection
                with pymysql.connect(host="localhost", user="root", passwd="7379", database="bankdb") as con:
                    cur = con.cursor()
                    cur.execute("SELECT balance FROM account WHERE username=%s", (name,))
                    data = cur.fetchone()

                    if data:
                        balance = data[0] if data[0] is not None else 0

                        # Check if the withdrawal amount is less than or equal to the balance
                        if amount <= balance:
                            if messagebox.askyesno("Confirm", f"Are you sure you want to withdraw ₹{amount}?"):
                                updated_amount = balance - amount
                                cur.execute("UPDATE account SET balance=%s WHERE username=%s", (updated_amount, name))
                                con.commit()

                                messagebox.showinfo("Success", f"Amount ₹{amount} withdrawn from {name.upper()}'s account SUCCESSFULLY!")
                                self.withdraw_frame.destroy()
                            else:
                                messagebox.showinfo("Cancelled", "Withdrawal cancelled.")
                        else:
                            messagebox.showerror("ERROR", "Insufficient balance for this withdrawal!")
                    else:
                        messagebox.showerror("ERROR", "INVALID USER!")
                        self.wname_in.delete(0, tk.END)  # Clear the username input
                        self.wamt_in.delete(0, tk.END)    # Clear the amount input

            except ValueError:
                messagebox.showerror("ERROR", "Please enter a valid amount.")
                self.wamt_in.delete(0, tk.END)  # Clear the amount input
            except pymysql.MySQLError as e:
                messagebox.showerror("Database Error", f"Error: {e}")
         else:
             messagebox.showerror("ERROR", "Please fill in all fields!")  
    #close deposit window
    def close_withdraw(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to close?"):
            self.withdraw_frame.destroy()

#check balance            
    def checkbalance(self):  
         
         self.checkbalance_frame= tk.Frame(self.root, bg="light grey", bd=5, relief="ridge")
         self.checkbalance_frame.place(x=450, y=140, width=500, height=600)
#name
         wname = tk.Label(self.checkbalance_frame, text="Username:", bg="light grey", font=("Arial", 15, "bold"))
         wname.grid(row=0, column=0, padx=20, pady=30)
#name input
         self.wname_in = tk.Entry(self.checkbalance_frame, width=15, font=("Arial", 15))
         self.wname_in.grid(row=0, column=1, padx=15, pady=30)

#Amount
         wamount = tk.Label(self.checkbalance_frame, text="Enter Amount:", bg="light grey", font=("Arial", 15, "bold"))
         wamount.grid(row=1, column=0, padx=20, pady=30)

#Amount input
         self.wamt_in = tk.Entry(self.checkbalance_frame, width=15, state=tk.DISABLED, font=("Arial", 15))  
         self.wamt_in.grid(row=1, column=1, padx=15, pady=30)

# balance check button
         ok = tk.Button(self.checkbalance_frame,command=self.check_amount, width=10, text="Balance",  bg="light blue", bd=5, relief="raised", font=("Arial", 15, "bold"))
         ok.grid(row=2, column=0, padx=50, pady=70)

# Close button
         wclose = tk.Button(self.checkbalance_frame, width=10, text="Close", bg="light blue", command=self.check_balanceclose, bd=5, relief="raised", font=("Arial", 15, "bold"))
         wclose.grid(row=2, column=1, padx=50, pady=70)

    def check_balanceclose(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to close?"):
            self.checkbalance_frame.destroy()  

    def check_amount(self):
         name=self.wname_in.get()
        #  amount=self.wamt_in.get()
         if name != "":    
                try:
#database connection
                    with pymysql.connect(host="localhost", user="root", passwd="7379", database="bankdb") as con:
                        cur = con.cursor()
                        cur.execute("select balance from account where username=%s",(name))
                        data=cur.fetchone()
                        if data:
                            balance=data[0]
                            self.wamt_in.config(state=tk.NORMAL)
                            self.wamt_in.insert(0,"₹"+str(balance))
                            
                            

                     
                        else:
                            messagebox.showerror("ERROR", "INVALID USER!")
                            self.wname_in.delete(0,tk.END)
                            
                                       
                except pymysql.MySQLError as e:
                    messagebox.showerror("Database Error", f"Error: {e}")
         else:
                messagebox.showerror("ERROR", "Field Empty!")  
#main window
root = tk.Tk()
obj = Bank(root)
root.mainloop()
