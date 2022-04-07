def generate_five_elements():
    generated_array = []

    for _ in range(5):
        element_entered = int(input('Please enter a number: '))
        generated_array.append(element_entered)

    ascending_array = sorted(generated_array)
    print(ascending_array)

    descending_array = sorted(generated_array, reverse=True)
    print(descending_array)


generate_five_elements()
