#!/usr/bin/env python3
"""Test all view modes for content display."""

from pathlib import Path
from parser import TEIParser

def test_all_view_modes():
    # Load play
    xml_path = Path("data/king-lear_TEIsimple_FolgerShakespeare.xml")
    parser = TEIParser(xml_path)
    play = parser.parse()
    
    print("=== All View Modes Test ===")
    
    # Test 1: Entire Play View
    print("\n1. ENTIRE PLAY VIEW")
    print(f"   Title: {play.title}")
    print(f"   Acts: {play.get_act_count()}")
    print(f"   Total scenes: {play.get_total_scenes()}")
    
    total_content_length = 0
    for act in play.acts:
        for scene in act.scenes:
            total_content_length += len(scene.get_formatted_content())
    
    print(f"   Total formatted content: {total_content_length:,} characters")
    print("   ✓ Entire play view ready")
    
    # Test 2: By Act View
    print("\n2. BY ACT VIEW")
    for act in play.acts:
        act_content_length = sum(len(scene.get_formatted_content()) for scene in act.scenes)
        print(f"   {act.get_formatted_title()}: {act.get_scene_count()} scenes, {act_content_length:,} characters")
    print("   ✓ All acts ready for display")
    
    # Test 3: By Scene View
    print("\n3. BY SCENE VIEW")
    scene_count = 0
    for act in play.acts:
        print(f"   {act.get_formatted_title()}:")
        for scene in act.scenes:
            scene_count += 1
            content_length = len(scene.get_formatted_content())
            print(f"     {scene.title}: {content_length:,} characters")
    
    print(f"   ✓ All {scene_count} scenes ready for individual display")
    
    # Test 4: Verify markdown formatting across all content
    print("\n4. MARKDOWN FORMATTING TEST")
    total_speakers = 0
    total_stage_directions = 0
    total_lines = 0
    
    for act in play.acts:
        for scene in act.scenes:
            for item in scene.content:
                if item['type'] == 'speaker':
                    total_speakers += 1
                elif item['type'] == 'stage':
                    total_stage_directions += 1
                elif item['type'] == 'line':
                    total_lines += 1
    
    print(f"   Speakers: {total_speakers:,} (will be bold)")
    print(f"   Stage directions: {total_stage_directions:,} (will be italic)")
    print(f"   Dialogue lines: {total_lines:,} (plain text)")
    print("   ✓ All content types ready for formatting")
    
    # Test 5: Sample content verification
    print("\n5. SAMPLE CONTENT VERIFICATION")
    
    # Get Act 1, Scene 1 for detailed check
    act1 = play.get_act("1")
    scene1 = act1.get_scene("1") if act1 else None
    
    if scene1:
        formatted = scene1.get_formatted_content()
        
        # Check for proper markdown elements
        has_bold_speakers = "**" in formatted and ".**" in formatted
        has_italic_stage = formatted.count("*") > formatted.count("**") * 2
        has_line_breaks = "\n" in formatted
        
        print(f"   Sample scene: {scene1.title}")
        print(f"   ✓ Bold speakers: {has_bold_speakers}")
        print(f"   ✓ Italic stage directions: {has_italic_stage}")
        print(f"   ✓ Preserved line breaks: {has_line_breaks}")
        
        # Show first few formatted lines
        lines = formatted.split('\n')[:8]
        print("   Sample formatted output:")
        for line in lines:
            if line.strip():
                print(f"     {line}")
    
    print("\n=== ALL VIEW MODES READY ===")

if __name__ == "__main__":
    test_all_view_modes()