class Dog():
    """Dog."""

    def __init__(self, name, age):
        """init."""
        self.name = name
        self.age = age

    def sit(self):
        """sit."""
        print("{} is now sitting.".format(self.name.title()))

    def roll_over(self):
        """roll over."""
        print("{} rolled over!".format(self.name.title()))
