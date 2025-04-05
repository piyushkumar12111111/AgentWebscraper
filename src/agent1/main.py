#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

# Use relative import instead of absolute import
from crew import Agent1  # Changed from 'agent1.crew import Agent1'

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'gamp.gg',
        'current_year': str(datetime.now().year)
    }
    
    try:
        Agent1().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()