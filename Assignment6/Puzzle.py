def valid(Board, i, j):
    return i >= 0 and j >= 0 and i < len(Board) and j < len(Board[i]) and Board[i][j] == '-'

def index_helper (i, j, Path, index_answers):
    
    index_answers.append(tuple((i, j)))
    for element in Path:
        if element == "U":
            i = i - 1
            index_answers.append(tuple((i, j)))
        if element == "D":
            i = i + 1
            index_answers.append(tuple((i, j)))
        if element == "L":
            j = j - 1
            index_answers.append(tuple((i, j)))
        if element == "R":
            j = j + 1
            index_answers.append(tuple((i, j)))
    
    return index_answers 


def dfs (Board, i, j, target, route, answers):

    if not valid(Board, i, j):
        return
    if(i, j) == target:
        
        answers.append(route)
        return Board
    
    Board[i][j] = 'visited'

    if valid(Board, i - 1, j):
        dfs(Board, i - 1, j, target, route + "U", answers)
    if valid(Board, i + 1, j):
        dfs(Board, i + 1, j, target, route + "D", answers)
    if valid(Board, i, j - 1):
        dfs(Board, i, j - 1, target, route + "L", answers)
    if valid(Board, i, j + 1):
        dfs(Board, i, j + 1, target, route + "R", answers)

    Board[i][j] = "-"
    

def solve_puzzle(Board, Source, Destination):

    index_answers = []
    answers = []

    dfs(Board, Source[0], Source[1], Destination, "", answers)
    
    minlen = 1e12
    for i in answers:
        minlen = min(minlen, len(i))
    
    actual = []

    for i in answers:
        if len(i) == minlen:
            actual.append(i)

    if not len(actual):
        print(None)
        return None


    print(tuple((index_helper(Source[0], Source[1], actual[0], index_answers), actual[0])))

    return tuple((index_helper(Source[0], Source[1], actual[0], index_answers), actual[0]))



if __name__ == "__main__":
    board = [["-","-","-","-","-"],
            ["-","-","#","-","-"],
            ["-","-","-","-","-"],
            ["#","-","#","#","-"],
            ["-","#","-","-","-"]]

    Source = (0,2)
    Destination = (2,2)
    solve_puzzle(board, Source, Destination)


