def loadIn(filename="musicrecplus.txt"):
    "Loads the music database from file named musicreccplus.txt"
    try:
        with open(filename, "r") as file:
            database = {}
            for line in file:
                user, artists = line.strip().split(":")
                database[user] = artists.split(",")
                database[user].sort()
            return database   
    except FileNotFoundError:
        return {}

def save(database, filename="musicrecplus.txt"):
    "Saves database to a file"
    with open(filename, "w") as file:
        for (user, artists) in sorted(database.items()):
            file.write(f"{user}:{','.join(sorted(artists))}\n")

def enterPreferences():
    '''allows user to enter artists they like'''
    newArtist = []
    while True:
        artist = input("Enter an artist that you like (Enter to finish): ")
        if artist == '':
            break
        newArtist.append(artist.title())
    return newArtist

def mostPopularArtist(prefArtists, name):
    '''prints the top 3 artists that are liked by the most users'''
    input = open('musicrecplus.txt', 'r+')
    artists = {}
    if type(prefArtists) != list:
        z = prefArtists.split(',')

def getRecommendations(current, preferences, userMap):
    bestUser = findBestUser(current, preferences, userMap)
    print(userMap[bestUser])
    print(preferences)
    print(drop(preferences, userMap[bestUser]))
    recommendations = drop(preferences, userMap[bestUser])
    return recommendations

def findBestUser(current, preferences, userMap):
    best = None
    bestScore = -1
    print("Prefs is", preferences)
    for user in userMap.keys():
        score = numMatches(preferences, userMap[user])
        if score > bestScore and current != user:
            bestScore = score
            bestUser = user
    return bestUser  

def drop(list1, list2):
    newList = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            print("Skipping", list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            newList.append(list2[j])
            j += 1
    while j < len(list2):
        newList.append(list2[j])
        j += 1
    return newList

def numMatches(list1, list2):
    matches = 0
    i = 0
    j = 0
    while(i < len(list1) and j < len(list2)):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches   

 
def startUpMenu():
    database = loadIn()
    userInput = input("Enter your name ( put a $ symbol after your name if you wish your preferences to remain private):")
    if userInput not in database:
        preferences = input("Looks like you are a new user! Please enter your favorite artists:")
        database[userInput] = preferences.split(",")   
        save(database)
    while True:
        print("Enter a letter to choose an option:")
        print("e - Enter preferences")
        print("r - Get recommendations")
        print("p - Show most popular artists")
        print("h - How popular is the most popular")
        print("m - Which user has the most likes")
        print("q - Save and quit")
        userDecision = input("Choose an option: ").strip().lower()
        if userDecision == "e":
            while True:
                favArtist = input("Enter an artist that you like ( Enter to finish ):")
                artists.append(favArtist)
                if favArtist == "":
                    break
                database[userInput] = preferences.split(",")   
                save(database)
        elif userDecision == "r":
            pass
        elif userDecision == "p":
            artists.sort()
            return artists
        elif userDecision == "h":
            pass
        elif userDecision == "m":
            pass
        elif userDecision == "q":
            break
        else:
            print("Invalid option. Please try again")

startUpMenu()
