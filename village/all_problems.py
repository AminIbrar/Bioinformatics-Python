# ----- intalling python -----

#import this

# ----- variables and some arithmetic -----

a = 3
b = 5
result = a**2 + b**2
print(result)

# ----- Strings and lists -----

strng = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain"
wordOneStart = 22
wordOneEnd = 27
wordTwoStart = 97
wordTwoEnd = 102
print(f"{strng[wordOneStart:wordOneEnd+1]} {strng[wordTwoStart:wordTwoEnd+1]}")

# ----- Conditions and loops -----

a = 100
b = 200
add = 0
for i in range(100,200 + 1):
    if i%2 !=0:
        add += i
print(add)

# ----- Reading and writing-----

outputFile = []
with open("village/input.txt",'r') as f:
    outputFile = [line for pos, line in enumerate(f.readlines())
                  if pos%2 != 0]
with open("village/out.txt",'w') as f:
    f.write(''.join([line for line in outputFile]))

# ----- Intro to Python Dictionary-----

txt = "We tried list and we tried dicts also we tried Zen"
word_lst = txt.split(' ')
word_dict = {key:0 for key in word_lst}
for word in word_lst:
    word_dict[word] += 1
for key,val in word_dict.items():
    print(f"{key} {val} \n")