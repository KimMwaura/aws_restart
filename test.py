# define the file path and name
file_path = "car_fleet.csv"
# define the headers of the csv file
headers = ["vin", "make", "model", "year", "range", "topSpeed", "zeroSixty", "mileage"]
# create an empty list to store the cars
cars = []

# read the csv file
with open(file_path, "r") as car_fleet.csv:
    reader = csv.DictReader(car_fleet.csv, fieldnames=headers)
    # skip the header row
    next(reader)
    # iterate over the remaining rows and create a dictionary for each car
    for row in reader:
        car = {
            "vin": row["vin"],
            "make": row["make"],
            "model": row["model"],
            "year": int(row["year"]),
            "range": int(row["range"]),
            "top_speed": int(row["topSpeed"]),
            "zero_to_sixty": float(row["zeroSixty"]),
            "mileage": int(row["mileage"])
        }
        # add the car dictionary to the list of cars
        cars.append(car)

# print the list of cars
for car in cars:
    print(car)