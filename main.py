from models.models import Toyota

while True:
    print("1. Add new Toyota\n" +
          "2. Get all Toyotas\n" +
          "3. Get Toyota by Id\n" +
          "4. Choose Toyota for using by Id\n" +
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
        while True:
            id = int(input("Type id to search: "))
            if Toyota.get_by_id(id):
                pass
            break
    elif flag == 4:
        while True:
            id = int(input("Type id to search: "))
            if Toyota.get_by_id(id):
                break
        while True:
            print("1. Drive\n2. Shift gear\n3. Change color\n4. Remove car by Id\n5. Quit")
            flag_option = int(input("Choose menu item: "))
            if flag_option == 1:
                Toyota.drive()
            elif flag_option == 2:
                Toyota.shift_gear()
            elif flag_option == 3:
                new_color = input("Choose new color: ")
                Toyota.change_color_by_id_s(id, new_color)
                print(f"New color is {new_color}!\n")
            elif flag_option == 4:
                print("Toyota №", id, "removed!\n")
                Toyota.remove_by_id(id)
                break
            elif flag_option == 5:
                print("By!\n")
                break
    if flag == 5:
        print("Good by!")
        break
