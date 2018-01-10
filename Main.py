
class Familienbuchhaltung:

    def __init__(self):
        self.data = [1, 1, 1970]
        self.person = ["admin"]
        file = open('Datenbank.txt', 'r')
        for line in file:
            entry = line.split(":")
            if entry[1] not in self.person:
                self.person.append(entry[1])
        if self.person.__len__() > 1:
            self.person.pop(0)

    #добавить человека
    def PersonHinzufügen(self, person):
        self.person.append(person)
        print(self.person)

    #изменить дату
    def ändernSiedasDatum(self, day, month, year):
        if (day > 0) & (day < 32) & (month > 0) & (month < 13) & (year > 1970):
            self.data = list([day, month, year])
            print("Date was changed")
        else:
            print("date format is incorrect \n Date not was changed")

    # добавить операцию с деньгами
    def OperationMitDemGeld(self, summ, person):
        file = open('Datenbank.txt', 'a')
        temp = str(self.data) + ":" + self.person[person] + ":" + str(summ) + "\n"
        file.write(temp)
        print("Done")

    # расход одного человека
    def Geldausgeben_Person(self, month, person):
        file = open('Datenbank.txt', 'r')
        person -= 1
        result = 0
        for line in file:
            entry = line.split(":")
            if (int(entry[0].split(",")[1]) == month) & (str(entry[1]) == self.person[person]) & (int(entry[2]) < 0):
                result -= int(entry[2])
        return (-result)

    # внесение денег одного человека
    def Geld_verdienen_Person(self, month, person):
        file = open('Datenbank.txt', 'r')
        person -= 1
        result = 0
        for line in file:
            entry = line.split(":")
            if (int(entry[0].split(",")[1]) == month) & (str(entry[1]) == self.person[person]) & (int(entry[2]) > 0):
                result += int(entry[2])
        return (result)

    # расход всех членов семьи
    def Verbrauch_aller_Geld(self):
        file = open('Datenbank.txt', 'r')
        result = 0
        for line in file:
            entry = line.split(":")
            if (int(entry[2]) < 0):
                result -= int(entry[2])
        return (-result)

    # внесение от всех членов семьи
    def Eintragung_aller_Geld(self):
        file = open('Datenbank.txt', 'r')
        result = 0
        for line in file:
            entry = line.split(":")
            if (int(entry[2]) > 0):
                result += int(entry[2])
        return (result)

    def __str__(self):
        return "data: " + str(self.data) + "| person: " + str(self.person)

