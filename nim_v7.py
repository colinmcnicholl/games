"""
nim.py
Colin McNicholl
07/06/2019

An implementation of the simple version of the nim game (better called the
subtraction game) in which you start with a variable number of counters
(stones, coins, matches, paper clips); two players take turns to pick up
1,,n counters where n is given by the computer.
The person who picks up the last counter(s) is the winner.
"""

import random

# User defined variables.
lower_limit_max_num = 5      
upper_limit_max_num = 9      
upper_limit_counters = 80    
minimum_number_of_plays = 3 
min_num = 1                  
plays = []             
play_levels = [0, 1, 2]
        

def play_at_level(level, counters, max_num):
    """Inputs:
    level is an interger from the set {0, 1 or 2}.
        level 0: - expert - computer plays perfectly
        level 1: - medium - computer makes about 1 mistake every 5 plays
                             (this should be enough to let a player make one
                             mistake and recover)
        level 2: - dummy - all computer plays are random
    counters, an integer, is the number of counters on the table.
    max_num, an integer, is the maximum number of counters a player can
    pick up.
    
    Output: An interger from the set {0, 1 or 2} denoting the
    degree of difficulty of the game.
    """
    if level == 0:
        return computers_turn(counters, max_num)
    elif level == 2:
        return random.randint(min_num, min(counters, max_num))
    elif level == 1:
        choice = random.randrange(5)
        if choice == 0:
            return random.randint(min_num, min(counters, max_num))
        else:
            return computers_turn(counters, max_num)
    else:
        print(f'Error: The value of level is {level}.  It must be 0, 1 or 2.')
    

def players_turn(players_turn_counter, lower_limit, upper_limit):
    """Inputs:  players_turn_counter, an integer, is the number of counters
    on the table.  lower_limit is the minimum number of counters the player
    must pick up and upper_limit is the maximum number of counters the player
    can pick up.
    
    Output: An integer denoting the number of counters the player picks up.
    It must be within the range (lower_limit to upper_limit) or if
    players_turn_counter is less than upper_limit the upper_limit becomes
    players_turn_counter.
    """
    players_resp = 0
    while players_resp > upper_limit or players_resp < lower_limit:
        user_val = input(f'Your turn.  How many counters do you want to pick up? Enter a number in the range {lower_limit}..{upper_limit}: ')
        try:
            players_resp = int(user_val)
        except:
            print(f'{user_val} is not an integer - try again.')
        else:
            if players_resp > upper_limit or players_resp < lower_limit:
                print(f'Error {players_resp} is outside the valid range {lower_limit}..{upper_limit}.')
    return players_resp
   

