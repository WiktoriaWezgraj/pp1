def speed():
    calculate = lambda distance,hours,minutes: distance/(hours+minutes/60)
    distance = float(input("Enter distance in km: "))
    hours = float(input("Enter number of travel hours: "))
    minutes = float(input("Enter number of travel minutes: "))
    average_speed =calculate(distance,hours,minutes)
    print(f"Average speed is {average_speed}")

if __name__ == "__main__":
    speed()