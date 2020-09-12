import random                               #PRINCIPLE MECHANISM
def dice_1():
    dice1=random.randint(1,6)
    return dice1
def dice_2():
    dice2=random.randint(1,6)
    return dice2


class Framework():
    def structure(self,f1,t1,r1,f2,t2,r2):             
        
        self.f1=f1                          #Front face of    dice 1
        self.t1=t1                          #Top face of      dice 1
        self.r1=r1                          #Right face of    dice 1
        self.f2=f2                          #Front face of    dice 2
        self.t2=t2                          #Top face         dice 2
        self.r2=r2                          #Right Face       dice 2
        


        print(f"      __________                      __________            ")
        print(f"    /  {t1[1]}  {t1[2]}  {t1[3]} /|                   /  {t2[1]}  {t2[2]}  {t2[3]} /|         ")
        print(f"   /  {t1[4]}  {t1[5]}  {t1[6]} / |                  /  {t2[4]}  {t2[5]}  {t2[6]} / |         ")
        print(f"  /  {t1[7]}  {t1[8]}  {t1[9]} / {r1[3]}|                 /  {t2[7]}  {t2[8]}  {t2[9]} / {r2[3]}|          ")
        print(f" /__________/ {r1[2]}{r1[6]}|                /__________/ {r2[2]}{r2[6]}|           ")
        print(f"|           |{r1[1]}{r1[5]}{r1[9]}|               |           |{r2[1]}{r2[5]}{r2[9]}|         ")
        print(f"|  {f1[1]}  {f1[2]}  {f1[3]}  |{r1[4]}{r1[8]} /               |  {f2[1]}  {f2[2]}  {f2[3]}  |{r2[4]}{r2[8]} / ")
        print(f"|  {f1[4]}  {f1[5]}  {f1[6]}  |{r1[7]} /                |  {f2[4]}  {f2[5]}  {f2[6]}  |{r2[7]} /            ")
        print(f"|  {f1[7]}  {f1[8]}  {f1[9]}  | /                 |  {f2[7]}  {f2[8]}  {f2[9]}  | /           ")
        print(f"|___________|/                  |___________|/          ")
        print(f" PLAYER 1                        PLAYER 2")

    def menu(self):
        print("\t\t\tWELCOME TO THE GAME OF DICE     \n\n")
        player=int(input("\t\t\tTWO PLAYERS OR ONE PLAYER :"))
        if player == 2:                          #INCREASE CHARGES IN virtualcoins PER CHANCE PLAYED
            gtype=int(input("\n WHICH GAME YOU WANT TO PLAY?? \n1.WHO GETS A SIX\n2. DOT WINNER(in development)\n -->"))
        elif player == 1:
            gtype=10
            gtype+=int(input("\n WHICH GAME YOU WANT TO PLAY?? \n1. SIX SIX\n2. TRY YOUR LUCK\n 3. ONE FACE\n4. TWO FACES\n5. THREE FACES\n-->"))
        input("\t\t\t\tPRESS ENTER TO BEGIN\n")
        return gtype

Fm = Framework()

