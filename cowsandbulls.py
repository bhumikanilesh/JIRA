# cows_bulls.py
import random
def generate_secret():
    digits = list("0123456789")
    # ensure first digit is not '0' by picking first digit separately
    first = random.choice(digits[1:])
    digits.remove(first)
    secret = first + ''.join(random.sample(digits, 3))
    return secret

def compare(secret, guess):
    cows = sum(1 for i in range(4) if guess[i] == secret[i])
    # For bulls (correct digit wrong place) handle duplicates properly:
    # Count matches by digit: total matched digits minus cows
    from collections import Counter
    sec_count = Counter(secret)
    guess_count = Counter(guess)
    total_matches = sum((sec_count & guess_count).values())
    bulls = total_matches - cows
    return cows, bulls

def play():
    secret = generate_secret()
    print("Welcome to Cows and Bulls!")
    attempts = 0
    while True:
        guess = input("Enter a 4-digit guess: ").strip()
        if len(guess) != 4 or not guess.isdigit():
            print("❌ Enter exactly 4 digits.")
            continue
        attempts += 1
        cows, bulls = compare(secret, guess)
        print(f"{cows} cows, {bulls} bulls")
        if cows == 4:
            print(f"🎉 You guessed the number {secret} in {attempts} tries.")
            break

if __name__ == '__main__':
    play()

