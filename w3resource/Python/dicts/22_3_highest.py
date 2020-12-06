#22. Write a Python program to find the highest 3 values in a dictionary. 

mydict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20, 'g' : 5i874} 
h1 = 0
h2 = 0
h3 = 0 #highest
h3= list(mydict.values())[0]
print("h3 is " + str(h3))
for k, v in mydict.items():
    if v > h3:
        h1 = h2
        h2 = h3
        h3 = v
    elif v == h3:
        h1 = h2
        h2 = v 
        
    if (v > h2 and v < h3):
        h1 = h2
        h2 = v
        
print ( " high3 {} , high2 {}, high1 {}" .format(h3, h2, h1))
