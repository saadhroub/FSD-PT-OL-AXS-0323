# function definition 
# function implementation
#math, english, arabic are called parameters 
def average(math=55,english=55, arabic=55):
    avg = (math+english+arabic)/3
    print(f"Math Grade = {math}")
    print(f"English Grade = {english}")
    print(f"Arabic Grade = {arabic}")
    return avg

lambda math,english, arabic: (math+english+arabic)/3

# montaser_avg = average(95,99)
# print(f'Montaser average  = {montaser_avg}')


hamada_avg = average(arabic=80,english=99)
print(f'Hamada average  = {hamada_avg}')

# in other languages  console.log((stacks>2?"AXSOS":"Not AXSOS")
# in PYthon [on_true] if [expression] else [on_false]


temperature = 35
if(temperature>=30):
    print("I will swim")

else:
    print("I will do hiking")

print('I will swim' if temperature>=30 else 'I will do hiking')

stacks = 5
if stacks >= 3:
    print('AXSOS Academy')
else:
    print('You are not AXSOS Academy!')
# ternary
print('AXSOS Academy' if stacks >= 3 else 'You are not AXSOS Academy!')
