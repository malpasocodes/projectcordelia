#!/usr/bin/env python3
"""Test that the text fix works properly."""

from pathlib import Path
from parser import TEIParser

def test_fixed_text():
    # Load play
    xml_path = Path("data/king-lear_TEIsimple_FolgerShakespeare.xml")
    parser = TEIParser(xml_path)
    play = parser.parse()
    
    print("=== Fixed Text Test ===")
    
    # Test Act 1, Scene 1
    act1 = play.get_act("1")
    scene1 = act1.get_scene("1")
    
    print(f"Scene: {scene1.title}")
    print(f"Content items: {len(scene1.content)}")
    
    # Show first 10 content items to verify proper sentence structure
    print("\nFirst 10 content items:")
    for i, item in enumerate(scene1.content[:10]):
        print(f"{i+1:2d}. {item['type'].upper()}: {item['text']}")
    
    # Test formatted content
    formatted = scene1.get_formatted_content()
    lines = formatted.split('\n')
    print(f"\nFormatted content:")
    print(f"Total lines: {len(lines)}")
    print(f"Content length: {len(formatted)} characters")
    
    # Show first 15 formatted lines
    print("\nFirst 15 formatted lines:")
    for i, line in enumerate(lines[:15]):
        if line.strip():  # Only show non-empty lines
            print(f"{i+1:2d}. {line}")
    
    # Test a few other scenes to make sure fix works across all content
    print(f"\n=== Testing Multiple Scenes ===")
    for act_num in ["1", "2", "3"]:
        act = play.get_act(act_num)
        if act and act.scenes:
            first_scene = act.scenes[0]
            if first_scene.content:
                first_line = first_scene.content[0]
                print(f"Act {act_num}, Scene 1 - {first_line['type']}: {first_line['text'][:100]}...")

if __name__ == "__main__":
    test_fixed_text()