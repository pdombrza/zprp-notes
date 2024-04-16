from collections import deque


def search(lines, pattern, history=2):
    previous_lines = deque(max_len=history)

    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == "__main__":
    with open("some_file.txt", "r") as fh:
        for line, prev_lines in search(fh, pattern="python", history=3):
            for prev_line in prev_lines:
                print(prev_line, end="")
            print(line, end="")
            print("-" * 20)
