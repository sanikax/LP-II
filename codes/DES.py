# Initial Permutation
IP = [1, 5, 2, 0, 3, 7, 4, 6]

# Final Permutation
IP_INV = [3, 0, 2, 4, 6, 1, 7, 5]

# Expansion Permutation
EP = [3, 0, 1, 2, 1, 2, 3, 0]

# P4 Permutation
P4 = [1, 3, 2, 0]

# S-Boxes
S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]


# permutation function
def permute(bits, table):
    return "".join(bits[i] for i in table)


# xor function
def xor(a, b):
    ans = ""
    for i in range(len(a)):
        ans += str(int(a[i]) ^ int(b[i]))
    return ans


# s-box function
def sbox(bits, box):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return format(box[row][col], '02b')


# feistel function
def feistel(right, key):

    # expansion
    temp = permute(right, EP)

    # xor with key
    temp = xor(temp, key)

    # split into 2 parts
    left = temp[:4]
    right = temp[4:]

    # s-box output
    temp = sbox(left, S0) + sbox(right, S1)

    # p4 permutation
    return permute(temp, P4)


# encryption
def encrypt(text, key):

    # initial permutation
    text = permute(text, IP)

    left = text[:4]
    right = text[4:]

    # 2 rounds
    for i in range(2):

        temp = feistel(right, key)

        # xor with left
        new_right = xor(left, temp)

        left = right
        right = new_right

    # combine and final permutation
    text = right + left

    return permute(text, IP_INV)


# main
plain = input("Enter 8-bit plaintext: ")
key = input("Enter 8-bit key: ")

cipher = encrypt(plain, key)

print("Encrypted Text:", cipher)