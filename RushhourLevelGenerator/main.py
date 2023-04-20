from board_generator import *
from solver import *
from converter import *


def generate(minimum_moves, line_size):
    number_of_levels = 10
    with open('sample_output.txt', mode='a') as csv_file:
        counter = 0
        while counter < number_of_levels:
            try:
                board_data = BoardGenerator(line_size, line_size, 4).board_to_string()
                moves = Board(board_data).solve()
                if len(moves) >= minimum_moves:
                    csv_file.write(board_data + ",\n")
                    counter += 1
                    print("new map appended..." + str(counter)+ "/"+str(number_of_levels))

            except CannotSolveException:
                print("cannot solve...")
                pass

    print("map generation ended...")


if __name__ == '__main__':
    
    minimum_moves = 6  # If it is 4, some level will have no blocks beside rr block.
    line_size = 6      # this will determine the board size


    generate(minimum_moves, line_size) #creates the board
    print("converting sample_output.txt")
    read_file(line_size)               # converts boards into csv files
    print("Done!"+str(line_size)+"x"+str(line_size))

    # this clears the text file so it can be used again 
    with open('sample_output.txt', mode='w') as csv_file:
        csv_file.write("")

    print("reset sample_output.txt")




