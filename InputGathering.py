def get_int_input(text):
    value = "a"
    while not value.isnumeric():
        value = input(text)
        if value.isnumeric():
            value = int(value)
            if value > 1000:
                print("The max input value is 1000")
                value = 1000
            return value
        print(f"Sorry, {value} is not recognized as an number, please try again.")

def get_yn_input(text):
    pending = True
    while pending:
        value = input(text).lower().strip()
        if len(value) == 0:
            continue
        response = value[0]
        if value == "y":
            return get_int_input("What is the target roll number?: ")
            
        if value == "n":
            return None
