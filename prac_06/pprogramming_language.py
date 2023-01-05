class ProgrammingLanguage:
    """Store data in a programming language."""
    def __init__(self, name, typing, reflection, year):
        self.name = nameself.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string of the program."""
        return "{}, {} Typing, Reflection={}, First appeared in{}".\
            format(self.name, self.typing, self.reflection,self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def run_tests():
        """Run simple tests on the class."""
        ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
        python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
        visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
        languages = [ruby, python, visual_basic]
        print(python)
        print("The dynamically typed languages are:")
        for language in languages:
            if language.is_dynamic():
                print(language.name)

    if __name__ == "__main__":
        run_tests()