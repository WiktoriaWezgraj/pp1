def convert_speed():
    ms_to_kmh = lambda ms: ms * 3.6
    speed_ms = float(input("Enter: "))
    speed_kmh = ms_to_kmh(speed_ms)
    print(f"{speed_ms} = {speed_kmh}")

if __name__ == "__main__":
    convert_speed()