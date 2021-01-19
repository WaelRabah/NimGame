from random import Random
def switchPlayer(currenPlayer):
    if currenPlayer==1:
        return 2
    else:
        return 1
def list_isIn (moves,move) :
    return move in moves
def possibleCombinations(number) :
    move=[]
    moves=[]
    for i in range(1,int(number/2)+1): 
        if(number-i!=i) : 
            move.append(i)
            move.append(number-i)
            move.sort(reverse=True)
            moves.append(move)
            move=[]
    return moves
def get_unique_moves(moves) :
    moves_aux=[]
    for move in moves :
        if not list_isIn(moves_aux,move) :
            moves_aux.append(move)
    return moves_aux
def actions(state):
    def extend(l,move):
        aux=l+move
        aux.sort(reverse=True)
        return aux.copy()
    moves=[]
    for index ,number in enumerate(state) :
        move=state.copy()
        move.pop(index)
        poss_moves=possibleCombinations(number)
        poss_moves=[ extend(l,move) for l in poss_moves]
        moves.extend(poss_moves)
    moves=get_unique_moves(moves)
    return moves

def isTerminal(state): 
    for n in state:
        if n!=1 and n!=2:
            return 0
        return 1

def player1(state):
    print("**** your turn ******")
    print(" your possible moves :")
    moves=actions(state)
    index=0
    for item in moves :
        print(index,". ",item)
        index+=1
    i=input("What is your move :  ")
    return(moves[int(i)].copy())

def minmax(state,maximizing_player) :
    global visited_nodes_number
    visited_nodes_number=visited_nodes_number+1
    moves=actions(state)
    if maximizing_player :
        best_value=float('inf')
        for move in moves :
            v=minmax(move,not maximizing_player)
            if isTerminal(state):
                return 1
            best_value=max(best_value,v)
    else :
        best_value=float('-inf')
        for move in moves :
            v=minmax(move,not maximizing_player)
            if isTerminal(state):
                return 0
            best_value=min(best_value,v)
    return best_value
def minmax_alpha_beta(state,alpha,beta,maximizing_player) :
    global visited_nodes_number
    visited_nodes_number=visited_nodes_number+1
    moves=actions(state)
    if maximizing_player :
        for move in moves :
            alpha=max(alpha,minmax_alpha_beta(move,alpha,beta,not maximizing_player))
            if beta <= alpha :
                return alpha
        return alpha
    else :
        for move in moves :
            v=min(beta,minmax_alpha_beta(move,alpha,beta,not maximizing_player))
            if beta <= alpha :
                return beta
        return beta

def player2(state):
    print("**** computers turn ******")
    print(" Computers moves :")
    moves=actions(state)
    index=0
    for item in moves :
        print(index,". ",item)
        index+=1
    moves=actions(state)
    for item in moves :
        if algorithm==True :
            min=minmax_alpha_beta(state,float('-inf'),float('inf'),False)
        else :
            min=minmax(state,False)
        if min == 0:
            return item
    
    return moves[0].copy()

def play(state,player):
    if player==1:
       return player1(state)
    else:
       return player2(state)

player=1
state=[Random().randint(4,15)]
valid=False
choice=None
visited_nodes_number=0
while valid == False:
    print("1.Minmax")
    print("2.Minmax with pruning")
    choice = int(input("Choisir l'algorithme qui vous convient: "))
    if choice in [1,2]:
        valid = True
    else:
        print("Le choix entré est invalide")
algorithm = False if choice==1 else True
while 1 :
    state=play(state,player)
    print(state)
    if isTerminal(state)==1:
        break
    player=switchPlayer(player)

    state=play(state,player)
    print(state)
    if isTerminal(state)==1:
        break
    player=switchPlayer(player)
print ("game is over")
print("The number of visited nodes is : ",visited_nodes_number)
if (player==1):
    print("the computer won !!")
else:
    print("you won !!")
    

