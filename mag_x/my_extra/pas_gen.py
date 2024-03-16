import random


def pas_gen(max_len=8):
    min_len = 8
    ch_list = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", "1234567890", "!@#$%&*(){}[]?"]
    taken_list = [False, False, False, False]
    result = ""
    last_ch = ""
    if max_len < min_len:
        max_len = min_len
    i = 0
    safe = 0
    while i < max_len:
        ch_type = random.randrange(0, 4)
        if i > (max_len - 4):
            for j in range(4):
                if not taken_list[j]:
                    ch_type = j
                    break
        ch = random.choice(ch_list[ch_type])
        if ch != last_ch:
            if not taken_list[ch_type]:
                taken_list[ch_type] = True
            result += ch
            last_ch = ch
            i += 1
        if safe >= (50 + max_len):
            break
        safe += 1
    return result
