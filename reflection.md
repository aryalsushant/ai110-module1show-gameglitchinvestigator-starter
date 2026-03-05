# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It is a simple interface. The game prompted me to guess a number between 1 and 100. It also has a developer debug info drop-down which shows information like secret, attempts, score, etc.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  1. I noticed that when the "show hint" button is toggled on, the hint says go lower even when the number I entered is 1, which is the lowest number in the range
  2. The "new game" button does not really work. When I click new game, enter a number and submit, it keeps showing the message "You already won. Start a new game to play again."
  3. I noticed that when I entered 9 and the secret was 11, the hint still told me to go higher. When I entered 12, it told me to go lower. The hint logic is probably random or broken. 1 and 3 could potentially be the same bug, Hence, I will try to find another bug to match the assignment requirement of 3 bugs.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- I used Claude Code, by adding the Claude code extension on VScode

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

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
