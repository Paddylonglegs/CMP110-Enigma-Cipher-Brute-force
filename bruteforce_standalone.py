#----------------------------------#
# Author: Patrick Collins          #
# ©️MIT license                     #
# https://github.com/Paddylonglegs/#
#----------------------------------#


#Brute forcing the enigma ciphertext
import time
print('Example Plaintext > THISXISXANXEXAMPLE')
print('Please Enter The Plaintext You Would Like To Brute-Force: ')
usertext = input()
cribtext = usertext[0:len(usertext)//2]
print("This is the cribtext: ", cribtext)
print("Example Start Position > SCC")
startpos = input('Please Enter The Start Position Of The Enigma Machine: ')
print("Example Rotor > I II IV")
userRotors = input('Please Enter The Rotors Of The Enigma Machine: ')

##Encrypt the usertext

from enigma.machine import EnigmaMachine
machine = EnigmaMachine.from_key_sheet(
    rotors= userRotors,
    reflector='B',
    ring_settings="1 1 1",
    plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')

machine.set_display(startpos)
ciphertext = machine.process_text(usertext)
print(ciphertext)
cribCiphertext =ciphertext[0:len(ciphertext)//2]
print(cribCiphertext)
start = time.time()

#List of possible rotor start positions
rotors = [ "I II III", "I II IV", "I II V", "I III II",
"I III IV", "I III V", "I IV II", "I IV III",
"I IV V", "I V II", "I V III", "I V IV",
"II I III", "II I IV", "II I V", "II III I",
"II III IV", "II III V", "II IV I", "II IV III",
"II IV V", "II V I", "II V III", "II V IV",
"III I II", "III I IV", "III I V", "III II I",
"III II IV", "III II V", "III IV I", "III IV II",
"III IV V", "IV I II", "IV I III", "IV I V",
"IV II I", "IV II III", "IV I V", "IV II I",
"IV II III", "IV II V", "IV III I", "IV III II",
"IV III V", "IV V I", "IV V II", "IV V III",
"V I II", "V I III", "V I IV", "V II I",
"V II III", "V II IV", "V III I", "V III II",
"V III IV", "V IV I", "V IV II", "V IV III" ]

#Function for finding start position
def find_rotor_start(rotor_choice, ciphertext, cribtext):
    from enigma.machine import EnigmaMachine

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Set up the Enigma machine
    machine = EnigmaMachine.from_key_sheet(
        rotors= rotor_choice,
        reflector='B',
        ring_settings="1 1 1",
        plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')

#Do a search over all possible starting positions
    for rotor1 in alphabet:
        for rotor2 in alphabet:
            for rotor3 in alphabet:

                #Generate a possible rotor start position
                start_position = rotor1 + rotor2 + rotor3

                #Set the starting position
                machine.set_display(start_position)

                #Attempt to decrypt the plaintext
                plaintext = machine.process_text(cribCiphertext)
                print(plaintext)

                #Check if decrypted version is the same as crib text
                if plaintext == cribtext:
                    ##Decrypt full text
                    #Set the initial position of the Enigma rotors after knowing decrypted start position
                    machine.set_display(start_position)
                    #Decrypting the ciphertext
                    print("Valid settings found")
                    print ("Rotor Choice: ", rotor_choice, "     ", "Start Position: ", start_position)
                    print("Attempting To Decrypt Full Ciphertext...")
                    Fullplaintext = machine.process_text(ciphertext)
                    print(Fullplaintext)
                    return rotor_choice, start_position            
                               
              
    #If unsuccessful in decrypting message
    return rotor_choice, "Cannot find settings"



#Calling the function
for rotor_setting in rotors:
    rotor_choice, start_position = find_rotor_start(rotor_setting, ciphertext, cribtext)
    if start_position != "Cannot find settings":
        end= time.time()
        minutes = end-start
        print("It took", minutes/60, " minutes to brute force the ciphertext")
        break

    
input('Enter any key to exit the program: ')
    
