import time

# print(time.strftime('%d-%m-%Y'))

def greet(local_time):
    if local_time >= 5 and local_time < 12:
        return 'Good Morning Sir.!'
    elif local_time >= 12 and local_time <= 15:
        return 'Good Afternoon Sir.!'
    elif local_time > 15 and local_time <= 19:
        return 'Good Evening Sir.!'
    elif local_time > 19 and local_time <= 23:
        return 'Good Night Sir.!'
    
    else:
        print("Please Sir go to sleep fast it's ghost time.👹☠️ it's very dark night.")


if __name__ == '__main__':
    print(time.strftime('%d-%h'))
    print(time.strftime("%H:%M:%S"))

    local_time = int(time.strftime('%H'))   # ---giving the time in HOUR only and change into int--
    # --call greet function---
    print(greet(local_time))