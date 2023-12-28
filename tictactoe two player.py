import random
a="1"
b="2"
c="3"
d="4"
e="5"
f="6"
g="7"
h="8"
i="9"
grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
print(grid)
#Asking the player names
name1=input("player 1 enter your name")
name2=input("player 2 enter your name")
your_selection=input("type 0 for Heads or 1 for Tails:")
while your_selection!="0" and your_selection!="1":
      print("invalid decision")
      your_selection=input("type 0 for Heads or 1 for Tails:")
if your_selection=="0":
      your_selection=0
elif your_selection=="1":
      your_selection=1
toss=random.randint(0,1)
#selection of symbol
if your_selection==toss:
    toss_winner=1
    print("you won the toss")
    symbol=input(f"{name1} chose your sign.Enter 0 for X and 1 for O:")
    while symbol!="0" and symbol!="1":
     symbol=input(f"{name2} chose your sign.Enter 0 for X and 1 for O:")
elif your_selection!=toss:
    toss_winner=2
    print("you lost the toss")
    symbol=input(f"{name2} chose your sign.Enter 0 for X and 1 for O:")
    while symbol!="0" and symbol!="1":
     symbol=input(f"{name2} chose your sign.Enter 0 for X and 1 for O:")
#Assigning the symbol
if symbol=="0" or symbol=="1":
    if your_selection==toss:
        if symbol=="0":
            player1_symbol="X"
            player2_symbol="O"
        elif symbol=="1":
            player1_symbol="O"
            player2_symbol="X"
    elif your_selection!=toss:
        if symbol=="0":
            player1_symbol="X"
            player2_symbol="O"
        elif symbol=="1":
            player1_symbol="O"
            player2_symbol="X"
#Making the toss winner the first player
if toss_winner==1:
     player1=f"{name1}"
     player2=f"{name2}"
elif toss_winner==2:
     player1=f"{name2}"
     player2=f"{name1}"
#printing both players symbol
print(f"{name1} symbol is",player1_symbol)
print(f"{name2} symbol is",player2_symbol)
grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
print(grid)
count=0
#Setting up the loop
while count<9:
       test=0
       print(f"{player1} Enter the box you want to mark :: ",end="")
       choice1=int(input())
       while choice1>10 or choice1<0:
              print("invalid choice")
              choice1=int(input(f"{player1} Enter the box you want to mark"))
#Anti override condition
       while test==0:
         if choice1==1:
              if a=="X" or a=="O":
                   print("invalid decision")
                   choice1=int(input(f"{player1} Enter the box you want to mark"))
              elif a=="1":
                   test=1
         elif choice1==2:
              if b=="X" or b=="O":
                   print("invalid decision")
                   choice1=int(input(f"{player1} Enter the box you want to mark"))
              elif b=="2":
                   test=1
         elif choice1==3:
              if c=="X" or c=="O":
                   print("invalid decision")
                   choice1=int(input(f"{player1} Enter the box you want to mark"))
              elif c=="3":
                   test=1
         elif choice1==4:
              if d=="X" or d=="O":
                   print("invalid decision")
                   choice1=int(input(f"{player1} Enter the box you want to mark"))
              elif d=="4":
                   test=1
         elif choice1==5:
              if e=="X" or e=="O":
                   print("invalid decision")
                   choice1=int(input(f"{player1} Enter the box you want to mark"))
              elif e=="5":
                   test=1
         elif choice1==6:
              if f=="X" or f=="O":
                   print("invalid decision")
                   choice1=int(input(f"{player1} Enter the box you want to mark"))
              elif f=="6":
                   test=1
         elif choice1==7:
              if g=="X" or g=="O":
                   print("invalid decision")
                   choice1=int(input(f"{player1} Enter the box you want to mark"))
              elif g=="7":
                   test=1
         elif choice1==8:
              if h=="X" or h=="O":
                   print("invalid decision")
                   choice1=int(input(f"{player1} Enter the box you want to mark"))
              elif h=="8":
                   test=1
         elif choice1==9:
              if i=="X" or i=="O":
                   print("invalid decision")
                   choice1=int(input(f"{player1} Enter the box you want to mark"))
              elif i=="9":
                   test=1  
