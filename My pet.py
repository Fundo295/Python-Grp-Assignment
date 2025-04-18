class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        old_hunger = self.hunger
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food. Hunger: {old_hunger} → {self.hunger}, Happiness: +1")

    def sleep(self):
        old_energy = self.energy
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a cat nap. Energy: {old_energy} → {self.energy}")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} chased a laser pointer! 🐾 Happiness: +2, Energy: -2, Hunger: +1")
        else:
            print(f"{self.name} is too tired to play. Let them rest 😴")

    def get_status(self):
        print(f"🐱 {self.name}'s Status:")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick} 🎉")
        else:
            print(f"{self.name} already knows how to {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def do_trick(self, trick):
        if trick in self.tricks:
            if trick == "roll over":
                print(f"{self.name} rolls over with style! 🌀🐱")
            elif trick == "sit":
                print(f"{self.name} sits down obediently. 🪑😺")
            else:
                print(f"{self.name} performs '{trick}'! ✨")
            self.happiness = min(10, self.happiness + 1)
        else:
            print(f"{self.name} looks confused... they haven’t learned '{trick}' yet!")

# Create your cat named Ginger
ginger = Pet("Ginger")

# Try it out!
ginger.get_status()
ginger.train("sit")
ginger.do_trick("sit")
ginger.play()
ginger.eat()
ginger.sleep()
ginger.get_status()
