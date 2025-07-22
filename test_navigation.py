#!/usr/bin/env python3
"""Test navigation functionality."""

from pathlib import Path
from parser import TEIParser

def test_navigation():
    # Load play
    xml_path = Path("data/king-lear_TEIsimple_FolgerShakespeare.xml")
    parser = TEIParser(xml_path)
    play = parser.parse()
    
    print("=== Navigation Structure Test ===")
    print(f"Play: {play.title}")
    print(f"Total acts: {play.get_act_count()}")
    
    # Test act navigation
    for act in play.acts:
        print(f"\n--- Act {act.number} ---")
        print(f"Scenes: {act.get_scene_count()}")
        
        # Test scene navigation within this act
        for scene in act.scenes[:2]:  # Just first 2 scenes per act
            print(f"  {scene.title}: {len(scene.content)} content items")
    
    # Test specific navigation paths
    print("\n=== Navigation Path Tests ===")
    
    # Test Act 1 navigation
    act1 = play.get_act("1")
    if act1:
        print(f"✓ Act 1 found: {act1.get_scene_count()} scenes")
        
        # Test Scene 1 navigation
        scene1 = act1.get_scene("1")
        if scene1:
            print(f"✓ Act 1, Scene 1 found: {len(scene1.content)} content items")
        else:
            print("✗ Act 1, Scene 1 not found")
    else:
        print("✗ Act 1 not found")
    
    # Test Act 5 navigation (last act)
    act5 = play.get_act("5")
    if act5:
        print(f"✓ Act 5 found: {act5.get_scene_count()} scenes")
        
        # Test last scene
        last_scene = act5.scenes[-1] if act5.scenes else None
        if last_scene:
            print(f"✓ Act 5, Scene {last_scene.number} found: {len(last_scene.content)} content items")
        else:
            print("✗ Last scene in Act 5 not found")
    else:
        print("✗ Act 5 not found")

if __name__ == "__main__":
    test_navigation()