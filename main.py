
from Registration  import registration

from Registration  import login

def signinup():

    print('---------------------Hi------------------------')
    print('----welcome to our crowdfunding console app----')
    print('-----------------------------------------------\n\n')

    choice = int(
        input("SIGN UP 1 : \nLOGIN 2 : \n\n"))
    try:
        choice == 1 or choice == 2
    except:
        print("something went wrong")
    else:
        if choice == 2:
            try:
                login()
            except:
                print("something went wrong")
        elif choice == 1:
            try:
                registration()
            except:
                print("something went wrong")
        else:
            print("invalid choice")


signinup()
