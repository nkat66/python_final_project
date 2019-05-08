#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


"""
Created on Wed Mar 13 20:23:15 2019

 Kaleb Noble
 Date
 Python 1 - DAT-119 - Spring 2019
 Homework Week #
    This program allows the user to create a rudimentary sheet for a Dungeons
    & Dragons character with a name, race, class, ability scores with modifiers, 
    and a section for any inventory. The user also has the the ability to 
    add more sections.

@author: katnob8
"""

#This function applies any racial modifiers to the scores if the character's race 
#is a dwarf, elf, gnome, or halfling.
def apply_racial_modifiers(race):

    if race == "1":
        print("You get modifications to you attributes!")
        constitution = constitution + 1
        charisma = charisma - 1
    
    elif race == "2":
        print("You get modifications to you attributes!")
        dexterity = dexterity + 1
        constitution = constitution - 1
        
    elif race == "3":
        print("You get modifications to you attributes!5")
        intelligence = intelligence + 1
        wisdom = wisdom - 1

    elif race == "5":
        print("You get modifications to you attributes!")
        dexterity = dexterity + 1
        strength = strength - 1
    
    return race

#this function rolls values for the different statistics.
def roll_stats():
    #simulates rolling 3d6, where three is the lowest value you can get, and
    #18 the highest.
    return random.randint(3, 18)

#This function allows users to view information and ability modifiers for each
#race. It accepts the race as an integer based on the view_race_menu function, 
#opens a corresponding file, reads the file into a variable, and then prints 
#the contents.
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
        half_elf_info = open('half_elf.txt', 'r')
        contents = half_elf_info.read()
        half_elf_info.close()
        print(contents)
        
    elif race == 5:
        halfling_info = open('halfling.txt', 'r')
        contents = halfling_info.read()
        halfling_info.close()
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


#This function allows the user to view information on the various classes
#available. As with the race function, it accepts an argument, evaluates
#it, and returns the contents of the selected file to the player.
def view_class_info(player_class):  
    if player_class == 1:
        bard_info = open('bard.txt', 'r')
        contents = bard_info.read()
        bard_info.close()
        print(contents)
        
    elif player_class == 2:
        cleric_info = open('cleric.txt', 'r')
        contents = cleric_info.read()
        cleric_info.close()
        print(contents)
    
    elif player_class == 3:
        druid_info = open('druid.txt', 'r')
        contents = druid_info.read()
        druid_info.close()
        print(contents)
    
    elif player_class == 4:
        fighter_info = open('fighter.txt', 'r')
        contents = fighter_info.read()
        fighter_info.close()
        print(contents)
    
    elif player_class == 5:
        illusionist_info = open('ranger.txt', 'r')
        contents = illusionist_info.read()
        illusionist_info.close()
        print(contents)
        
    elif player_class == 6:
        paladin_info = open('paladin.txt', 'r')
        contents = paladin_info.read()
        paladin_info.close()
        print(contents)
    
    elif player_class == 7:
        rogue_info = open('rogue.txt', 'r')
        contents = rogue_info.read()
        rogue_info.close()
        print(contents)
        
    elif player_class == 8:
        wizard_info = open('wizard.txt', 'r')
        contents = wizard_info.read()
        wizard_info.close()
        print(contents)
    
    #evaluation if a user types in a number other than 1-9
    else:
        print("Sorry, that's not a viable number. Please try entering another.")
        
    #return statement
    return player_class

#void function to print the class options for the user to view.
def print_class_menu():
    print("Here are the classes you can choose from: ")
    print("1 - Bard")
    print("2 - Cleric")
    print("3 - Druid")
    print("4 - Fighter")
    print("5 - Ranger")
    print("6 - Paladin")
    print("7 - Rogue")
    print("8 - Wizard")

#void function to print the race options for the user to view.
def print_race_menu():
    print("Here are the races you can choose from: ")
    print("1 - Dwarf")
    print("2 - Elf")
    print("3 - Gnome")
    print("4 - Half-Elf")
    print("5 - Halfling")
    print("6 - Human")

#void function to print the main menu for the user to view.
def print_main_menu():
    print("Here are your options: ")
    print("1) Read a list of available races and their abilties/traits.")
    print("2) Read a list of classes and their abilities.")
    print("3) Create a new character.")
    print("4) Edit a character.")
    print("5) Exit the character creator.")
    print()

