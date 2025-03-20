import random
import string

replacement_dict = {}
selected_letters = set()

for _ in range(5):
    while True:
        letter = input("Enter a lowercase letter: ")
        if letter in string.ascii_lowercase and letter not in selected_letters:
            selected_letters.add(letter)
            replacement_dict[letter] = set()
            break
        print("Invalid or duplicate letter. Please enter a different letter.")

    while len(replacement_dict[letter]) < 3:
        replacement = input(f"Enter a replacement character for '{letter}': ")
        if len(replacement) == 1 and replacement not in replacement_dict[letter]:
            replacement_dict[letter].add(replacement)
        else:
            print("Invalid input! Enter a single character and avoid duplicates.")

passwords = [''.join(random.choices(string.ascii_lowercase, k=15)) for _ in range(5)]

categorized_passwords = {"strong": [], "weak": []}

for password in passwords:
    modified_password = list(password)
    replaced_count = 0

    for i, char in enumerate(modified_password):
        if char in replacement_dict:
            modified_password[i] = random.choice(list(replacement_dict[char]))
            replaced_count += 1

    modified_password = ''.join(modified_password)

    if replaced_count > 4:
        categorized_passwords["strong"].append(modified_password)
    else:
        categorized_passwords["weak"].append(modified_password)

print("\nGenerated Passwords:")

print("\nSTRONG PASSWORDS:")
if categorized_passwords["strong"]:
    print(*categorized_passwords["strong"], sep="\n")
else:
    print("(No strong passwords found)")

print("\nWEAK PASSWORDS:")
if categorized_passwords["weak"]:
    print(*categorized_passwords["weak"], sep="\n")
else:
    print("(No weak passwords found)")
