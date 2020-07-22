from cell_state import cell_state, alive_amount


def population(field):
    """
    This function makes changes in the population's field according to the game rules.
    (list) -> (list)
    :param field: str field of the first generated randomly population.
    :return: str field.
    """

    for i, line in enumerate(field):
        for j, cell in enumerate(line):

            # If-statements verify particular positions of cells to prevent IndexError

            if i == 0 and j == 0:
                # Stores all neighbors of the current cell
                cell_neighbors = [field[i + 1][j], field[i][j + 1], field[i + 1][j + 1]]

                # Changes cell according to neighbors' state
                field[i][j] = cell_state(alive_neighbors=alive_amount(cell_neighbors),
                                         cell=cell)

            elif i == 0 and j == 7:
                cell_neighbors = [field[i + 1][j], field[i][j - 1], field[i + 1][j - 1]]

                field[i][j] = cell_state(alive_neighbors=alive_amount(cell_neighbors),
                                         cell=cell)

            elif i == 0 and 0 < j < 7:
                cell_neighbors = [field[i + 1][j], field[i][j + 1], field[i][j - 1],
                                  field[i + 1][j + 1], field[i + 1][j - 1]]

                field[i][j] = cell_state(alive_neighbors=alive_amount(cell_neighbors),
                                         cell=cell)

            elif 0 < i < 7 and j == 0:
                cell_neighbors = [field[i + 1][j], field[i][j + 1], field[i - 1][j],
                                  field[i - 1][j + 1], field[i + 1][j + 1]]
                field[i][j] = cell_state(alive_neighbors=alive_amount(cell_neighbors),
                                         cell=cell)

            elif 0 < i < 7 and 0 < j < 7:
                cell_neighbors = [field[i + 1][j], field[i][j + 1], field[i - 1][j],
                                  field[i][j - 1], field[i - 1][j - 1], field[i - 1][j + 1],
                                  field[i + 1][j - 1], field[i + 1][j + 1]]
                field[i][j] = cell_state(alive_neighbors=alive_amount(cell_neighbors),
                                         cell=cell)

            elif 0 < i < 7 and j == 7:
                cell_neighbors = [field[i + 1][j], field[i - 1][j], field[i][j - 1],
                                  field[i - 1][j - 1], field[i + 1][j - 1]]

                field[i][j] = cell_state(alive_neighbors=alive_amount(cell_neighbors),
                                         cell=cell)

            elif i == 7 and j == 0:
                cell_neighbors = [field[i][j + 1], field[i - 1][j], field[i - 1][j + 1]]

                field[i][j] = cell_state(alive_neighbors=alive_amount(cell_neighbors),
                                         cell=cell)

            elif i == 7 and 0 < j < 7:
                cell_neighbors = [field[i][j + 1], field[i - 1][j], field[i][j - 1],
                                  field[i - 1][j - 1], field[i - 1][j + 1]]
                field[i][j] = cell_state(alive_neighbors=alive_amount(cell_neighbors),
                                         cell=cell)

            elif i == 7 and j == 7:
                cell_neighbors = [field[i - 1][j], field[i][j - 1], field[i - 1][j - 1]]
                field[i][j] = cell_state(alive_neighbors=alive_amount(cell_neighbors),
                                         cell=cell)

    return field
