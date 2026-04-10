import csv
import time

def send_email(to_email, name):
    print(f"Sending email to {name} ({to_email})")
    time.sleep(1)

def load_csv(file_path):
    users = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users

def process_queue(users, batch_size=2):
    for i in range(0, len(users), batch_size):
        batch = users[i:i+batch_size]
        print(f"\nProcessing batch {i//batch_size + 1}")
        
        for user in batch:
            send_email(user['email'], user['name'])

        print("Waiting before next batch...\n")
        time.sleep(2)

if __name__ == "__main__":
    users = load_csv("users.csv")
    process_queue(users)

## Note

This POC focuses on system design and workflow simulation. 
The implementation is a simplified prototype to demonstrate the email pipeline, queueing, and personalization logic, and is not intended as a production-grade system.
