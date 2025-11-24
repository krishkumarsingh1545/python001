import statistics
def inp(op):
    print(op, "\nEnter 0 to stop taking input")
    li = []
    i = 1
    while True:
        k = float(input(f"Enter number {i}: "))
        if k==0: break
        li.append(k)
        i+=1
    return li
    
print("Mean", statistics.mean(inp("Mean")))
print("Median", statistics.median(inp("Median")))
print("Mode", statistics.mode(inp("Mode")))
