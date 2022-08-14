from datetime import datetime

year = int(input("Enter Year of Birth: "))
month = int(input("Enter Month of Birth: "))
day = int(input("Enter Day of Birth: "))
while True:
    currentDate = datetime.now()
    age = [currentDate.year - year, currentDate.month - month, currentDate.day - day, currentDate.hour,
           currentDate.minute, currentDate.second, currentDate.microsecond]
    if age[1] < 0:
        age[0] -= 1
        age[1] = (12 - month) + currentDate.month
    if age[2] < 0:
        age[1] -= 1
        age[2] = (30 - day) + currentDate.day

    print(
        f"You are {age[0]} year {age[1]} month {age[2]} day {age[3]} hours {age[4]} min {age[5]} sec {age[6]} microseconds old.\r",
        end="")
    # time.sleep(1)
