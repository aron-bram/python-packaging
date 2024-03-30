import click
import numpy as np


def board(rows: int = 5, cols: int = 5, sym: str = "*"):
    """Given two integers rows, cols, render a square in console and select
    random indices that are replaced with with random symbols.
    
    Returns
        the square shape as a string
    """
    s = np.full((cols, rows), sym, dtype=str)
    mask = np.random.choice([True, False], size=(cols, rows))
    # randomly swap out some symbols to some other ones
    chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
              "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x", "y", "z", "0", "1", "2", "3",
              "4", "5", "6", "7", "8", "9", "!", "@", "#", "$",
              "%", "^", "&", "*", "(", ")", "_", "-", "+", "=",
              "{", "}", "[", "]", "|", ";", ":", ",", ".", "<",
              ">", "/", "?", "`", "~", "'", '"']
    np.random.shuffle(chars)
    s[mask] = chars[:mask.sum()]
    # print board to console
    print(s)

    return s

@click.command()
@click.option("--rows", type=int, default=5)
@click.option("--cols", type=int, default=5)
@click.option("--sym", type=str, default="*")
def cmd_board(rows, cols, sym):
    board(rows, cols, sym)


if __name__ == "__main__":
    board()
