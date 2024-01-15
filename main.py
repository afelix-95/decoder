import numpy as np
import supportft


def decoderdrive():  # Testing unit; the for-loop is to make sure that all 3 messages appear well decoded at least once
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
    txt = list(fileread(filename))
    txt = [downlow(char) for char in txt]

    key = np.random.permutation(27) + 1  # Random initial guess

    for _ in range(10000):
        k1, k2 = np.random.randint(1, 28, size=2)
        keymaybe = key.copy()
        keymaybe[[k1 - 1, k2 - 1]] = keymaybe[[k2 - 1, k1 - 1]]  # Here is generated a possible alternate key by switching two random elements within the initial guess

        l1 = loglike(txt, key)
        l2 = loglike(txt, keymaybe)

        if l1 < l2 or np.random.rand() < np.exp(-l1 + l2):  # Conditions to replace the initial guess with the new guess based on log-likelihood
            key = keymaybe

    txt = [key[char - 1] for char in txt]
    txt = [downlowinv(char) for char in txt]

    return ''.join(map(chr, txt))


# Example usage
decoderdrive()
