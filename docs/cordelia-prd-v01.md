# Project Cordelia - Product Requirements Document (First Prototype)
## Shakespeare Text Display Prototype

**Version:** 0.1 (First Prototype)  
**Date:** July 21, 2025  
**Project Codename:** Cordelia  

---

## 1. Executive Summary

Project Cordelia is a prototype web application that displays the complete text of Shakespeare's King Lear with navigation between acts and scenes.

## 2. Prototype Goal

Create a simple, functional demonstration of displaying Shakespeare's text from TEI XML format in a web interface with basic navigation.

## 3. Core Requirements

### 3.1 Text Display
- Display complete King Lear text from TEI XML file
- Maintain original formatting: speaker names, stage directions, line breaks
- Clean, readable presentation

### 3.2 Navigation
- Sidebar showing play structure (Acts → Scenes)
- Click any scene to view it
- Show current location in sidebar

### 3.3 Data
- TEI XML file will be provided in `/data` directory
- No dynamic data retrieval needed
- Parse once on application start

## 4. Technical Specifications

### 4.1 Technology Stack
- **Framework:** Streamlit
- **Language:** Python 3.9+
- **Data Format:** TEI XML (provided)

### 4.2 Basic Error Handling
- If XML file missing: Show error message
- If parsing fails: Show error message
- Continue running even with errors

## 5. Success Criteria

- Successfully displays complete King Lear text
- Users can navigate to any scene
- Test with 10 users: Average rating 8/10 for design and experience

## 6. Out of Scope for First Prototype

- Downloads
- Citations  
- Synopsis
- Performance optimization
- Accessibility
- Multiple plays
- Search
- Mobile optimization
- User authentication

---

**Next Step:** Build functional prototype focusing only on text display and navigation.