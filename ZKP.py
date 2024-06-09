#pip install pycrypto
from Crypto.Random import random
from Crypto.Util.number import getPrime, bytes_to_long

# Setup Phase (Server-side)
def setup(bits=1024):
    p = getPrime(bits)
    g = random.randint(2, p - 1)
    print(f"p: {p}\ng: {g}\n\n")
    return p, g

# Registration Phase (Client-side)
def register(username, password, p, g, user_db):
    x = bytes_to_long(password.encode('utf-8'))
    v = pow(g, x, p)
    user_db[username] = v
    print(f"x: {x}\nv: {v}\n\n")
    return x, v

# Proof Generation Phase (Client-side)
def generate_proof(password, p, g, e):
    x = bytes_to_long(password.encode('utf-8'))
    r = random.randint(1, p - 1)
    a = pow(g, r, p)
    y = (r + x * e) % (p - 1)
    print(f"x: {x}\nr: {r}\na: {a}\ny: {y}\n\n")
    return a, y

# Proof Verification Phase (Server-side)
def verify_proof(a, e, y, v, p, g):
    left_hand_side = pow(g, y, p)
    right_hand_side = (a * pow(v, e, p)) % p
    print(f"Left-hand side: {left_hand_side}\nRight-hand side: {right_hand_side}\n\n")
    return left_hand_side == right_hand_side

# Main Example with Login Process
if __name__ == "__main__":
    user_db = {}
    p, g = setup()

    print("=== User Registration ===")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    # User registration
    _, v = register(username, password, p, g, user_db)
    print(f"Registration complete for user '{username}'.")

    print("\n=== User Login ===")
    username_login = input("Enter your username: ")
    
    # Check if username exists
    if username_login not in user_db:
        print("Username not found. Authentication failed.")
    else:
        password_login = input("Enter your password: ")

        # Server generates challenge
        e = random.randint(1, p - 1)
        print(f"e: {e}\n\n")

        # User generates proof of knowledge of password
        a, y = generate_proof(password_login, p, g, e)
        print(f"Proof generated. a: {a}\ny: {y}\n\n")

        # Server verifies proof
        print("Verifying proof of knowledge of password...")
        is_valid = verify_proof(a, e, y, user_db[username_login], p, g)
        print("Proof verification complete. Result:", is_valid)
        if is_valid:
            print("Proof is valid. User is authenticated.")
        else:
            print("Proof is invalid. Authentication failed.")
