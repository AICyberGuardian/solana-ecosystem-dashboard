#!/usr/bin/env python3
"""
Solana Ecosystem Auto-Updating Report & Interactive Bento Dashboard
Root execution entrypoint.
"""
import sys
from pathlib import Path

# Ensure package root is in sys.path
sys.path.insert(0, str(Path(__file__).parent.resolve()))

from src.cli import main

if __name__ == "__main__":
    main()
