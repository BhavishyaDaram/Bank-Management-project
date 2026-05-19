import json
import random
import string
from pathlib import Path


class Bank:
    database = Path(__file__).parent / "data.json"
    data = []

    # Load existing data
    try:
        if database.exists():
            with open(database, 'r') as fs:
                data = json.load(fs)
        else:
            data = []
    except Exception as err:
        print(f"Error loading data: {err}")
        data = []

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        acc_id = alpha + num + spchar
        random.shuffle(acc_id)
        return "".join(acc_id)

    def Createaccount(self):
        name = input("Tell your name :- ")
        age = int(input("Tell your age :- "))
        email = input("Tell your email id :- ")
        pin = int(input("Tell your pin (4 digits) :- "))

        # Validation
        if age < 18 or len(str(pin)) != 4:
            print("Sorry, you cannot create your account")
            return

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": Bank.__accountgenerate(),
            "balance": 0
        }

        print("\nAccount created successfully!\n")
        for key, value in info.items():
            print(f"{key} : {value}")

        print("\nPlease note down your account number\n")

        Bank.data.append(info)

        print("Saving data to file...")   # DEBUG
        Bank.__update()
    def depositmoney(self):
        accnumber = input("please tell your pin aswell")
        pin= int(input("please tell your pin"))
# -------- MAIN PROGRAM --------

user = Bank()

print("\n1. Create Account")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. View Details")
print("5. Update Details")
print("6. Delete Account")

check = int(input("\nEnter your choice :- "))

if check == 1:
    user.Createaccount()
if check == 2:
    user.depositmoney()