plaintext = "informationsecurity"
key = "lock"

col = len(key)
row = len(plaintext) // len(key) + 1

while len(plaintext) < row * col:
    plaintext += "x"

matrix = []
index = 0

for i in range(row):
    rows = []
    for j in range(col):
        rows.append(plaintext[index])
        index += 1
    matrix.append(rows)

order = []
for i in range(col):
    count = 0
    for j in range(col):
        if key[j] < key[i]:
            count += 1
    order.append(count)

ciphertext = ""
for num in range(col):
    for i in range(col):
        if (order[i] == nums):
            for j in range(row):
                ciphertext += matrix[j][i]

print("CipherText: ", ciphertext)