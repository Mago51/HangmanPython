from colorama import Fore, Style, init
import random
import time
import sys

init(autoreset=True)

EasyWords = ["Baum","Blume","Auto","Haus","Buch","Stuhl","Tisch","Katze","Hund","Fisch","Tiger","Vogel","Apfel","Banane","Orange","Traube","Melone","Kirsche","Zitrone","Ananas"]
MediumWords = ["Computer","Programmieren","Entwicklung","Datenbank","Sicherheit","Algorithmus","Interface","Bibliothek","Landeskrankenhaus","Umweltfreundlich"]
HardWords = ["Quantenmechanik","Transzendentalismus","Interdisziplinarität","Philosophieren","Unabhängigkeitsbewegung","Klimawandelanpassung"]


def logo(): 
    print(Fore.MAGENTA + r"""
  ___ ___                                              
 /   |   \_____    ____    ____   _____ _____    ____  
/    ~    \__  \  /    \  / ___\ /     \\__  \  /    \ 
\    Y    // __ \|   |  \/ /_/  >  Y Y  \/ __ \|   |  by Mago51
 \___|_  /(____  /___|  /\___  /|__|_|  (____  /___|  /
       \/      \/     \//_____/       \/     \/     \/       
          
          
          
          
          
          
          """ )
    

def play_Again():
    time.sleep(1)
    print(Fore.YELLOW + """
——————————————————————————————     
Willst du noch einmal spielen?
——————————————————————————————          
""")
    
    bkt = input("1. Ja | 2. Nein: " + Style.RESET_ALL)
    if bkt == '1':
        start_game()
    elif bkt == "2":
        sys.exit()
    else:
        print(Fore.RED + 'Du hast nur diese zwei Möglichkeiten, versuch es nochmal' + Style.RESET_ALL)
        return play_Again()

def easy_mode():
    return random.choice(EasyWords).lower()

def medium_mode():
    return random.choice(MediumWords).lower()

def hard_mode():
    return random.choice(HardWords).lower()

def choose_difficulty():
    print(Fore.CYAN + "Wähle ein Schwiergkeitsgrad:")
    print(Fore.GREEN + "1. Einfach")
    print(Fore.YELLOW + "2. Mittel")
    print(Fore.RED + "3. Schwer")

    choice = input("Gib die Zahl deines Schwierigkeitsgrads ein (1-3): ")
    if choice == '1':
        return easy_mode()
    elif choice == '2':
        return medium_mode()
    elif choice == "3":
        return hard_mode()
    else:
        print(Fore.RED + "Du hast nur diese Auswahl freundchen.")
        return choose_difficulty()

def play_game(word_to_guess, guessed_letters, attempts):
    while attempts > 0:
        display = ' '.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
        guessed_display = ', '.join(sorted(guessed_letters)) if guessed_letters else '(keine)'
        print(f"\nWort: {display} | Versuche: {attempts} | Buchstaben: {guessed_display}")
        while True:
            guess = input("Errate einen Buchstaben: ").lower()
            if len(guess) == 1 and guess.isalpha():
                break
            print(Fore.YELLOW + "Bitte gib genau 1 Buchstaben ein")
        
        if guess in guessed_letters:
            print(Fore.YELLOW + "Du hast den schon.")
            continue
        guessed_letters.append(guess)
        
        if guess not in word_to_guess:
            attempts -= 1
            print(Fore.RED + f"Falsch! '{guess}' ist nicht im Wort")
        else:
            print(Fore.GREEN + f"Richtig! '{guess}' ist im Wort.")
        
        if set(word_to_guess).issubset(set(guessed_letters)):
            print(Fore.GREEN + f"Glückwunsch! Das Wort ist: {word_to_guess}")
            play_Again()

    print(Fore.RED + f"Versager! Das Wort wa: {word_to_guess}")
    play_Again()

def start_game():
    logo()
    print(Fore.CYAN + "Willkommen zu Hangman!")
    time.sleep(0.5)
    word_to_guess = choose_difficulty()
    print(Fore.CYAN + f"\nDas Wort hat {len(word_to_guess)} Buchstaben.")
    print(' '.join(['_' for _ in word_to_guess]))
    guessed_letters = []
    attempts = 6
    play_game(word_to_guess, guessed_letters, attempts)

if __name__ == "__main__":
    start_game()
