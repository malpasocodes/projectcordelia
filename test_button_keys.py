#!/usr/bin/env python3
"""Test that button keys match expected format."""

from pathlib import Path
from parser import TEIParser

def test_button_keys():
    # Load play
    xml_path = Path("data/king-lear_TEIsimple_FolgerShakespeare.xml")
    parser = TEIParser(xml_path)
    play = parser.parse()
    
    print("=== Button Key Format Test ===")
    
    # Test Act button keys (should be act_1, act_2, etc.)
    print("\nAct button keys:")
    for act in play.acts:
        key = f"act_{act.number}"
        print(f"  Act {act.number}: {key}")
    
    # Test Scene button keys (should be scene_1_1, scene_2_3, etc.)
    print("\nScene button keys (sample):")
    for act_num in ["1", "2"]:
        act = play.get_act(act_num)
        if act:
            for scene in act.scenes[:3]:  # First 3 scenes
                key = f"scene_{act.number}_{scene.number}"
                print(f"  {scene.title}: {key}")
    
    # Test Scene Act selection keys (should be scene_act_1, etc.)
    print("\nScene Act selection keys:")
    for act in play.acts:
        key = f"scene_act_{act.number}"
        print(f"  Act {act.number} (for scene selection): {key}")

if __name__ == "__main__":
    test_button_keys()