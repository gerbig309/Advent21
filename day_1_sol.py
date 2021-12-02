lines = []
with open('day_1.txt') as f:
    lines = f.readlines()
    
first = 0
next = 1
count = 0
for line in lines:
    if lines[next] > lines[first]:
        count += 1
        first += 1
        next += 1
        if next == 2001:
            print(count)
            break
    else:
        first += 1
        next += 1
        
