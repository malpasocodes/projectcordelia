#!/usr/bin/env python3
"""Debug text extraction to see what's causing word-per-line display."""

from pathlib import Path
from parser import TEIParser

def debug_text():
    # Load play
    xml_path = Path("data/king-lear_TEIsimple_FolgerShakespeare.xml")
    parser = TEIParser(xml_path)
    play = parser.parse()
    
    # Get Act 1, Scene 1
    act1 = play.get_act("1")
    scene1 = act1.get_scene("1")
    
    print("=== Debug Text Extraction ===")
    
    # Look at raw content
    print("\nFirst 5 content items (raw):")
    for i, item in enumerate(scene1.content[:5]):
        print(f"{i+1}. Type: {item['type']}")
        print(f"   Text: {repr(item['text'])}")
        print(f"   Length: {len(item['text'])}")
        print()
    
    # Look at formatted content
    formatted = scene1.get_formatted_content()
    lines = formatted.split('\n')
    
    print(f"Total formatted lines: {len(lines)}")
    print("\nFirst 20 formatted lines:")
    for i, line in enumerate(lines[:20]):
        print(f"{i+1:2d}. {repr(line)}")
    
    # Check for specific issues
    print(f"\nFormatted content length: {len(formatted)}")
    print(f"Number of newlines: {formatted.count(chr(10))}")
    print(f"Number of spaces: {formatted.count(' ')}")

if __name__ == "__main__":
    debug_text()