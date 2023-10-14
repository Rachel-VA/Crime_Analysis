#this program created  on 3/24/23 using python version 3.10.10 64bit
#this is the last assignment in w5 CSC370 (AI)
from deepface import DeepFace #pip install deepface
import cv2 #pip install opencv-python
import pandas as pd #to create AI label dataset for images
import os #for working w/ files
import numpy as np #pip install numpy for plotting
import matplotlib.pyplot as plt #pip install matplotlib for plotting and showing the bar chart

from colorama import init  #pip install colorama
init()
from colorama import Fore, Back, Style

""" 

LIST vs ARRAY:List can store elements of different data types while array can only store the same data type
LIST provides more flexibility and doesn't require explicit looping while array does require

LIST[]
*LIST: store ordered index collection and allow same elems and changeable.
TUPLE()
*TUPLE: store collection no order, no changeable, allow repeate elms
SET{}
*SET:collection no order,no index,no repeate elem.
DICTIONARY{key:value}
*DICTIONARY: collection no order,changeable and allow to create index, no repeate elems
"""
#create a main function to restart the program
#makesure to select all codes and hit tap to indent one time inside the main()
def main():
    

    print("\n\n\n")
    input_dir = "C:\dataIMG"  #link a folder, copy the path and pass in as a string
    target_image = "Ivan.jpg"  #just ab image

    #target_image=cv2.imread("Ivan.jpg")
    
    #create the data dictionary to append the analysis results and extracting the name from images inside the data dictionary
    data = {
        "Name": [],
        "Age": [], #empty list of age
        "Gender": [],
        "Race": []      
    }


    #results= DeepFace.analyze(target_image, action=("name","gender","age"))

    #the command line below for joining the two path of folder/img to find a match
    image_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.jpg')]

    #the line of code below is for returning analysis results using Deepface module
    # we can modify the string for the action function to return a list of results
    analysis_results = DeepFace.analyze(cv2.imread(target_image), actions=("name","age", "gender", "race"))

    #analyzie a single image
    #analysis_results = DeepFace.analyze(target_image, actions=("name","age", "gender", "race"))



    print(Fore.LIGHTMAGENTA_EX + "\n\t***** WELCOME TO C.I.A CRIME SOLVING ASSISTANT PROGRAM****\n")
    print(Fore.LIGHTMAGENTA_EX + "This A.I. program is aimed to assist C.I.A. agents in boosting their capabilities in finding suspects\n")
    print(Fore.LIGHTYELLOW_EX + "\tPROGRAM DESCRIPTION:\n")
    print("*. The program can perform a search for a target image in a large database and return a result.")
    print("*. If the program found a match image, it will return with the person name, and an estimation of age, gender, and race.")
    print("*. The program can also analyze images and return a list of results with the estimation of age, gender, and race.\n")

    print(Fore.LIGHTWHITE_EX + "\n\tTWO OPTIONS:\n")
    print(Fore.LIGHTBLUE_EX + "1. FIND A TARGET IAMGE")
    print("Option 1 allow agents to perform a search using an image of a suspect to find a match in a database\n")
    print(Fore.MAGENTA +"2. ANALYZE IMAGES OF SUSPECTS ")
    print("Option 2 let agents analyze images to find an estimation for age, gender, and race")

    print("Please select an option to start the program")
    print(Fore.GREEN + "If you want OPTION 1 for FIND, enter the name of F")
    print(Fore.YELLOW + "If you want OPTION 2 for ANALYSIS, enter A")

    print("If you want to see crime rate graph, enter G")
    agent_choice = input(Fore.LIGHTRED_EX + "\n\tplease enter F or A or G: ")
    if agent_choice == "A":
            
        #load the image file to extract features
        for file in os.listdir("crime"):
            print(Fore.YELLOW +"\n")
            analysis_results = DeepFace.analyze(cv2.imread(f"crime/{file}"), actions=("age", "gender", "race"))
            #append the file contains images, 0 stands for 1st part without extension: name on the image, not the jpg extension
            data["Name"].append(file.split(".")[0])
            data["Age"].append(analysis_results[0]["age"])
            data["Gender"].append(analysis_results[0]["dominant_gender"])
            data["Race"].append(analysis_results[0]["dominant_race"])
            
            
        #keep the output align as shown below to print out the result one time 
        #create data frame to display the extraction results and pass in the data dictionary
        df = pd.DataFrame(data) 
        print(df)
        df.to_csv("people.csv")
            
    if agent_choice == "F":   
            
        #data =analysis_results
        #make sure to use the same var names/string keywords as many of them are already built-in within the DeepFace package
        #
        for image_file in image_files:
            result = DeepFace.verify(target_image, image_file)
            if result['verified']:          #specify 'f' for reading file
                #print("MATCHED IMAGE FOUND: ",f"{image_file} matches the identity of {target_image}")
                matched = result['verified'] #link the result in a var
                
                #print(Fore.LIGHTCYAN_EX + "\nHERE IS THE IMAGE MATCHED of : ",f"{image_file} matches the identity of {target_image}")
                
                if result['verified'] and matched:
                    print(Fore.LIGHTRED_EX + "\nFOUND MATCHED IMAGE: ",f"{image_file} matches the identity of {target_image}\n")
                    #split the name from the jpg and display it
                    print("Name: ",target_image.split(".")[0])       
                    #print("", analysis_results)                   
                    print("\n\n")   
                if result['verified'] and matched:
                    print(Fore.GREEN + "\tSHOW THE POSSIBILITIES FOR AGE, RACE, AND GENDER\n")
                    print("====== Explaination on how to read the analysis results ========\n")
                    print("Because the analysis result is estimated, the program will return list of possibilities in PROBABILITY form")
                    print(Fore.LIGHTWHITE_EX + "\nThe PROBABILITY number ranging from 0-1\n")
                    print("The PROBABILITY number that most close to 1 is the highest possible result that we should consider first")
                    print(Fore.LIGHTMAGENTA_EX + "\nESTIMATIONS: ",analysis_results)
                
                    print("\n")
                else:
                    print(Fore.LIGHTBLUE_EX +"------NO MATCHED IMAGE FOUND IN THIS DATABASE----------")   
                    print("Please consider running the program with another database")


    if agent_choice == "G":
            
        #create arrays for plotting crime types for 4 cities
        #murder cases for 4 cities: Virginia Beach,Chesapeake, Norfolk, Portsmouth
        murder = (4555, 7678, 3960, 9234)
        rape = (5012, 6875, 8096, 3124) #rape cases in order by of cities
        robbery = (2618, 9270, 1056, 7722)
        thief = (6018, 2803, 4960, 8037)

        #var city and store array of cities name corresponding to to 4 array data numbers with type of crimes
        city = ["St.Louis-Miss", "Oakland-Cal", "Memphis-Tenn","Detroit-Mich"]
        index = np.arange(4)#specify index elements number
        #create 4 bar charts and specify the with, label and assign each bar to the var arrays that defined above
        plt.bar(index, murder, width =0.2, label = "Murder")
        plt.bar(index + 0.2, rape, width =0.2, label = "Rape")
        plt.bar(index + 0.4, robbery, width =0.2, label = "Robbery")
        plt.bar(index + 0.6, thief, width =0.2, label = "Thief")


        #load the array on the graph and define a scale range
        plt.title("Crimes Comparison: St.Louis,Oakland,Memphis,Detroit\n")
        plt.xlabel("Dangerous Cities with High Crime Rate")
        plt.ylabel("Number of Cases")
        plt.xticks(index + 0.2, city)
        plt.legend(loc = 'upper left')
        plt.ylim(1000,10000)
        plt.show()#show graph
    
    #this block of code is for restart the program. make sure to indent it inside the main() for it to run same time
    #as other codes above
    #use lower() to convert user input to lowercase ensuring matching letters for the program to work
    restart = input(Fore.LIGHTYELLOW_EX + "Would you like to restart the program? (y/n): ").lower() 
    if restart == "y":
        main()
    else:
        print("You chose to end the program. Goodbye!")
        exit()    

    print("\n\n\n\n\n")
#call the main() to restart the program
#make sure to keep it outside of the main() for it to restart
#where the code start to go back from the begining after the it ended
main()