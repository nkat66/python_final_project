#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


"""
Created on Wed Mar 13 20:23:15 2019

 Kaleb Noble
 Date
 Python 1 - DAT-119 - Spring 2019
 Homework Week #
    This program ________.

@author: katnob8
"""

'''
This function accepts the user input as an argument, then evaluates it and
returns information on the proper readout. Each if/elif opens the corresponding
file, reads it into the contents variable, and returns contents to the main
function.
'''

#this function rolls values for the different statistics.
def roll_stats():
    #simulates rolling 3d6, where three is the lowest value you can get, and
    #18 the highest.
    return random.randint(3, 18)

def view_race_info(race):
    if race == 1:
        dwarf_info = open('dwarf.txt', 'r')
        contents = dwarf_info.read()
        dwarf_info.close
        print(contents)
        
    elif race == 2:
        elf_info = open('elf.txt', 'r')
        contents = elf_info.read()
        elf_info.close()
        print(contents)
        
    elif race == 3:
        gnome_info = open('gnome.txt', 'r')
        contents = gnome_info.read()
        gnome_info.close()
        print(contents)
    
    elif race == 4:
        halfling_info = open('halfling.txt', 'r')
        contents = halfling_info.read()
        halfling_info.close()
        print(contents)
    
    elif race == 5:
        half_elf_info = open('half_elf.txt', 'r')
        contents = half_elf_info.read()
        half_elf_info.close()
        print(contents)
    
    elif race == 6:
        human_info = open('human.txt', 'r')
        contents = human_info.read()
        human_info.close()
        print(contents)
        
    #evaluation if a user types in a number other than 1-6
    else:
        print("Sorry, that's not a viable number. Please try entering another.")
    
    #returns the result to the main function.
    return race

'''
This function allows the user to view information on the various classes
available. As with the previous function, it accepts an argument, evaluates
it, and returns the contents of the selected file to the player.
'''
def view_class_info(player_class):
    if player_class == 1:
        barbarian_info = open('barbarian.txt', 'r')
        contents = barbarian_info.read()
        barbarian_info.close
        print(contents)
        
    elif player_class == 2:
        bard_info = open('bard.txt', 'r')
        contents = bard_info.read()
        bard_info.close()
        print(contents)
        
    elif player_class == 3:
        cleric_info = open('cleric.txt', 'r')
        contents = cleric_info.read()
        cleric_info.close()
        print(contents)
    
    elif player_class == 4:
        druid_info = open('druid.txt', 'r')
        contents = druid_info.read()
        druid_info.close()
        print(contents)
    
    elif player_class == 5:
        fighter_info = open('fighter.txt', 'r')
        contents = fighter_info.read()
        fighter_info.close()
        print(contents)
    
    elif player_class == 6:
        illusionist_info = open('illusionist.txt', 'r')
        contents = illusionist_info.read()
        illusionist_info.close()
        print(contents)
        
    elif player_class == 7:
        paladin_info = open('paladin.txt', 'r')
        contents = paladin_info.read()
        paladin_info.close()
        print(contents)
    
    elif player_class == 8:
        rogue_info = open('rogue.txt', 'r')
        contents = rogue_info.read()
        rogue_info.close()
        print(contents)
        
    elif player_class == 9:
        wizard_info = open('wizard.txt', 'r')
        contents = wizard_info.read()
        wizard_info.close()
        print(contents)
    
    #evaluation if a user types in a number other than 1-6
    else:
        print("Sorry, that's not a viable number. Please try entering another.")
        
    #return statement
    return player_class

def print_class_menu():
    print("Here are the classes you can choose from: ")
    print("1 - Barbarian")
    print("2 - Bard")
    print("3 - Cleric")
    print("4 - Druid")
    print("5 - Fighter")
    print("6 - Illusionist")
    print("7 - Paladin")
    print("8 - Rogue")
    print("9 - Wizard")
    print("10 - Done")

def print_race_menu():
    print("Here are the races you can choose from: ")
    print("1 - Dwarf")
    print("2 - Elf")
    print("3 - Gnome")
    print("4 - Half-Elf")
    print("5 - Halfling")
    print("6 - Human")
    print("7 - Done")

def print_main_menu():
    print("Here are your options: ")
    print("1) Read a list of available races and their abilties/traits.")
    print("2) Read a list of classes and their abilities.")
    print("3) Create a new character.")
    print("4) Edit a character.")
    print("5) List the menu options again.")
    print("6) Exit the character creator.")
    print()

