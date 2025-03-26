#!/usr/bin/env python
import sys
import warnings
from crew import AiNews
from dotenv import load_dotenv
load_dotenv()
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
        'topic': 'AI LLMs'
    }
    AiNews().crew().kickoff(inputs=inputs)


run()

#C:\Users\Hamza\Desktop\News Scraper agent\ai_news\src\ai_news\main.py