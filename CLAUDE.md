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

## Architecture

### File Structure
- `app.py` - Streamlit web application (✓ COMPLETED)
- `parser.py` - TEI XML parser and data models (✓ COMPLETED)
- `data/` - Directory containing King Lear TEI XML file (✓ COMPLETED)
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
   - Session state management for navigation persistence
   - Cached data loading with `@st.cache_resource`
   - Three view modes: Entire Play, By Act, By Scene
   - Interactive navigation with full-width buttons
   - Scrollable content containers with 600px height

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
- `current_view`: "full" | "act" | "scene"
- `current_act`: Act number (1-5)
- `current_scene`: Scene number

### Button Keys Format
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
2. Test "Entire Play" view (shows all content)
3. Test "By Act" navigation and content display
4. Test "By Scene" navigation and content display  
5. Verify text formatting (bold speakers, italic stage directions)
6. Check button text displays horizontally

## Implementation Status - v0.1 COMPLETE ✓
- ✅ Project structure and dependencies
- ✅ TEI XML parser with proper text extraction
- ✅ Data models with formatting methods
- ✅ Complete Streamlit app with three view modes
- ✅ Interactive navigation system
- ✅ Markdown text formatting
- ✅ Session state management
- ✅ Cached data loading
- ✅ All 5 acts and 25 scenes accessible
- ✅ Proper button layout and text display