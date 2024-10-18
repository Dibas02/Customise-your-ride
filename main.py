print('''There are 2 ways to customize your ride
      1.Bike
      2.Car''')

choice1 = int(input("Enter '1' for bike and '2' for car: "))

if choice1 == 1:
    print('''There are 2 options for bike
          1.Petrol operated bike
          2.Electronic bike/e-bike''')
    choice_bike = int(input("Enter '1' for Petrol operated bike and '2' for Electronic bike/e-bike: "))

    if choice_bike == 1:
        print("Petrol operated bike is selected for your ride.")

    else:
        print("Electronic bike/e-bike is selected for your ride.")


else:
    print('''There are 2 options for car
          1.suv
          2.sedan''')
    choice_car = int(input("Enter '1' for suv '2' for sedan: "))

    if choice_car == 1:
        print("suv is selected for your ride.")

    else:
        print("Sedan is selected for your ride.")
