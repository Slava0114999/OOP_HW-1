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
    def get_by_id(cls, id):
        toyotas = cls.get_data()
        counter = 0
        for toyota in toyotas:
            if id == toyota["id"]:
                print(toyota["id"], end=" ")
                print(toyota["name"], end=" - ")
                print(toyota["engine"], end=" - ")
                print(toyota["color"])
                break
            counter += 1
            if counter == len(toyotas):
                print("Not found Toyota with this id!")

    def toyota_to_driv(cls, id):
        toyotas = cls.get_data()
        for toyota in toyotas:
            if id == toyota["id"]:
                name = (toyota["name"])
                engine = (toyota["engine"])
                color = (toyota["color"])
                print(name, engine,color)

    def save(self):
        data = self.get_data()
        new_Toyota = {"name": self.name, "engine": self.engine, "color": self.color}
        if len(data) > 0:
            new_Toyota["id"] = data[-1]['id'] + 1
        else:
            new_Toyota["id"] = 1
        data.append(new_Toyota)
        file = open("database/" + self.file, "w")
        data_in_json = json.dumps(data)
        file.write(data_in_json)

    # Drive Shift gear Change color

    def drive():
        print("Drive!")

    def shift_gear():
        print("Gear is shifted!")

    def change_color(color):
        print(f"New color is {color}!\n")
