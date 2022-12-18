from programminglanguage import ProgrammingLanguage
def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby)
    print(python)
    print(vb)

    languages = [ruby,python,vb]
    languages_dynamic = []
    for language in languages:
        dynamic = language.is_dynamic()
        if dynamic == True:
            languages_dynamic.append(language.name)
            print("Dynamically typed languages are: ")
            for i in languages_dynamic:
                print(i)

main()