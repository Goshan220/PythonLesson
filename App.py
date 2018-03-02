from Main import FamilyAccounting
import GUI
# import multiprocessing
import threading
import queue

def console():
    family = FamilyAccounting()
    while(True):
        print("********MENU********")
        print("Enter operation: ")
        print("1: Add person to database")
        print("2: Change date")
        print("3: Add operation")
        print("4: Expenses one person")
        print("5: Expenses family")
        print("6: Income one person")
        print("7: Income family")
        print("8: Close program")
        key = int(input(">> "))
        if key == 1:
            print(family.__str__())
            family.AppPerson(input("Name: "))
            continue
        elif key == 2:
            family.ChangeDate(int(input("Day: ")), int(input("month: ")), int(input("year: ")))
            continue
        elif key == 3:
            print(family.__str__())
            family.AddOperationMoney(input("Enter summ (minus sign at the beginning means expenses): "), int(input("Number person: ")))
            continue
        elif key == 4:
            print(family.__str__())
            print(family.ExpenseOnePerson(int(input("Month: ")), int(input("Number person: "))))
            continue
        elif key == 5:
            print(family.ExpenseAllPerson())
            continue
        elif key == 6:
            print(family.__str__())
            print(family.AddMoneyPerson(int(input("Month: ")), int(input("Number person: "))))
            continue
        elif key == 7:
            print(family.AddMoneyAllPerson())
            continue
        elif key == 8:
            break
        else:
            print("Error key, enter key again")
            continue
    print("close console")

# def run():
#     qu = queue.Queue()
#     qu.put()
#     t = threading.Thread(target=console)
#     t.start()
#     gu = threading.Thread(target=GUI.run)
#     gu.start()
#
#
# run()
