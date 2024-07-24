import zipfile
import itertools
import string

def brute_force_zip(zip_file, max_length):
    charset = string.ascii_letters + string.digits
    zf = zipfile.ZipFile(zip_file)

    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            password = ''.join(guess)
            try:
                zf.extractall(pwd=password.encode())
                print(f"Password found: {password}")
                return password
            except (RuntimeError, zipfile.BadZipFile):
                continue
    print("Password not found")
    return None

zip_file_path = "protected.zip"
brute_force_zip(zip_file_path, 5)