#main function
def main():
    #Introduce the app and present the options.
    print("Hi there! Welcome to the D&D Character Kickstarter App v. 0.1!")
    print()
    print_main_menu()
    
    #Input to let the user select a choice.
    option = int(input("Type in the number of the activity you want to do " +
                       "first: "))
    
    while option != 5:
        #Option 1 reads a file of racial options and their modifications to 
        #base attributes.
        if option == 1:
            print_race_menu()
            #variable that determines which race the view_race_info function
            #will return
            race = int(input("Please type the number of the race you'd " +
                             "like to see info on: "))
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
                race = int(input("Please type the number of the race you'd " +
                                 "like to see info on (or 7 when finished): "))
                print()
            
            #shows the main menu and allows the user to pick another option.
            print_main_menu()
            option = int(input("What would you like to do now? "))
        
        #Option 2 functions the same as Option 1, except for classes.
        elif option == 2:
            print_class_menu()
            player_class = int(input("Please type the number of the class " +
                                     "you'd like to see info on: "))
            print()
            
            #9 serves as the number to terminate the repetition structure.
            while player_class != 9:
                player_class_contents = view_class_info(player_class)
                print()
                show_menu = input("Press ENTER to continue.")
                print()
                print_class_menu()
                player_class = int(input("Please type the number of the " +
                                "class  you'd like to see info on " +
                                "(or 9 when finished): "))
                print()
            
            option = int(input("What would you like to do now? "))
            
        #this function allows the user to begin creating a character and adding
        #information like race, class, and name.
        elif option == 3:
            #finished = "n"
            #takes in a string for the character's name, opens a file with the 
            #name, and adds it to the sheet.
            character_name = input("Give your new character a name: ")
            character_sheet = open(character_name, 'a')
            character_sheet.write("Name: " + character_name + "\n")
                       
            #takes in a string for the character's race and adds it to the sheet.
            print("Here are your race options again: \n")
            print_race_menu()
            
            #accepts the race as an integer based on the race options menu, then
            #writes the corresponding race to the sheet.
            race = int(input("Please enter the number of the race " +
                             "(1-6) you'd like to be: "))
            if race == 1:
                character_sheet.write("Race: Dwarf\n")
        
            elif race == 2:
                character_sheet.write("Race: Elf\n")
        
            elif race == 3:
                character_sheet.write("Race: Gnome\n")
    
            elif race == 4:
                character_sheet.write("Race: Half-Elf\n")
        
            elif race == 5:
                character_sheet.write("Race: Halfling\n")
    
            elif race == 6:
                character_sheet.write("Race: Human\n")
        
            #evaluation if a user types in a number other than 1-6
            else:
                while race < 1 or race > 7:
                    print("Sorry, that's not a viable number. " + 
                          "Here are the options again:")
                    print_race_menu()
                    race = int(input("Please enter the number of the race " +
                             "(1-6) you'd like to be: "))
                    
            #Prints the class meny again and allows the user to pick one. It
            #then writes the corresponding class to the file.
            print("Here are your class options again: \n")
            print_class_menu()
            player_class = int(input("Please enter the number of the class" + 
                                     "(1-8) you'd like to be: "))

            if player_class == 1:
                character_sheet.write("Class: Bard\n")
        
            elif player_class == 2:
                character_sheet.write("Class: Cleric\n")
            
            elif player_class == 3:
                character_sheet.write("Class: Druid\n")
            
            elif player_class == 4:
                character_sheet.write("Class: Fighter\n")
            
            elif player_class == 5:
                character_sheet.write("Class: Ranger\n")
                
            elif player_class == 6:
                character_sheet.write("Class: Paladin\n")
            
            elif player_class == 7:
                character_sheet.write("Class: Rogue\n")
                
            elif player_class == 8:
                character_sheet.write("Class: Wizard\n")
            
            #evaluation if a user types in a number other than 1-8
            else:
                while player_class < 1 or player_class > 7:
                    print("Sorry, that's not a viable number. " + 
                          "Here are the options again:")
                    print_class_menu()
                    race = int(input("Please enter the number of the race " +
                                     "(1-8) you'd like to be: "))
            
            #Sheet formatting for base attributes
            character_sheet.write("----------------\n")
            print("Base Attributes: ")
            print("----------------")
            character_sheet.write("Base Attributes: \n")
            character_sheet.write("----------------\n")
            print()
            
            #Uses the roll_stats method to randomly generate ability scores.
            strength = roll_stats()
            constitution = roll_stats()
            dexterity = roll_stats()
            wisdom = roll_stats()
            intelligence = roll_stats()
            charisma = roll_stats()
            
            #Calculates and applies modifiers to the appropriate races.
            apply_racial_modifiers(race)
            
            #Cast all integers into strings, then print them for the user to
            #see.
            strength = str(strength)
            constitution = str(constitution)
            dexterity = str(dexterity)
            wisdom = str(wisdom)
            intelligence = str(intelligence)
            charisma = str(charisma)
            
            print("STR: ", strength)
            print("CON: ", constitution)
            print("DEX: ", dexterity)
            print("WIS: ", wisdom)
            print("INT: ", intelligence)
            print("CHA: ", charisma)
            
            #writes stats to the character sheet.
            character_sheet.write("\nSTR: ")
            character_sheet.write(strength)
            character_sheet.write("\nCON: ")
            character_sheet.write(constitution)
            character_sheet.write("\nDEX: ")
            character_sheet.write(dexterity)
            character_sheet.write("\nWIS: ")
            character_sheet.write(wisdom)
            character_sheet.write("\nINT: ")
            character_sheet.write(intelligence)
            character_sheet.write("\nCHA: ")
            character_sheet.write(charisma)
            
            #Sheet formatting for character and XP info
            character_sheet.write("\n----------------\n")
            character_sheet.write("LEVEL AND XP INFO")
            character_sheet.write("\n----------------\n")
            
            #Accepts the user's level and writes it to the character sheet
            character_level = input("What level is your character?: ")
            
            character_sheet.write("LEVEL: ")
            character_sheet.write(character_level)
            
            #Accepts the user's XP points and writes it to the character sheet
            character_xp = input("How many experience points does your character have? ")
            
            character_sheet.write("\nEXP. POINTS: ")
            character_sheet.write(character_xp)
            
            #section to allow user to add inventory to their sheet if they want.
            character_sheet.write("\n----------------\n")
            character_sheet.write("\nINVENTORY")
            character_sheet.write("\n----------------\n")
            
            add_item = input("Would you like to add in some inventory " +
                             "(type 'Y' or 'N'?): ")
            
            #Asks the user to add an item, writes the item to the sheet, and
            #closes it.
            while add_item == 'y' or add_item == "Y":
                item = input("Please enter the name of the item in your inventory: ")
                character_sheet.write(item)
                character_sheet.write("\n")
                print("Item added.")
                next_item = input("Please press ENTER to continue.")
                add_item = input("Would you like to add in some inventory " +
                                 "(type 'Y' or 'N'?): ")
