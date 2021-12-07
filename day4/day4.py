from pprint import pprint

with open("input.txt") as f:
        data = f.readlines()
 
drawn_number = data[0].split(",")
boards = data[1:]
boards = [i.strip() for i in data[1:]]  #Removes \n and ''
boards = [i for i in boards if i != ''] #Removes the spaces

class Board:
    def __init__(self, board):
        self.board = board

    def getBoard(self):
        return self.board

    def sumUnmarked(self, listNumbers):
        print("")
        anBoard = self.getBoard()
        for dnumber in listNumbers:
            for rowNumber in range(len(anBoard)):
                for number in anBoard[rowNumber]:
                    #print(f"number : {number}")
                    if number == dnumber:
                        #print(f"loong {anBoard[rowNumber]}")
                        anBoard[rowNumber].remove(number)

        summation = 0
        for rows in anBoard:
            for i in rows:
                summation += int(i)

        return summation 

    def checkBoard(self, listNumbers): #True or false when this board has won
        for rows in range(0, len(self.board)):
            rowCounter = 0
            for i in listNumbers:
                if i in self.board[rows]:
                    rowCounter += 1
                if rowCounter == 5:
                    return True

        for row in range(0, len(self.board)):
            columCounter = 0
            temp = []
            for colums in range(0, len(self.board)):      
                temp.append(self.board[colums][row])
            for i in listNumbers:
                if i in temp:
                    columCounter += 1  
                if columCounter == 5:
                    return True
        return False

obj_boards = []   
for i in range(0, len(boards)-3, 5):
    obj_boards.append(Board([[x for x in boards[i].split(' ') if x != ''],
                             [x for x in boards[i+1].split(' ') if x != ''],
                             [x for x in boards[i+2].split(' ') if x != ''],
                             [x for x in boards[i+3].split(' ') if x != ''],
                             [x for x in boards[i+4].split(' ') if x != '']]))

def main():
    winner_list = []
    for a in range(1, len(drawn_number)):
        #print(f"list of drawn Numbers : {drawn_number[0:a]}")

        for b in obj_boards:
            if b.checkBoard(drawn_number[0:a]):
                winner_list.append([b, drawn_number[0:a]])
                obj_boards.remove(b)
            
    #print(f"Current List : {drawn_number[0:a]}")
    print(f"winner sum: {winner_list[0][0].sumUnmarked(winner_list[0][1])} winner drawn number {winner_list[0][1][-1]}")
    print(f"loser sum: {winner_list[-1][0].sumUnmarked(winner_list[-1][1])} winner drawn number {winner_list[-1][1][-1]}")

print(main())