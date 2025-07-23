#!/usr/bin/env python3
"""Test the text formatting functionality."""

from pathlib import Path
from parser import TEIParser

def test_formatting():
    # Parse the King Lear XML
    xml_path = Path("data/king-lear_TEIsimple_FolgerShakespeare.xml")
    parser = TEIParser(xml_path)
    play = parser.parse()
    
    # Test formatting for Act 1, Scene 1
    act1 = play.get_act("1")
    if act1:
        scene1 = act1.get_scene("1")
        if scene1:
            print(f"=== {scene1.title} ===\n")
            formatted_content = scene1.get_formatted_content()
            
            # Print first 50 lines to see formatting
            lines = formatted_content.split('\n')
            for i, line in enumerate(lines[:50]):
                print(line)
            
            print(f"\n... (showing first 50 lines of {len(lines)} total)")
            
            # Also test the parser's format method
            print("\n\n=== Testing parser._format_scene_content() ===\n")
            formatted_by_parser = parser._format_scene_content(scene1.content[:10])
            print(formatted_by_parser)

if __name__ == "__main__":
    test_formatting()