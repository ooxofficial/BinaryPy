while True:
    try:
        print("Welcome! Please enter your string.")
        string = input("> ")
        binary = ' '.join(format(ord(char), '08b') for char in string)
        print(binary)
        print("Do you want to convert something again? (Y/N)")
        yn = input("> ")
        if yn == "y" or yn == "Y" or yn == "yes" or yn == "Yes":
            continue
        elif yn == "n" or yn == "N" or yn == "no" or yn == "No":
            exit()
        else:
            print("Invalid answer to Y/N")
            print("Exiting program.")
            exit()
    except KeyboardInterrupt:
        continue