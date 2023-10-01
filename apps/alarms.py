import sched
import time
import threading
import pyttsx3

# Initialize the scheduler
alarm_scheduler = sched.scheduler(time.time, time.sleep)

# Speak function for alarms
def speak_alarm(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

# Function to schedule an alarm
def set_alarm(time_str, message):
    try:
        alarm_time = time.strptime(time_str, "%H:%M")
        alarm_timestamp = time.mktime(alarm_time)
        alarm_scheduler.enterabs(alarm_timestamp, 1, speak_alarm, argument=(message,))
        return f"Alarm set for {time_str}."
    except ValueError:
        return "Invalid time format. Please use HH:MM."

# Function to start the alarm scheduler
def start_alarm_scheduler():
    t = threading.Thread(target=alarm_scheduler.run)
    t.daemon = True
    t.start()

# Function to cancel an alarm
def cancel_alarm(time_str):
    try:
        alarm_time = time.strptime(time_str, "%H:%M")
        alarm_timestamp = time.mktime(alarm_time)
        events = alarm_scheduler.queue
        for event in events:
            if event.time == alarm_timestamp:
                alarm_scheduler.cancel(event)
                return f"Alarm for {time_str} canceled."
        return f"No alarm found for {time_str}."
    except ValueError:
        return "Invalid time format. Please use HH:MM."

# Function to list all scheduled alarms
def list_alarms():
    events = alarm_scheduler.queue
    if not events:
        return "No alarms are currently scheduled."
    else:
        alarm_list = []
        for event in events:
            alarm_time = time.strftime("%H:%M", time.localtime(event.time))
            alarm_list.append(alarm_time)
        return "Scheduled alarms: " + ", ".join(alarm_list)

if __name__ == "__main__":
    start_alarm_scheduler()
