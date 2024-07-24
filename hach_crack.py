import hashlib

def crack_hash(hash_to_crack, dictionary_file):
    with open(dictionary_file, 'r') as file:
        for word in file:
            word = word.strip()
            hash_guess = hashlib.sha256(word.encode()).hexdigest()
            if hash_guess == hash_to_crack:
                print(f"Password found: {word}")
                return word
    print("Password not found")
    return None

hashed_password = "5e884898da28047151d0e56f8dc6292773603d0d6aabbddff4f65e6a6c7f17dd"  # Example SHA-256 hash of "password"
dictionary_file_path = "dictionary.txt"
crack_hash(hashed_password, dictionary_file_path)