#Filling boxes condition
       if choice1==1:
            a=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            count=count+1
            print(grid)
       elif choice1==2:
            b=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            count=count+1
            print(grid)
       elif choice1==3:
            c=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
            count=count+1
       elif choice1==4:
            d=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
            count=count+1
       elif choice1==5:
            e=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
            count=count+1
       elif choice1==6:
            f=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
            count=count+1
       elif choice1==7:
            g=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
            count=count+1
       elif choice1==8:
            h=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
            count=count+1
       elif choice1==9:
            i=player1_symbol
            grid=f"""
                          |            |
                   {a}      |      {b}     |     {c}
             _____________|____________|_______________
                          |            |
                   {d}      |      {e}     |     {f}
             _____________|____________|_______________
                          |            |
                   {g}      |      {h}     |      {i}
                          |            |
"""
            print(grid)
            count=count+1
       if a==b==c==player1_symbol or d==e==f==player1_symbol or g==h==i==player1_symbol or a==d==g==player1_symbol or b==e==h==player1_symbol or c==f==i==player1_symbol or a==e==i==player1_symbol or c==e==g==player1_symbol:
            print(f"{player1} won")
            count=9
       elif a==b==c==player2_symbol or d==e==f==player2_symbol or g==h==i==player2_symbol or a==d==g==player2_symbol or b==e==h==player2_symbol or c==f==i==player2_symbol or a==e==i==player2_symbol or c==e==g==player2_symbol:
            print(f"{player2} won")
            count=9
       elif count==9:
              print("its a draw")
         
