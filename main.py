import json
import random
import string
from pathlib import Path

class Bank:
    data_Base = "data.json"
    data = [] # Dummy data

    try:
        if Path(data_Base).exists:
            with open(data_Base, 'r') as fs:
                data = json.loads(fs.read())
        else:
            print("NO SUCH FILE EXISTS")
    except Exception as error:
        print(f"Error occured as {error}")

    @classmethod
    def __update(cls):
        with open(cls.data_Base, "w") as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __generate_acc_no(cls):
        num = random.choices(string.digits, k = 11)
        # alpha = random.choices(string.ascii_uppercase, k = 3)
        special_char = random.choices("@#$&!", k = 1)
        id = num + special_char
        random.shuffle(id)
        return "".join(id)
    
    @classmethod
    def generate_ifsc_code(cls):
        alpha = random.choices(string.ascii_uppercase, k = 4)
        num = random.choices(string.digits, k = 5)
        id2 = alpha + num
        return "".join(id2)



    def Create_account(self):
        info = {
            "Name"  : input("Name    : "),
            "Age"   : int(input("Age : ")),
            "E-mail" : input("E-mail  : "),
            "PIN"   : int(input("PIN     : ")),
            "Account_No": Bank.__generate_acc_no(),
            "IFSC CODE" : Bank.generate_ifsc_code(),
            "Balance" : 0
        }

        if info['Age'] < 18 or len(str(info['PIN'])) != 4:
            print("SORRY,YOUR ARE NOT ELIGIABLE FOR ACCOUNT CREATION\n\n")
        else:
            print("\n======================YOUR DETAILS=========================\n")
            for i in info:
                print(f"{i} : {info[i]}")
            print("========NOTE DOWN YOUR ACCOUNT NUMBER and IFSC CODE carefully====\n\n")
            Bank.data.append(info)
            Bank.__update()

    def Deposit_money(self):
        acc_no = input("Enter your Account Number : ")
        ifsc_code = input("Enter your IFSC CODE : ")
        pin = int(input("Enter your 4-digits PIN : "))

        user_data = [i for i in Bank.data if i['Account_No'] == acc_no and i['IFSC CODE'] == ifsc_code and i['PIN'] == pin]

        if bool(user_data) == False:
            print("xxxxxxxxxxxxxxxx{ NO SUCH ACCOUNT EXISTS }xxxxxxxxxxxxxxxx\n\n")
        else:
            amount = int(input(("Enter your Deposit amount : ")))

            if 100000 < amount < 0:
                print("The Amount must be between 0 to 100000\n\n")
            else:
                user_data[0]['Balance'] += amount
                Bank.__update()
                print("AMOUNT DEPOSIT SUCESSFULLY\n")

    def Withdrew_money(self):
        print("\n======================FILL THE DETAILS=========================\n\n")
        acc_no = input("Enter your Account Number : ")
        ifsc_code = input("Enter your IFSC CODE : ")
        pin = int(input("Enter your 4-digits PIN : "))

        user_data = [i for i in Bank.data if i['Account_No'] == acc_no and i['IFSC CODE'] == ifsc_code and i['PIN'] == pin]

        if bool(user_data) == False:
            print("xxxxxxxxxxxxxxxx{ NO SUCH ACCOUNT EXISTS }xxxxxxxxxxxxxxxx\n\n")
        else:
            amount = int(input(("Enter your Withdrew amount : ")))

            if user_data[0]['Balance'] < amount < 0:
                print("WITHDREW AMOUNT INSUFFICIENT\n\n")
            else:
                user_data[0]['Balance'] -= amount
                print("AMOUNT WITHDREW SUCCESFULLY\n\n")
                Bank.__update()

    def show_details(self):
        print("\n=========================FILL THE DETAILS=========================\n")
        acc_no = input("Enter your Account Number : ")
        ifsc_code = input("Enter your IFSC CODE : ")
        pin = int(input("Enter your 4-digits PIN : "))
        user_data = [i for i in Bank.data if i["Account_No"] == acc_no and i["IFSC CODE"] == ifsc_code and i["PIN"] == pin]

        if bool(user_data) == False:
            print("xxxxxxxxxxxxxxxx{ NO SUCH ACCOUNT EXISTS }xxxxxxxxxxxxxxxx\n\n")
        else:
            print("\n=================================YOUR DETAILS=================================\n")
            for i in user_data[0]:
                print(f"{i} : {user_data[0][i]}")
            
    def update_details(self):
        print("\n=========================FILL THE DETAILS=========================\n")
        acc_no = input("Enter your Account Number : ")
        ifsc_code = input("Enter your IFSC CODE : ")
        pin = int(input("Enter your 4-digits PIN : "))

        user_data = [i for i in Bank.data if i["Account_No"] == acc_no and i["IFSC CODE"] == ifsc_code and i["PIN"] == pin]

        if bool(user_data) == False:
            print("xxxxxxxxxxxxxxxx{ NO SUCH ACCOUNT EXISTS }xxxxxxxxxxxxxxxx\n\n")
        else:
            print("Press enter to skip")
            new_data = {
                "Name"   : input("Name    : "),
                "E-mail" : input("E-mail  : "),
                "PIN"    : input("PIN     : "),
            }
            if new_data["Name"] == "":
                new_data["Name"] = user_data[0]["Name"]

            if new_data["E-mail"] == "":
                new_data["E-mail"] = user_data[0]["E-mail"]
            
            if new_data["PIN"] == "":
                new_data["PIN"] = user_data[0]["PIN"]

            new_data['Age']         = user_data[0]["Age"]
            new_data['Account_No']  = user_data[0]["Account_No"]
            new_data['IFSC CODE']   = user_data[0]["IFSC CODE"]
            new_data['Balance']     = user_data[0]["Balance"]

            if type(new_data["PIN"]) == str:
                new_data['PIN'] = int(new_data["PIN"])

            for i in new_data:
                if  new_data[i] == user_data[0][i]:
                    continue
                else:
                    user_data[0][i] = new_data[i]
            
            Bank.__update()
            print("DETAILS UPDATED SUCCESSFULLY\n\n")

    def Delete_Account(self):
        print("\n=========================FILL THE DETAILS=========================\n")
        acc_no = input("Enter your Account Number : ")
        ifsc_code = input("Enter your IFSC CODE : ")
        pin = int(input("Enter your 4-digits PIN : "))

        user_data = [i for i in Bank.data if i["Account_No"] == acc_no and i["IFSC CODE"] == ifsc_code and i["PIN"] == pin]

        if bool(user_data) == False:
            print("xxxxxxxxxxxxxxxxxxxxx{ NO SUCH ACCOUNT EXISTS }xxxxxxxxxxxxxxxxxxxxxxxxx\n\n")
        else:
            option = input("DO you really want to Delete your Account (Yes/No) : ").upper()
            print(option)
            if option == "YES":
                index = Bank.data.index(user_data[0])
                Bank.data.pop(index)
                print("ACCOUNT DELETED SUCCESSFULY")
                Bank.__update()
            else:
                print("YOUR ACCOUNT IS SAFE")
                print(option)

user = Bank()
print("\n============================================== WELCOME TO APNA BANK =====================================================\n")

while True:
    print("\n========================= SELECT YOUR OPERATION =========================\n")
    print("1. Creating an Account.")
    print("2. Deposit Money.")
    print("3. Withdraw Money.")
    print("4. Know your details.")
    print("5. Update details.")
    print("6. Delete-Account.")
    print("7. Exit\n")

    choice = int(input("Enter your choice : "))
    
    if choice == 1:
        user.Create_account()
    
    elif choice == 2:
        user.Deposit_money()

    elif choice == 3:
        user.Withdrew_money()

    elif choice == 4:
        user.show_details()
    
    elif choice == 5:
        user.update_details()
    
    elif choice == 6:
        user.Delete_Account()

    else:
        print("Existing program.....")
        break