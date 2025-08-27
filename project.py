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
        print(f"{i}) Name: {name} | Date: {date} | Time: {time}")
    print()  

