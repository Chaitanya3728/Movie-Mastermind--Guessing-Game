'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.


'''

import random
movies = ['anand', 'drishyam', 'uri', 'inception', 'gol mal', 'intersteller', 'vampire diaries', 'dangal', 'tare zameen pr']

def create_question(movie):
    n = len(movie)                          # including spaces as well
    letters = list(movie)                   # convert it into list of individual characters
    temp = []
    for i in range(n):
        if(letters[i] == ' '):              # if the letter[i] is space 
            temp.append(' ')                # append space in temp
        else:
            temp.append('*')                # else append *
    qn = ''.join(str(x) for x in temp)      # to make list of all characters into 1 string 
    return qn
    
def is_present(letter, movie):
    c = movie.count(letter)                 # predefined functionality for finding the number of occurances within the character
    if(c == 0):
        return False
    else:
        return True

def unlock(qn, movie, letter):
    reference = list(movie)
    qn_list = list(qn)
    temp = []
    n = len(movie)
    for i in range(n):
        if(reference[i] == ' ' or reference[i] == letter):
            temp.append(reference[i])
        else:
            if(qn_list[i] == '*'):
                temp.append('*')
            else:
                temp.append(reference[i])       # can also be temp.append(qn[i])        
    qn_new = ''.join(str(x) for x in temp)      # to make list of all characters into 1 string 
    return qn_new

def play():
    p1name = input("player 1, please enter your name : ")
    p2name = input("player 2, please enter your name : ")
    pp1 = 0
    pp2 = 0
    turn = 0
    willing = True                                                                                           # willing to keep track of whether player want to continue or not 
    while(willing):
        for turn in range(2,100):
            if(turn %2 == 0):                                                                                    # player 1 turn
                # player1
                print(p1name, 'its your turn')
                picked_movie = random.choice(movies)                                                             # picking random choice from movies
                qn = create_question(picked_movie)                                                               # creating blank as stars for the total letters in movie (spaces to not be included as stars) 
                print(qn)
        
                modified_qn = qn
                not_said = True                                                                                  # player not said correct ans
                while(not_said):
                    letter = input("your letter : ")
                    if(is_present(letter, picked_movie)):                                                        # if letter picked byb player1 is one of the picked movie       
                        # unlock
                        modified_qn = unlock(modified_qn, picked_movie, letter)
                        print(modified_qn)
                        if '*' not in modified_qn:
                            print("Congrats, You won!")
                            pp1 += 1
                            not_said = False
                            break
                        decision = int(input("press 1 to guess movie directly or press 2 to unlock next letter "))    # decision on player1 to guess movie or unlock next letter
                        if(decision == 1):
                            ans = input("OK , so tell me the movie name : ")
                            if ans.lower() == picked_movie.lower():  # ".lower()" method is used to convert both strings to lowercase, so that the comparison is case-insensitive.
                                print("yeahh !!", ans, "is the correct one")
                                pp1 = pp1 + 1 
                                not_said = False                                                                 # as he has now said the correct ans , so here False
                                print(p1name, "your score becomes", pp1)
                            else:
                                print("OOh !!", ans, "is not the correct one. Try again ")
                    else:
                        print("opss", letter, "not found")
                    # if '*' not in modified_qn:
                    #     print("Congrats, You won!")
                    #     pp1 += 1
                    #     not_said = False
                    #     break
            
                # c = int(input("press 1 to continue or 0 to quit - "))
                # if(c == 0):
                #     print(p1name," your score is ", pp1)
                #     print(p2name," your score is ", pp2)
                #     print("thanks for playing")
                #     willing = False
                 
            else: 
                # player2
                print(p2name, 'its your turn')
                picked_movie = random.choice(movies)                                                             # picking random choice from movies
                qn = create_question(picked_movie)                                                               # creating blank as stars for the total letters in movie (spaces to not be included as stars) 
                print(qn)
            
                modified_qn = qn
                not_said = True                                                                                  # player not said correct ans
                while(not_said):
                    letter = input("your letter : ")
                    if(is_present(letter, picked_movie)):                                                        # if letter picked byb player1 is one of the picked movie       
                        # unlock
                        modified_qn = unlock(modified_qn, picked_movie, letter)
                        print(modified_qn)
                        if '*' not in modified_qn:
                            print("Congrats, You won!")
                            pp1 += 1
                            not_said = False
                            break
                        decision = int(input("press 1 to guess movie directly or press 2 to unlock next letter "))    # decision on player1 to guess movie or unlock next letter
                        if(decision == 1):
                            ans = input("OK , so tell me the movie name : ")
                            if ans.lower() == picked_movie.lower():  # ".lower()" method is used to convert both strings to lowercase, so that the comparison is case-insensitive.
                                print("yeahh !!", ans, "is the correct one")
                                pp2 = pp2 + 1 
                                not_said = False                                                                 # as he has now said the correct ans , so here False
                                print(p2name, "your score becomes", pp2)
                            else:
                                print("OOh !!", ans, "is not the correct one. Try again ")
                    else:
                        print("opss", letter, "not found")
                    # if '*' not in modified_qn:
                    #     print("Congrats, You won!")
                    #     pp1 += 1
                    #     not_said = False
                    #     break
            
                # c = int(input("press 1 to continue or 0 to quit - "))
                # if(c == 0):
                #     print(p1name," your score is ", pp1)
                #     print(p2name," your score is ", pp2)
                #     print("thanks for playing")
                #     willing = False
            
            c = int(input("press 1 to continue or 0 to quit - "))
            if(c == 0):
                print(p1name," your score is ", pp1)
                print(p2name," your score is ", pp2)
                print("thanks for playing")
                willing = False
                break
            
            # x = int(input("u want to close the game ? (press 1 for yes | press 0 for No)"))
            # if(x == 1):
            #     willing=False
            #     break
            # else:
            #     continue
        
        
            
play()
