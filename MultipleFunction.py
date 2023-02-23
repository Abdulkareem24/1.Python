class multiplefunctions():    
    def Subfields():
        print("""
        Sub-fields in AI are:
        Machine Learning
        Neural Networks
        Vision
        Robotics
        Speech Processing
        Natural Language Processing
        """) 
        
    def Elegible():  
        gender=input("Enter your gender: ").lower()
        age=int(input("Enter your age: "))
        if (gender in ("male","m")):
            if(age >= 21):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif (gender in ("female","f")):
            if(age >= 18):
                print("ELIGIBLE")
            else:
                 print("NOT ELIGIBLE")
        else:
              print('INVALID INPUT DATA')    
                
    def percentage():
        Sub1=int(input("Subject1="))
        Sub2=int(input("Subject2="))
        Sub3=int(input("Subject3="))
        Sub4=int(input("Subject1="))
        Sub5=int(input("Subject5="))
        T=(Sub1+Sub2+Sub3+Sub4+Sub5)
        print("Total:",T)
        P=T/5
        print("Percentage:",float(P))
        
    def OddEven():
        num=int(input("Enter a number:"))
        if((num%2)==0):
            print(num,"is Even number")
            message=num,"is Even number"
        else:        
            print(num,"is odd number")
            message=num,"is odd number"
        return message    
    