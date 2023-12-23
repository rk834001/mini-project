import random

class TimetableGenerator:
    def __init__(self, professors, classrooms, laboratories, days_of_week, time_slots):
        self.professors = professors
        self.classrooms = classrooms
        self.laboratories = laboratories
        self.days_of_week = days_of_week
        self.time_slots = time_slots
        self.timetable = {}

    def generate_timetable(self):
        for day in self.days_of_week:
            for time_slot in self.time_slots:
                professors_list = list(self.professors.keys())
                random.shuffle(professors_list)
                for professor in professors_list:
                    subjects = self.professors[professor]
                    subject = self.get_subject_for_professor(subjects)
                    room = self.get_available_room(day, time_slot, subject)
                    if room:
                        key = (day, time_slot)
                        self.timetable[key] = (day, subject, professor, room)

    def get_subject_for_professor(self, subjects):
        return next((s for s in subjects if s.lower() == "python"), random.choice(subjects))

    def get_available_room(self, day, time_slot, subject):
        if subject == "Python":
            available_rooms = self.laboratories
        else:
            available_rooms = self.classrooms

        assigned_rooms = set(r for (_, _, _, r) in self.timetable.values() if _ == day and _ == time_slot)
        available_rooms = list(set(available_rooms) - assigned_rooms)

        return random.choice(available_rooms) if available_rooms else None

    def display_timetable(self):
        print("Complete Timetable:")
        for day in self.days_of_week:
            print(f"\n{day}:")
            for time_slot in self.time_slots:
                key = (day, time_slot)
                if key in self.timetable:
                    _, subject, professor, room = self.timetable[key]
                    if time_slot == "1:00 PM - 2:00 PM":
                        print(f"Lunch Break: 1:00 PM - 2:00 PM")
                    else:
                        print(f"{time_slot}: Professor {professor} - Subject {subject} - Room {room}")

def get_user_input(prompt, input_type=str):
    while True:
        try:
            user_input = input(prompt)
            return input_type(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid value.")

# Get user input for professors
professors = {}
while True:
    professor_name = get_user_input("Enter professor name (or 'done' to finish): ")
    if professor_name.lower() == 'done':
        break
    subjects = get_user_input("Enter subjects for the professor (comma-separated): ", input_type=lambda x: x.split(','))
    professors[professor_name] = subjects

# Get user input for classrooms, laboratories, days_of_week, and time_slots
classrooms = get_user_input("Enter classrooms (comma-separated): ", input_type=lambda x: x.split(','))
laboratories = get_user_input("Enter laboratories (comma-separated): ", input_type=lambda x: x.split(','))
days_of_week = get_user_input("Enter days of week (comma-separated): ", input_type=lambda x: x.split(','))
time_slots = get_user_input("Enter time slots (comma-separated): ", input_type=lambda x: x.split(','))

# Example usage
generator = TimetableGenerator(professors, classrooms, laboratories, days_of_week, time_slots)
generator.generate_timetable()
generator.display_timetable()

