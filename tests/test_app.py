#!/usr/bin/env python3
"""Test the basic app functionality."""

from pathlib import Path
from parser import TEIParser

def test_app_components():
    # Test that we can load the play
    xml_path = Path("data/king-lear_TEIsimple_FolgerShakespeare.xml")
    parser = TEIParser(xml_path)
    play = parser.parse()
    
    print(f"✓ Play loaded: {play.title}")
    print(f"✓ Acts: {play.get_act_count()}")
    print(f"✓ Total scenes: {play.get_total_scenes()}")
    
    # Test that the load_play function from app works
    try:
        from app import load_play
        cached_play = load_play()
        print(f"✓ Cached play loaded: {cached_play.title}")
        print(f"✓ Matches original: {cached_play.title == play.title}")
    except Exception as e:
        print(f"✗ Error loading cached play: {e}")

if __name__ == "__main__":
    test_app_components()