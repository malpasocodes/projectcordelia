# Project Cordelia - Claude Code Implementation Guide
## Quick Reference for Implementation

**Version:** 0.1 (First Prototype)  
**Date:** July 21, 2025  

---

## 1. Implementation Order

Follow the phases in the Project Plan document. Start with Phase 1.

## 2. Key Implementation Details

### 2.1 TEI XML Namespace
The XML uses namespace. Always use:
```python
self.ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
```

### 2.2 XML Structure to Expect
```
<TEI> → <text> → <body> → <div type="act"> → <div type="scene">
```

Inside scenes:
- `<stage>` = stage directions
- `<sp>` = speech block
- `<speaker>` = character name
- `<p>` = text paragraph

### 2.3 Session State Keys
Use exactly these keys in Streamlit:
```python
st.session_state.current_view = 'entire_play' | 'act' | 'scene'
st.session_state.current_act = '1' | '2' | '3' | '4' | '5' | None
st.session_state.current_scene = '1' | '2' | '3' | etc. | None
```

### 2.4 Button Key Format
For Streamlit button unique keys:
```python
# Act buttons
key=f"act_{act.number}"

# Scene buttons  
key=f"scene_{act.number}_{scene.scene_number}"
```

## 3. Common Pitfalls to Avoid

1. **XML Parsing**: The TEI namespace must be used for all searches
2. **Empty Text**: Check for None before using .text on XML elements
3. **Scene Numbers**: Some might be '4a' or '4b', not just integers
4. **Streamlit Rerun**: Use `st.rerun()` after changing session state
5. **Column Width**: Use `[1, 3]` ratio for sidebar and main content

## 4. Testing the Implementation

### Quick Smoke Test
1. Run: `uv run streamlit run app.py`
2. Click "Entire Play" - should see all text
3. Click "Act 1" - should see only Act 1 scenes  
4. Click "Act 1, Scene 1" - should see only that scene
5. Click "Act 5, Scene 3" - should see final scene

### Text Formatting Check
Look for:
- **GLOUCESTER.** (bold speaker names)
- *Enter Edgar.* (italic stage directions)
- Line breaks in speeches

## 5. Sample Test Data

If you need to test with minimal XML:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <teiHeader>
    <titleStmt>
      <title>King Lear</title>
    </titleStmt>
  </teiHeader>
  <text>
    <body>
      <div type="act" n="1">
        <head>Act 1</head>
        <div type="scene" n="1">
          <head>Act 1, Scene 1</head>
          <stage>Enter Kent and Gloucester.</stage>
          <sp who="#kent">
            <speaker>KENT</speaker>
            <p>I thought the King had more affected the Duke of Albany than Cornwall.</p>
          </sp>
        </div>
      </div>
    </body>
  </text>
</TEI>
```

## 6. File Organization

Create files in this order:
1. `parser.py` - Data models and TEIParser class
2. `app.py` - Streamlit application

Don't create subdirectories or complex structure for the prototype.

## 7. Success Verification

You know it's working when:
1. No errors in terminal
2. Can navigate to any scene
3. Text displays with correct formatting
4. Navigation state persists (clicking a scene keeps it selected)

## 8. If You Get Stuck

Most common issues:
- **"No module named X"** → Check virtual environment is activated
- **XML parsing errors** → Check namespace usage
- **Buttons not working** → Check session state and st.rerun()
- **Text not formatted** → Check markdown string construction

## 9. Implementation Shortcuts

For the prototype, it's OK to:
- Hard-code the XML file path as "data/king_lear.xml"
- Assume the XML structure is consistent
- Skip validation and just use try/except
- Use Streamlit's default styling

## 10. Final Notes

- Keep it simple - this is a prototype
- Don't add features not in the requirements
- Test frequently as you build
- The Project Plan phases are a good checkpoint system

---

**Remember:** The goal is a working prototype that displays King Lear with navigation. Everything else is out of scope.