import json


class Toyota:
    file = "Toyotas.json"

    def __init__(self, name, engine, color):
        self.name = name
        self.engine = engine
        self.color = color

    # Creating cars

    @classmethod
    def get_data(cls):
        file = open("database/" + cls.file, "r")
        data_in_json = file.read()
        data = json.loads(data_in_json)
        file.close()
        return data

    @classmethod
    def get_all_Toyotas(cls):
        data = cls.get_data()
        for toyota in data:
            print("№", toyota["id"], end=" ")
            print(toyota["name"], end=" - ")
            print(toyota["engine"], end=" - ")
            print(toyota["color"])

    @classmethod
    def get_by_id(cls, id):  # return True if ID to be, and return False if ID ERROR
        toyotas = cls.get_data()  # list with dict
        counter = 0
        for toyota in toyotas:
            if id == toyota["id"]:
                print("Your Toyota is №", end="")
                print(toyota["id"], end=" ")
                print(toyota["name"], end=" - ")
                print(toyota["engine"], end=" - ")
                print(toyota["color"], "\n")
                return True
            counter += 1
            if counter == len(toyotas):
                print("Not found Toyota with this id!\n")
                return False

    def save(self):
        data = self.get_data()
        new_Toyota = {"name": self.name, "engine": self.engine, "color": self.color} #dict
        if len(data) > 0:
            new_Toyota["id"] = data[-1]['id'] + 1
        else:
            new_Toyota["id"] = 1
        data.append(new_Toyota)
        file = open("database/" + self.file, "w")
        data_in_json = json.dumps(data)
        file.write(data_in_json)

    @classmethod
    def remove_by_id(self, id):
        data = self.get_data()
        data.pop(id-1) # i = id-1
        file = open("database/" + self.file, "w")
        data_in_json = json.dumps(data)
        file.write(data_in_json)

    # Drive Shift gear Change color
    @staticmethod
    def drive():
        print("Drive!\n")

    @staticmethod
    def shift_gear():
        print("Change gear!\n")

    @classmethod
    def change_color_by_id_s(cls, id, new_color):
        toyotas = cls.get_data()  # list with dict
        for toyota in toyotas:
            if id == toyota["id"]:
                toyota["color"] = new_color
                toyotas[id - 1]["name"] = toyota["name"]
                toyotas[id - 1]["engine"] = toyota["engine"]
                toyotas[id - 1]["color"] = toyota["color"]
        file = open("database/" + cls.file, "w")
        data_in_json = json.dumps(toyotas)
        file.write(data_in_json)
