
n = int(input("enter your rug size(n*n): "))

pattern = ["🟥","🟧","🟨","🟩","🟦","🟪","🟫"]
def generate_rug(n):
    f = 0
    for row in range(n):
        for i in range(1, n + 1):
            print(pattern[f], end="")
            f += 1
            if f == 6:
                f = 0
        print()
    

generate_rug(n)
        
