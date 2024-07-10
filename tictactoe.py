def issafe(dict1,str1,str2,row,column,r,c):
    if(dict1[row][column]=="_"):
        return True
    else:
        return False
    
def win(dict1,row,column,str1,r,c):
    c1=dict1[row]
    count=c1.count(str1)
    i=1
    if(count==r):
        return True 
    elif(column==row-1):
      while(i<=c):
        if(dict1[i][i-1]!=str1):
            return False
        else:
            i+=1
      return True
    elif(row==column-1):
      i=1
      while(i<=c):
        if(dict1[i][r-i]!=str1):
            return False
        else:
            i+=1
      return True
    else:
        i=1
        while(i<=r):
         if(dict1[i][column]!=str1):
            return False
         else:
            i+=1
    return True
    
def board(dict1):
    for i in dict1:
        l2=dict1[i]
        for j in l2:
            print(j,"|",end=" ")
        print()
    print()
    return
def tictactoe(dict1,str1,str2,cnt,row,column,r,c):
    column-=1
    if(cnt==(r*c)-1):
        dict1[row][column]=str1
        print("Match Draw")
        print("GAME ENDS THANK YOU FOR PLAYING!!!")
        board(dict1)
        return
    if(row>r or column>c):
        print("INVALID ROW OR COLUMN.ENTER AGAIN")
        row=int(input("Enter the row"))
        column=int(input("Enter the column"))
        tictactoe(dict1,str1,str2,cnt,row,column,r,c)
        return
    
    if(issafe(dict1,str1,str2,row,column,r,c)==True):
         dict1[row][column]=str1
         board(dict1)
         if(win(dict1,row,column,str1,r,c)==True):
            print("Player",str1,"wins the game")
            print("GAME ENDS THANK YOU FOR PLAYING!!!")
            print()
            board(dict1)
            return
         else:
            row=int(input("Enter the row"))
            column=int(input("Enter the column"))
            cnt+=1
            tictactoe(dict1,str2,str1,cnt,row,column,r,c)
            return
    else:
         board(dict1)
         print("Invalid Move.Enter the row and column again")
         row=int(input("Enter the row"))
         column=int(input("Enter the column"))
         tictactoe(str1,str1,str2,cnt,row,column,r,c)
         return
           
            
    
    
r=int(input("Enter the total no of rows"))
c=int(input("Enter the  total no of columns"))
str1=input("Enter the name of player1")
str2=input("Enter the name of player2")
cnt=1
dict1={}
for i in range(1,r+1):
    list1=[]
    for j in range(0,c):
        list1.append("_")
    dict1[i]=list1
board(dict1)
try:
  row=int(input("Enter the row"))
  column=int(input("Enter the column"))
  tictactoe(dict1,str1,str2,0,row,column,r,c)
except Exception as e:
  print("Enter the integer no only!")
  print("Please re-enter the values")
  row=int(input("Enter the row"))
  column=int(input("Enter the column"))
  tictactoe(dict1,str1,str2,0,row,column,r,c)



        
    
        
