
with open('in.txt') as fh:
    bitmap = fh.read().strip()


block_size = 25 * 6
layers = {}
layer_num = 1
lowest_zero_layer = 1
lowest_zero_count = len(bitmap)
while layer_num * block_size <= len(bitmap):
    layers[layer_num] = {}
    layer = bitmap[layer_num * block_size - block_size:layer_num * block_size]
    for char in layer:
        try:
            layers[layer_num][char] += 1
        except KeyError:
            layers[layer_num][char] = 1
    if layers[layer_num]['0'] < lowest_zero_count:
        lowest_zero_layer = layer_num
        lowest_zero_count = layers[layer_num]['0']
    layer_num += 1

answer = layers[lowest_zero_layer]['1'] * layers[lowest_zero_layer]['2']
print(answer)
