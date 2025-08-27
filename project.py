appointments = []
def Add_reservation():
    name = input(" name: ")
    date = input(" date: ")
    time = input(" time: ")
    appointments.append((name, date, time))
    print("Your reservation has been completed successfully\n")

