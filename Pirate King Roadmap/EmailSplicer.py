# 4/20/2024

# collect email from user
# split email using the @: first part as username, second part as domain
# split domain using .

def main():
    print("Email splicing program\n")

    while True:
        email = input("Enter your email address: ")

        (username, domain) = email.split("@")
        domain, extension = domain.split(".")

        print("Username : ", username)
        print("Domain : ", domain)
        print("Extension : ", extension)
        
        if (input("\nContinue? Y/N\n :: ").lower() == "n"):
            print("Thank you!")
            break

main()