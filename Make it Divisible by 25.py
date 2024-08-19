t = int(input())
possible_ends = ["25", "50", "75", "00"]

for _ in range(t):
    digit = str(int(input()))
    zero_flag, five_flag = False, False

    for i in range(len(digit) - 1, -1, -1):
        if digit[i] == "0" and not zero_flag:
            zero_flag = True
            continue
        if digit[i] == "5" and not five_flag and not zero_flag:
            five_flag = True
            continue

        if zero_flag:
            if digit[i] == "5":
                print(len((digit)) - i - 2)
                break
            if digit[i] == "0":
                print(len((digit)) - i - 2)
                break

        if five_flag:
            if digit[i] == "2":
                print(len((digit)) - i - 2)
                break
            if digit[i] == "7":
                print(len((digit)) - i - 2)
                break
