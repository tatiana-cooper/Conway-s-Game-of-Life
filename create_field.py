from random import choice


def create_field(n=8):
    """
    This function creates a field with alive and dead cells: ☼ — alive, † — dead.
    (int) -> (list)
    :param n: size of the field.
    :return: list, representation of field
    """
    field = [[choice(('☼', '†')) + '  ' for _ in range(n)] for _ in range(n)]
    print('The first population: \n')
    for i in field:
        print(*i)
    return field
