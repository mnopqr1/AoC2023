def report(filename, p, x, expected):
    print(f"File {filename}, part {p+1}, answer: {x}", end="")
    if expected is not None:
        print(f", expected answer: {expected[p]}, ", end="")
        if expected[p] == x:
            print("CORRECT")
        else:
            print("WRONG ANSWER")
    else:
        print()
