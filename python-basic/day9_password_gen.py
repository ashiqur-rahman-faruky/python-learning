# A program that creates random passwords.
import secrets
import math

def generate_secure_password(length: int, include_special: bool = True, include_digits: bool = True) -> str:
    LETTERS  = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    SPECIALS = "!@#$%^&*()-+"
    DIGITS   = "0123456789"

    # Build the active pools
    pools = [("letters", LETTERS)]
    if include_special:
        pools.append(("special", SPECIALS))
    if include_digits:
        pools.append(("digits", DIGITS))

    num_pools = len(pools)

    # --- Guarantee at least one character from every active pool ---
    chars: list[str] = [secrets.choice(pool) for _, pool in pools]
    remaining = length - num_pools

    # --- Distribute remaining slots proportionally across pools ---
    # Each pool gets floor(remaining / num_pools); leftover slots go to
    # randomly chosen pools so the total always equals `length`.
    base, leftover = divmod(remaining, num_pools)
    extra_indices = secrets.SystemRandom().sample(range(num_pools), leftover)

    for i, (_, pool) in enumerate(pools):
        count = base + (1 if i in extra_indices else 0)
        chars.extend(secrets.choice(pool) for _ in range(count))

    # --- Shuffle so the guaranteed characters aren't always at the front ---
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def get_user_preferences() -> tuple[int, bool, bool]:
    while True:
        try:
            length = int(input("Enter password length (>= 3): "))
            if length < 3:
                print("Password length must be at least 3.")
                continue

            use_special = input("Include special characters? (y/n): ").strip().lower() == "y"
            use_digits  = input("Include digits? (y/n): ").strip().lower() == "y"
            return length, use_special, use_digits

        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    length, use_special, use_digits = get_user_preferences()
    password = generate_secure_password(length, use_special, use_digits)
    print("Generated password:", password)
