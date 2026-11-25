# vowels

string=input("Enter the string: ")
vow=0
con=0

for i in string.lower():
    if i in "aeiou":
        vow+=1
    else:
        con+=1

print(f"Vowels {vow}")            
print(f"Concunent {con}")