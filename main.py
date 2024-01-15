import numpy as np


def decoderdrive():
    for i in range(3):
        text1 = decoder('encodedtext1.txt')
        text2 = decoder('encodedtext2.txt')
        text3 = decoder('encodedtext3.txt')
        print('Text 1:')
        print(text1)
        print('\nText 2:')
        print(text2)
        print('\nText 3:')
        print(text3)
        print('\n')


def decoder(filename):
    T = list(fileread(filename))
    T = [downlow(char) for char in T]

    y = np.random.permutation(27) + 1  # Random initial guess

    for _ in range(10000):
        k1, k2 = np.random.randint(1, 28, size=2)
        ymaybe = y.copy()
        ymaybe[[k1 - 1, k2 - 1]] = ymaybe[[k2 - 1, k1 - 1]]

        l1 = loglike(T, y)
        l2 = loglike(T, ymaybe)

        if l1 < l2 or np.random.rand() < np.exp(-l1 + l2):
            y = ymaybe

    T = [y[char - 1] for char in T]
    T = [downlowinv(char) for char in T]

    return ''.join(map(chr, T))


def fileread(filename):
    with open(filename, 'r') as file:
        return file.read()


def downlow(n):
    return 27 if n == '`' else ord(n) - 96


def downlowinv(n):
    return 32 if n == 27 else n + 96


def loglike(T, y):
    x = 0
    M = np.loadtxt('letterprob.txt')

    for j in range(len(T) - 1):
        x += np.log(M[y[T[j] - 1] - 1, y[T[j + 1] - 1] - 1])

    return x


# Example usage
decoderdrive()
