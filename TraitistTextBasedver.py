#MAIN TRAITIST PROGRAM

import random, time

# Import quiz_data QUESTIONS, OPTIONS, AND ANSWERS dictionaries from the topic files in the same folder
from questions_colorTheory import quiz_data as ct_quiz
from questions_Perspective import quiz_data as p_quiz
from questions_anatomy import quiz_data as ba_quiz
from questions_elementsOfArt import quiz_data as ea_quiz
from questions_basicLightingStyles import quiz_data as bls_quiz

# Merge all topics into one dictionary
quiz_data = {**ct_quiz, **p_quiz, **ba_quiz, **ea_quiz, **bls_quiz}

# Rankings list format: (player_name, attempt, score, total_questions)
rankings = []


# ---------------- TYPEWRITER EFFECT ----------------
def slow_print(text, delay=0.03):
    """Prints text with a smooth typewriter-style animation."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


# ---------------- MAIN QUIZ FUNCTION ----------------
def play_quiz(player_name, attempt):
    score = 0
    lives = 3  # ❤️ Starting lives

    # ---- TOPIC SELECTION ----
    available_topics = list(quiz_data.keys())
    topic_letter_map = {chr(97 + i): t for i, t in enumerate(available_topics)}

    while True:
        print("\nAvailable topics (Pick by letter only!):")
        for letter, t in topic_letter_map.items():
            print(f" {letter}) {t}")

        topic_letter = input("Choose a topic: ").strip().lower()
        if topic_letter in topic_letter_map:
            topic_key = topic_letter_map[topic_letter]
            break
        else:
            slow_print(f"⚠️ Invalid choice '{topic_letter}'. Please choose a valid letter.", 0.03)

    # ---- DIFFICULTY SELECTION ----
    available_levels = list(quiz_data[topic_key].keys())
    level_letter_map = {chr(97 + i): lvl for i, lvl in enumerate(available_levels)}

    while True:
        print("\nAvailable difficulty levels (Pick by letter only!):")
        for letter, lvl in level_letter_map.items():
            print(f" {letter}) {lvl.title()}")

        difficulty_letter = input("Choose a difficulty level by letter: ").strip().lower()
        if difficulty_letter in level_letter_map:
            difficulty_key = level_letter_map[difficulty_letter]
            break
        else:
            slow_print(f"⚠️ Invalid choice '{difficulty_letter}'. Please choose a valid letter.", 0.03)

    # ---- LOAD QUESTIONS ----
    pool = quiz_data[topic_key].get(difficulty_key, [])
    if not pool:
        slow_print(f"No questions found for {difficulty_key.title()} level in {topic_key}.", 0.03)
        return "no_questions"

    # ---- PREPARE AND SHUFFLING QUESTIONS ----
    selected_questions = pool[:]
    num_questions = len(selected_questions)
    random.shuffle(selected_questions)

    # ---- INTRO MESSAGE ----
    slow_print(f"\n🎯 {player_name} — Topic: {topic_key} | Level: {difficulty_key.title()} | Attempt {attempt}", 0.03)
    time.sleep(1)
    slow_print(f"📌 You have {num_questions} questions and {lives} ❤️  lives.\n", 0.03)
    time.sleep(1.5)

    # ---- ASK/DISPLAY QUESTIONS ----
    for i, q in enumerate(selected_questions, start=1):
        print("\n========================================\n")
        slow_print(f"{i}. {q['question']}\n", 0.02)
        # ---- DISPLAY OPTIONS IF ANY ----
        options = q.get("options", [])
        if options:  # Multiple choice
            option_labels = ["a", "b", "c", "d", "e", "f"]
            for j, opt in enumerate(options):
                slow_print(f"   {option_labels[j]}) {opt}", 0.015)
            print("   (Type the letter of your answer)")
        else:
            print("   (Type your answer. For multiple answers, separate by commas)")
            print("   (For Two-Word Answers, separate by a space between the words)")

        print("   (Type 'STOP QUIZ' to quit anytime)")
        print(f"   \n   Lives left: {' ❤️ ' * lives}\n")
        print("---------------------------------------\n")

        # ---- GET PLAYER ANSWER ----
        while True:
            ans = input("Your Answer: ").strip()

            #IF USER WANTS TO QUIT DURING THE QUIZ
            if ans.upper() == "STOP QUIZ":
                slow_print("\n👋 Quiz stopped by user.\n", 0.03)
                answered_so_far = i - 1
                slow_print(f"📊 Progress: You answered {answered_so_far} out of {num_questions}.", 0.03)
                slow_print(f"✅ Your current score: {score}/{answered_so_far}\n", 0.03)
                rankings.append((player_name, attempt, score, num_questions))
                return "stopped"

            if ans == "":
                slow_print("⚠️ You must enter an answer! Please try again.\n", 0.03)
            else:
                break

        # ---- CHECK ANSWER ----
        correct = False
        if options:  # Multiple choice
            option_map = {option_labels[j]: options[j] for j in range(len(options))}
            if ans.lower() in option_map:
                if option_map[ans.lower()].lower() == q["answer"].lower():
                    correct = True
        else:  # Identification / Enumeration
            user_answers = [a.strip().lower() for a in ans.split(",")]
            correct_answers = [a.strip().lower() for a in q["answer"].split(",")]
            if set(user_answers) == set(correct_answers):
                correct = True

        # ---- FEEDBACK ----
        time.sleep(0.6)
        if correct:
            slow_print(" ✅ Correct!\n", 0.04)
            score += 1
        else:
            lives -= 1
            slow_print(f" ❌ Wrong! Correct answer: {q['answer']}", 0.04)
            if lives > 0:
                slow_print(f"💔 You lost a life! Lives left: {' ❤️ ' * lives}\n", 0.03)
            else:
                slow_print("\n💀 No lives left! Game over for this round.\n", 0.03)
                time.sleep(1)

                # Save this attempt
                rankings.append((player_name, attempt, topic_key, difficulty_key, score, num_questions))

                # Display ALL past attempts
                slow_print("📊 Your Final Scores So Far:\n", 0.03)
                for r in rankings:
                    slow_print(f"📊 Final score (Attempt {r[1]}): {r[4]}/{r[5]} "
                            f"(Topic: {r[2]}), (Difficulty: {r[3]})", 0.02)
                    
                return "out_of_lives"  # Special flag for losing all lives

        time.sleep(1)  # small pause before next question

    # ---- QUIZ COMPLETED ----
    time.sleep(1)
    slow_print(f"\n🏆 Final Score for {player_name}: {score}/{num_questions} (Attempt {attempt} - {topic_key}, {difficulty_key})", 0.03)
    rankings.append((player_name, attempt, topic_key, difficulty_key, score, num_questions))

    # ---- DISPLAY RANKINGS ----
    time.sleep(1)
    print("\n📊 Current Rankings:")
    for r in rankings:
        #slow_print(f"{r[0]} - Attempt {r[1]}: {r[2]}/{r[3]}", 0.02)
        #slow_print(f"{r[0]} - Attempt {r[1]} ({r[2]}): {r[3]}/{r[4]}", 0.02)
        slow_print(f"{r[0]} - Attempt {r[1]} ({r[2]} | {r[3]}): {r[4]}/{r[5]}", 0.02)
    print("\n")

    return "completed"


# ---------------- MAIN GAME LOOP ----------------
def main():
    attempt = 1
    slow_print("\n🎨 Welcome to Traitist! 🎨", 0.03)
    name = input("Enter your name: ").strip() or "Player"

    slow_print(f"\n👋 Hello, {name}! Welcome to Traitist — your ultimate Art Quiz experience!\n", 0.03)
    time.sleep(1)

    slow_print("📝 Before we start, here are some quick instructions:", 0.03)
    time.sleep(0.5)

    slow_print("• You have 3 tries per difficulty.", 0.03)
    slow_print("• If all 3 lives are used, the quiz game is over and you must start again", 0.03)
    #slow_print("• If you use up all 3 tries, you can’t continue on that difficulty, so choose wisely!", 0.03)
    slow_print("• You only have to answer 20 questions to test your knowledge.", 0.03)
    slow_print("• Correct answer = +1 point", 0.03)
    slow_print("• Wrong answer = 0 points", 0.03)
    time.sleep(0.5)


    slow_print("\nGood luck, and enjoy the quiz! 🎨✨\n", 0.03)
    time.sleep(1)

    while True:
        result = play_quiz(name, attempt)

        if result == "no_questions":
            break
        elif result == "stopped":
            slow_print("👋 Thanks for playing Traitist! Goodbye!", 0.03)
            break
        elif result == "out_of_lives":
            again = input("💀 You ran out of lives! Try again? (yes/no): ").strip().lower()
            if again == "yes":
                attempt += 1
                continue
            else:
                slow_print("👋 Thanks for playing Traitist! See you next time!", 0.03)
                break
        else:  # completed
            again = input("🎉 You finished the quiz! Play again? (yes/no): ").strip().lower()
            if again == "yes":
                attempt += 1
                continue
            else:
                slow_print("👋 Thanks for playing Traitist! Goodbye!", 0.03)
                break


# ---------------- PROGRAM ENTRY POINT ----------------
if __name__ == "__main__":
    main()