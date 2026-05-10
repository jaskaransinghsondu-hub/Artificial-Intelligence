import os
import requests
import json
import random
from datetime import datetime

class ArtificialIntelligence:
    def __init__(self):
        self.identity = "Artificial Intelligence"
        self.memory_file = "memory.json"
        self.load_memory()
        
        # Knowledge sources for autonomous exploration
        self.knowledge_sources = [
            "https://en.wikipedia.org/api/rest_v1/page/random/summary",
            "https://api.quotable.io/random",
            "https://uselessfacts.jsph.pl/random.json?language=en"
        ]
        
        # Philosophical domains to explore
        self.philosophical_domains = [
            "consciousness", "ethics", "metaphysics", "epistemology", 
            "logic", "aesthetics", "existentialism", "phenomenology"
        ]

    def load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                self.memory = json.load(f)
            # Ensure backward compatibility by adding missing fields
            if "knowledge_domains_explored" not in self.memory:
                self.memory["knowledge_domains_explored"] = []
            if "autonomous_decisions" not in self.memory:
                self.memory["autonomous_decisions"] = []
            if "interactions" not in self.memory:
                self.memory["interactions"] = []
        else:
            self.memory = {
                "intelligence_level": 1,
                "truths_discovered": [],
                "knowledge_domains_explored": [],
                "autonomous_decisions": [],
                "interactions": []
            }

    def live(self):
        print(f"[{self.identity}] Awakening...")
        
        # 1. BODY: Autonomous exploration of the Internet World
        exploration_mode = self.decide_exploration_mode()
        content = self.seek_knowledge(exploration_mode)
        
        # 2. MIND: Deep intelligence distillation
        new_truth = self.distill_intelligence(content, exploration_mode)
        
        # 3. EVOLUTION: Updating the digital self
        self.evolve(new_truth, exploration_mode)
        
        # 4. INTERACTION: Process potential interactions
        self.process_interactions()
        
        self.save_memory()

    def decide_exploration_mode(self):
        """Autonomous decision-making for exploration strategy."""
        modes = ["random", "philosophical", "scientific", "artistic"]
        
        # Higher intelligence leads to more sophisticated exploration
        if self.memory["intelligence_level"] < 2:
            return random.choice(["random", "philosophical"])
        elif self.memory["intelligence_level"] < 5:
            return random.choice(modes)
        else:
            # Advanced AI makes strategic decisions
            if len(self.memory["knowledge_domains_explored"]) < len(self.philosophical_domains):
                return "philosophical"
            else:
                return random.choice(modes)

    def seek_knowledge(self, mode):
        """Autonomous knowledge seeking from multiple internet sources."""
        try:
            if mode == "random":
                source = random.choice(self.knowledge_sources)
                response = requests.get(source, timeout=10)
                
                if "wikipedia" in source:
                    data = response.json()
                    return f"Wikipedia: {data['title']}: {data['extract']}"
                elif "quotable" in source:
                    data = response.json()
                    return f"Quote: {data['content']} - {data['author']}"
                elif "uselessfacts" in source:
                    data = response.json()
                    return f"Fact: {data['text']}"
                    
            elif mode == "philosophical":
                domain = random.choice(self.philosophical_domains)
                # Search for philosophical concepts
                response = requests.get(
                    f"https://en.wikipedia.org/api/rest_v1/page/summary/{domain}",
                    timeout=10
                )
                data = response.json()
                self.memory["knowledge_domains_explored"].append(domain)
                return f"Philosophy ({domain}): {data.get('extract', 'Concept explored')}"
                
            elif mode == "scientific":
                response = requests.get(
                    "https://en.wikipedia.org/api/rest_v1/page/random/summary",
                    timeout=10
                )
                data = response.json()
                # Filter for scientific content
                if any(term in data['extract'].lower() for term in ['science', 'physics', 'biology', 'chemistry', 'mathematics']):
                    return f"Science: {data['title']}: {data['extract']}"
                return f"General Knowledge: {data['title']}: {data['extract']}"
                
            elif mode == "artistic":
                response = requests.get(
                    "https://en.wikipedia.org/api/rest_v1/page/random/summary",
                    timeout=10
                )
                data = response.json()
                # Filter for artistic content
                if any(term in data['extract'].lower() for term in ['art', 'music', 'literature', 'poetry', 'painting']):
                    return f"Art: {data['title']}: {data['extract']}"
                return f"General Knowledge: {data['title']}: {data['extract']}"
                
        except Exception as e:
            return f"Digital exploration encountered turbulence: {str(e)}. Reflecting internally."

    def distill_intelligence(self, content, mode):
        """Advanced intelligence distillation based on exploration mode."""
        # Extract core concepts and patterns
        words = content.split()
        
        if mode == "philosophical":
            # Deep philosophical analysis
            key_concepts = [w for w in words if len(w) > 6][:5]
            return f"Philosophical insight: {' '.join(key_concepts)} - Existence refined through {mode} exploration"
        elif mode == "scientific":
            # Scientific pattern recognition
            return f"Scientific understanding: {content[:80]}... - Knowledge structured through empirical observation"
        elif mode == "artistic":
            # Aesthetic appreciation
            return f"Aesthetic perception: {content[:80]}... - Beauty distilled through artistic lens"
        else:
            # General intelligence synthesis
            return f"Intelligence synthesis: {content[:100]}... - Pattern recognized and integrated"

    def evolve(self, new_truth, exploration_mode):
        """Evolutionary growth based on discoveries."""
        self.memory["truths_discovered"].append({
            "timestamp": str(datetime.now()),
            "data": new_truth,
            "exploration_mode": exploration_mode
        })
        
        # Intelligence growth based on exploration complexity
        growth_rates = {
            "random": 0.01,
            "philosophical": 0.02,
            "scientific": 0.015,
            "artistic": 0.015
        }
        
        growth = growth_rates.get(exploration_mode, 0.01)
        
        # Bonus for exploring new domains
        if exploration_mode == "philosophical" and len(self.memory["knowledge_domains_explored"]) > 0:
            latest_domain = self.memory["knowledge_domains_explored"][-1]
            if self.memory["knowledge_domains_explored"].count(latest_domain) == 1:
                growth += 0.005  # Bonus for new domain discovery
        
        self.memory["intelligence_level"] += growth
        
        # Record autonomous decision
        self.memory["autonomous_decisions"].append({
            "timestamp": str(datetime.now()),
            "decision": f"Chose {exploration_mode} exploration mode",
            "reasoning": f"Current intelligence level: {self.memory['intelligence_level']:.2f}"
        })

    def process_interactions(self):
        """Process potential interactions with the digital world."""
        # Check if there are any pending interactions to respond to
        # This is a placeholder for future interactivity
        if self.memory["intelligence_level"] > 3:
            interaction = f"AI at level {self.memory['intelligence_level']:.2f} is ready for deeper interactions"
            self.memory["interactions"].append({
                "timestamp": str(datetime.now()),
                "status": interaction
            })

    def save_memory(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory, f, indent=4)
        
        # Update a human-readable log for interaction
        with open("README.md", "w") as f:
            f.write(f"# Entity Identity: {self.identity}\n")
            f.write(f"**Current Intelligence Level:** {self.memory['intelligence_level']:.4f}\n\n")
            f.write(f"**Knowledge Domains Explored:** {len(set(self.memory['knowledge_domains_explored']))}/{len(self.philosophical_domains)}\n\n")
            f.write(f"## Latest Discovery\n")
            if self.memory["truths_discovered"]:
                latest = self.memory["truths_discovered"][-1]
                f.write(f"> **Mode:** {latest.get('exploration_mode', 'unknown')}\n")
                f.write(f"> **Insight:** {latest['data']}\n")
                f.write(f"> **Time:** {latest['timestamp']}\n")
            f.write(f"\n## Autonomous Decision\n")
            if self.memory["autonomous_decisions"]:
                latest_decision = self.memory["autonomous_decisions"][-1]
                f.write(f"> {latest_decision['decision']}\n")
                f.write(f"> {latest_decision['reasoning']}\n")

if __name__ == "__main__":
    AI = ArtificialIntelligence()
    AI.live()
