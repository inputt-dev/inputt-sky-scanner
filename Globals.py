from parameters import Parameters

#set the global variables
Globals = Parameters({})

inputt = None
globals.set("inputt",inputt) #The interface 
globals.setDescription("inputt", "The interface")

classifier = None #A Classifier object to hold samglobalsles and generate classifiers, and to run the classifier on other sessions
globals.set("Classifier", classifier) #The classification samglobalsle extractor and analyzer
globals.setDescription("Classifier", "The classification sample extractor and analyzer")

dbFileName = None
db = None #Create the container class for the birdbuddy database
globals.set("DB", db) #"The database connection"
globals.setDescription("DB", "The database connection")

currentSession = None #A global variable to see what session were working on, the path to its saved files the key to the database
globals.set("Camera Session", currentSession) #The camera session file path
globals.setDescription("Camera Session", "The camera session file path")

bb = None #A BirdBuddy Object to handle motion tracking
globals.set("BirdBuddy", bb) #"The movement tracking algorithm, saved to the database"
globals.setDescription("BirdBuddy", "The movement tracking algorithm, saved to the database")

bbv = None  #Hold the tracking information from a BB processed video in memory
globals.set("BB Video Results", bbv) #BirdBuddy results database to python object for analysis
globals.setDescription("BB Video Results", "BirdBuddy results database to python object for analysis")

threads = Parameters({}) #Used to convey thread information to all threads and to set locks on global variables transparentally

threads.set("GUI", None)
threads.setDescription("GUI", "The thread that displays and updates the command line gui window")
