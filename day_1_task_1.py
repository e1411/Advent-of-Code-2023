
file = open('Day1Input.txt', 'r')
numbers = ['0','1','2','3','4','5','6','7','8','9']
total = 0

for line in file:   
    num_in_line = []
    #line = line.replace('one','1')
    #line = line.replace('two','2')
    #line = line.replace('three','3')
    #line = line.replace('four','4')
    #line = line.replace('five','5')
    #line = line.replace('six','6')
    #line = line.replace('seven','7')
    #line = line.replace('eight','8')
    #line = line.replace('nine','9')
    for letter in line:
        if letter in numbers:
            num_in_line.append(letter)
    #if len(num_in_line) < 2:
     #   total += int(num_in_line[0])
    print (num_in_line)
    total += int(str(num_in_line[0])+str(num_in_line[-1]))
print(total)
        
