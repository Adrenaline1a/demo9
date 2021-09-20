# X = (A\B) /\ ( C u D)     Y = (A /\ not(B)) u (C\D)
if __name__ == "__main__":
    U = set("abcdefghijklmnopqrstuvwxyz")
    A = {'c', 'e', 'h', 'n'}
    B = {'e', 'f', 'k', 'n', 'x'}
    C = {'b', 'c', 'h', 'p', 'r', 's'}
    D = {'b', 'e', 'g'}
    print('X =', (A - B) & (C | D))
    print('Y =', (C - D) | (A & (U - B)))
