class Myclass:
    def __init__(self, firstN, lastN):
        self.firstName = firstN
        self.lastName = lastN
    def email(self):
        print(f"{self.firstName}.{self.lastName}@gmail.com")


john = Myclass("john","doe")
john.email()