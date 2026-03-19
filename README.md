# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The game's purpose is to allow the user to play a game where they guess the secret number. The program gives them hints based on whether their guesses are lower or higher than the secret number. The user wins when they guess the correct number. 
- [ ] Detail which bugs you found.
- One bug I investigated was that after submitting a hint, the program gave the opposite of what the hint should have been. For example, when the guess was higher than secret, the game gave a hint to incorrectly go higher instead of lower and vice versa. Another bug I investigated was that the history of guesses was not being reset when the user created a new game so the record of guesses per game session was not correct.
- [ ] Explain what fixes you applied.
- [ ] To fix the incorrect hint output, I modified the output string for the condition where "guess > secret" to tell the user to "go lower" instead of "go higher" and modified the else case to tell the user to "go higher" instead of "go lower" when they guess less than secret. To fix the history of guesses not being reset, I applied creating an empty history list when "if new_game" ran so that each time a new game session was started, the list of recorded numbers would only hold the values for that session. Additionally, I applied refactoring check_guess and parse_guess into logic_utils.py.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

<img width="551" height="417" alt="Screenshot 2026-03-19 185243" src="https://github.com/user-attachments/assets/665d15e7-d6d8-4cf9-8524-777d65c3c2bb" />


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
