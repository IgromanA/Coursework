from timeit import *

def NotBalancedTree(Tree, t):
    Tree.append(t)


def search(Tree, t):
    start_time = default_timer()

    i=0
    while i < len(Tree) and t > Tree[i]:
        i += 1
    if t == Tree[i]:
        elapsed_time = default_timer() - start_time
        return elapsed_time
    else:
        return None
        

def main():
    Tree = []

    for i in range(10000):
        NotBalancedTree(Tree, i)

    print('\n--- INSERT & SEARCH ---\n')
    print(Tree)

    keys_to_search_for = [9842]
    for key in keys_to_search_for:
        if search(Tree, key) is not None:
            print(f'{key} is in the tree\nTime spent: {search(Tree, key):.9f}')
        else:
            print(f'{key} is NOT in the tree\nTime spent: {search(Tree, key):.9f}')

if __name__ == "__main__":
    main()