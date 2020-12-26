# find one loop size
public_keys = [15113849, 4206373]
value = 1
loop_size = 0
while value not in public_keys:
    loop_size += 1
    value = (value * 7) % 20201227

# find encryption key
public_keys.remove(value)
encryption_key = 1
for i in range(loop_size):
    encryption_key = (encryption_key * public_keys[0]) % 20201227

print(encryption_key)
