def emailprocess(email):
    email_username = email[0:email.index("@")]
    email_domain = email[email.index("@")+1:]
    return [email_username,email_domain]

def printMsg(email_username,email_domain):
    print(f"Email username is: {email_username}")
    print(f"Email domain is {email_domain}")

def main():
    email = input("Enter your email here please: ").strip()
    email_username, email_domain = emailprocess(email)
    printMsg(email_username,email_domain)

if __name__ == "__main__":
    main()