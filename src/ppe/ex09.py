"""Given a row number and a column number, determine the color of the tile of a chess board
at the intersection of the given row and column."""

def get_chess_square_color(row: int, column: int) -> str:
    if row > 7 or column > 7:
        return ""
    
    if row % 2 == 0:
        return "white" if column % 2 == 0 else "black"
    return "black" if column % 2 == 0 else "white"