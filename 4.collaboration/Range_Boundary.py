def print_top_three():
    rankings = ["Gold", "Silver", "Bronze", "Runner-up"]
    
    print("Top 3 Medals:")
    
    # HINT: In Python, range(start, stop) stops BEFORE the 'stop' number. 
    # How far should the range go to print exactly 3 items?
    for i in range(1, 3):
        print(f"Rank {i}: {rankings[i-1]}")

print_top_three()