def computers_turn(computers_turn_counter, max_num):
    """Inputs: computers_turn_counter is the number of counters on the table.
    max_num is the maximum number of counters the computer can pick up.
    
    Output:  An integer - how many counters the computer picked up.
    """
    remainder = computers_turn_counter % (max_num + 1)
    
    if remainder == 0:
        computers_resp = random.randint(min_num, max_num // 2)
        return computers_resp
    else:
        temp = computers_turn_counter
        for num in range(min_num, max_num + 1):
            if (temp - num) % (max_num + 1) == 0:
                computers_resp = num
                return computers_resp
            else:
                continue
    return computers_resp
        
            
def nim_prompt(play, counters):
    """Inputs: play is the number of counters picked up for this play.
    counters is the number of counters left after play.
    
    Output: A string showing the game history.  Example:
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXccccPPPPcccccPPP'
    Shows thers are 43 counters on the table.  The game started with
    59 counters.  The past plays ('P' player, 'c' computer) are
    shown in order (3,5,4,4 respectively).
    """
    plays.append(play)
    return show_counters(counters)
    
       
def show_counters(counters):
    """Input: counters, an integer,  is the number of counters on the table.
    
    Output: A string containing an "X" for each counter on the table.
    """
    output_string = ''
    for x in range(counters):
        output_string += 'X'
    # output_string += reverse()  # Optional, insted of pop_plays().
    output_string += pop_plays()
    return output_string
    
    
def reverse_append_plays():
    """Inputs: The global variable plays, a list containing integers, which
    holds the history of the game.  Each integer in the list is the number
    of counters picked up by the player or computer.
    
    Note: This function is not called.  It could optionally be called
    from within the function show_counters() instead of the
    function pop_plays().
    
    Output: A string, e.g. 'ccccPPPPcccccPPP' indicates that on the first play
    of the game the player picked up 3, then the computer picked up 5,
    player picked up 4 and on most recent play computer picked up 4.
    """
    output_string = ''
    plays.reverse()
    if len(plays) % 2 == 0:
        player_char = 'c'
    else:
        player_char = 'P'
        
    if player_char == 'c':
        not_player_char = 'P'
    else:
        not_player_char = 'c'
    
    for play in plays:
        output_string += player_char * play
        player_char, not_player_char = not_player_char, player_char
        
    plays.reverse()
    return output_string
    
    
def pop_plays():
    """Inputs: The global variable plays, a list containing integers, which
    holds the history of the game.  Each integer in the list is the number
    of counters picked up by the player or computer.
    
    Output: Output: A string, e.g. 'ccccPPPPcccccPPP' indicates that on the first play
    of the game the player picked up 3, then the computer picked up 5,
    player picked up 4 and on most recent play computer picked up 4.
    """
    temp_copy_plays = plays[:]
    output_string = ''
    if len(plays) % 2 == 0:
        player_char = 'c'
    else:
        player_char = 'P'
        
    if player_char == 'c':
        not_player_char = 'P'
    else:
        not_player_char = 'c'
    
    for play in plays:
        number_picked = temp_copy_plays.pop()
        output_string += player_char * number_picked
        player_char, not_player_char = not_player_char, player_char
        
    return output_string
    
    
def set_legend(length, last_counter):
    """Inputs: length, an integer, is the number of counters
    the game started with.  last_counter, an integer, is the
    number of counters on the table.
    
    Output: A string, example (the second line below):
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXccccPPPPcccccPPP
        '    1    '    2    '    3    '    4  ^  '    5    '    
    printed as a legend directly under the game history.
    """
    legend_list = []
    for i in range(length + 1):
        legend_list.append(' ')
    for i in range(length + 1):
        if i % 5 == 0:
            legend_list[i] = "'"
    for i in range(length + 1):
        if i % 10 == 0:
            legend_list[i] = str(i).rstrip('0')
    legend_list[last_counter] = '^'
    return ''.join(legend_list)


def main():

    def welcome():
        print('Welcome to the game Nim.')
        print('Here are the rules: ')
        print('Two players start with n counters with n chosen by the computer..')
        print('The players take it in turn to pick up, up to k counters on each turn,')
        print('were k is chosen by the computer and 1 <= k <= n.')
        print('In the normal game the player who picks up the last counter(s) is the winner.')
        print()
        
    welcome()

    max_num = random.randint(lower_limit_max_num, upper_limit_max_num)
    counters = random.randint(minimum_number_of_plays * max_num, upper_limit_counters)
    print(f'The number of counters is {counters}.')
    
    level = -1
    while level not in play_levels:
        user_level = input('Enter a play level from 0, 1 or 2: ')
        try:
            level = int(user_level)
        except:
            print(f'{user_level} is not an integer in 0, 1 or 2.')
        else:
            if level not in play_levels:
                print(f'{level} is not 0, 1 or 2.  Please try again.')
                                   
    winner = 'computer'
    while counters > 0:
        players_resp = players_turn(counters, min_num, min(counters, max_num))
        counters -= players_resp
        print(f"You picked up {players_resp} counters.  There are {counters} left.")
        print(nim_prompt(players_resp, counters))
        print(set_legend(counters + sum(plays), counters))
        if counters > 0:
            computers_resp = play_at_level(level, counters, max_num)
            counters -= computers_resp
            print(f"Computer picked up {computers_resp} counters.  There are {counters} left.")
            nim_prompt(computers_resp, counters)
        else:
            winner = 'player'
            
    print(f'The {winner} has won!')
            

if __name__ == '__main__':
    main()

# nim_v7.py
#-----------------------------------------------------------------------------#
