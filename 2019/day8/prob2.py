import matplotlib.pyplot as plt

with open('in.txt') as fh:
    bitmap = fh.read().strip()

block_size = 25 * 6
#block_size = 2 * 2
layers = []
layer_num = 1
while layer_num * block_size <= len(bitmap):
    layer = bitmap[layer_num * block_size - block_size:layer_num * block_size]
    layers.append(layer)
    layer_num += 1

message = [[]]
row = 0
for i in range(block_size):
    for layer in layers:
        if layer[i] != '2':
            message[row].append([float(layer[i]), float(layer[i]), float(layer[i])])
            if len(message[row]) == 25:
                row += 1
                if row < 6:
                    message.append([])
            break
#print(layers)

#for row in range(0, 150, 25):
#    for char in bitmap[row:row+25]:
#        if char == '0':
#            print('+', end='')
#        else:
#            print('-', end='')
#    print()

for i, row in enumerate(message):
    print(f'row {i} has {len(row)} elements')
print(message)
plt.imshow(message)
plt.show()
