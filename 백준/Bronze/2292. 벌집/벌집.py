N = int(input())
    
room = 1
layer = 1
    
while room < N:
    room += 6 * layer
    layer += 1
        
print(layer)