school_timetable = {
    "Monday": {
        "1st Period": "English",
        "2nd Period": "Science",

    },
    "Tuesday": {
        "1st Period": "History",
        "2nd Period": "English",
        # Add more periods for Tuesday
    },

}

def get_timetable(day):
    """Get the school timetable for a specific day."""
    day = day.capitalize()  # Ensure the day's name is capitalized
    if day in school_timetable:
        timetable = school_timetable[day]
        return timetable
    else:
        return "Timetable not available for that day."

def display_timetable(day):
    """Display the school timetable for a specific day."""
    timetable = get_timetable(day)
    if timetable:
        print(f"Timetable for {day}:")
        for period, subject in timetable.items():
            print(f"{period}: {subject}")
    else:
        print("Timetable not available for that day.")
