def gen_patt(n):
    k = int(1)
    for i in range(n):
        row = ""
        for j in range(i+1):
            # print(k)
            row += str(k) + " "
            k = k+1
        print(row)


n = input()
gen_patt(int(n))
