battery = int("Enter the battery percentage: ")

while battery < 100:
    print("Charging phone... Battery at", battery, "%")
    battery += 10

print("Battery is full. Stop charging.")