#main function
def main():
    #Introduce the app and present the options.
    print("Hi there! Welcome to the D&D Character Kickstarter App v. 0.1!")
    print()
    print_main_menu()
    
    #Input to let the user select a choice.
    option = int(input("Type in the number of the activity you want to do first: "))
    
    while option != 6:
        #Option 1 reads a file of racial options and their modifications to 
        #base attributes.
        if option == 1:
            print_race_menu()
            #variable that determines which race the view_race_info function
            #will return
            race = int(input("Please type the number of the race you'd like to see info on (or 7 when finished): "))
            print()
            
            #loop to allow the user to view the available races as many 
            #times as they want
            while race != 7:
                #accepts race as a variable and passes it to the view_race_info
                #function
                race_contents = view_race_info(race)
                print()
                show_menu = input("Press ENTER to continue.")
                print()
                print_race_menu()
                print()
                race = int(input("Please type the number of the race you'd like to see info on (or 7 when finished): "))
                print()
            
            #shows the menu and allows the user to pick another option.
            print_main_menu()
            option = int(input("What would you like to do now? "))
            
        elif option == 2:
            print_class_menu()
            player_class = int(input("Please type the number of the class you'd like to see info on: "))
            print()
            
            while player_class != 10:
                player_class_contents = view_class_info(player_class)
                print()
                show_menu = input("Press ENTER to continue.")
                print()
                print_class_menu()
                player_class = int(input("Please type the number of the class you'd like to see info on: "))
                print()
            
            option = int(input("What would you like to do now? "))
            
        #this function allows the user to begin creating a character and adding
        #information like race, class, and name.
        elif option == 3:
            #finished = "n"
             #takes in a string for the character's name, opens a file with the name, and adds it to the sheet.
            character_name = input("Give your new character a name: ")
            character_sheet = open(character_name, 'a')
            character_sheet.write("Name: " + character_name + "\n")
                       
            #takes in a string for the character's race and adds it to the sheet.
            race = input("What race would you like your character to be? ")
            character_sheet.write("Race: " + race + "\n")
            race.lower()
            
            #takes in a string for the character's class and adds it to the sheet.
            player_class = input("What class would you like your character to be? ")
            character_sheet.write("Player: " + player_class + "\n")
            player_class.lower()
            character_sheet.write("----------------")
            print()
            
            #For now, this randomly rolls the statistics for the PC's 
            #attributes.
            print("Base Attributes: ")
            print("----------------")
            character_sheet.write("Base Attributes: ")
            character_sheet.write("----------------")
            #Each statistic is assigned its own variable to make assigning the
            #racial penalties and bonuses for each class easier later on.
            strength = str(roll_stats())
            print("STRENGTH: ", strength)
            character_sheet.write("STRENGTH: ")
            character_sheet.write(strength)
            character_sheet.write("\n")
            
            constitution = str(roll_stats())
            print("CONSTITUTION: ", constitution)
            character_sheet.write("CONSTITUTION: ")
            character_sheet.write(constitution)
            character_sheet.write("\n")
            
            dexterity = str(roll_stats())
            print("DEXTERITY: ", dexterity)
            character_sheet.write("DEXTERITY: ")
            character_sheet.write(dexterity)
            character_sheet.write("\n")
            
            wisdom = str(roll_stats())
            print("WISDOM: ", wisdom)
            character_sheet.write("WISDOM: ")
            character_sheet.write(wisdom)
            character_sheet.write("\n")
            
            intelligence = str(roll_stats())
            print("INTELLIGENCE: ", intelligence)
            character_sheet.write("INTELLIGENCE: ")
            character_sheet.write(intelligence)
            character_sheet.write("\n")
            
            charisma = str(roll_stats())
            print("CHARISMA: ", charisma)
            character_sheet.write("CHARISMA: ")
            character_sheet.write(charisma)
            character_sheet.write("\n")
            print("\n")
            print("Since your character is ", race, "two of these scores need \
                  to be modified.")
            
            strength = int(strength)
            constitution = int(constitution)
            dexterity = int(dexterity)
            wisdom = int(wisdom)
            intelligence = int(intelligence)
            charisma = int(charisma)
            
            if race == "dwarf":
                #logic
                
            elif race == "elf":
                dexterity = dexterity + 2
                constitution = constitution - 1
            
            print()
            
            character_sheet.write("----------------")
            
            print()
            
            character_sheet.close()
            
            print("Information added.")
            
            option = int(input("What would you like to do now? "))
            
        
        #Option 5 allows the user to view the menu options again.
        elif option == 5:
            print("Here are the menu options again: ")
            print()
            print("1) Read a list of available races and their abilties/traits.")
            print("2) Read a list of classes and their abilities.")
            print("3) Create a new character.")
            print("4) Edit a character.")
            print("5) List the menu options again.")
            print("6) Exit the character creator.")
            option = str(input("What would you like to do now? "))
    
    print("Thanks for using the D&D Character Kickstarter App!")

    
#incantation to prevent main from running in imports
if __name__ == "__main__":
    main()
