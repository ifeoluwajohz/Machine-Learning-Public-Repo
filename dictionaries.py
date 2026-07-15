birthday = {
    "Alice": "1990-01-01",
    "Bob": "1985-05-12",
    "Charlie": "1992-07-23",
    "David": "1988-11-30",}

while True:
    print("Enter a name to look up their birthday (or type 'exit' to quit):")
    name = input().strip()
    if name == 'exit':
        break
    if name in birthday:
        print(f"{name}'s birthday is on {birthday[name]}.")
    else:
        print(f"Sorry, I don't have the birthday information for {name}.")
        print('Birthday database updated.')
        