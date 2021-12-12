with open("verksted_npst.txt") as f:
    data = f.readlines()
    del data[0]
    data = [e.split(";") for e in data]

    for i, line in enumerate(data):
        for j, string in enumerate(line):
            data[i][j] = "".join(string.split())

    data.sort(key=lambda e: e[2])

    letters_hex = []
    for line in data:
        if len(line[1]) == 2:
            try:
                dec = chr(int(line[1], 16))
                if dec.isalpha() or line[1] == "7b" or line[1] == "7d":
                    letters_hex.append(dec)
            except:
                continue

    print("".join(letters_hex))
