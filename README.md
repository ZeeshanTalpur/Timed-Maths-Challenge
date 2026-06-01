  ➕ Timed Maths Challenge

A 60-second math game with three difficulty levels, real-time countdown, and a persistent scoreboard — all in the terminal.

   📋 About

Race against the clock to answer as many math problems as possible in 60 seconds! The game supports addition, subtraction, multiplication, and division. Your score gets saved to a local scoreboard file after every game.

   ⚙️ How It Works

- Enter your name and pick a difficulty level
-   Easy:   Numbers between 2–10
-   Medium:   Numbers between 5–20
-   Difficult:   Numbers between 10–30
- A random expression is generated every round using `+`, `-`, `*`, or `/`
- The timer counts down from 60 seconds in real time
- Your score and difficulty are saved to `scoreboard.txt` at the end

   🚀 How to Run

```bash
python math_challenge.py
```

   🛠️ Built With

- Python 3
- `random`, `os`, `time` modules
- File I/O (`scoreboard.txt`)

   📁 File Structure

```
Timed-Maths-Challenge/
├── math_challenge.py
└── scorebaord.txt
```

   💡 Concepts Used

- Real-time timer with `time.time()`
- Global variables
- File I/O (appending scores)
- Difficulty modes
- Floating-point answer tolerance (`abs(answer - correct) < 0.1`)

---
 Part of my Python beginner projects series 🐍 
