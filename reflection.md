# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---
- The game asked me to enter a guess with a button to submit guess and another button to create a new game. It also showed developer debug info to help me test the output it was giving, which showed me the game was quite buggy because for instance some of the first bugs I saw were that the hints were opposite of what they should have been and history list was not reset for new game sessions.
- After I submit a guess, it gives me the opposite of what a correct hint would be. For example, I guessed 21 and the AI told me to guess lower even though the secret was 28. I guessed 50 and the AI told me to guess higher instead of lower like it should have.
- When I select a new game, it doesn’t reset the history. I expected it to reset the history so it could record the guesses only for that game session but it didn’t.
- When the user switches to hard mode, the range of numbers changes from 1 to 50 compared to 1 to 100 for normal. When switching to hard mode, it should have increased the options available therefore increasing the range but it actually decreased it, making hard mode easier than normal mode.


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- I used Copilot. 
- One example of an AI suggestion that was correct was that it suggested creating a variable that holds an empty array and putting that inside the "if new_game" condition in order to fix the history not being reset when the user selects a new game. The fix works because it resets the recorded numbers to an empty history list when a new game is created so when numbers are added, it only adds the numbers from that game session. I verified the result by adding the code and running the game again, which allowed me to see the history being reset in the developer debug info. 
- One example of an AI suggestion that was incorrect was in the tests when it checked an outcome string for check_guess() when check_guess() is actually supposed to return a tuple of (outcome, message). I verified the result by running the tests and seeing there was an AssertionError because check_guess() was returning a String instead of a tuple.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

I decided whether a bug was really fixed by checking the new output in the updated program and running tests on it to verify it was working properly. For the bug where it didn't reset the history upon starting a new game, one manual test I ran was running the app, making several guesses and checking that they were all recorded in the history list ([25,50,75]), clicking the New Game button, and checking that the Developer Debug info did reset the history list to [] and that once I added numbers, it only recorded numbers from that new game session ([80,90,100]). This showed me that my code was properly resetting the history list upon the user creating a new game session. Yes, AI helped me understand how to write the corresponding pytest by helping me learn how to use asserts since I am not too familiar with it. For the bug where it was giving incorrect hints, I fixed it by changing the string in the case where "guess > secret" to say "Go Lower" instead of "Go Higher" and in the else case to say "Go Higher" instead of "Go Lower." This fixed the bug because the issue was simply that the wrong string was being output based on the condition. One manual test I ran was running the program again and guessing below and above the secret to check the program was telling me to guess higher when I guessed too low and to guess lower when I guessed too high. I also tested that it still worked properly after different game sessions. This showed me that the code succesfully output the correct hint string based on whether the user's guess was lower/higher than the secret. Yes, I also used AI to help me understand how to write the corresponding pytest by helping me use the asserts keyword.  

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
