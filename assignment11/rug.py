n = int(input("Enter a number: "))

def generate_rug(n):
    if n % 2 == 0:
        return "Please enter an odd number."
    
    emojis = ["⚪", "🟡", "🟠", "🔴", "🟢", "🔵", "🟣", "🟤", "⚫"]
    rug = [[0] * n for _ in range(n)]
    middle = n // 2
    
    for i in range(middle, -1, -1):
        for j in range(n):
            rug[i][j] = emojis[middle - i]
            rug[n-1-i][j] = emojis[middle - i]
            rug[j][i] = emojis[middle - i]
            rug[j][n-1-i] = emojis[middle - i]
            
    for row in rug:
        for c in row:
            print(c, end=' ')
        print()

generate_rug(n)