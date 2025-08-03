import time
import csv

file = open('records.csv', "w", newline="")
writer = csv.writer(file)
writer.writerow(["user_name", "Timestamp", "Delay", "Number entered"])

last_time = None
user_name = input("Enter your name: ")

while True:
    user_num = input("Enter a number between 0-9 (or 'quit' to exit): ")

    if user_num.lower() == "quit":
        break

    if user_num.isdigit() and 0 <= int(user_num) <= 9:
        current_time = time.time()

        if last_time is None:
            delay = 0
        else:
            delay = current_time - last_time

        last_time = current_time

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([user_name, timestamp, delay, user_num])

file.close()