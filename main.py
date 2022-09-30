from models.models import Toyota

while True:
    print("1. Add new Toyota\n" +
            "2. Get all Toyotas\n" +
            "3. Get Toyota by Id\n" +
            "4. Choose Toyota for driving by Id\n" +
            "5. End"
            )
    flag = int(input("Choose menu item: "))
    if flag == 1:
        name = input("Toyota name: ")
        engine = input("Toyota engine: ")
        color = input("Toyota color: ")
        toyota = Toyota(name, engine, color)
        toyota.save()
    elif flag == 2:
        Toyota.get_all_Toyotas()
    elif flag == 3:
        id = int(input("Type id to search: "))
        Toyota.get_by_id(id)
    elif flag == 4:

        id = int(input("Type id to search: "))
        print("Your Toyota is №", end="")
        Toyota.get_by_id(id) and Toyota.toyota_to_driv(id, )
        your_car = Toyota

        while True:
            print("1. Drive\n2. Shift gear\n3. Change color\n4. Quit")
            flag_option = int(input("Choose menu item: "))

            if flag_option == 1:
                your_car.drive()
            elif flag_option == 2:
                your_car.shift_gear()
            elif flag_option == 3:
                color = input("Choose new color: ")
                your_car.change_color(color)
            elif flag_option == 4:
                break
    if flag == 5:
        print("Good by!")
        break