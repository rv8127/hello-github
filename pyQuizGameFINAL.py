#ART QUIZ GAME (DESIGN THINKING PROJECT)
#By: 
# Alcasid, Rovine Gabriel E.
# Rama, John Wilfred Y.
# Sanchez, Jerlie Mae A.

#-------------------------------------------MAIN GAME FILE-------------------------------------------#

#Import "random" module for shuffling questions and choices
import random

# Import your quiz_data dictionaries from the topic files in the same folder
from questions_colorTheory import quiz_data as ct_quiz
from questions_Perspective import quiz_data as p_quiz
from questions_anatomy import quiz_data as ba_quiz
from questions_elementsOfArt import quiz_data as ea_quiz
from questions_basicLightingStyles import quiz_data as bls_quiz

# Merge all topics into one dictionary
quiz_data = {**ct_quiz, **p_quiz, **ba_quiz, **ea_quiz,  **bls_quiz}

rankings = []  # list of tuples: (player_name, attempt, score, total_questions)

#Defining the main quiz function [The Player's name, and attempts they have made]
def play_quiz(player_name, attempt):
    score = 0

    # ---- LETTER-BASED TOPIC SELECTION (NO DEFAULT) ----
    available_topics = list(quiz_data.keys())
    topic_letter_map = {chr(97 + i): t for i, t in enumerate(available_topics)}

    #Shows available topics and prompts user to select one (a, b, c...)
    while True:
        print("\nAvailable topics (Pick by letter only!):")
        for letter, t in topic_letter_map.items():
            print(f" {letter}) {t}")

        topic_letter = input("Choose a topic: ").strip().lower()
        if topic_letter in topic_letter_map:
            topic_key = topic_letter_map[topic_letter]
            break
        else:
            print(f"⚠️ Invalid choice '{topic_letter}'. Please choose a valid letter.")

    # ---- LETTER-BASED DIFFICULTY SELECTION (NO DEFAULT) ----
    available_levels = list(quiz_data[topic_key].keys())
    level_letter_map = {chr(97 + i): lvl for i, lvl in enumerate(available_levels)}

    #Shows available difficulty levels and prompts user to select one
    while True:
        print("\nAvailable difficulty levels (Pick by letter only!):")
        for letter, lvl in level_letter_map.items():
            print(f" {letter}) {lvl.title()}")

        difficulty_letter = input("Choose a difficulty level by letter: ").strip().lower()
        if difficulty_letter in level_letter_map:
            difficulty_key = level_letter_map[difficulty_letter]
            break
        else:
            print(f"⚠️ Invalid choice '{difficulty_letter}'. Please choose a valid letter.")

    # ---- SELECT ALL QUESTIONS FOR CHOSEN LEVEL ----
    pool = quiz_data[topic_key].get(difficulty_key, [])
    if not pool:
        print(f"No questions found for {difficulty_key.title()} level in {topic_key}.")
        return False

    # ---- PREPARE QUIZ ----
    selected_questions = pool[:]
    num_questions = len(selected_questions)
    random.shuffle(selected_questions)

    # ---- INTRO MESSAGE ----
    print(f"\n🎯 {player_name} — Topic: {topic_key} | Level: {difficulty_key.title()} | Attempt {attempt}")
    print(f"📌 Answer all {num_questions} questions in this level.\n")

    # ---- ASK QUESTIONS ----
    for i, q in enumerate(selected_questions, start=1):
        print("\n========================================\n")
        print(f"{i}. {q['question']}\n")

        options = q.get("options", [])
        if options:  # Multiple choice
            
            option_labels = ["a", "b", "c", "d", "e", "f"]
            for j, opt in enumerate(options):
                print(f"   {option_labels[j]}) {opt}")
            print("   (Type the letter of your answer)")
        else:
            print("   (Type your answer. For multiple answers, separate by commas)")

        print("   (Type 'STOP QUIZ' to quit anytime)\n")
        print("\n---------------------------------------\n")

       # ---- ASK FOR ANSWER ----
        while True:
            ans = input("Your Answer: ").strip()

            # check if user typed STOP QUIZ
            if ans.upper() == "STOP QUIZ":
                print("\n👋 Quiz stopped by user.\n")
                total_questions = len(selected_questions)
                rankings.append((player_name, attempt, score, total_questions))
                return False

            # if empty, re-ask
            if ans == "":
                print("⚠️ You must enter an answer! Please try again.\n")
            else:
                break

        # ---- CHECK ANSWER ----
        correct = False
        if options:  # Multiple choice
            option_map = {option_labels[j]: options[j] for j in range(len(options))}
            if ans.lower() in option_map:
                if option_map[ans.lower()].lower() == q["answer"].lower():
                    correct = True
        else:  # Identification / Enumeration type (Case insensitive, order insensitive for multiple answers)
            user_answers = [a.strip().lower() for a in ans.split(",")]
            correct_answers = [a.strip().lower() for a in q["answer"].split(",")]
            if set(user_answers) == set(correct_answers):
                correct = True

        if correct:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}\n")

    # ---- FINAL SCORE & RANKINGS ----
    total_questions = len(selected_questions)
    print(f"\n🏆 Final Score for {player_name}: {score}/{total_questions} (Attempt {attempt})\n")
    rankings.append((player_name, attempt, score, total_questions))

    # ---- DISPLAY RANKINGS ----
    print("📊 Current Rankings:")
    for r in rankings:
        print(f"{r[0]} - Attempt {r[1]}: {r[2]}/{r[3]}")
    print("\n")
    return True

# ---- MAIN PROGRAM LOOP ----
def main():
    attempt = 1
    print("\n🎨 Welcome to the Art Quiz! 🎨")
    name = input("Enter your name: ").strip() or "Player"

    while True:
        keep_playing = play_quiz(name, attempt)
        if not keep_playing:
            break
        # Ask if the player wants to play again
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("👋 Thanks for playing the Art Quiz! Goodbye!")
            break

        attempt += 1

#Shows that the program starts here
if __name__ == "__main__":
    main()