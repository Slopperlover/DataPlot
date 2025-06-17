import csv
import random
import time

x_value = 0
total_1 = 1000
total_2 = 100
total_3 = 1000

fieldnames = ["0", "1", "2", "3"]


with open('live.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('live.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "0": x_value,
            "1": total_1,
            "2": total_2,
            "3": total_3
        }

        csv_writer.writerow(info)
        print(x_value, total_1, total_2, total_3)

        x_value += 1
        total_1 = total_1 + random.randint(-6, 8)
        total_2 = total_2 + random.randint(-20, 30)
        total_3 = total_3 + random.randint(-10, 15)

    time.sleep(0.5)
