import datetime

def log_error(error, where):
    time = datetime.datetime.now().strftime("%Y-%m-%d (%H:%M:%S)")
    file = open("err.txt", 'a')
    file.write("Time: " + time + "\n")
    file.write("Place: " + where + "\n")
    file.write("Error: " + error + "\n")
    file.write("\n\n\n")

def log_full(action, where):
    time = datetime.datetime.now().strftime("%Y-%m-%d (%H:%M:%S)")
    file = open("err.txt", 'a')
    file.write("Time: " + time + "\n")
    file.write("Place: " + where + "\n")
    file.write("Action: " + action + "\n")
    file.write("\n\n\n")






