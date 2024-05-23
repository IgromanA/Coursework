from time import *

def NotBalancedTree(Tree, t):
    Tree.append(t)


def search(Tree, t):
    start_time = time()

    i=0
    while i < len(Tree) and t > Tree[i]:
        i += 1
    if t == Tree[i]:
        end_time = time()
        elapsed_time = round(end_time - start_time, 9)
        return elapsed_time
    else:
        return None
        

def main():
    Tree = []

    for i in range(1000000):
        NotBalancedTree(Tree, i)

    print(Tree)

    keys_to_search_for = [994937]
    for key in keys_to_search_for:
        if search(Tree, key) is not None:
            print(f'{key} is in the tree\nTime spent: {search(Tree, key)}')
        else:
            print(f'{key} is NOT in the tree\nTime spent: {search(Tree, key)}')

if __name__ == "__main__":
    main()