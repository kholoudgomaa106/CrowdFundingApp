# login/registration
import re
from DealingwithProjects import projects


# function for first and second name validation

def validate_name():
    print("--------------------------------------\n")
    firstname = input("please,enter your first name : ").strip().lower()
    while True:
        if firstname.isalpha():
            lastname = input("please,enter your last name : ").strip().lower()
            if lastname.isalpha():
                break
            else:
                print("please,enter your last name without spaces or digits")
        elif firstname.isspace() or firstname.isalnum():
            print("please,enter your first name without spaces or digits")
            firstname = input("please,enter your first name : ").strip().lower()
    return [firstname, lastname]

# function for email validation

def validate_email():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com\b'
    print("----------------------------------------")
    email = input("please,enter your email : ").strip().lower()
    while True:
        if(re.fullmatch(regex, email)):
            break
        else:
            print("Invalid Email")
            email = input(
                "enter valid email contains @ and .com : ").strip().lower()
    return email

# function for password validation

def validate_pass():
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$'
    password = input("please,enter your password : ").strip()
    while True:
        if(re.fullmatch(regex, password)):
            confirmedpassword = input("confirm your password : ").strip()
            if password != confirmedpassword:
                print("please confirm  your password , they are not the same")
            else:
                break
        else:
            print("Invalid password")
            password = input(
                "enter valid password contains uppercase , lowercase , number ,special character and al least 8 : ").strip().lower()
    return password

# function for phone validation

def validate_phone():
    phone = input("please ,enter your number : ").strip().lower()
    while True:
        if len(phone) == 11 and phone.isnumeric():
            break
        else:
            print("please ,enter a valid egyptian number")
            phone = input("please enter your number : ").strip().lower()
    return phone

# main functions

# function for resgister

def registration():

    fullname = validate_name()
    with open("users.txt", 'a') as userfile:
        userfile.writelines(
            [f"{id(fullname)}:{fullname[0]}:{fullname[1]}:"])

    email = validate_email()
    with open("users.txt", 'a') as userfile:
        userfile.write(f"{email}:")

    password = validate_pass()
    with open("users.txt", 'a') as userfile:
        userfile.write(f"{password}:")

    phone = validate_phone()
    with open("users.txt", 'a') as userfile:
        userfile.write(f"{phone}")
    # #
    # user_=[f'{fullname} ":"{email} ":" {password} ":" {phone}"."']

    # with open("users.json","w") as userfile:
    #     for line in user_:
    #         userfile.write(line +'\n')
    # loaded_data=[]
    # try:
    # with open("users.json", "r") as file:
    #     for line in file:
    #         x = json.load(line)
    #         loaded_data.append(x)
    #
    # with open("users.json", "w") as file:
    #    json.dump(data, file)
    # with open("users.json","a") as userfile:
    #     for line in user_:
    #         userfile.write('\n'.join(user_)+'\n')





    print("----------------------------------------")
    print("your registration goes successfully")
    print("----------------------------------------\n\n")
    choiceforlogin = input("do you want to login now?[y/n] ").strip().lower()
    try:
        choiceforlogin == "y" or choiceforlogin == "n"
    except:
        print("something went wrong")
    else:
        if choiceforlogin == "y":
            login()
        elif choiceforlogin == "n":
            print("ok bye bye , hope to see you soon")
        else:
            print("invalid input")
# function for login

def login():
    loginemail = input("please enter your email : ").strip().lower()
    try:
        with open("users.txt", 'r') as userfile:
            data = userfile.read()
            data = data.split(":")
            print(data)
    except:
        print("something went wrong")
    else:
        while True:
            if loginemail in data:
                passuser = input("please enter your password : ").strip()
                print("data:   ", data)
                if data[data.index(loginemail)+1] == passuser:
                    print("----------------------------------------")

                    print(
                        f"welcome {data[data.index(loginemail)-2]} {data[data.index(loginemail)-1]}")

                    print("----------------------------------------\n")

                    try:
                        #print("id:  ", data[data.index(loginemail)-3])
                        #projects(data[data.index(loginemail)-3])
                        projects(data[0])
                    except:
                        print("something went wrong")
                    break
                else:
                    print("Invalid password , try again")
            else:
                print("Invalid email , try again")
                loginemail = input(
                    "please enter your email : ").strip().lower()

