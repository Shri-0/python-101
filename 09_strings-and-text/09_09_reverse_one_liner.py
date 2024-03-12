# Reverse the string given below in a single line of code
# with the help of string slicing.

palindrome = "too bad i hid a boot "

toob = palindrome[-2] + (palindrome[-3] * 2) + palindrome[-5: -1: 4]
a = palindrome[-7]
hid = palindrome[-11:-8:3] + palindrome[-10] + palindrome[6:7]
i = palindrome[-10]
#bad = palindrome[-5: -1: 4] + palindrome[-7] + palindrome[6:7]
dab = palindrome[6:7] + palindrome[-7] + palindrome[-5: -1: 4]
oot = (palindrome[-3] * 2) + palindrome[-2]

space = palindrome[-1]

#print(space)

#print(toob + space + a + space + hid + space + i + space + dab + space + oot)

print(palindrome[::-1])     #I could have done just this :(
