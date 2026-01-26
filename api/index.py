import sys
import os

# Add the parent directory to sys.path so we can import 'api' from root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend import app

# This is the entry point for Vercel serverless functions
