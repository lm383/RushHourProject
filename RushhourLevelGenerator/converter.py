"""
This progam will take 1 txt file and hopefully convert it into several csv files
while converting it should: 
    - change any '.' into '-1' and
    - put a ',' between all elements
    - convert any '0' into an unused higher number and then convert any 'r' into '0'  
the csv files should then be saved in the boards folder
"""
import csv

def read_file(size):
    board = []
    text = open("sample_output.txt", "r")
    csvCount =0
    for count in text:
        board.append(count)
        if count.__contains__(","):
            # end of board
            csvCount+=1
            #board.append(count)
            make_file(board, csvCount, size)
            board.clear() 
            

    text.close

    return 


def make_file(linesBoard, boardId, size):
    # gets 1 board line by line processes and saves it
    completeBoard = []
    #print(linesBoard)
    boardSize = size
    boardSize = boardSize.__str__() + "x"+ boardSize.__str__()

    max = 0
    # finds the max vehicle and adds 1 so that will be the vehicle id for the current vehicle '0'
    for line in linesBoard:
        #print(linesBoard.__str__())
        for element in line:
            #print(line.__str__())
            if element.isnumeric() and max<int(element):
                max = int(element)
    max+=1
    for count in linesBoard:
        completeBoard.append(process_file(count, max.__str__()))
    #print(completeBoard.__str__()+ "  P")
    with open("boards\\board"+boardSize+"_"+boardId.__str__()+".csv", "w", newline='') as csvFile:
        write = csv.writer(csvFile)
        for count in completeBoard:
            write.writerow(count)
    csvFile.close()

    return

def process_file(unprocessedText, max):
    processed = []
    
    #print(unprocessedText.__str__()+ "U")
    for element in unprocessedText:
        if element == ".":
            processed.append( "-1")
        elif element == '0':
            #print(max)
            processed.append(max)
        elif element == ',' or element == '\n':
            break # dont add it to processed
        elif element == 'r':
            processed.append("0")
        else:
            processed.append(element)
    #print(processed.__str__()+ "  P")
    return processed


if __name__ == '__main__':
    # first open the txt file, read it and separate from the ',' while removing them 
    print("converting sample_output.txt")
    read_file(9)

    print("Done!")

