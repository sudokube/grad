class student:
    def __init__(self, name, computer_score):
        self.name = name
        self.computer_score = computer_score

    def get_name(self):
        return self.name

    def get_average_score(self):
        return self.computer_score

    def edit_computer_score(self, computer_score):
        self.computer_score = computer_score


class natural_science(student):
    def __init__(self, name, computer_score, science_score):
        super(student, self).__init__(name, computer_score)
        self.science_score = science_score

    def get_average_score(self):
        return (self.computer_score + self.science_score) / 2

    def edit_science_score(self, science_score):
        self.science_score = science_score


class liberal_arts(student):
    def __init__(self, name, computer_score, sociology_score):
        super(student, self).__init__(name, computer_score)
        self.sociology_score = sociology_score

    def get_average_score(self):
        return (self.computer_score + self.sociology_score) / 2

    def edit_sociology_score(self, sociology_score):
        self.sociology_score = sociology_score
