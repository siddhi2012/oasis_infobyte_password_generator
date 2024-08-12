import random
def password(length=0, complexity=0):
    length=int(input("Enter a length of password:"))
    a=("choose complexity (easy, medium, hard)")
    print(a.center(50))
    complexity=input("Enter the complexity of password: ")
    match complexity:
        case 'easy':
            easy=("1234567890")
            password = ''.join(random.choice(easy)for _ in range(length))
            return password
            
        case 'medium':
            medium=("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
            password = ''.join(random.choice(medium) for _ in range(length))
            return password
            
        case 'hard':
            hard=("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()[]{};:',./<>?")
            password = ''.join(random.choice(hard)for _ in range(length))
            return password
            
        case "":
            print("invalid input")
        
print("genrated password:",password())
while True:     
    next=input("Do you want to do another password? (yes/no):")
    if next=='yes':
        print("genrated password:",password())  
    else:
        print("Thank You")
        break