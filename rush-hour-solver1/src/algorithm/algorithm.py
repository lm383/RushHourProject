import collections
import heapq
from dataclasses import dataclass
from typing import List, Set

from ..model.board import Board
from ..model.node import ChildNode, Node

import psutil

class NoSolutionFoundException(Exception):
    pass


@dataclass(frozen=True)
class Result:
    node: Node
    number_of_explored_states: int
    complete_board: list
    max_memory: str

def breadth_first_search(board: Board, max_depth: int = 1000) -> Result:
    max_memory = 0
    depth = 0
    visited_nodes: Set[Board] = set()
    root = Node(board)
    queue = list([root])
    complete_board =[]

    if root.board.is_final_configuration():
        return Result(root, len(visited_nodes))

    while len(queue) & depth < max_depth:
        current_node = queue.pop(0)
        depth = current_node.depth

        if current_node.board.is_final_configuration():
            
            return Result(node, len(visited_nodes), complete_board)
        else:
            for possible_move in current_node.board.get_moves():
                child_board = current_node.board.move_vehicle(move=possible_move)

                if child_board not in visited_nodes:
                    node = ChildNode(
                        board=child_board, parent=current_node, depth=depth + 1
                    )
                    visited_nodes.add(child_board)
                    queue.append(node)
                    # checks how many bytes are currently being used and if its the maximum
                    memory = psutil.Process().memory_info().rss
                    if memory> max_memory:
                        max_memory = memory

                    if child_board.is_final_configuration():
                        complete_board= child_board
                        return Result(node, len(visited_nodes), complete_board, str(max_memory))

    raise NoSolutionFoundException()


def depth_first_search(board: Board, max_depth: int = 10000) -> Result:
    depth = 0
    visited_nodes: Set[Board] = set()
    root = Node(board)
    queue = list([root])
    complete_board =[]
    max_memory = 0

    if root.board.is_final_configuration():
        return Result(node, len(visited_nodes), complete_board)

    while len(queue) & depth < max_depth:
        current_node = queue.pop()
        depth = current_node.depth

        for possible_move in current_node.board.get_moves():
            child_board = current_node.board.move_vehicle(move=possible_move)

            if child_board not in visited_nodes:
                node = ChildNode(
                    board=child_board, parent=current_node, depth=depth + 1
                )
                visited_nodes.add(child_board)
                queue.append(node)
                # checks how many bytes are currently being used and if its the maximum
                memory = psutil.Process().memory_info().rss
                if memory> max_memory:
                    max_memory = memory

                if child_board.is_final_configuration():
                    return Result(node, len(visited_nodes), complete_board, str(max_memory))

    raise NoSolutionFoundException


def iterative_deepening_depth_first_search(
    board: Board, max_depth: int = 1000
) -> Result:
    local_max_depth = 1
    visited_nodes: Set[Node] = set()
    root = Node(board)
    stack = collections.deque()
    stack.append(root)
    complete_board =[]

    if root.board.is_final_configuration():
        return Result(node, len(visited_nodes), complete_board)

    while len(stack):
        current_node = stack.popleft()
        depth = current_node.depth

        for possible_move in current_node.board.get_moves():
            child_board = current_node.board.move_vehicle(move=possible_move)

            if child_board not in visited_nodes and depth <= local_max_depth:
                node = ChildNode(
                    board=child_board, parent=current_node, depth=depth + 1
                )
                visited_nodes.add(child_board)
                stack.append(node)

                if child_board.is_final_configuration():
                    return Result(node, len(visited_nodes), complete_board)

        if len(stack) == 0 and local_max_depth <= max_depth:
            stack.append(root)
            visited_nodes.clear()
            visited_nodes.add(root)
            local_max_depth += 1

    raise NoSolutionFoundException


def a_star(board: Board, max_depth: int = 1000) -> Result:
    depth = 0
    visited_nodes: Set[Board] = set()
    sorted_list: List[Node] = list()
    root = Node(board, depth)
    heapq.heappush(sorted_list, root)
    complete_board =[]
    max_memory = 0

    if root.board.is_final_configuration():
        return Result(node, len(visited_nodes), complete_board)

    while len(sorted_list) & depth < max_depth:
        current_node = heapq.heappop(sorted_list)
        depth = current_node.depth

        for possible_move in current_node.board.get_moves():
            child_board = current_node.board.move_vehicle(move=possible_move)

            if child_board not in visited_nodes:
                visited_nodes.add(child_board)
                node = ChildNode(
                    board=child_board,
                    parent=current_node,
                    depth=depth + 1,
                    value=child_board.get_minimum_cost() + depth,
                )
                heapq.heappush(sorted_list, node)
                # checks how many bytes are currently being used and if its the maximum
                memory = psutil.Process().memory_info().rss
                if memory> max_memory:
                    max_memory = memory

                if child_board.is_final_configuration():
                    return Result(node, len(visited_nodes), complete_board, str(max_memory))

    raise NoSolutionFoundException


def beam_search(board: Board, width: int = 2, max_depth: int = 1000) -> Result:
    depth = 0
    visited_nodes: Set[Board] = set()
    root = Node(board, depth)
    queue: List[Node] = list([root])
    complete_board =[]
    max_memory = 0

    if root.board.is_final_configuration():
        return Result(node, len(visited_nodes), complete_board)

    while len(queue) & depth < max_depth:
        current_node = queue.pop(0)
        depth = current_node.depth

        beam: List[Node] = list()

        for possible_move in current_node.board.get_moves():
            child_board = current_node.board.move_vehicle(move=possible_move)

            if child_board not in visited_nodes:
                visited_nodes.add(child_board)
                node = ChildNode(
                    board=child_board,
                    parent=current_node,
                    depth=depth + 1,
                    value=child_board.get_minimum_cost() + depth,
                )

                heapq.heappush(beam, node)
                # checks how many bytes are currently being used and if its the maximum
                memory = psutil.Process().memory_info().rss
                if memory> max_memory:
                    max_memory = memory

                if child_board.is_final_configuration():
                    return Result(node, len(visited_nodes), complete_board, str(max_memory))

        for i, child in enumerate(beam):
            if i < width:
                queue.append(child)

    raise NoSolutionFoundException