class PrintMechanism():
    def dot_printer(self,value):
        self.value=value
        a=[]
        i=0
        while i<10:
            a.append(' ')
            i+=1              #later replace item with blank space and dot the number arrays
        if value == 1:
            a[5]="O"
        elif value ==2:
            a[4]="O"
            a[6]="O"
        elif value == 3:
            a[4]="O"
            a[5]="O"
            a[6]="O"
        elif value == 4:
            a[1]="O"
            a[3]="O"
            a[7]="O"
            a[9]="O"
        elif value == 5:
            a[1]="O"
            a[3]="O"
            a[4]="O"
            a[6]="O"
            a[8]="O"
        elif value == 6:
            a[1]="O"
            a[2]="O"
            a[3]="O"
            a[7]="O"
            a[8]="O"
            a[9]="O"
        return a

    def top_generator(self,num):                             #dice theory left incomplete
        self.num=num
        a=[]
        for item in range(7):
            if item!=num and item!=0:
                a.append(item)
        return random.choice(a)

    def right_gen(self,front):                               #dice theory left incomplete
        self.front=front
        a=[]
        top=self.top_generator(front)
        for item in range(7):
            if item!=front and item!=top and item!=7-top and item!=0:
                a.append(item)
        return random.choice(a)

    def run_code(self):
        dice1=dice_1()
        dice2=dice_2()
        f1=self.dot_printer(dice1)
        t1=self.dot_printer(self.top_generator(dice1))
        r1=self.dot_printer(self.right_gen(dice1))
        f2=self.dot_printer(dice2)
        t2=self.dot_printer(self.top_generator(dice2))
        r2=self.dot_printer(self.right_gen(dice2))
        Fm.structure(f1,t1,r1,f2,t2,r2)
        if f1==f2 and t1==t2 and r1==r2 :
            return 3                                            #3 faces found matching
        elif f1==f2 and t1==t2 or t1==t2 and r1==r2 :
            return 2                                            #2 faces found matching
        elif f1==f2 :
            if dice1==6 and dice2==6:
                return 6                                        # both got a six
            else:
                return 1                                        #1 face found matching                                       #both front faces are six
        elif dice1==6:
            return 16                                           #player 1 got a six
        elif dice2==6:
                return 26                                       #player 2 got a six
        else:
            return 0

Pm = PrintMechanism()                                       #assign to the object

class GameFunction():
    def __init__(self,choice):
        self.choice=choice
        score=0
        if choice==1:
            print("\n\tLETS SEE WHO GETS A SIX FIRST\n\n")
            decision=""
            p1=0
            p2=0
            count=0
            while decision=="" :
                y=Pm.run_code()
                if y==16:
                    p1+=1
                elif y==26:
                    p2+=1
                count+=1
                print(f"                                                 PLAYED={count}    PLAYER1:{p1}  PLAYER2:{p2} ")
                decision=input("\n\tPRESSS ENTER TO PLAY AGAIN         TYPE 'no' TO STOP\n")
        if choice==11:
            print("\n\tSIX SIX : IF FRONT FACE COMES SIX, YOU WIN\n\n")
            decision=""
            count=0
            while decision=="" :
                y=Pm.run_code()
                if y==6:
                    score+=1
                count+=1
                print(f"                                                           PLAYED={count}    SCORE = {score}")
                decision=input("\n\tPRESSS ENTER TO PLAY AGAIN         TYPE 'no' TO STOP\n")
        elif choice==2 :
            print("\n\tThis fearure has not been implemented by the developer yet\n\n")
            input("press enter to play another game")
            GameFunction(Fm.menu())

        elif choice==12 or choice==13:
            print("\n\tFRONT FACE MATCHING || TRY YOUR LUCK\n\n")
            decision=""
            count=0
            while decision=="" :
                y=Pm.run_code()
                if y==1:
                    score+=1
                count+=1
                print(f"                                                      PLAYED={count}    SCORE = {score}")
                decision=input("\n\tPRESSS ENTER TO PLAY AGAIN         TYPE 'no' TO STOP\n")
        elif choice==14:
            print("\n\tTWO FACE MATCHING\n\n")
            decision=""
            count=0
            while decision=="" :
                y=Pm.run_code()
                if y==2:
                    score+=1
                count+=1
                print(f"                                                   PLAYED={count}    SCORE = {score}")
                decision=input("\n\tPRESSS ENTER TO PLAY AGAIN         TYPE 'no' TO STOP\n")
        elif choice==15:
            print("\n\tTHREE FACE MATCHING\n\n")
            decision=""
            count=0
            while decision=="" :
                y=Pm.run_code()
                if y==3:
                    score+=1
                count+=1
                print(f"                                                   PLAYED={count}    SCORE = {score}")
                decision=input("\n\tPRESSS ENTER TO PLAY AGAIN         TYPE 'no' TO STOP\n")
        
        

GameFunction(Fm.menu())                             #pass gtype argument to choice parameter



      
