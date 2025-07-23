from dataclasses import dataclass
from typing import List, Dict
from pathlib import Path
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# TEI namespace
TEI_NS = {'tei': 'http://www.tei-c.org/ns/1.0'}

@dataclass
class Scene:
    number: str
    title: str
    content: List[Dict[str, str]]  # [{"type": "speaker"|"line"|"stage", "text": "..."}]
    
    def get_formatted_title(self) -> str:
        """Return a formatted scene title."""
        return f"Scene {self.number}"
    
    def has_content(self) -> bool:
        """Check if the scene has any content."""
        return len(self.content) > 0
    
    def get_formatted_content(self) -> str:
        """Return markdown-formatted content for display."""
        formatted_lines = []
        
        for item in self.content:
            if item['type'] == 'speaker':
                # Bold speakers
                formatted_lines.append(f"**{item['text'].upper()}.**")
            elif item['type'] == 'stage':
                # Italicize stage directions
                formatted_lines.append(f"*{item['text']}*")
            elif item['type'] == 'line':
                # Regular dialogue with preserved line breaks
                formatted_lines.append(item['text'])
            
            # Add blank line after each element for spacing
            formatted_lines.append("")
        
        return '\n'.join(formatted_lines).strip()

@dataclass
class Act:
    number: str
    title: str
    scenes: List[Scene]
    
    def get_formatted_title(self) -> str:
        """Return a formatted act title."""
        return f"Act {self.number}"
    
    def get_scene_count(self) -> int:
        """Return the number of scenes in this act."""
        return len(self.scenes)
    
    def get_scene(self, scene_number: str) -> Scene:
        """Get a scene by its number."""
        for scene in self.scenes:
            if scene.number == scene_number:
                return scene
        return None

@dataclass
class Play:
    title: str
    acts: List[Act]
    
    def get_act_count(self) -> int:
        """Return the number of acts in the play."""
        return len(self.acts)
    
    def get_act(self, act_number: str) -> Act:
        """Get an act by its number."""
        for act in self.acts:
            if act.number == act_number:
                return act
        return None
    
    def get_total_scenes(self) -> int:
        """Return the total number of scenes in the play."""
        return sum(act.get_scene_count() for act in self.acts)

class TEIParser:
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.tree = None
        self.root = None
    
    def parse(self) -> Play:
        """Parse the TEI XML file and return a Play object."""
        # Parse the XML file
        self.tree = ET.parse(self.file_path)
        self.root = self.tree.getroot()
        
        # Get play title
        title = self._get_play_title()
        
        # Get all acts (without scene details for now)
        acts = self._get_acts()
        
        return Play(title=title, acts=acts)
    
    def _get_play_title(self) -> str:
        """Extract the play title from the TEI header."""
        # Look for title in teiHeader/fileDesc/titleStmt/title
        title_elem = self.root.find('.//tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title', TEI_NS)
        if title_elem is not None and title_elem.text:
            return title_elem.text.strip()
        return "Unknown Play"
    
    def _get_acts(self) -> List[Act]:
        """Extract all acts from the play with their scenes."""
        acts = []
        
        # Find all act divs in the body
        body = self.root.find('.//tei:body', TEI_NS)
        if body is None:
            return acts
        
        # Get only direct children act divs, not nested ones
        act_divs = body.findall('./tei:div[@type="act"]', TEI_NS)
        
        for act_div in act_divs:
            act_number = act_div.get('n', '')
            act_title = f"Act {act_number}"
            
            # Get scenes for this act
            scenes = self._get_scenes(act_div, act_number)
            
            acts.append(Act(
                number=act_number,
                title=act_title,
                scenes=scenes
            ))
        
        return acts
    
    def _get_scenes(self, act_div, act_number: str) -> List[Scene]:
        """Extract all scenes from an act."""
        scenes = []
        
        # Find all scene divs within this act
        scene_divs = act_div.findall('./tei:div[@type="scene"]', TEI_NS)
        
        for scene_div in scene_divs:
            scene_number = scene_div.get('n', '')
            scene_title = f"Act {act_number}, Scene {scene_number}"
            
            # Extract scene content
            content = self._extract_scene_content(scene_div)
            
            scenes.append(Scene(
                number=scene_number,
                title=scene_title,
                content=content
            ))
        
        return scenes
    
    def _extract_scene_content(self, scene_div) -> List[Dict[str, str]]:
        """Extract all content from a scene (speakers, lines, stage directions)."""
        content = []
        
        # Process all children elements in order
        for elem in scene_div:
            if elem.tag == f"{{{TEI_NS['tei']}}}stage":
                # Stage direction
                stage_text = self._get_element_text(elem)
                if stage_text:
                    content.append({"type": "stage", "text": stage_text})
                    
            elif elem.tag == f"{{{TEI_NS['tei']}}}sp":
                # Speech - contains speaker and paragraphs
                speaker_elem = elem.find('./tei:speaker', TEI_NS)
                if speaker_elem is not None:
                    speaker_text = self._get_element_text(speaker_elem)
                    if speaker_text:
                        content.append({"type": "speaker", "text": speaker_text})
                
                # Get all paragraphs in this speech (prose)
                for p in elem.findall('./tei:p', TEI_NS):
                    p_text = self._get_element_text(p)
                    if p_text:
                        content.append({"type": "line", "text": p_text})
                
                # Get all lines in this speech (verse)
                for l in elem.findall('./tei:l', TEI_NS):
                    l_text = self._get_element_text(l)
                    if l_text:
                        content.append({"type": "line", "text": l_text})
        
        return content
    
    def _get_element_text(self, elem) -> str:
        """Get all text content from an element, including nested elements."""
        text_parts = []
        
        # Get text directly in this element
        if elem.text:
            # Clean whitespace and newlines from element text
            cleaned_text = ' '.join(elem.text.split())
            if cleaned_text:
                text_parts.append(cleaned_text)
        
        # Get text from all child elements
        for child in elem:
            # For word elements, get their text
            if child.tag == f"{{{TEI_NS['tei']}}}w":
                if child.text:
                    # Clean the word text
                    word = child.text.strip()
                    if word:
                        text_parts.append(word)
            # For character elements (spaces), add a space
            elif child.tag == f"{{{TEI_NS['tei']}}}c":
                text_parts.append(" ")
            # For punctuation elements
            elif child.tag == f"{{{TEI_NS['tei']}}}pc":
                if child.text:
                    punct = child.text.strip()
                    if punct:
                        text_parts.append(punct)
            # Recursively get text from other elements
            else:
                child_text = self._get_element_text(child)
                if child_text:
                    text_parts.append(child_text)
            
            # Get any tail text after this child, cleaning whitespace
            if child.tail:
                cleaned_tail = ' '.join(child.tail.split())
                if cleaned_tail:
                    text_parts.append(cleaned_tail)
        
        # Join and clean up - collapse multiple spaces
        result = ' '.join(text_parts)
        # Remove extra spaces and clean up
        return ' '.join(result.split())
    
    def _format_scene_content(self, content: List[Dict[str, str]]) -> str:
        """Format scene content with markdown for display."""
        formatted_lines = []
        
        for item in content:
            if item['type'] == 'speaker':
                # Bold speakers
                formatted_lines.append(f"**{item['text'].upper()}.**")
            elif item['type'] == 'stage':
                # Italicize stage directions
                formatted_lines.append(f"*{item['text']}*")
            elif item['type'] == 'line':
                # Regular dialogue with preserved line breaks
                formatted_lines.append(item['text'])
            
            # Add blank line after each element for spacing
            formatted_lines.append("")
        
        return '\n'.join(formatted_lines).strip()