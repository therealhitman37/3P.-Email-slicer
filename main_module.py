from sub_module import emailprocess,printMsg

def main():
    emails = ["therealhacker@youtube.us","nocoopyrightsound@stuck.gg","remixmusic@gmail.com"]
    for email in emails:
        email_username, email_domain = emailprocess(email)
        printMsg(email_username, email_domain)

if __name__ == "__main__":
    main()