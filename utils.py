from typing import List


def read_file(input_file: str) -> List[str]:
    with open(input_file) as f:
        return f.readlines()


def write_file(output_file: str, input_lst: List[str],new_line=False):
    with open(output_file, "w+") as f:
        for item in input_lst:
            if new_line:
                f.write(item + "\n")
            else:
                f.write(item)
