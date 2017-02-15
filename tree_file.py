import os
root = "/Users/lovestudy/Desktop/tree_test"

def space(n):
    i = 1
    while i <= n:
        print('  ', end = "")
        i += 1
        
def tree(root, n):
    if n == 1:
        print(os.path.basename(root))
    dirs = os.listdir(root)
    for dir in dirs:
        path = os.path.join(root, dir)
        if os.path.isdir(path):
            space(n)
            print(os.path.basename(path))
            tree(path, n + 1)
        if os.path.isfile(path):
            temp_path = os.path.basename(path)
            if temp_path[0] != '.':
                space(n)
                print(os.path.basename(path))

tree(root, 1)
