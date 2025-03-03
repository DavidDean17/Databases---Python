def get_lift_record(exercise, current_record):
    while True:
        user_input = input(f"How much did you lift on the {exercise} (kg): ").strip()
        try:
            weight = int(user_input)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if weight > current_record:
            return weight
        return current_record
    

def trackweight():
    lifts = {"Bench": 0, "Deadlift": 0, "Squat": 0}
    
    lifts["Bench"] = get_lift_record("bench press", lifts["Bench"])
    lifts["Deadlift"] = get_lift_record("deadlift", lifts["Deadlift"])
    lifts["Squat"] = get_lift_record("squat", lifts["Squat"])
    
    return lifts


def main():
    print(trackweight())
    

if __name__ == "__main__":
    main()