from collections import Counter
import random
import sys

def actual(iterable):
    return len(Counter(iterable).keys())

def estimate(iterable, size=100):
    assert size >= 1
    board, p  = set(), 1
    for i,symbol in enumerate(iterable):
        if symbol in board:
            board.remove(symbol)
        if random.random() < p:
            board.add(symbol)
        if len(board) == size:
            p /= 2
            board = {symbol for symbol in board if random.randint(0,1)}
    return len(board) / p

def main():
    if len(sys.argv) not in {2,3}:
        print("Usage: python script_name.py <file_path> <size>")
        sys.exit(1)

    file_path = sys.argv[1]
    board_size = 100
    if len(sys.argv) == 3:
        board_size = int(sys.argv[2])

    try:
        with open(file_path, 'r') as file:
            def traverse(f):
                for line in f:
                    for word in line.split():
                        yield word
            print(estimate(traverse(file), board_size))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
