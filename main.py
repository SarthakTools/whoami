from dataclasses import replace


binary_digit = int(input("Enter a number : "))
binary_form = bin(binary_digit)
replace_binary_form = binary_form.replace("0b", "")
print(f'The number in binary form of {binary_digit} is : {replace_binary_form}')
