def report(filename, answers, expected):
    for p, x in enumerate(answers):
        print(f"File {filename}, part {p+1}, answer: {x}", end="")
        if expected is not None:
            print(f", expected answer: {expected[p]}, ", end="")
            if expected[p] == x: print("CORRECT")
            else: print("WRONG")
        else:
            print()