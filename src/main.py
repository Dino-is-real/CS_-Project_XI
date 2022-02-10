import car
import Pedestrian

running = True
print("Welcome to the Program...")
print("What do you want to perform:-")
while running:
    print("1. Detect cars\n2. Detect pedestrians\n")
    choice = input("What to perform [1/2]:").strip()
    if choice == "1":
        car.run()
    elif choice == "2":
        Pedestrian.run()
    else:
        print("Invalid input... ;-;")

    print("That's all from our side\nThank you for choosing us")