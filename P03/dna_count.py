#another way
def count_bases(s):
    bases = {"A": 0, "G": 0, "C": 0, "T": 0}
    for base in s:
        if base in bases:
            bases[base] += 1
    return bases

def main():
    seq = str(input("Enter a DNA sequence"))
    result = count_bases(seq)

    for base, count in result.items():
       print(f"{base}: {count}")

if __name__ == "__main__":  #because if not, so that you can import count_bases in the other file, you will execute all the program
    main()