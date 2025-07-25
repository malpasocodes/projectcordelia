# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Project Cordelia is a Streamlit-based web application for displaying Shakespeare's "King Lear" with interactive navigation. This is version 0.1 - a fully functional prototype that provides modern web interface for Shakespeare's texts with theatrical formatting and multi-level navigation.

## Commands

### Setup
```bash
# Install uv package manager (if not installed)
curl -LsSf https://astral.sh/uv/install.sh | sh  # macOS/Linux

# Create and activate virtual environment
uv venv
source .venv/bin/activate  # macOS/Linux

# Install dependencies
uv add streamlit lxml beautifulsoup4
```

### Development
```bash
# Run the application
uv run streamlit run app.py

# The app auto-reloads on file changes
# Access at http://localhost:8501
```

### Testing
```bash
# Run all tests (from project root)
python tests/test_app.py
python tests/test_formatting.py
python tests/test_navigation.py

# Run specific test for debugging
python tests/debug_text.py
python tests/test_all_views.py
```

## Architecture

### File Structure
- `app.py` - Streamlit web application with home page (✓ COMPLETED)
- `parser.py` - TEI XML parser and data models (✓ COMPLETED)
- `data/` - Directory containing King Lear TEI XML file (✓ COMPLETED)
- `images/` - Shakespeare portrait for home page (✓ COMPLETED)
- `docs/` - Comprehensive project documentation (✓ COMPLETED)

### Key Components

1. **TEIParser** (in `parser.py`):
   - Parses TEI XML with namespace `{'tei': 'http://www.tei-c.org/ns/1.0'}`
   - Returns structured Play object with Acts and Scenes
   - Handles theatrical formatting (speakers, stage directions)
   - Text extraction with proper sentence formatting
   - Markdown formatting methods for display

2. **Streamlit App** (in `app.py`):
   - Two-column layout: navigation sidebar + main content
   - Beautiful home page with Shakespeare portrait and synopsis
   - Session state management for navigation persistence
   - Cached data loading with `@st.cache_resource`
   - Six view modes: Home, Characters, Synopsis, Entire Play, By Act, By Scene
   - Interactive navigation with full-width buttons
   - Scrollable content containers with 600px height
   - Dark crimson (#8B0000) title styling throughout
   - Folger Shakespeare Library attribution

### Data Models
```python
@dataclass
class Scene:
    number: str
    title: str
    content: List[Dict[str, str]]  # [{"type": "speaker"|"line"|"stage", "text": "..."}]
    
    def get_formatted_title(self) -> str: # Returns "Scene X"
    def has_content(self) -> bool:         # Check if scene has content
    def get_formatted_content(self) -> str: # Returns markdown-formatted content

@dataclass
class Act:
    number: str
    title: str
    scenes: List[Scene]
    
    def get_formatted_title(self) -> str:   # Returns "Act X"
    def get_scene_count(self) -> int:       # Number of scenes
    def get_scene(self, scene_number: str) -> Scene: # Get scene by number

@dataclass
class Play:
    title: str
    acts: List[Act]
    
    def get_act_count(self) -> int:         # Number of acts (5)
    def get_act(self, act_number: str) -> Act: # Get act by number
    def get_total_scenes(self) -> int:      # Total scenes (25)
```

## Implementation Notes

### Session State Keys
- `current_view`: "home" | "characters" | "synopsis" | "full" | "act" | "scene"
- `current_act`: Act number (1-5)
- `current_scene`: Scene number

### Button Keys Format
- Navigation buttons: `home`, `characters`, `synopsis`, `entire_play`
- Act buttons: `act_1`, `act_2`, etc.
- Scene buttons: `scene_1_1`, `scene_2_3`, etc.
- Scene act selection: `scene_act_1`, `scene_act_2`, etc.

### Text Formatting
- **Speakers**: `**SPEAKER.**` (bold, uppercase)
- **Stage directions**: `*stage direction*` (italic)
- **Dialogue**: Plain text with proper sentence structure

### Common Pitfalls
- TEI XML requires namespace handling in all XPath queries
- Text extraction needs whitespace cleaning to avoid word-per-line display
- Scene numbering may vary in source XML (Act 4 has no Scene 4)
- Streamlit button callbacks need unique keys
- Sidebar buttons need `use_container_width=True` for proper text display

## Quick Testing Steps
1. Run `uv run streamlit run app.py`
2. Test "Home" page (Shakespeare portrait + synopsis)
3. Test "Characters" view (character list with descriptions)
4. Test "Synopsis" view (dedicated synopsis page)
5. Test "Entire Play" view (shows all content)
6. Test "By Act" navigation and content display
7. Test "By Scene" navigation and content display  
8. Verify text formatting (bold speakers, italic stage directions)
9. Check button text displays horizontally
10. Verify dark crimson titles and Folger attribution

## Implementation Status - v0.1 COMPLETE ✓
- ✅ Project structure and dependencies
- ✅ TEI XML parser with proper text extraction
- ✅ Data models with formatting methods
- ✅ Complete Streamlit app with six view modes
- ✅ Beautiful home page with Shakespeare portrait
- ✅ Character list view with descriptions
- ✅ Synopsis dedicated view
- ✅ Interactive navigation system
- ✅ Markdown text formatting
- ✅ Dark crimson title styling
- ✅ Session state management
- ✅ Cached data loading
- ✅ All 5 acts and 25 scenes accessible
- ✅ Proper button layout and text display
- ✅ Folger Shakespeare Library attribution