# Project Cordelia - UI Design Document (First Prototype)
## Shakespeare Text Display

**Version:** 0.1 (First Prototype)  
**Date:** July 21, 2025  

---

## 1. Layout Overview

Simple two-column layout using Streamlit's default styling:

```
┌─────────────────┬─────────────────────────────────────────┐
│                 │                                         │
│   NAVIGATION    │         MAIN TEXT DISPLAY               │
│   (Narrow)      │         (Wide)                          │
│                 │                                         │
└─────────────────┴─────────────────────────────────────────┘
```

## 2. Navigation Column (Left)

### 2.1 Structure
```
Scenes
─────────────────
📖 Entire Play

🎭 Act 1
  Act 1, Scene 1
  Act 1, Scene 2
  Act 1, Scene 3
  Act 1, Scene 4
  Act 1, Scene 5

🎭 Act 2
  Act 2, Scene 1
  Act 2, Scene 2

🎭 Act 3
  Act 3, Scene 1
  Act 3, Scene 2
  [etc...]
```

### 2.2 Navigation Options
- **Entire Play button**: Shows complete text
- **Act buttons**: Shows all scenes within that act
- **Scene buttons**: Shows individual scene

### 2.3 Behavior
- User can select:
  - Entire play (all acts and scenes)
  - Individual act (all scenes in that act)
  - Individual scene (just that scene)
- Current selection highlighted by Streamlit default

## 3. Main Content Area (Right)

### 3.1 Content Structure
- Play title at top (e.g., "King Lear")
- Content depends on selection:
  
**When "Entire Play" selected:**
- All acts with their scenes in order
- Act headers → Scene headers → Scene text

**When individual Act selected:**
- Selected act title
- All scenes within that act
- Scene headers → Scene text

**When individual Scene selected:**
- Scene title only
- Scene text only

### 3.2 Text Formatting
- **SPEAKER.** Speech text here
- *Stage directions in italics*
- Line breaks preserved for verse

## 4. Visual Design

Use Streamlit defaults:
- White background
- Default font (Sans-serif)
- Default colors
- Default spacing
- Default button styles

## 5. Responsive Behavior

- Let Streamlit handle responsive layout
- Columns will stack on mobile automatically
- No custom mobile optimization

## 6. Example Text Display

```
**KENT.** I thought the King had more affected  
the Duke of Albany than Cornwall.

**GLOUCESTER.** It did always seem so to us, but  
now in the division of the kingdom it  
appears not which of the Dukes he values  
most.

*Enter Edgar.*

**EDGAR.** My services to your lordship.
```

---

**Note:** This is a minimal UI design relying entirely on Streamlit's default components and styling.