import json
from datetime import datetime

EVENTS_FILE = 'events.json'
TICKETS_FILE = 'tickets.json'

def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

def authenticate_admin(username, password):
    admin_username = "admin"
    admin_password = "123456"  
    if username == admin_username and password == admin_password:
        print("Successful login as administrator.")
        return True
    else:
        print("The username or password is incorrect!")
        return False

def add_event():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    
    if not authenticate_admin(username, password):
        print("Access denied. Only the administrator can add events.")
        return
    
    title = input("Enter event title: ")
    total_capacity = int(input("Enter total capacity: "))
    date = input("Enter event date (%Y-%m-%d %H:%M:%S): ")
    
    events = load_data(EVENTS_FILE)
    event_id = str(len(events) + 1)
    events[event_id] = {
        'title': title,
        'total_capacity': total_capacity,
        'remaining_capacity': total_capacity,
        'date': date
    }
    save_data(EVENTS_FILE, events)
    print(f" event '{title}' added Successfuly")

def list_events( ):
    events = load_data(EVENTS_FILE)
    if not events:
        print("There are no events available.")
        return
    for event_id, event in events.items():
         print_event(event_id, event)

def print_event(event_id, event):
    print(f"ID: {event_id}, Title: {event['title']}, remaining_capacity: {event['remaining_capacity']}, Date: {event['date']}")


def reserve_ticket(event_id, National_code):
    events = load_data(EVENTS_FILE)
    tickets = load_data(TICKETS_FILE)
    event_id=str(event_id) 
    if event_id not in events:
        print("event not found")
        return

    event = events[event_id]
    if event['remaining_capacity'] > 0:
        ticket_id = str(len(tickets) + 1)
        reservation_date = datetime.now().strftime("%H:%M:%S")

        tickets[ticket_id] = {
            'event_id': event_id,
            'National code': National_code,
            'is_confirmed': False,
            'reservation_date': reservation_date
        }
        
        event['remaining_capacity'] -= 1
        save_data(EVENTS_FILE, events)
        save_data(TICKETS_FILE, tickets)
        print(f"Ticket code: {ticket_id} , successfully booked! ")

        confirm = input("Do you confirm your reservation? (Yes/No): ")
        if confirm.lower() == "yes":
            tickets[ticket_id]['is_confirmed'] = True
            save_data(TICKETS_FILE, tickets)
            print(f"ticket with ID:{ticket_id} , confirmed. ")
        else:
            event['remaining_capacity'] += 1
            del tickets[ticket_id]
            save_data(EVENTS_FILE, events)
            save_data(TICKETS_FILE, tickets)
            print(f"Ticket reservation with ID:{ticket_id} was  canceled. ")

    else:
        print("The event capacity is full.")


def cancel_reservation(ticket_id):
    tickets = load_data(TICKETS_FILE)
    events = load_data(EVENTS_FILE)

    if ticket_id not in tickets:
        print("ticket not found! ")
        return

    ticket = tickets[ticket_id]
    event_id = ticket['event_id']
    events[event_id]['remaining_capacity'] += 1
    del tickets[ticket_id]
    save_data(EVENTS_FILE, events)
    save_data(TICKETS_FILE, tickets)
    print(f"Ticket reservation with ID:{ticket_id} was  canceled.")



def show_menu():
    print("\n--- Main menu---")
    print("1. add event")
    print("2. view events")
    print("3. ticket reservation")
    print("4. view specifice event")
    print("5. cancel reservation")
    print("6.exit")
    
def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
           add_event()
        
        elif choice == '2':
            print("\n--- List of events---")
            list_events()
        
        elif choice == '3':
            event_id = int(input("Enter the event ID: "))
            national_code = input("Enter your national code:")
            reserve_ticket(event_id, national_code)

        elif choice == '4':
            event_id = input("Enter event ID to view details: ")
            events = load_data(EVENTS_FILE)
            if event_id in events:
                print_event(event_id, events[event_id])
            else:
                print("Event not found.")

        elif choice=='5':
            ticked_id=input("enter thet icket id to cancel")
            cancel_reservation(ticked_id)
        elif choice == '6':
            print("Exit the program...")
            break
        else:
            print("Please enter the correct choice number.")

if __name__ == "__main__":
    main()
