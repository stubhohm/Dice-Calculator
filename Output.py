def print_target_percentages(target:int, proabilities:dict[int, float]):
    exactly = proabilities.get(target, 0)
    exceed = 0
    below = 0
    most_likely = None
    max_percent = 0
    percent_sum = 0
    five_percent, ninty_five_percent = None, None
    twenty_percent, eighty_percent = None, None
    for item in proabilities.items():
        value, percent = item
        if target:
            if value < target:
                below += percent
            elif value > target:
                exceed += percent
            else:
                exactly = percent

        if percent == max_percent:
            most_likely.append(value)

        if percent > max_percent:
            most_likely = [value]
            max_percent = percent
        percent_sum += percent
        if percent_sum < .05:
            five_percent = value
        if percent_sum < .95:
            ninty_five_percent = value
        if percent_sum < .20:
            twenty_percent = value
        if percent_sum < .80:
            eighty_percent = value
    
    output_dict = {}
    if target:
        output_dict["Exceed"] = exceed
        output_dict["Below"] = below
        output_dict["Exactly"] = exactly
        output_dict["Meet or Exceed"] = exceed + exactly
        output_dict["Meet or Below"] = below + exactly
        
    output_dict["Most Likely"] = most_likely
    output_dict["20-80 Range"] = [twenty_percent, eighty_percent]
    output_dict["5-95 Range"] = [five_percent, ninty_five_percent]
    

    for item in output_dict.items():
        name, percent = item
        if type(percent) == float:
            percent = round((percent * 100), 2)
            percent = str(percent) + "%"
        if type(percent) == list:
            percent = ", ".join([str(num) for num in percent])
        print(f"{name}: {percent}")
    print("\n")

def output_header(number_of_dice:int, sides:int, target:int):
    text = f"\n+++Results when rolling {number_of_dice} d{sides}'s"
    if target:
        text +=  f" when aiming for a value of {target}"
    text += ".+++\n"
    print(text)