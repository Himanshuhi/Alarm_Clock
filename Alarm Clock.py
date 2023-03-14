import time

def get_alarm_time():
    while True:
        try:
            hours = int(input("Enter the hour (0-23) for the alarm: "))
            minutes = int(input("Enter the minute (0-59) for the alarm: "))
            if 0 <= hours <= 23 and 0 <= minutes <= 59:
                return hours, minutes
            else:
                print("Invalid input. Please enter a valid hour and minute.")
        except ValueError:
            print("Invalid input. Please enter a valid integer hour and minute.")


while True:
    # himanshu
    current_time = time.localtime()
    current_hour, current_minute = current_time.tm_hour, current_time.tm_min
    

    alarm_hour, alarm_minute = get_alarm_time()
    

    while current_hour != alarm_hour or current_minute != alarm_minute:
        time.sleep(1)
        current_time = time.localtime()
        current_hour, current_minute = current_time.tm_hour, current_time.tm_min
        
 
    print("ALARM!")
