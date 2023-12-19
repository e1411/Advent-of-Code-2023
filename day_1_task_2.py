
file = open('Day1Input.txt', 'r')
numbers = ['0','1','2','3','4','5','6','7','8','9']
spelt_nums = ['one','two','three','four','five','six','seven','eight','nine']
total = 0

for line in file:   
    num_in_line = []
    line = line.replace('one','o1e')
    line = line.replace('two','t2o')
    line = line.replace('three','th3ee')
    line = line.replace('four','fo4r')
    line = line.replace('five','fi5e')
    line = line.replace('six','s6x')
    line = line.replace('seven','se7en')
    line = line.replace('eight','ei8ht')
    line = line.replace('nine','ni9e')
    for letter in line:
        if letter in numbers:
            num_in_line.append(letter)
    #if len(num_in_line) < 2:
     #   total += int(num_in_line[0])
    print (int(str(num_in_line[0])+str(num_in_line[-1])))
    total += int(str(num_in_line[0])+str(num_in_line[-1]))
print(total)
        
