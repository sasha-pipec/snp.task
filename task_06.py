class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(list):
    buf = "SPR"
    if len(list) > 2:
        raise WrongNumberOfPlayersError
    elif len(list) == 1 and list[0][-1] in buf:
        return "'" + str(list[0][0]) + ' ' + str(list[0][-1]) + "'"
    else:
        if list[0][-1] not in buf or list[1][-1] not in buf:
            raise NoSuchStrategyError
        else:
            if list[0][-1] == 'S' and list[1][-1] == 'P':
                return "'" + str(list[0][0]) + ' ' + str(list[0][-1]) + "'"
            elif list[0][-1] == 'P' and list[1][-1] == 'S':
                return "'" + str(list[1][0]) + ' ' + str(list[1][-1]) + "'"
            elif list[0][-1] == 'S' and list[1][-1] == 'R':
                return "'" + str(list[1][0]) + ' ' + str(list[1][-1]) + "'"
            elif list[0][-1] == 'R' and list[1][-1] == 'S':
                return "'" + str(list[0][0]) + ' ' + str(list[0][-1]) + "'"
            elif list[0][-1] == 'P' and list[1][-1] == 'R':
                return "'" + str(list[0][0]) + ' ' + str(list[0][-1]) + "'"
            elif list[0][-1] == 'R' and list[1][-1] == 'P':
                return "'" + str(list[1][0]) + ' ' + str(list[1][-1]) + "'"
            else:
                return "'" + str(list[0][0]) + ' ' + str(list[0][-1]) + "'"


print(rps_game_winner([['player1', 'S']]))
