from InputGathering import get_int_input, get_yn_input
from Calculations import get_probability_curve
from Output import output_header, print_target_percentages


def main():
    number_of_dice = get_int_input("How many Dice are you rolling?: ")
    sides = get_int_input("How many sides do they have?: ")
    target = get_yn_input("Is there a target you are rolling for? (y/n): ")
    output_header(number_of_dice, sides, target)

    proability = get_probability_curve(number_of_dice, sides)
    print_target_percentages(target, proability)

main()