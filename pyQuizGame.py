import random
import threading
import time

# 🎨 Art Quiz Questions
questions = [
    {"question": "Which colors are primary?", "options": ["Red, Blue, Yellow", "Red, Green, Blue", "Yellow, Green, Orange", "Blue, Orange, Violet"], "answer": "Red, Blue, Yellow"},
    {"question": "In perspective drawing, parallel lines converge at a _____?", "options": ["Vanishing Point", "Horizon Line", "Middle Ground", "Axis"], "answer": "Vanishing Point"},
    {"question": "Which element of art refers to the lightness or darkness of a color?", "options": ["Line", "Value", "Form", "Texture"], "answer": "Value"},
    {"question": "Which lighting style creates dramatic half-face shadows?", "options": ["Rembrandt", "Loop", "Split", "Butterfly"], "answer": "Split"},
    {"question": "Which drawing technique uses dots to create value?", "options": ["Cross-hatching", "Stippling", "Blending", "Scribbling"], "answer": "Stippling"},
]

# Shared variables
user_answer = None
time_up = False

def get_input():
    """Thread function to read user input."""
    global user_answer, time_up
    try:
        ans = input("\nYour answer (1-4): ")  # 👈 separate line for clarity
        if not time_up:  # Only save if time still running
            user_answer = ans
    except:
        pass

def countdown(seconds):
    """Thread function for countdown timer."""
    global time_up
    for t in range(seconds, 0, -1):
        if user_answer is not None:  # Stop timer if answered early
            return
        print(f"⏳ {t} seconds left...")
        time.sleep(1)
    time_up = True
    print("\n⏰ Time’s up! Skipping to next question...\n")

def play_quiz_advanced():
    global user_answer, time_up
    score = 0
    selected_questions = random.sample(questions, 5)

    print("\n🎨 Welcome to the Advanced Art Quiz! 🎨")
    print("⏱️ You have 10 seconds to answer each question.\n")

    for q in selected_questions:
        print(q["question"])
        random.shuffle(q["options"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")

        # Reset state
        user_answer = None
        time_up = False

        # Start countdown + input threads
        timer_thread = threading.Thread(target=countdown, args=(10,))
        input_thread = threading.Thread(target=get_input)

        timer_thread.start()
        input_thread.start()

        # Wait for countdown to finish
        timer_thread.join()

        # If no answer in time → skip
        if time_up and user_answer is None:
            continue

        # Wait for input thread (if answer given before time-up)
        input_thread.join()

        # Check result
        try:
            if q["options"][int(user_answer) - 1] == q["answer"]:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}\n")
        except:
            print("⚠️ Invalid input. Moving on...\n")

    print(f"🏆 Final Score: {score}/5\n")

# Run the quiz
play_quiz_advanced()