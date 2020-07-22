from create_field import create_field
from copy import deepcopy
from population_process import population
from string import digits


def life_cycle(field, view_year=None, count=1):
    """
    This function maintains a population's life cycle.
    (list), (list or None), (int) -> None
    :param field: generated field.
    :param view_year: Years in which the user wants to see the population state. (Default is None).
    Each year of the population's life is received by one recursion call.
    :param count: needed to identify the age of the population. (Default is 1).
    :return: None or recursion call.
    """

    # If the user doesn't want to see specific years of a population's life cycle
    if view_year is None:
        view_year = []

    field_new = population(deepcopy(field))
    zip_fields = zip(field_new, field)

    for i in zip_fields:

        # if user entered years in which he wants to see the population state
        if count in view_year:
            print('\n\nThe', count, 'years old population: \n')
            view_year.remove(count)

            for j in field_new:
                print(*j)

        # if current field and previous field are not the same — recursion continues,
        # otherwise — comes out from the for loop to prevent infinite cycle
        if i[0] != i[1]:
            return life_cycle(field_new, view_year, count + 1)

    print('\n\nThe last one', count, 'years old population: \n')
    for i in field_new:
        print(*i)


if __name__ == '__main__':

    while True:
        user_input = input("Enter the ages of the population (space separated), "
                           "in which you want to see the state (otherwise skip by pressing enter): ")

        # Checks the user's input to consist only numbers
        if all(i in digits + ' ' for i in user_input):
            user_input = user_input.split()
            population_ages = list(map(int, user_input))
            break

        else:
            print('Only digits!')
    # Start of the game
    life_cycle(create_field(), population_ages)
