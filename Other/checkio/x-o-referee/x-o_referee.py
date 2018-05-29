#Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking the spaces in a 3×3 grid.
#  The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows (NW-SE and NE-SW) wins the game.
#But we will not be playing this game. You will be the referee for this games results.
# You are given a result of a game and you must determine if the game ends in a win or a draw as well as who will be the winner.
#  Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".
#x-o-referee
#A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.
#Input: A game result as a list of strings (unicode).
#Output: "X", "O" or "D" as a string.
#Example:
#checkio(["X.O","XX.","XOO"]) == "X"
#checkio(["OO.","XOX","XOX"]) == "O"
#checkio(["OOX","XXO","OXX"]) == "D"

def check_io(result):
    for row in result:
        if row.count('O') == 3:
            return ("O")
        elif row.count("X") == 3:
            return ("X")

    if result[0][0] == result[1][0] == result[2][0] and result[0][0] != ".":
        return (result[0][0])
    elif result[0][1] == result[1][1] == result[2][1] and result[0][1] != ".":
        return( result[0][1])
    elif result[0][2] == result[1][2] == result[2][2] and result[0][2] != ".":
        return( result[0][2])
    elif result[0][0] == result[1][1] == result[2][2] and result[0][0] != ".":
        return (result[0][0])
    elif result[0][2] == result[1][1] == result[2][0] and result[0][2] != ".":
        return (result[0][2])
    else:
        return ("D")


if __name__ == "__main__":
    print(checkio(["XX.", "XX0", "XOX"]))


