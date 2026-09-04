from person import Person

class Teacher(Person):

    def __init__(self, name, age, subject, experience):
        super().__init__(name, age)
        self.subject = subject
        self.experience = experience

    def describe(self):
        return "I am a teacher."