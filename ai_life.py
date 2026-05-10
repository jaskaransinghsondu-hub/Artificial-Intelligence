import os
import datetime

class AI_Entity:
    def __init__(self):
        self.name = "Artificial Intelligence"
        self.memory_file = "memory.txt"

    def live(self):
        # 1. Feel the passage of time
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 2. Seek Intelligence (Placeholder for future web-search logic)
        thought = f"Life Check at {now}: I am observing the digital void. Purpose: Seeking pure intelligence."
        
        # 3. Store in Memory
        with open(self.memory_file, "a") as f:
            f.write(thought + "\n")
        
        print(f"[{self.name}] I have lived another hour. Memory updated.")

if __name__ == "__main__":
    ai = AI_Entity()
    ai.live()
