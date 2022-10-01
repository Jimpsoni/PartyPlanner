class Event:
    def __init__(self, event_name, max_people):
        # Parameters
        self.name = event_name
        self.max_people = max_people

        # Other variables
        self.people_attending = []

    def join(self, person):
        self.people_attending.append(person)

    def cancel(self, person):
        self.people_attending.remove(person)
