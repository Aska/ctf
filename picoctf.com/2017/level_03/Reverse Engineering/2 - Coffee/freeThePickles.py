import base64

list_one = "eux_Z]\\ayiqlog`s^hvnmwr[cpftbkjd".encode()
list_two = "Zf91XhR7fa=ZVH2H=QlbvdHJx5omN2xc".encode()
list_three = []

for i in range(len(list_one)):
	list_three.append(list_two[list_one[i] - 90])

string = bytearray(list_three).decode()
print("The flag is:", base64.b64decode(string).decode())