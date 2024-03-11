# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."



btc = s[-20:-10]
b4 = s[-44:-37]
grap = s[5:13]
leg = s[25:32]
space = s[4]

'''
s = "plumage"

s[:4]  # plum
s[4:]  # age
'''


print(btc + space + b4 + grap + space + leg)

#print(btc)
