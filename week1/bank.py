greeting = input("Whats your greeting? ").lower()

if greeting == "hello":
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")
