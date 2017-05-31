# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #  
  
# Jedrzej Lewandowski         #
# progreacja@gmail.com        #  
# --------------------------- #


# Example string input.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
# -----------------------------------------------------------------------------
# Function is creating dictionary, which contains user names, 
# connection list and game list.

def create_data_structure(string_input):
    network = {}
    
# If input string is empty return empty dictionary 'newtwork'.
    if not string_input:
        return network
    
# Uses helper function to return list of users from the string.
# Function's parameters are: string, look up value (single character) before every name,
# look up value after every name and type 'names' - helper function will
# return list of names.
    userList = find_data(string_input,
                         "."," ", "names") 
    
# Uses helper function to find connection lists and liked games, first
# lookup values in those cases are strings,
# which appear in every sentence before connections or games are listed.
# type is 'lists' - helper function will return list of list.
    connectionList = find_data(string_input,
                               "is connected to",".", "lists") 
    
    gameList = find_data(string_input,
                         "likes to play",".", "lists") 

# Loops through all three lists at once and
# creates dictionary containing names of users, 
# which are dictionaries of two lists: connections lists and games lists.
    for eachUser,eachConnect,eachGame in zip(userList,
                                             connectionList,gameList):    
                                                 
# Adds an empty dictionary to the network called after each username.
        network[eachUser] = {}
        
# Adds to username dictionary, list of connections, called 'connections'.   
        network[eachUser]['connections'] = eachConnect
        
# Adds to username dictionary, list of like games, called 'games'.
        network[eachUser]['games'] = eachGame
    return network

#-------------------------------------------------------------------------------
# Helper function called in create_data_structure, to return list of names
# or list of lists of connections or games 
#-------------------------------------------------------------------------------
def find_data(string_input, firstCh, lastCh, type):  
    returnList = []

# Loop until condition for breaking the loop is met. 
    while True:

# Use helper function lookfor_text, which takes as input: string 
# and two look up values.  
# Helper function returns string and last postion of returned string.        
        name, endPos = lookfor_text(string_input,
                                    firstCh, lastCh) 

# If returned name is valid, shorten the input string for next search
# else break the code to stop the loop.
        if name:
            string_input = string_input[endPos:]
        else:
            break
            
# If type is 'names' as for user names, where found string is a single word
# append the string to the list.
        if type == "names":  
            
# Since every name is mentioned twice in input string, 
# check if name was already added. 
            if name not in returnList:
                returnList.append(name)

# If type is 'lists' returned string will be longer - for example long string 
# listing connection names. Function uses 'split' method to dvide string into
# the list and then appends list to the list. 
        if type == "lists":
            name = name.split(', ')
            returnList.append(name)
        
    return returnList  

#-------------------------------------------------------------------------------
# Helper function called in find_data, finds a string in the text, 
# returns string and position of last character of the returned string.
#-------------------------------------------------------------------------------
def lookfor_text(string_input, firstCh, lastCh):
# In order to find position of first letter of looked string, define length of
# 'fritsCh' which is lookup value. If it is a single character add 1.
# Assumption here is that one character lookup value will be a space.
# If it is longer string add 1 plus the length of the string,
# since every word is divided by space or a dot.
    if len(firstCh) > 1:
        addN = len(firstCh) +1
    else:
        addN = 1
        
# Find position of the first character by finding position of first lookup
# value and add length of lookup value.
    startText = string_input.find(firstCh)+addN
    
# If nothing was found return None so the loop in find_data will break.
    if startText == -1:
        return None, 0
    
# Find the position of second lookup value to find end of string.     
    endText = string_input.find(lastCh, startText)
    
# Define the looked string using first position and last.
    text = string_input[startText:endText]
    return text, endText

## ----------------------------------------------------------------------------- 
## get_connections(network, user): 
## ----------------------------------------------------------------------------- 
# Returns list of connections of the user
def get_connections(network, user):
    if user not in network:
        return None
    else:
	return network[user]['connections']
    
## ----------------------------------------------------------------------------- 
## get_games_liked(network, user): 
## -----------------------------------------------------------------------------
# Returns list liked gamnes by user.
def get_games_liked(network , user):
    if user not in network:
        return None
    else:
	return network[user]['games']

