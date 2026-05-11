class ChessGame:
    def __init__(self, board, current_player, move_history):
        self.board = board
        self.current_player = current_player
        self.move_history = move_history
        self.game_over = False


    def printBoard(self):
        pieces_pos = [
            ["r", "n", "b", "q", "k", "b", "n", "r"], 
            ["p", "p", "p", "p", "p", "p", "p", "p"], 
            ["", "", "", "", "", "", "", ""], 
            ["", "", "", "", "", "", "", ""], 
            ["", "", "", "", "", "", "", ""], 
            ["", "", "", "", "", "", "", ""]
        ]
        print("  A  B  C  D  E  F  G  H")
        for i in range(0, 9):
            print(f"{8-i} ")
            for j in range (0, 9):
                print(f"{pieces_pos[i][j]}")

        self.board = pieces_pos


    def startGame(self):
        printBoard()


    def makeMove(self, startPos, endPos):
        pass 

    def switchTurn(self):
        pass

    def checkGameState(self):
        pass

    def undoMove(self):
        pass

    def isGameOver(self):
        pass 