#Condition to terminate if all the moves are out
       if count!=9:
              print(f"{player2} Enter the box you want to mark :: ",end="")
              choice2=int(input())
              while choice2<0 or choice2>9:
                     print("invalid choice")
                     print(f"{player2} Enter the box you want to mark :: ",end="")
                     choice2=int(input())
              test=0
       #Anto override rules
              while test==0:
                     if choice2==1:
                            if a=="X" or a=="O":
                                   print("invalid decision")
                                   choice2=int(input(f"{player2} Enter the box you want to mark"))
                            elif a=="1":
                                   test=1
                     elif choice2==2:
                            if b=="X" or b=="O":
                                   print("invalid decision")
                                   choice2=int(input(f"{player2} Enter the box you want to mark"))
                            elif b=="2":
                                   test=1
                     elif choice2==3:
                            if c=="X" or c=="O":
                                   print("invalid decision")
                                   choice2=int(input(f"{player2} Enter the box you want to mark"))
                            elif c=="3":
                                   test=1
                     elif choice2==4:
                            if d=="X" or d=="O":
                                   print("invalid decision")
                                   choice2=int(input(f"{player2} Enter the box you want to mark"))
                            elif d=="4":
                                   test=1
                     elif choice2==5:
                            if e=="X" or e=="O":
                                   print("invalid decision")
                                   choice2=int(input(f"{player2} Enter the box you want to mark"))
                            elif e=="5":
                                   test=1
                     elif choice2==6:
                            if f=="X" or f=="O":
                                   print("invalid decision")
                                   choice2=int(input(f"{player2} Enter the box you want to mark"))
                            elif f=="6":
                                   test=1
                     elif choice2==7:
                            if g=="X" or g=="O":
                                   print("invalid decision")
                                   choice2=int(input(f"{player2} Enter the box you want to mark"))
                            elif g=="7":
                                   test=1
                     elif choice2==8:
                            if h=="X" or h=="O":
                                   print("invalid decision")
                                   choice2=int(input(f"{player2} Enter the box you want to mark"))
                            elif h=="8":
                                   test=1
                     elif choice2==9:
                            if i=="X" or i=="O":
                                   print("invalid decision")
                                   choice2=int(input(f"{player2} Enter the box you want to mark"))
                            elif i=="9":
                                   test=1                 
       #Filling the boxes
              if choice2==1:
                            a=player2_symbol
                            grid=f"""
                                   |            |
                            {a}      |      {b}     |     {c}
                     _____________|____________|_______________
                                   |            |
                            {d}      |      {e}     |     {f}
                     _____________|____________|_______________
                                   |            |
                            {g}      |      {h}     |      {i}
                                   |            |
              """
                            print(grid)
                            count+=1
              elif choice2==2:
                            b=player2_symbol
                            grid=f"""
                                   |            |
                            {a}      |      {b}     |     {c}
                     _____________|____________|_______________
                                   |            |
                            {d}      |      {e}     |     {f}
                     _____________|____________|_______________
                                   |            |
                            {g}      |      {h}     |      {i}
                                   |            |
              """
                            print(grid)
                            count+=1
              elif choice2==3:
                            c=player2_symbol
                            grid=f"""
                                   |            |
                            {a}      |      {b}     |     {c}
                     _____________|____________|_______________
                                   |            |
                            {d}      |      {e}     |     {f}
                     _____________|____________|_______________
                                   |            |
                            {g}      |      {h}     |      {i}
                                   |            |
              """
                            print(grid)
                            count+=1
              elif choice2==4:
                            d=player2_symbol
                            grid=f"""
                                   |            |
                            {a}      |      {b}     |     {c}
                     _____________|____________|_______________
                                   |            |
                            {d}      |      {e}     |     {f}
                     _____________|____________|_______________
                                   |            |
                            {g}      |      {h}     |      {i}
                                   |            |
              """
                            print(grid)
                            count+=1
              elif choice2==5:
                            e=player2_symbol
                            grid=f"""
                                   |            |
                            {a}      |      {b}     |     {c}
                     _____________|____________|_______________
                                   |            |
                            {d}      |      {e}     |     {f}
                     _____________|____________|_______________
                                   |            |
                            {g}      |      {h}     |      {i}
                                   |            |
              """
                            print(grid)
                            count+=1
              elif choice2==6:
                            f=player2_symbol
                            grid=f"""
                                   |            |
                            {a}      |      {b}     |     {c}
                     _____________|____________|_______________
                                   |            |
                            {d}      |      {e}     |     {f}
                     _____________|____________|_______________
                                   |            |
                            {g}      |      {h}     |      {i}
                                   |            |
              """
                            print(grid)
                            count+=1
              elif choice2==7:
                            g=player2_symbol
                            grid=f"""
                                   |            |
                            {a}      |      {b}     |     {c}
                     _____________|____________|_______________
                                   |            |
                            {d}      |      {e}     |     {f}
                     _____________|____________|_______________
                                   |            |
                            {g}      |      {h}     |      {i}
                                   |            |
              """
                            print(grid)
                            count+=1
              elif choice2==8:
                            h=player2_symbol
                            grid=f"""
                                   |            |
                            {a}      |      {b}     |     {c}
                     _____________|____________|_______________
                                   |            |
                            {d}      |      {e}     |     {f}
                     _____________|____________|_______________
                                   |            |
                            {g}      |      {h}     |      {i}
                                   |            |
              """
                            print(grid)
                            count+=1
              elif choice2==9:
                            i=player2_symbol
                            grid=f"""
                                   |            |
                            {a}      |      {b}     |     {c}
                     _____________|____________|_______________
                                   |            |
                            {d}      |      {e}     |     {f}
                     _____________|____________|_______________
                                   |            |
                            {g}      |      {h}     |      {i}
                                   |            |
              """
                            print(grid)
                            count+=1
              if a==b==c==player1_symbol or d==e==f==player1_symbol or g==h==i==player1_symbol or a==d==g==player1_symbol or b==e==h==player1_symbol or c==f==i==player1_symbol or a==e==i==player1_symbol or c==e==g==player1_symbol:
                     print(f"{player1} won")
                     count=9
              elif a==b==c==player2_symbol or d==e==f==player2_symbol or g==h==i==player2_symbol or a==d==g==player2_symbol or b==e==h==player2_symbol or c==f==i==player2_symbol or a==e==i==player2_symbol or c==e==g==player2_symbol:
                     print(f"{player2} won")
                     count=9
              elif count==9:
                    print("its a draw")
              