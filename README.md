# Project Cordelia v0.1

A modern web interface for Shakespeare's "King Lear" built with Streamlit and TEI XML parsing.

![Version](https://img.shields.io/badge/version-0.1-blue.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.47.0%2B-red.svg)

## Features

### Interactive Navigation
- Beautiful home page with Shakespeare portrait and synopsis
- View entire play at once
- Navigate by individual acts (5 acts)
- Browse by individual scenes (25 scenes total)
- Character list view with descriptions

### Theatrical Formatting
- **Bold speakers** with proper names
- *Italic stage directions*
- Clean dialogue text with proper sentence structure
- Dark crimson titles throughout for elegant styling

### Modern Interface
- Responsive two-column layout
- Home page with image and synopsis side-by-side
- Sidebar navigation with full-width buttons
- Scrollable content areas
- Session state persistence
- Acknowledgment of Folger Shakespeare Library as data source

## Quick Start

### Prerequisites
- Python 3.9+
- [uv package manager](https://docs.astral.sh/uv/) (recommended)

### Installation

1. **Clone and navigate to project**
   ```bash
   git clone <repository-url>
   cd ProjectCordelia
   ```

2. **Install uv (if not installed)**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Set up environment and dependencies**
   ```bash
   uv venv
   source .venv/bin/activate  # macOS/Linux
   uv add streamlit lxml beautifulsoup4
   ```

### Running the App

```bash
uv run streamlit run app.py
```

Then open your browser to `http://localhost:8501`

## Usage

### Navigation Modes

1. **Home**: Landing page with Shakespeare portrait and play synopsis
2. **Characters**: View all characters with their descriptions and groupings
3. **Synopsis**: Dedicated view of the play's synopsis
4. **Entire Play**: View the complete text of King Lear in one scrollable view
5. **By Act**: Select any of the 5 acts to view all scenes within that act
6. **By Scene**: Select an act, then choose a specific scene to view

### Text Formatting

The app displays Shakespeare's text with proper theatrical formatting:
- **SPEAKER.** names appear in bold
- *Stage directions appear in italics*
- Dialogue flows naturally with proper sentence structure

## Project Structure

```
ProjectCordelia/
├── app.py                 # Main Streamlit application
├── parser.py              # TEI XML parser and data models
├── data/                  # King Lear TEI XML file
├── images/                # Shakespeare portrait
├── docs/                  # Project documentation
├── pyproject.toml         # Python dependencies
├── CLAUDE.md              # Development guidance
└── README.md              # This file
```

## Architecture

### Data Models
- **Play**: Contains 5 acts with metadata
- **Act**: Contains multiple scenes (3-7 per act)
- **Scene**: Contains formatted content (speakers, lines, stage directions)

### Key Components
- **TEIParser**: Handles TEI XML namespace parsing and text extraction
- **Streamlit App**: Provides interactive UI with session state management
- **Content Formatting**: Converts parsed content to markdown for display

## Technical Details

- **TEI XML Support**: Handles Text Encoding Initiative standard for digital texts
- **Namespace Handling**: Proper XML namespace resolution for complex documents
- **Text Processing**: Cleans XML whitespace to display proper sentences
- **Caching**: Uses Streamlit's `@st.cache_resource` for performance
- **State Management**: Maintains navigation state across user interactions

## Development

### Testing
Run the included test files to verify functionality:
```bash
uv run python test_navigation.py    # Test navigation structure
uv run python test_fixed_text.py    # Test text formatting
uv run python test_all_views.py     # Test all view modes
```

### Data Source
The app uses the Folger Shakespeare Library's TEI encoding of King Lear, which provides:
- Accurate text with proper lineation
- Detailed stage directions
- Character speech attribution
- Act and scene structure

## Version History

### v0.1 (Current)
- Complete TEI XML parser implementation
- Full Streamlit web interface
- Six navigation modes (Home, Characters, Synopsis, Full Play, By Act, By Scene)
- Beautiful home page with Shakespeare portrait
- Dark crimson (#8B0000) title styling throughout
- Theatrical text formatting
- All 5 acts and 25 scenes accessible
- Responsive sidebar layout
- Session state management
- Folger Shakespeare Library attribution with link

## Future Enhancements

Potential improvements for future versions:
- Search functionality within the text
- Character index and appearance tracking
- Export options (PDF, plain text)
- Additional Shakespeare plays
- Mobile responsiveness improvements
- Performance optimizations for large texts

## Contributing

This is a prototype project. For issues or suggestions, please refer to the project documentation in `docs/` or the development guidance in `CLAUDE.md`.

## License

This project is a prototype for educational and research purposes. The Shakespeare text is in the public domain.

---

**Project Cordelia** - Making Shakespeare accessible through modern web technology