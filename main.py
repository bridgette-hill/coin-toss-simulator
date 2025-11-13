import random
from collections import Counter
flip = random.choice(['Heads', 'Tails'])
print("The coin landed on:", flip)
while True:
    try:
        num_flips = int(input("How many times should we flip the coin? "))
        print("DEBUG: User entered", num_flips)
        if num_flips > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Please enter a valid integer.")

results = [random.choice(['Heads', 'Tails']) for _ in range(num_flips)]
print("DEBUG: Results list =", results)

counts = Counter(results)
print("DEBUG: Counter =", counts)

heads = counts.get('Heads', 0)
tails = counts.get('Tails', 0)


print("\n--- Results ---")
print(f"Heads: {heads} ({heads / num_flips:.1%})")
print(f"Tails: {tails} ({tails / num_flips:.1%})")
