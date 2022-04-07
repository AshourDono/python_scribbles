generated_array = []
length = int(input('Please enter array length: '))
start = int(input('Please enter your starting number: '))


def generate_array(length, start):
    for _ in range(start, start+length):
        generated_array.append(start)
        start += 1

    print(generated_array)


generate_array(length, start)
