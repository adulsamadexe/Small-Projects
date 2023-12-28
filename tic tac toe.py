import random
print('''                                          WELCOME TO                                                         
                                        TIC TAC TOE GAME                                               ''')
print('''                            PLEASE FOLLOW THE GIVEN INSTRUCTIONS                   ''')
repeat=True
while repeat==True:
#name
    name2='Computer'
    name=input("Enter your name  ")
    while name.isalpha() is False:
        print("Enter alpabets only")
        name=input("Enter your name  ")
#symbol selection
    symbol1=input("Enter your symbol.Enter o for ( O ) and x for ( X )  ").upper()
    while symbol1 != "O" and symbol1 != "X":
        print("Enter valid decision")
        symbol1=input("Enter your symbol.Enter o for ( O ) and x for ( X )  ").upper()
    if symbol1=="O":
        player_symbol="O"
        computer_symbol="X"
    else:
        player_symbol="X"
        computer_symbol="O"
#toss
    user=input("select heads or tails  ").upper()
    while user!="HEADS" and user!="TAILS":
        print("Enter valid decision")
        user=input("select heads or tails  ").upper()
    toss=["HEADS","TAILS"]
    a=random.choice(toss)
    if user==a:
        print(f"{name} won the toss")
        toss_winner=1
        turn=1
    else:
        print("Computer won the toss")
        toss_winner=2
        turn=2
    a, b, c, d, e, f, g, h, i = 1, 2, 3, 4, 5, 6, 7, 8, 9
    print('',a,'|',b ,'|',c,'\n__________\n',d,'|',e ,'|',f,'\n__________\n',g,'|',h ,'|',i)
    game_end =False
    count=1
    while game_end==False:
        if toss_winner==1:
            choice =input("Enter the box number you wish to mark   ")
            while choice!="1" and choice!="2" and choice!="3" and choice!="4" and choice!="5" and choice!="6" and choice!="7" and choice!="8" and choice!="9":
                print("Enter valid decision")
                choice=input("Enter the box number you wish to mark   ")
            choice=int(choice)
            turn=name
            symbol=player_symbol
            toss_winner=2
        elif toss_winner==2:
            turn=name2
            symbol=computer_symbol
            toss_winner=1
            if e==5:
                 choice=5
#ANTI WIN CONDITIONS

            elif (b==player_symbol and c==player_symbol) or (e==player_symbol and i==player_symbol) or (d==player_symbol and g==player_symbol):
                if a==1:
                        choice=1
            elif (a==player_symbol and c==player_symbol) or (e==player_symbol and h==player_symbol):
                if b==2:
                        choice=2
            elif (a==player_symbol and b==player_symbol) or (f==player_symbol and i ==player_symbol) or (e==player_symbol and g==player_symbol):
                if c==3:
                      choice=3
            elif (a==player_symbol and g==player_symbol) or (e==player_symbol and f==player_symbol):
                if d==4:
                        choice=4
            elif (a==player_symbol and i==player_symbol) or (c==player_symbol and g==player_symbol) or (b==player_symbol and h==player_symbol) or (d==player_symbol and f==player_symbol):
                if e==5:
                    choice=5                 
            elif (e==player_symbol and d==player_symbol) or (c==player_symbol and i==player_symbol):
                if f==6:
                        choice=6
            elif (a==player_symbol and d==player_symbol) or (e==player_symbol and c==player_symbol) or (h==player_symbol and i==player_symbol):
                if g==7:
                        choice=7
            elif (b==player_symbol and e==player_symbol) or (g==player_symbol and i==player_symbol):
                if h==8:
                        choice=8
            elif (a==player_symbol and e==player_symbol) or (g==player_symbol and h==player_symbol) or (c==player_symbol and f==player_symbol):
                if i==9:
                        choice=9

        # # special moves
            elif a==player_symbol and i==player_symbol and e==computer_symbol:
               if f==6:
                    choice=6
            elif a==player_symbol and i==player_symbol and e==computer_symbol: 
               if h==8:
                    choice=8
            elif c==player_symbol and g==player_symbol and e==computer_symbol:
               if d==4:
                    choice=4
            elif c==player_symbol and g==player_symbol and e==computer_symbol:
               if h==8:
                    chooice=8
            elif e==player_symbol and i==9:
                 choice=9
            elif b==player_symbol and d==player_symbol and e==computer_symbol:
               if a==1:
                    choice=1
            elif h==player_symbol and d==player_symbol and e==computer_symbol:
               if g==7:
                    choice=7
            elif b==player_symbol and f==player_symbol and e==computer_symbol:
               if c==3:
                    choice=3
            elif f==player_symbol and h==player_symbol and e==computer_symbol:
               if i==9:
                    choice=9

 # checking the rest edges
            elif a==1:
                 choice=1
            elif g==7:
                 choice=7
            elif i==9:
                 choice=9
            elif c==3:
                 choice=3
 # checking the restparts
            elif d==4:
                 choice=4
            elif h==8:
                 choice=8
            elif f==6:
                 choice=6
            elif b==2:
                 choice=2

