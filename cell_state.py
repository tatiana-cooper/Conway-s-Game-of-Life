def alive_amount(cell_neighbors):
    """
    Returns amount of alive neighbors of current cell.
    (list) -> (int)
    :param cell_neighbors: list of current cell's neighbors.
    :return: amount of alive neighbors
    """
    return len([i for i in cell_neighbors if i == '☼  '])


def cell_state(alive_neighbors, cell):
    """
    Returns state (alive or dead) of the current cell according to the cell's alive neighbors.
    (int, str) -> (str)
    :param alive_neighbors: amount of alive neighbors of current cell.
    :param cell: current cell.
    :return: if alive — returns ☼, if dead — returns †.
    """
    # Defines the cell's state according to the game's rule

    if alive_neighbors >= 4:
        return '†  '

    elif cell == '☼  ' and alive_neighbors <= 1:
        return '†  '

    elif cell == '†  ' and alive_neighbors == 3:
        return '☼  '
    else:
        return cell
