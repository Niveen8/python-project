appointments = []
def Add_reservation():
    name = input(" name: ")
    date = input(" date: ")
    time = input(" time: ")
    appointments.append((name, date, time))
    print("Your reservation has been completed successfully\n")
def show_appointments():
    
    if not appointments:
        print("No reservation unfortunately\n")  
        return
    
    print("Appointments List:") 
    for i, app in enumerate(appointments, start=1):
        name, date, time = app 
        print(f"{i}) Name: {name}")
        print(f"   Date: {date}")
        print(f"   Time: {time}\n")
    print()  
def delete_reservation():
    show_appointments()
    if not appointments:
        return
    try:
        num = int(input("Please enter your reservation number in order to delete your reservation.: "))
        if 1 <= num <= len(appointments):
            removed = appointments.pop(num - 1)
            print(f"Reservation for {removed[0]} deleted successfully\n")
        else:
            print("Invalid number\n")
    except ValueError:
        print("Please enter a valid number\n")
while True:
    print("1:Add reservation")
    print("2: Show reservations")
    print("3: Delete reservation")
    print("4: Exit")
    choice = input("Choose an option please: ")

    if choice == "1":
        Add_reservation()
    elif choice == "2":
        show_appointments()
    elif choice == "3":
        delete_reservation()
    elif choice == "4":
        print("We are honored by you")
        break
    else:
        print("Invalid choice, try again\n")    

