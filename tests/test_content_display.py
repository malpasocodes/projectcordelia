#!/usr/bin/env python3
"""Test content display functionality."""

from pathlib import Path
from parser import TEIParser

def test_content_display():
    # Load play
    xml_path = Path("data/king-lear_TEIsimple_FolgerShakespeare.xml")
    parser = TEIParser(xml_path)
    play = parser.parse()
    
    print("=== Content Display Test ===")
    
    # Test entire play structure
    print(f"✓ Entire Play: {play.title}")
    print(f"  Acts: {play.get_act_count()} | Total scenes: {play.get_total_scenes()}")
    
    # Test act display
    act1 = play.get_act("1")
    if act1:
        print(f"\n✓ Act Display: {act1.get_formatted_title()}")
        print(f"  Scenes: {act1.get_scene_count()}")
        
        # Show first few lines of act content
        if act1.scenes:
            first_scene = act1.scenes[0]
            formatted_content = first_scene.get_formatted_content()
            lines = formatted_content.split('\n')[:10]  # First 10 lines
            print(f"  Sample content from {first_scene.title}:")
            for line in lines:
                if line.strip():
                    print(f"    {line}")
    
    # Test scene display
    scene1_1 = act1.get_scene("1") if act1 else None
    if scene1_1:
        print(f"\n✓ Scene Display: {scene1_1.title}")
        print(f"  Content items: {len(scene1_1.content)}")
        
        # Show formatted content structure
        formatted_content = scene1_1.get_formatted_content()
        print(f"  Formatted content length: {len(formatted_content)} characters")
        
        # Check if formatting is applied
        has_bold = "**" in formatted_content
        has_italic = "*" in formatted_content and not formatted_content.count("*") == formatted_content.count("**") * 2
        print(f"  Contains bold formatting: {has_bold}")
        print(f"  Contains italic formatting: {has_italic}")
        
        # Show sample formatted content
        lines = formatted_content.split('\n')[:15]  # First 15 lines
        print(f"  Sample formatted content:")
        for line in lines:
            if line.strip():
                print(f"    {line}")
    
    # Test different scene types
    print(f"\n✓ Testing different scene sizes:")
    for act in play.acts[:2]:  # First 2 acts
        for scene in act.scenes[:2]:  # First 2 scenes per act
            content_len = len(scene.get_formatted_content())
            print(f"  {scene.title}: {content_len} characters")

if __name__ == "__main__":
    test_content_display()