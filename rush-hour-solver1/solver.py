import time
import os
#import click

from src.algorithm.algorithm import (a_star, beam_search, breadth_first_search,
                                     depth_first_search)
from src.model.board import Board

ALGORITHM_NAME_MAPPING = {
    "astar": a_star,
    "beam": beam_search,
    "bfs": breadth_first_search,
    "dfs": depth_first_search,
}


"""@click.command()
@click.option(
    "--algorithm",
    required=True,
    type=click.Choice(ALGORITHM_NAME_MAPPING.keys(), case_sensitive=True),
)
@click.option(
    "--board",
    required=True,
    type=click.Path(exists=True, readable=True),
)"""

def solve2(algorithm, board, id):
    algorithm_implementation = ALGORITHM_NAME_MAPPING[algorithm]
    # This will solve boards in the sub folders 6x6/7x7/8x8/etc depending on the board variable
    board_to_solve = Board.from_csv("./boards/"+board+"/board"+board+"_"+id+".csv")

    start = time.perf_counter()
    result = algorithm_implementation(board_to_solve)
    end = time.perf_counter()
    print(
        f"Found solution of {board} board id:{id} in {result.node.depth} "
        f"steps with {algorithm_implementation.__name__}. "
        f"Explored {result.number_of_explored_states} "
        f"states in {end - start} seconds."
    )

def solve(algorithm: str, board: str) -> None:
    algorithm_implementation = ALGORITHM_NAME_MAPPING[algorithm]
    board_to_solve = Board.from_csv(board)

    start = time.perf_counter()
    result = algorithm_implementation(board_to_solve)
    end = time.perf_counter()
    print(
        f"Found solution of {result.node.depth} "
        f"steps with {algorithm_implementation.__name__}. "
        f"Explored {result.number_of_explored_states} "
        f"states in {end - start} seconds."
    )


if __name__ == "__main__":
    #solve()
    alo = "astar"
    board = os.path.join(os.path.dirname(__file__), "./boards/board1.csv")

    solve(alo, board)

    """
    # This following code was used to solve all the boards in the 6x6/7x7/8x8/etc folders
    board = "6x6"
    #this will solve all boards in folder 6x6
    for count in range(1,11):
        solve2(alo, board, str(count))
    
    board = "7x7"
    #this will solve all boards in folder 7x7
    for count in range(1,11):
        solve2(alo, board, str(count))

    board = "8x8"
    for count in range(1,11):
        solve2(alo, board, str(count))


    board = "9x9"
    for count in range(1,11):
        solve2(alo, board, str(count))


    board = "10x10"
    for count in range(1,11):
        solve2(alo, board, str(count))


    board = "11x11"

    for count in range(1,11):
        solve2(alo, board, str(count))

    board = "12x12"
    for count in range(1,11):
        solve2(alo, board, str(count))


    board = "13x13"
    for count in range(1,11):
        solve2(alo, board, str(count))


    board = "14x14"
    for count in range(1,11):
        solve2(alo, board, str(count))


    board = "15x15"
    for count in range(1,11):
        solve2(alo, board, str(count))"""
    
    print("done!")








