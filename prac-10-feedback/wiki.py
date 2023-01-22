import wikipedia

while True:
    user_input = input("Enter a page title or search phrase: ")

    if user_input == "":
        break

    try:
        page = wikipedia.page(user_input, autosuggest=False)
        print("Title: ", page.title)
        print("Summary: ", page.summary)
        print("URL: ", page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Multiple pages found, please select one of the following:")
        for option in e.options:
            print(option)