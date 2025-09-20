# pyQuizGame_clean.py
import random
import time
from inputimeout import inputimeout, TimeoutOccurred

# Import your quiz_data dictionaries
from questions_colorTheory import quiz_data as ct_quiz
from questions_Perspective import quiz_data as p_quiz

# Merge dictionaries into one
quiz_data = {**ct_quiz, **p_quiz}

rankings = []  # list of tuples (name, attempt, score, total_questions)


def play_quiz(player_name, topic, attempt):
    score = 0

    topic_key = topic.strip()
    if topic_key not in quiz_data:
        print(f"⚠️ Invalid topic '{topic_key}', defaulting to Color Theory.")
        topic_key = "Color Theory"

    # Run from easy → medium → hard automatically
    difficulties = ["easy", "medium", "hard"]
    for difficulty_key in difficulties:
        pool = quiz_data[topic_key].get(difficulty_key, [])
        if not pool:
            continue

        num_questions = min(5, len(pool))
        selected_questions = random.sample(pool, num_questions)

        print(f"\n🎨 {player_name} — Topic: {topic_key} | Level: {difficulty_key.title()} | Attempt {attempt}")
        print(f"⏱️ Answer {num_questions} questions.\n")

        for i, q in enumerate(selected_questions, start=1):
            print(f"{i}. {q['question']}")

            # Multiple choice or Identification/Enumeration
            options = q.get("options", [])
            time_limit = 10 if options else 20

            if options:
                random.shuffle(options)
                option_labels = ["a", "b", "c", "d", "e", "f"]
                for j, opt in enumerate(options):
                    print(f"   {option_labels[j]}) {opt}")
                print("")
                print(f"⏳ You have {time_limit} seconds to answer (type letter).")
            else:
                print(f"⏳ You have {time_limit} seconds to answer (type answer).")
                print("   (For enumeration: separate answers with commas)")
            print("   (Type 'STOP QUIZ' to quit anytime)\n")

            try:
                ans = inputimeout(prompt="Your Answer: ", timeout=time_limit)
            except TimeoutOccurred:
                print("⏰ Time’s up!\n")
                continue

            ans = ans.strip()
            if ans.upper() == "STOP QUIZ":
                print("\n👋 Quiz stopped by user.\n")
                rankings.append((player_name, attempt, score, num_questions))
                return False  # quit quiz

            correct = False
            if options:  # Multiple choice
                option_map = {option_labels[j]: options[j] for j in range(len(options))}
                if ans.lower() in option_map:
                    if option_map[ans.lower()].lower() == q["answer"].lower():
                        correct = True
            else:  # Identification / Enumeration
                user_answers = [a.strip().lower() for a in ans.split(",")]
                correct_answers = [a.strip().lower() for a in q["answer"].split(",")]
                if all(ca in user_answers for ca in correct_answers):
                    correct = True

            if correct:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}\n")

    print(f"\n🏆 Final Score for {player_name}: {score} (Attempt {attempt})\n")
    rankings.append((player_name, attempt, score, score))

    print("📊 Current Rankings:")
    for r in rankings:
        print(f"{r[0]} - Attempt {r[1]}: {r[2]}")
    print("\n")
    return True


def main():
    attempt = 1
    print("\n🎨 Welcome to the Art Quiz! 🎨")
    name = input("Enter your name: ").strip() or "Player"

    while True:
        print("\nAvailable topics:")
        for t in quiz_data.keys():
            print(" -", t)
        topic = input("Choose a topic: ").strip()

        if attempt == 1:
            ready = input("Are you ready to take the quiz? (yes/no): ").strip().lower()
            if ready != "yes":
                print("Okay — maybe next time!")
                break

        keep_playing = play_quiz(name, topic, attempt)
        if not keep_playing:
            break

        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("👋 Thanks for playing the Art Quiz! Goodbye!")
            break

        attempt += 1


if __name__ == "__main__":
    main()