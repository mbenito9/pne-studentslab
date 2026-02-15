if __name__ == "__main__":
    flag = True
    while flag:
        score = input("Enter a numeric score")
        if score == "no":
            flag = False
            print("You stopped analysizing grades")
        else:
            score = float(score)
            if 0.0 <= score <= 2.9:
                print("F")
            elif 3.0 <= score <= 4.9:
                print("D")
            elif 5.0 <= score <= 6.9:
                print("C")
            elif 7.0 <= score <= 8.9:
                print("B")
            elif 9.0 <= score <= 10.0:
                print("A")