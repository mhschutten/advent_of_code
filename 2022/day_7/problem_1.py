import re

ls_re = re.compile(r'(dir|\d+) (.*)')


def peek_line(f):
    pos = f.tell()
    line = f.readline()
    f.seek(pos)

    return line


def get_current_dir(file_tree, cur_path):
    current_folder = file_tree

    for folder in cur_path:
        current_folder = current_folder[folder]

    return current_folder


def create_file_tree(lines):
    file_tree = {"/": dict()}
    cur_path = ['/']

    while True:
        line = f.readline()[:-1]
        print(line)
        if not line:
            break

        if line == '$ cd /':
            cur_path = ['/']

        if line == '$ ls':
            cur_dir = get_current_dir(file_tree, cur_path)

            while not peek_line(f).startswith('$'):
                dir_content = f.readline()
                size, filename = ls_re.match(dir_content).groups()
                cur_dir[filename] = dict() if size == 'dir' else int(size)

            break


with open('input.txt', 'r') as f:
    create_file_tree(f)
