def avg_speed():
    distance = float(input("Enter distance in km: "))
    hours = float(input("Enter number of travel hours: "))
    minutes = float(input("Enter number of travel minutes: "))
    average_speed = distance/(hours+minutes/60)
    print(f"Average speed: {average_speed} km/h")

if __name__ == "__main__":
    avg_speed()