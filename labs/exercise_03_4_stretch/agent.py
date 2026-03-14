"""AgentForge Exercise 03.4 — Developer & DevOps Agents (stretch)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from core.agent_base import AgentBase

def main():
    agent = AgentBase(name="ex-03-4", instruction="You are a Developer & DevOps Agents agent.")
    print(f"Exercise 03.4 ready: {agent.name}")

if __name__ == "__main__":
    main()
