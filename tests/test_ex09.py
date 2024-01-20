from ppe import ex09

def test_get_chess_square_color():
    assert ex09.get_chess_square_color(1, 1) == 'white'
    assert ex09.get_chess_square_color(2, 1) == 'black'
    assert ex09.get_chess_square_color(1, 2) == 'black'
    assert ex09.get_chess_square_color(7, 7) == 'white'
    assert ex09.get_chess_square_color(0, 8) == ''
    assert ex09.get_chess_square_color(2, 9) == ''