# Project Cordelia - Data Processing Specification (First Prototype)
## TEI XML Parsing

**Version:** 0.1 (First Prototype)  
**Date:** July 21, 2025  

---

## 1. Overview

Parse King Lear TEI XML file to extract acts, scenes, and formatted text for display.

## 2. TEI XML Structure

Key elements we need to parse:

```xml
<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <teiHeader>
    <titleStmt>
      <title>King Lear</title>
    </titleStmt>
  </teiHeader>
  <text>
    <body>
      <div type="act" n="1">
        <head>ACT 1</head>
        <div type="scene" n="1">
          <head>Act 1, scene 1</head>
          <stage>Enter KENT, GLOUCESTER, and EDMUND</stage>
          <sp who="#kent">
            <speaker>KENT</speaker>
            <p>I thought the king had more affected...</p>
          </sp>
        </div>
      </div>
    </body>
  </text>
</TEI>
```

## 3. Data Models

```python
# parser.py
from dataclasses import dataclass
from typing import List

@dataclass
class Scene:
    act_number: str      # "1", "2", etc.
    scene_number: str    # "1", "2", etc.
    title: str          # "Act 1, Scene 1"
    content: str        # Formatted text with markdown

@dataclass
class Act:
    number: str         # "1", "2", etc.
    title: str         # "Act 1"
    scenes: List[Scene]

@dataclass
class Play:
    title: str         # "King Lear"
    acts: List[Act]
    all_scenes: List[Scene]  # Flat list for easy lookup
```

## 4. Parser Implementation

```python
# parser.py
import xml.etree.ElementTree as ET
from typing import List, Optional

class TEIParser:
    def __init__(self, xml_path: str):
        self.xml_path = xml_path
        # Handle namespace
        self.ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
    
    def parse(self) -> Play:
        """Parse TEI XML and return Play object"""
        tree = ET.parse(self.xml_path)
        root = tree.getroot()
        
        # Get title
        title_elem = root.find('.//tei:title', self.ns)
        title = title_elem.text if title_elem is not None else "King Lear"
        
        # Parse acts
        acts = []
        all_scenes = []
        
        body = root.find('.//tei:body', self.ns)
        act_divs = body.findall('.//tei:div[@type="act"]', self.ns)
        
        for act_div in act_divs:
            act = self._parse_act(act_div)
            acts.append(act)
            all_scenes.extend(act.scenes)
        
        return Play(title=title, acts=acts, all_scenes=all_scenes)
    
    def _parse_act(self, act_div) -> Act:
        """Parse a single act"""
        act_num = act_div.get('n', '')
        
        # Get act title
        head = act_div.find('tei:head', self.ns)
        act_title = head.text if head is not None else f"Act {act_num}"
        
        # Parse scenes
        scenes = []
        scene_divs = act_div.findall('tei:div[@type="scene"]', self.ns)
        
        for scene_div in scene_divs:
            scene = self._parse_scene(scene_div, act_num)
            scenes.append(scene)
        
        return Act(number=act_num, title=act_title, scenes=scenes)
    
    def _parse_scene(self, scene_div, act_num: str) -> Scene:
        """Parse a single scene"""
        scene_num = scene_div.get('n', '')
        
        # Get scene title
        head = scene_div.find('tei:head', self.ns)
        scene_title = head.text if head is not None else f"Act {act_num}, Scene {scene_num}"
        
        # Format content
        content = self._format_scene_content(scene_div)
        
        return Scene(
            act_number=act_num,
            scene_number=scene_num,
            title=scene_title,
            content=content
        )
    
    def _format_scene_content(self, scene_div) -> str:
        """Convert scene XML to formatted markdown text"""
        lines = []
        
        for elem in scene_div:
            if elem.tag.endswith('stage'):
                # Stage directions in italics
                if elem.text:
                    lines.append(f"*{elem.text.strip()}*")
                    lines.append("")  # Empty line after
            
            elif elem.tag.endswith('sp'):
                # Speech
                speaker_elem = elem.find('tei:speaker', self.ns)
                speaker = speaker_elem.text if speaker_elem is not None else "UNKNOWN"
                
                # Get speech text from <p> tags
                speech_parts = []
                for p in elem.findall('tei:p', self.ns):
                    if p.text:
                        speech_parts.append(p.text.strip())
                
                if speech_parts:
                    # Format as **SPEAKER.** Speech text
                    speech_text = " ".join(speech_parts)
                    lines.append(f"**{speaker}.** {speech_text}")
                    lines.append("")  # Empty line after
        
        return "\n".join(lines)
```

## 5. Usage in Streamlit

```python
# app.py
@st.cache_data
def load_play():
    """Load and cache the play data"""
    parser = TEIParser("data/king_lear.xml")
    return parser.parse()
```

## 6. Error Handling

Basic try/except around parsing:

```python
try:
    parser = TEIParser("data/king_lear.xml")
    play = parser.parse()
except Exception as e:
    st.error(f"Failed to parse XML: {e}")
    st.stop()
```

---

**Note:** This minimal parser extracts only what's needed for display:
- Play title
- Act/scene structure  
- Speaker names and dialogue
- Stage directions

No validation, no extra metadata, no performance optimization.