## ----------------------------------------------------------------------------- 
## add_connection(network, user_A, user_B): 
## -----------------------------------------------------------------------------
# Adds new connection to user_A list of connections.
def add_connection(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    conneList = get_connections(network, user_A)
    if user_B not in conneList:
       network[user_A]['connections'].append(user_B)
       return network

## ----------------------------------------------------------------------------- 
## add_new_user(network, user, games): 
## -----------------------------------------------------------------------------
# Adds information about new user to the newtork.
def add_new_user(network, user, games):
    if user not in network:
        network[user] = {}
        network[user]['connections'] = []
        network[user]['games'] = games
        return network
    else:
        return network
	
## ----------------------------------------------------------------------------- 
## get_secondary_connections(network, user): 
## -----------------------------------------------------------------------------
# Returns list of connections of user's connections.
def get_secondary_connections(network, user):
    returnList = []
    connections = get_connections(network, user) 
    if connections is None:
        return None
    for e in connections:
# Adds connection lists of every user linked to input user.        
        returnList += network[e]['connections'] 
        
# Uses set for removing duplicates.        
    returnList = list(set(returnList))  
    return returnList    

## ----------------------------------------------------------------------------- 	
## connections_in_common(network, user_A, user_B): 
## ----------------------------------------------------------------------------- 
# Returns the number of connections in common between user_A and user_B. 
def connections_in_common(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False    
    returnList = []
    connList_A = get_connections(network, user_A)
    connList_B = get_connections(network, user_B)
    for e in connList_A:
        if e in connList_B:
            returnList.append(e)
    return len(returnList)
    
## ----------------------------------------------------------------------------- 
## path_to_friend(network, user_A, user_B): 
## ----------------------------------------------------------------------------- 
# Returns the path as list of connections from user_A to user_B.
def path_to_friend(network, user_A, user_B):
    returnList = []
    checked = []
    if user_A not in network or user_B not in network:
        return None
    else:       
        
# Calls helper function to find a path.            
        rt = check_path(network,user_A, user_B, checked) 
        
# If returned path was valid, 
# create return list including user_A and retuned path.          
        if rt:              
            returnList = [user_A]+rt
            return returnList
        else:
            return None

#-------------------------------------------------------------------------------
#Helper function for path_to_friend
#-------------------------------------------------------------------------------
def check_path(network,user_A, user_B, checked):
    
# Sets up return value to False if no path was found.   
    Rt = False 
    
# Finds the connection list of user_A.
    connList_A = get_connections(network, user_A)
    
# Loops through the list to find user_B.    
    for each in connList_A:
        
# If connection is not in checked list.
        if each not in checked: 
            
# Check if current connection is a user_B, if yes, return it, since this is end 
# of the path.
            if each == user_B:
                return [each]
# Else, append current connection to checked list.
            checked.append(each)
            
# Use recursion procedure to check current connection's connection list.           
            next = check_path(network,each, user_B, checked) 
            if next:
                Rt = [each] + next
    return Rt    

## -----------------------------------------------------------------------------
## Make-Your-Own-Procedure (MYOP)
## ----------------------------------------------------------------------------- 

##1 MYOP for removing connection user_B from user_A's connection list
def remove_connection (network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    else:
        connList_A = get_connections(network, user_A)
        if user_B in connList_A:
            connList_A.remove(user_B)
            network[user_A]['connections']=connList_A
        return network    
    
##2 MYOP for finding most popular games, in this case top 5 most liked.
def top5_games (network):
    returnList = []
    gameList = []
    from collections import Counter  
    for each in network: 
        
# Append all the games liked by every user of the network.        
        gameList += get_games_liked(network , each) 
        
# Count occurrences of the games and return top 5.        
    top5 = Counter(gameList).most_common(5)  
    for element, count in top5: 
        
# Extract top 5 to remove Tuples from output.        
        returnList.append(element)
        
# Add index numbers for better display.       
    returnList = list(enumerate((returnList),1)) 
    print   
    print "Top 5 Games - Most Liked"
    
# Print list in new lines with number in front and colon in between.
    print('\n'.join('{} : {}'.format(*k) for k in returnList)) 


net = create_data_structure(example_input)
print net
print path_to_friend(net, "John", "Olive")
print get_connections(net, "Debra")
print add_new_user(net, "Debra", []) 
print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
print get_connections(net, "Mercedes")
print get_games_liked(net, "John")
print get_connections(net, "John")
print add_connection(net, "John", "Freda")
print get_secondary_connections(net, "Mercedes")
print connections_in_common(net, "Freda", "John")
print get_connections(net, "John")
remove_connection(net, "John", "Freda")
print get_connections(net, "John")
top5_games (net)