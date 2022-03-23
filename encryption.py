import string
import random


class Encryption:
    printables = string.printable

    def __init__(self, seed: int):
        self.seed = seed

    def encrypt(self, message):
        """
        This method will take in a string message and encrypt it.
        """
        output = ""
        encrypted = ""
        random.seed(self.seed)
        rand_alpha = ''.join(random.sample(Encryption.printables, len(Encryption.printables)))

        ########################  STEP 1  ##############################
        ####### REPLACE EVERY OTHER LETTER WITH A RANDOM LETTER ########
        ################################################################
        for letter in message:
            output += letter + random.choice(Encryption.printables)

        ########################  STEP 2  ##############################
        #################### REVERSE THE STRING ########################
        ################################################################
        encrypted_phrase = output[::-1]

        ########################  STEP 3  ##############################
        ##### USE THE RANDOM SHUFFLED ALPHABET FOR A CEASAR CIPHER #####
        ################################################################
        for letter in encrypted_phrase:
            if letter in Encryption.printables:  # letter.isalpha():
                i = Encryption.printables.index(letter)
                encrypted += rand_alpha[i]
            else:
                encrypted += letter
        encrypted_phrase = encrypted

        return encrypted_phrase

    @staticmethod
    def decrypt(message, seed):
        """
        This method takes in a message and a seed for the random shuffled alphabets.
        It then returns the decrypted message.
        """
        random.seed(seed)
        rand_alpha = ''.join(random.sample(Encryption.printables, len(Encryption.printables)))
        decrypted = ""

        ########################  STEP 1  ##############################
        ################# DECRYPT THE CEASAR CIPHER ####################
        ################################################################
        for letter in message:
            if letter in Encryption.printables:
                i = rand_alpha.index(letter)
                decrypted += Encryption.printables[i]
            else:
                decrypted += letter

        ########################  STEP 2  ##############################
        ########## REVERSE THE STRING AND EXTRACT THE MESSAGE ##########
        ################################################################
        decrypted_phrase = decrypted[::-1][::2]

        return decrypted_phrase
