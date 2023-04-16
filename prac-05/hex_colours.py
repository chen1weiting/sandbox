COLORS = {
    'ALICEBLUE': '#f0f8ff',
    'ANTIQUEWHITE': '#faebd7',
    'AQUA': '#00ffff',
    'AZURE': '#f0ffff',
    'BEIGE': '#f5f5dc',
    'BISQUE': '#ffe4c4',
    'BLACK': '#000000',
    'BLANCHEDALMOND': '#ffebcd',
    'BLUE': '#0000ff',
    'BLUEVIOLET': '#8a2be2'
}

while True:
    color_name = input("Enter a color name (blank to stop): ").strip().upper()
    if not color_name:
        break
    
    color_code = COLORS.get(color_name)
    if color_code:
        print(f"The hexadecimal code for {color_name} is {color_code}.")
    else:
        print(f"Sorry, we couldn't find a color code for {color_name}.")
