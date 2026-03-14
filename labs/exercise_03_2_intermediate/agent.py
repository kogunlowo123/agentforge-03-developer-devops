"""AgentForge Exercise 03.2 — Developer & DevOps Agents (intermediate)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from core.agent_base import AgentBase

def main():
    agent = AgentBase(name="ex-03-2", instruction="You are a Developer & DevOps Agents agent.")
    print(f"Exercise 03.2 ready: {agent.name}")

if __name__ == "__main__":
    main()
