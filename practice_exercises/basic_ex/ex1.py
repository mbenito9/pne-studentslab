def find_sub(s, subseq):
    flag = True
    count = 0
    while flag:
        index = s.find(subseq)
        if index != -1:
            count += 1
            new = index + 1
            s = s[new::]
        else:
            flag = False
            print("Sequence analysized!")
    return count


if __name__ == "__main__":

    seq = "ATGCGATCGATCGATCGATCGA"
    print("Length:", len(seq))
    print("First 5:", seq[0 : 5])
    print("Last 3:", seq[-3::])
    print("Lowercase:", seq.lower())
    print("The subsequence appears:", find_sub(seq, "ATC"), "times")
    
    lst = []
    for i in seq:
        lst.append(i)
    new = ""
    for j in lst:
        if j == "T":
            index = lst.index(j)
            lst[index] = "U"
    for l in lst:
        new += l
    print("RNA:", new)