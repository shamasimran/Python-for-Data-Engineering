def is_valid_email(email):
    return "@" in email and "." in email.split("@")[-1]

if __name__ == "__main__":
    print(is_valid_email("test@example.com"))
