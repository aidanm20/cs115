#CS Group Project 2
#Rudraneel, Aidan Miller, Jasraj
#I pledge my honor that I have abided by the Stevens Honor System.




#Aidan Miller
def loadIn(filename="musicrecplus.txt"):
    "Loads the music database from file named musicreccplus.txt"
    try:
        with open(filename, "r") as file:
            database = {}
            for line in file:
                user, artists = line.strip().split(":")
                database[user] = artists.split(",")
            return database
    except FileNotFoundError:
        return {}


#Aidan Miller
def save(database, filename="musicrecplus.txt"):
    "Saves database to a file"
    with open(filename, "w") as file:
        for (user, artists) in sorted(database.items()):
            file.write(f"{user}:{','.join(sorted(artists))}\n")


#Aidan Miller
def startUpMenu():
    "Start up menu Code"
    database = loadIn()
    userInput = input("Enter your name ( put a $ symbol after your name if you wish your preferences to remain private):")

    if database[userInput] != True:
        prefs = input("Looks like you are a new user! Please enter your favorite artists:")
        database["userInput"] = "prefs"
        save(database)

    while True:
        print("Enter a letter to choose an option:")
        print("e - Enter preferences")
        print("r - Get recommendations")
        print("p - Show most popular artists")
        print("h - How popular is the most popular")
        print("m - Which user has the most likes")
        userDecision = input("q - Save and quit")

        if userDecision == "e":
            while True:
                favArtist = input("Enter an artist that you like ( Enter to finish ):")
                if favArtist == "":
                    break
                database["userInput"] = "prefs"
                save(database)
        elif userDecision == "r":
            pass
        
        elif userDecision == "p":
            pass
        
        elif userDecision == "h":
            pass
        
        elif userDecision == "m":
            pass
        
        elif userDecision == "q":
            pass
        
        else:
            break
























            
