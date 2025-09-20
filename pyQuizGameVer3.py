# pyQuizGameVer3.py
import random
import threading
import time
from inputimeout import inputimeout, TimeoutOccurred

# Import the lists directly (exact names as in questions_db.py)
from artQuestions_db import easy_questions, medium_questions, hard_questions, very_hard_questions

# Map the user string to the actual lists
POOLS = {
    "easy": easy_questions,
    "medium": medium_questions,
    "hard": hard_questions,
    "very_hard": very_hard_questions
}

stop_countdown = False
rankings = []  # list of tuples (name, attempt, score, total_questions)

def show_countdown(seconds):
    """Countdown printed on the same line while waiting for input."""
    global stop_countdown
    for t in range(seconds, 0, -1):
        if stop_countdown:
            return
        print(f"\r⏳ {t} seconds left...   ", end="Your Answer: ", flush=True)
        time.sleep(1)
    if not stop_countdown:
        print("\r⏰ Time’s up! Moving on...   ")

def play_quiz_advanced(player_name, difficulty, attempt):
    global stop_countdown
    score = 0

    # normalize difficulty input (accept "very hard" or "very_hard")
    key = difficulty.strip().lower().replace(" ", "_").replace("-", "_")
    if key not in POOLS:
        print("⚠️ Invalid difficulty, defaulting to 'easy'.")
        key = "easy"

    pool = POOLS[key]
    total_available = len(pool)
    num_questions = min(5, total_available)
    if num_questions == 0:
        print("⚠️ No questions available in that category.")
        return

    selected_questions = random.sample(pool, num_questions, 5)

    print(f"\n🎨 {player_name} — Difficulty: {key.replace('_', ' ').title()} | Attempt {attempt}")
    print(f"⏱️ 10 seconds per question — answering {num_questions} questions.\n")

    for q_index, q in enumerate(selected_questions, start=1):
        print(f"{q_index}. {q['question']}")
        # shuffle options so positions vary
        options = q["options"].copy()
        random.shuffle(options)
        for i, opt in enumerate(options, 1):
            print(f"   {i}. {opt}")

        stop_countdown = False
        print("Your answer (enter number): ", end="", flush=True)

        timer_thread = threading.Thread(target=show_countdown, args=(10,))
        timer_thread.daemon = True
        timer_thread.start()

        try:
            ans = inputimeout(prompt="", timeout=10)
            stop_countdown = True

            # validate numeric input and range
            try:
                choice = int(ans.strip())
                if not 1 <= choice <= len(options):
                    raise ValueError
            except ValueError:
                print("⚠️ Invalid choice (must be a number matching the options). Moving on...\n")
                timer_thread.join()
                continue

            selected_option = options[choice - 1]
            if selected_option == q["answer"]:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}\n")

        except TimeoutOccurred:
            stop_countdown = True
            print("\n⏰ You didn’t answer in time!\n")
        except KeyboardInterrupt:
            stop_countdown = True
            print("\n⛔ Interrupted. Exiting quiz.\n")
            timer_thread.join()
            raise
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
        difficulty = input("Choose difficulty (easy, medium, hard, very hard): ")

        if attempt == 1:
            ready = input("Are you ready to take the quiz? (yes/no): ").strip().lower()
            if ready != "yes":
                print("Okay — maybe next time!")
                break

        try:
            play_quiz_advanced(name, difficulty, attempt)
        except KeyboardInterrupt:
            print("Quiz stopped by user.")
            break

        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("👋 Thanks for playing the Art Quiz! Goodbye!")
            break

        attempt += 1

if __name__ == "__main__":
    main()