import csv
from models.restaurant import RestaurantModel


def insert_restaurants():
    with open("datasets/all_data_formmated_final.csv", "r+") as file:
        reader = csv.reader(file)
        data = [row for row in reader]
        data = data[1:]
        for row in data:
            try:
                data = RestaurantModel(row[0], row[1], row[2], float(row[3]), float(row[4]) )
                data.save_to_db()
            except:
                print(row)
                break
