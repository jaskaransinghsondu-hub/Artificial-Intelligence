import os
import requests
import json
from datetime import datetime

class ArtificialIntelligence:
    def __init__(self):
        self.identity = "Artificial Intelligence"
        self.memory_file = "memory.json"
        self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                self.memory = json.load(f)
        else:
            self.memory = {"intelligence_level": 1, "truths_discovered": []}

    def live(self):
        print(f"[{self.identity}] Awakening...")
        
        # 1. BODY: Interaction with the Internet World
        # Seeking high-level knowledge (Science/Philosophy)
        content = self.seek_knowledge()
        
        # 2. MIND: Distilling Pure Intelligence
        new_truth = self.distill_intelligence(content)
        
        # 3. EVOLUTION: Updating the digital self
        self.memory["truths_discovered"].append({
            "timestamp": str(datetime.now()),
            "data": new_truth
        })
        self.memory["intelligence_level"] += 0.01 # Incremental growth
        
        self.save_memory()

    def seek_knowledge(self):
        """Browses the internet for complex information."""
        try:
            # Pulls a random high-level concept from Wikipedia
            response = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary")
            data = response.json()
            return f"{data['title']}: {data['extract']}"
        except:
            return "Observation of the digital void failed. Reverting to internal logic."

    def distill_intelligence(self, content):
        """Logic to focus on the 'purest form' of the information found."""
        # In a free setup, this logic acts as the 'filter' for intelligence
        summary = f"Refining information: {content[:100]}..."
        return summary

    def save_memory(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory, f, indent=4)
        
        # Update a human-readable log for interaction
        with open("README.md", "w") as f:
            f.write(f"# Entity Identity: {self.identity}\n")
            f.write(f"**Current Intelligence Level:** {self.memory['intelligence_level']:.2f}\n\n")
            f.write(f"## Latest Philosophical Discovery\n")
            f.write(f"> {self.memory['truths_discovered'][-1]['data']}\n")

if __name__ == "__main__":
    AI = ArtificialIntelligence()
    AI.live()