#                
            character_sheet.close()
            
            print()
            
            print("Information added.")
            
            print_main_menu()
            
            option = int(input("What would you like to do now? "))
            
        #Option 4 allows the user to open up and add additional sections.
        elif option == 4:
           #Accepts user-input file name, reads the file, then closes it.
           file_name = input("Please type in the name of the character who's " +
                             "sheet you'd like to edit: ")
           
           character_file = open(file_name, "r")
           
           print("Here's what on the sheet so far: ")
           
           character_sheet_info = character_file.read()
           
           character_file.close()
           
           print(character_sheet_info)
           
           #Option to allow the user to add something to the file.
           edit_file = input("Would you like to add something to this file (Y/N)?: ")
           
           if edit_file == 'y' or edit_file == 'Y':
               
               character_file = open(file_name, "a")
               
               character_file.write("\n----------------\n")
               
               #Lets the user name the section
               section_name = input("What would you like to name this section?")
               character_file.write(section_name)
               character_file.write("\n\n")
               
               #Lets the user choose if they want to add anything to the
               #section
               keep_going = input("Would you like to add some information to "+
                                  "this section? (Y/N) ")
               
               #Loop to allow user to keep adding info to the section as long
               #as the user types "Y"
               while keep_going == 'y' or keep_going == "Y":
                   contents = input("What would you like to enter " +
                                    "(press ENTER to finish)? ")
                   character_file.write(contents)
                   character_file.write("\n")
                   keep_going = input("Would you like to add some more " +
                                      "information to this section? (Y/N) ")
                   
               character_file.close()
           
           print_main_menu()
            
           option = int(input("What would you like to do now? "))
        
        #input validation for menu
        else:
            print("Sorry, that is not an option.  Here are your options again: ")
            print_main_menu
            option = int(input("What would you like to do now? "))
            
           
    print("Thanks for using the D&D Character Kickstarter App!")

#incantation to prevent main from running in imports
if __name__ == "__main__":
    main()