#winning conditions for computer
#first row
            if b==computer_symbol and c==computer_symbol and a==1:
                      choice=1
            elif a==computer_symbol and c==computer_symbol and b==2:
                      choice=2
            elif b==computer_symbol and a==computer_symbol and c==3:
                      choice=3
#secon row
            elif d==computer_symbol and e==computer_symbol and f==6:
                      choice=6
            elif d==computer_symbol and f==player_symbol and e==5:
                      choice=5
            elif e==computer_symbol and f==computer_symbol and d==4:
                      choice=4
#third row
            elif g==computer_symbol and h==computer_symbol and i==9:
                      choice=9
            elif g==computer_symbol and i==computer_symbol and h==8:
                      choice=8
            elif h==computer_symbol and i==computer_symbol and g==7:
                      choice=7
#first coloumn
            elif a==computer_symbol and d==computer_symbol and g==7:
                      choice=7
            elif a==computer_symbol and g==computer_symbol and d==4:
                      choice=4
            elif d==computer_symbol and g==computer_symbol and a==1:
                     choice=1
#second coloumn
            elif b==computer_symbol and e==computer_symbol and h==8:
                      choice=8
            elif b==computer_symbol and h==computer_symbol and e==5:
                      choice=5
            elif e==computer_symbol and h==computer_symbol and b==2:
                      choice=2
#third coloumn
            elif c==computer_symbol and f==computer_symbol and i==9:
                      choice=9
            elif c==computer_symbol and i==computer_symbol and f==6:
                      choice=6
            elif f==computer_symbol and i==computer_symbol and c==3:
                      choice=3
#first diagonal
            elif a==computer_symbol and e==computer_symbol and i==9:
                      choice=9
            elif a==computer_symbol and i==computer_symbol and e==5:
                      choice=5
            elif e==computer_symbol and i==computer_symbol and a==1:
                      choice=1
#second diagonal
            elif c==computer_symbol and e==computer_symbol and g==7:
                      choice=7
            elif c==computer_symbol and g==computer_symbol and e==5:
                      choice=5
            elif e==computer_symbol and g==computer_symbol and c==3:
                      choice=3            

#anti override
        while True:
            if toss_winner==2:
                    if (choice==1 and a!=1) or (choice==2 and b!=2) or (choice==3 and c!=3) or (choice==4 and d!=4) or(choice==5 and e!=5) or (choice==6 and f!=6) or (choice==7 and g!=7) or (choice==8 and h!=8) or (choice==9 and i!=9):
                        print(name,"the box you chose is not currently available")
                        choice =input("Enter the box number you wish to mark")
                        while choice!="1" and choice!="2" and choice!="3" and choice!="4" and choice!="5" and choice!="6"   and   choice!="7" and choice!="8" and choice!="9":
                            print("Enter valid decision")
                            choice=input("Enter the box number you wish to mark")
                        choice=int(choice)
                    else:
                        break
            elif toss_winner==1:
                if (choice==1 and a!=1) or (choice==2 and b!=2) or (choice==3 and c!=3) or (choice==4 and d!=4) or(choice==5 and e!=5) or (choice==6 and f!=6) or (choice==7 and g!=7) or (choice==8 and h!=8) or (choice==9 and i!=9):
                       choice=random.randint(1,9)
                else:
                    break
        if choice==1:
             a=symbol
        elif choice==2:
             b=symbol
        elif choice==3:
             c=symbol
        elif choice==4:
             d=symbol
        elif choice==5:
             e=symbol
        elif choice==6:
             f=symbol
        elif choice==7:
             g=symbol
        elif choice==8:
             h=symbol
        elif choice==9:
             i=symbol
        print(f"{turn} turn")
        print('',a,'|',b ,'|',c,'\n__________\n',d,'|',e ,'|',f,'\n__________\n',g,'|',h ,'|',i)
        count+=1
        if count==10 and game_end==False:
             game_end= True
             print("---- Match is a Tie ----")
             break
        elif a==b==c==player_symbol or d==e==f==player_symbol or g==h==i==player_symbol or a==e==i==player_symbol or c==e==g==player_symbol or a==d==g==player_symbol or b==e==h==player_symbol or c==f==i==player_symbol:
             game_end= True
             print(f"{name} won the game")
        elif a==b==c==computer_symbol or d==e==f==computer_symbol or g==h==i==computer_symbol or a==e==i==computer_symbol or c==e==g==computer_symbol or a==d==g==computer_symbol or b==e==h==computer_symbol or c==f==i==computer_symbol:
             game_end=True
             print("Computer won the game")
    again=input("DO YOU WANT TO PLAY AGAIN...\nTYPE YES OR NO").upper()
    while again!="YES" and again!="NO":
         print("PLEASE ENTER YES OR NO")
         again=input("DO YOU WANT TO PLAY AGAIN...\nTYPE YES OR NO").upper()
    if again=="YES":
         repeat==True
    else:
         repeat=False
print("THANK YOU FOR PLAYING THE GAME")
             
              

        
            


