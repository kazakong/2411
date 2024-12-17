n = int(input())
n = 1 < n < 100000

for dataset in range(10):
    n = int(input())
adresses = []
for i in range(n):
    address = input()
    address = clean(adress)
    if not address in addresses:
        addresses.append(address)

print(len(addresses))

