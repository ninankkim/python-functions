class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def description(self):
        print('I am {self.name}, my email is {self.email}, and my phone number is {self.phone}!'.format(self.name, self.email, self.phone))

Sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
Jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

Jordan.greet(Sonny)
Sonny.greet(Jordan)

print(f" {Sonny.name}: \n {Sonny.email}: \n {Sonny.phone}:")
print(f" {Jordan.name}: \n {Jordan.email}: \n {Jordan.phone}:")

