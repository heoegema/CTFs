import os
import sys

# This script runs the password cracker for picoCTF level X against a file containing potential passwords
def run_pw_cracker(program_name: str, password_file: str) -> None: 

    with open(password_file, "r") as file: 
        content = file.read()
        passwords = content.split("\n")
        print(f"Found {len(passwords)} passwords in {password_file}")
        for password in passwords:
            cmd = f"echo {password} | python3 {program_name}"
            print("Running command:", cmd)
            os.system(cmd)


if __name__ == "__main__":
    program_name = sys.argv[1] if len(sys.argv) > 1 else "password_cracker.py"
    password_file = sys.argv[2] if len(sys.argv) > 1 else "passwords.txt"

    print(f"Running password cracker...{program_name} with passwords from {password_file}")
    run_pw_cracker(program_name, password_file)
    print("Finished running password cracker")