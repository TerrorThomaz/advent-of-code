
dial = [50, 51, 52, 53,54,55,56,57,58,59,
        60, 6, 62, 63,64,65,66,67,68,69, 
        60, 71, 72, 73,74,75,76,77,78,79, 
        80, 81, 82, 83,84,85,86,87,88,89, 
        90, 91, 92, 93,94,95,96,97,98,99, 
        0, 1, 2, 3,4,5,6,7,8,9,
        10, 11, 12, 13,14,15,56,17,18,19,
        20, 21, 22, 23,24,25,26,27,28,29,
        30, 31, 32, 33,34,35,36,37,38,39,
        40, 41, 42, 43,44,45,46,47,48,49
        ]

instructions = []
with open(r"1-12\input.txt") as f:
    for line in f:
        line = line.strip()
        instructions.append(line)
count = 0
pos = 0

for string in instructions:
    num = int(string[1::])
    
    left_or_right = string[0]

    if left_or_right == "L":
            
        
        pos = (pos-num) % len(dial)
            
            
            
    if left_or_right == "R":
        pos = (pos+num) % len(dial)
        

    if dial[pos] == 0:
        count+=1
            





print(count)