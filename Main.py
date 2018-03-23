class FamilyAccounting:

    def __init__(self, file):
        self.data = [1, 1, 1970]
        self.person = []
        self.file = file
        # file = open('Datenbank.txt', 'r')
        for line in self.file:
            entry = line.split(":")
            if entry[1] not in self.person:
                self.person.append(entry[1])
        if self.person.__len__() < 1:
            self.person.append("admin")

    # добавить человека
    def app_person(self, person):
        self.person.append(person)
        print(self.person)

    # изменить дату
    def change_date(self, day, month, year):
        if (day > 0) and (day < 32) and (month > 0) and (month < 13) and (year > 1970):
            self.data = [day, month, year]
            print("Date was changed")
        else:
            print("date format is incorrect \n Date not was changed")

    # добавить операцию с деньгами
    def add_operation_money(self, summ, person):
        # file = open('Datenbank.txt', 'a')
        temp = "{0}:{1}:{2}\n".format(str(self.data), str(self.person[person]), str(summ))
        self.file.write(temp)
        print("Done")

    # расход одного человека
    def expense_one_person(self, month, person):
        # file = open('Datenbank.txt', 'r')
        person -= 1
        result = 0
        for line in self.file:
            entry = line.split(":")
            if (int(entry[0].split(",")[1]) == month) and \
                    (str(entry[1]) == self.person[person]) and (int(entry[2]) < 0):
                result -= int(entry[2])
        return -result

    # внесение денег одного человека
    def add_money_person(self, month, person):
        # file = open('Datenbank.txt', 'r')
        person -= 1
        result = 0
        for line in self.file:
            entry = line.split(":")
            if (int(entry[0].split(",")[1]) == month) \
                    and (str(entry[1]) == self.person[person]) and (int(entry[2]) > 0):
                result += int(entry[2])
        return result

    # расход всех членов семьи
    def expense_all_person(self):
        # file = open('Datenbank.txt', 'r')
        result = 0
        for line in self.file:
            print (line)
            entry = line.split(":")
            if int(entry[2]) < 0:
                result -= int(entry[2])
        return -result

    # внесение от всех членов семьи
    def add_money_all_person(self):
        # file = open('Datenbank.txt', 'r')
        result = 0
        for line in self.file:
            entry = line.split(":")
            if int(entry[2]) > 0:
                result += int(entry[2])
        return result

    def __str__(self):
        return "data: " + str(self.data) + "| person: " + str(self.person)
