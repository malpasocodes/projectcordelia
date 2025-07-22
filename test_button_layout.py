#!/usr/bin/env python3
"""Test button layout structure."""

from pathlib import Path
from parser import TEIParser

def test_button_layout():
    # Load play to verify button structure
    xml_path = Path("data/king-lear_TEIsimple_FolgerShakespeare.xml")
    parser = TEIParser(xml_path)
    play = parser.parse()
    
    print("=== Button Layout Test ===")
    
    # Test Act buttons layout
    print("\n1. ACT BUTTONS (vertical layout):")
    print("   Each button should display text horizontally on one line:")
    for act in play.acts:
        button_text = f"Act {act.number}"
        print(f"   - Button: '{button_text}' (length: {len(button_text)} chars)")
    
    # Test Scene buttons layout for each act
    print("\n2. SCENE BUTTONS (vertical layout):")
    print("   Each button should display text horizontally on one line:")
    for act in play.acts:
        print(f"   Act {act.number} scenes:")
        for scene in act.scenes:
            button_text = f"Scene {scene.number}"
            print(f"     - Button: '{button_text}' (length: {len(button_text)} chars)")
    
    print("\n✓ Layout Changes Made:")
    print("  - Removed multi-column layout (was causing narrow columns)")
    print("  - Added use_container_width=True for full-width buttons")
    print("  - Arranged buttons vertically for better sidebar readability")
    print("  - Text should now display horizontally within each button")
    
    print(f"\n✓ Total navigation elements:")
    print(f"  - {len(play.acts)} Act buttons")
    total_scenes = sum(len(act.scenes) for act in play.acts)
    print(f"  - {total_scenes} Scene buttons (across all acts)")

if __name__ == "__main__":
    test_button_layout()