def fileread(filename):
    with open(filename, 'r') as file:
        return file.read()


def downlow(n):
    return 27 if n == '`' else ord(n) - 96


def downlowinv(n):
    return 32 if n == 27 else n + 96


def loglike(txt, key):
    x = 0
    matrix = np.loadtxt('letterprob.txt')

    for j in range(len(txt) - 1):
        x += np.log(matrix[key[txt[j] - 1] - 1, key[txt[j + 1] - 1] - 1])

    return x
