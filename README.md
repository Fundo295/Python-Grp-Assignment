# 🐾 Ginger the Virtual Cat

Welcome to **Ginger the Virtual Cat**, a fun and interactive digital pet built with Python and Object-Oriented Programming! 🎉

Ginger is more than just a cat — she's a cuddly, trick-learning, laser-pointer-chasing ball of fluff who responds to your care and attention.

## 🧠 Features

- Track Ginger’s **hunger**, **energy**, and **happiness**
- Feed her, let her sleep, or play to boost her mood
- Teach her **new tricks** like `"sit"` and `"roll over"`
- Have her **perform tricks** she’s learned!
- Print Ginger’s current status anytime

## 🐱 Class Overview

### `Pet` Class Attributes:
- `name`: Name of the pet (e.g., "Ginger")
- `hunger`: Ranges from 0 (full) to 10 (starving)
- `energy`: Ranges from 0 (tired) to 10 (fully rested)
- `happiness`: Ranges from 0 (sad) to 10 (very happy)
- `tricks`: List of tricks the pet has learned

### Methods:
- `eat()`: Lowers hunger, raises happiness
- `sleep()`: Restores energy
- `play()`: Increases happiness, drains energy and adds hunger
- `train(trick)`: Teaches Ginger a new trick
- `do_trick(trick)`: Has Ginger perform a learned trick
- `show_tricks()`: Lists all learned tricks
- `get_status()`: Displays current hunger, energy, and happiness
