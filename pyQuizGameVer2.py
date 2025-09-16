import random
import threading
import time
from inputimeout import inputimeout, TimeoutOccurred

# 🎨 Art Quiz Questions
questions = [
    {"question": "Which colors are primary?", "options": ["Red, Blue, Yellow", "Red, Green, Blue", "Yellow, Green, Orange", "Blue, Orange, Violet"], "answer": "Red, Blue, Yellow"},
    {"question": "In perspective drawing, parallel lines converge at a _____?", "options": ["Vanishing Point", "Horizon Line", "Middle Ground", "Axis"], "answer": "Vanishing Point"},
    {"question": "Which element of art refers to the lightness or darkness of a color?", "options": ["Line", "Value", "Form", "Texture"], "answer": "Value"},
    {"question": "Which lighting style creates dramatic half-face shadows?", "options": ["Rembrandt", "Loop", "Split", "Butterfly"], "answer": "Split"},
    {"question": "Which drawing technique uses dots to create value?", "options": ["Cross-hatching", "Stippling", "Blending", "Scribbling"], "answer": "Stippling"},
]

# Shared state
stop_countdown = False
rankings = []  # Store (name, attempt, score)

def show_countdown(seconds):
    """Countdown timer shown next to the input prompt (your original style)."""
    global stop_countdown
    for t in range(seconds, 0, -1):
        if stop_countdown:
            return
        print(f"\r⏳ {t} seconds left...   ", end="Your Answer: ", flush=True)
        time.sleep(1)
    if not stop_countdown:
        print("\r⏰ Time’s up! Skipping to next question...   ")

def play_quiz_advanced(player_name, difficulty, attempt):
    global stop_countdown
    score = 0
    selected_questions = random.sample(questions, 5)

    print(f"\n🎨 Welcome {player_name}! Difficulty: {difficulty.capitalize()} | Attempt {attempt}")
    print("⏱️ You have 10 seconds to answer each question. Answer in Numbers indicated in the choices\n")

    for q in selected_questions:
        print("\n" + q["question"])
        random.shuffle(q["options"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")

        # Reset countdown
        stop_countdown = False

        # Print input prompt first
        print("Your answer (1-4): ", end="", flush=True)

        # Start countdown thread
        timer_thread = threading.Thread(target=show_countdown, args=(10,))
        timer_thread.daemon = True
        timer_thread.start()

        try:
            ans = inputimeout(prompt="", timeout=10)  # 👈 empty prompt, input on same line
            stop_countdown = True

            if q["options"][int(ans) - 1] == q["answer"]:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}\n")

        except TimeoutOccurred:
            stop_countdown = True
            print("\n⏰ You didn’t answer in time!\n")
        except:
            stop_countdown = True
            print("⚠️ Invalid input. Moving on...\n")

        timer_thread.join()

    print(f"\n🏆 Final Score for {player_name}: {score}/5 (Attempt {attempt})\n")
    rankings.append((player_name, attempt, score))

    # Show updated ranking after attempt
    print("📊 Current Rankings:")
    for r in rankings:
        print(f"{r[0]} - Attempt {r[1]}: {r[2]}/5")
    print("\n")

# -------------------------------
# Main Game Loop
# -------------------------------
def main():
    attempt = 1

    print("\n🎨 Welcome to the Art Quiz! 🎨")
    name = input("Enter your name: ")

    while True:
        # Difficulty asked every attempt
        difficulty = input("Choose difficulty (easy, medium, hard, difficult): ").lower()

        # Only ask "ready?" in the first attempt
        if attempt == 1:
            ready = input("Are you ready to take the quiz? (yes/no): ").lower()
            if ready != "yes":
                print("Okay, maybe next time!")
                break

        # Run quiz
        play_quiz_advanced(name, difficulty, attempt)

        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thanks for playing the Art Quiz! Goodbye!")
            break

        attempt += 1

# Run it
main()