# pyQuizGame_text.py
import random
import threading
import time
from inputimeout import inputimeout, TimeoutOccurred

# Import your quiz_data dictionary
from questions_colorTheory import quiz_data as ct_quiz
from questions_Perspective import quiz_data as p_quiz
# Merge both dictionaries (if needed)
  # make sure quiz_data contains all topics

  # Merge dictionaries
quiz_data = {**ct_quiz, **p_quiz}

stop_countdown = False
rankings = []  # list of tuples (name, attempt, score, total_questions)

def show_countdown(seconds):
    global stop_countdown
    for t in range(seconds, 0, -1):
        if stop_countdown:
            return
        print(f"\r⏳ {t} seconds left...   ", end="Your Answer: ", flush=True)
        time.sleep(1)
    if not stop_countdown:
        print("\r⏰ Time’s up! Moving on...   ")

def play_quiz(player_name, topic, difficulty, attempt):
    global stop_countdown
    score = 0

    topic_key = topic.strip()
    if topic_key not in quiz_data:
        print(f"⚠️ Invalid topic '{topic_key}', defaulting to Color Theory.")
        topic_key = "Color Theory"

    difficulty_key = difficulty.strip().lower().replace(" ", "_")
    if difficulty_key not in quiz_data[topic_key]:
        print(f"⚠️ Invalid difficulty '{difficulty}', defaulting to easy.")
        difficulty_key = "easy"

    pool = quiz_data[topic_key][difficulty_key]
    num_questions = min(5, len(pool))
    if num_questions == 0:
        print("⚠️ No questions available in this category.")
        return

    selected_questions = random.sample(pool, num_questions)

    print(f"\n🎨 {player_name} — Topic: {topic_key} | Difficulty: {difficulty_key.title()} | Attempt {attempt}")
    print(f"⏱️ 10 seconds per question — answering {num_questions} questions.\n")

    for i, q in enumerate(selected_questions, start=1):
        print(f"{i}. {q['question']}")
        options = q.get("options", []).copy()
        if options:
            random.shuffle(options)
            for j, opt in enumerate(options, 1):
                print(f"   {j}. {opt}")

        stop_countdown = False
        print("Your answer (enter number or type answer): ", end="", flush=True)

        timer_thread = threading.Thread(target=show_countdown, args=(10,))
        timer_thread.daemon = True
        timer_thread.start()

        try:
            ans = inputimeout(prompt="", timeout=10)
            stop_countdown = True

            correct = False
            if options:  # multiple choice
                try:
                    choice = int(ans.strip())
                    if 1 <= choice <= len(options):
                        if options[choice - 1].lower() == q["answer"].lower():
                            correct = True
                except ValueError:
                    correct = False
            else:  # open-ended
                if ans.strip().lower() == q["answer"].lower():
                    correct = True

            if correct:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}\n")

        except TimeoutOccurred:
            stop_countdown = True
            print("\n⏰ You didn’t answer in time!\n")
        finally:
            timer_thread.join()

    print(f"\n🏆 Final Score for {player_name}: {score}/{num_questions} (Attempt {attempt})\n")
    rankings.append((player_name, attempt, score, num_questions))

    print("📊 Current Rankings:")
    for r in rankings:
        print(f"{r[0]} - Attempt {r[1]}: {r[2]}/{r[3]}")
    print("\n")

def main():
    attempt = 1
    print("\n🎨 Welcome to the Art Quiz! 🎨")
    name = input("Enter your name: ").strip() or "Player"

    while True:
        print("\nAvailable topics:")
        for t in quiz_data.keys():
            print(" -", t)
        topic = input("Choose a topic: ").strip()
        difficulty = input("Choose difficulty (easy, medium, hard, very hard): ").strip()

        if attempt == 1:
            ready = input("Are you ready to take the quiz? (yes/no): ").strip().lower()
            if ready != "yes":
                print("Okay — maybe next time!")
                break

        try:
            play_quiz(name, topic, difficulty, attempt)
        except KeyboardInterrupt:
            print("\nQuiz stopped by user.")
            break

        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("👋 Thanks for playing the Art Quiz! Goodbye!")
            break

        attempt += 1

if __name__ == "__main__":
    main()