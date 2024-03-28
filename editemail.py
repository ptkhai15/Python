User = input("Please enter your name: ")
User_Edit = User.replace(" ","")
Company_Name = input("Pelase enter your company name: ")
Company_Edit = Company_Name.replace(" ","")
Email_Address = User_Edit + "@" + Company_Edit + ".com"
Email_Edit = Email_Address.lower()
print("Email_Address: ", Email_Edit)
