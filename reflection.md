# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It is a simple interface. The game prompted me to guess a number between 1 and 100. It also has a developer debug info drop-down which shows information like secret, attempts, score, etc.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  1. I noticed that when the "show hint" button is toggled on, the hint says go lower even when the number I entered is 1, which is the lowest number in the range
  2. The "new game" button does not really work. When I click new game, enter a number and submit, it keeps showing the message "You already won. Start a new game to play again."
  3. I noticed that when I entered 9 and the secret was 11, the hint still told me to go higher. When I entered 12, it told me to go lower. The hint logic is probably random or broken. 1 and 3 could potentially be the same bug,

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- I used Claude Code, by adding the Claude code extension on VScode

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- One example of an AI suggestion that was correct was the messages are swapped in app.py lines 38-40. If the guess is too high, the hint should tell us to go lower. Instead it says go higher and vice versa. I verified this by checking lines 38-40 in app.py, and the hint message is indeed opposite of what it should be. The outcome label (too high, too low)is correct, but the player-facing message is inverted.


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
- One of the errors was that on every even numbered attempt, the secret is passed as a string to check_guess. Claude code suggested me to fix this by removing the "if attempts % 2 ==0" block entirely. However, when this entire if-else block is removed, the variable name secret is not defined anymore. I tested this by commenting out the block that Claude code asked me to get rid of, then running my app in streamlit and submitting a guess which gave an error message "NameError: name 'secret' is not defined". This is lines 158-163 in app.py

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I decided a bug was really fixed when I could reproduce the original broken behavior, apply the fix, and then confirm the broken behavior no longer occurred. For the "new game" bug, I manually clicked New Game after winning, submitted a guess, and verified the game actually accepted it instead of immediately showing "You already won." Seeing the game respond normally was my confirmation the fix worked.

- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
  I added a pytest regression test called `test_new_game_resets_status` in `tests/test_game_logic.py`. The test simulates a session state dict with `status` set to `"won"`, applies the new_game reset logic, and asserts that `status` becomes `"playing"`, `attempts` resets to `0`, and `history` is cleared. Running `pytest` confirmed all assertions passed, which showed me that the reset logic was complete and not missing any fields. Before the fix, the test would have failed because `status` was never updated.

- Did AI help you design or understand any tests? How?
  Yes — I asked Claude Code to both fix the bug and write a test for it. Claude identified that the root cause was `st.session_state.status` never being reset to `"playing"` in the new_game handler, and then designed a test that simulated the session state as a plain dictionary to verify the reset logic without needing to spin up Streamlit. This helped me understand that you can test Streamlit app logic by isolating the state manipulation into something a unit test can check directly, without needing a real browser or session.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
