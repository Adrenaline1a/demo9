if __name__ == "__main__":
    U = set("abcdefghijklmnopqrstuvwxyz")
    A = {'c', 'e', 'h', 'n'}
    B = {'e', 'f', 'k', 'n', 'x'}
    C = {'b', 'c', 'h', 'p', 'r', 's'}
    D = {'b', 'e', 'g'}
    print((A - B) & (C | D))
    print((C - D) | (A & (U - B)))
