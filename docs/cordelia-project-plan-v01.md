# Project Cordelia - Project Plan (First Prototype)
## 10-Phase Development Plan

**Version:** 0.1 (First Prototype)  
**Date:** July 21, 2025  

---

## Phase 1: Environment Setup
**Duration:** 2 hours

**Tasks:**
- Install uv package manager
- Create project directory
- Initialize virtual environment
- Install dependencies (streamlit, lxml, beautifulsoup4)

**Success Criteria:**
- [ ] `uv --version` shows version number
- [ ] Virtual environment activated
- [ ] `uv run streamlit hello` runs without errors
- [ ] All dependencies installed

---

## Phase 2: Project Structure
**Duration:** 1 hour

**Tasks:**
- Create `app.py` and `parser.py` files
- Create `data/` directory
- Add King Lear XML file to `data/`
- Create basic file headers with imports

**Success Criteria:**
- [ ] Project structure matches specification
- [ ] `king_lear.xml` present in data directory
- [ ] Basic imports work without errors
- [ ] Can run `uv run streamlit run app.py` (even if empty)

---

## Phase 3: Data Models
**Duration:** 2 hours

**Tasks:**
- Create dataclasses for Scene, Act, and Play
- Add type hints
- Implement basic methods
- Test dataclass creation

**Success Criteria:**
- [ ] All three dataclasses defined
- [ ] Can create test instances of each class
- [ ] No import errors
- [ ] Type hints properly defined

---

## Phase 4: XML Parser - Basic Structure
**Duration:** 3 hours

**Tasks:**
- Create TEIParser class
- Implement XML namespace handling
- Parse play title
- Extract act structure (without scene details)

**Success Criteria:**
- [ ] Parser can open and read XML file
- [ ] Successfully extracts "King Lear" as title
- [ ] Identifies 5 acts in the play
- [ ] No XML parsing errors

---

## Phase 5: XML Parser - Scene Extraction
**Duration:** 4 hours

**Tasks:**
- Parse scenes within acts
- Extract scene titles
- Extract speakers and dialogue
- Format stage directions

**Success Criteria:**
- [ ] All scenes extracted (approximately 26 scenes)
- [ ] Scene titles match "Act X, Scene Y" format
- [ ] Speaker names extracted correctly
- [ ] Stage directions identified

---

## Phase 6: Text Formatting
**Duration:** 3 hours

**Tasks:**
- Implement markdown formatting for speakers (**SPEAKER.**)
- Format stage directions in italics
- Preserve line breaks
- Create `_format_scene_content()` method

**Success Criteria:**
- [ ] Speakers display as **SPEAKER.** Text
- [ ] Stage directions display as *Stage direction*
- [ ] Line breaks preserved in verse
- [ ] Clean, readable text output

---

## Phase 7: Basic Streamlit App
**Duration:** 3 hours

**Tasks:**
- Set up page configuration
- Create two-column layout
- Implement `load_play()` function with caching
- Display play title

**Success Criteria:**
- [ ] App runs without errors
- [ ] Two columns visible (1:3 ratio)
- [ ] "King Lear" title displays
- [ ] Page title shows in browser tab

---

## Phase 8: Navigation Implementation
**Duration:** 4 hours

**Tasks:**
- Create navigation sidebar
- Add "Entire Play" button
- List all Acts with clickable buttons
- List Scenes under each Act
- Implement session state for tracking selection

**Success Criteria:**
- [ ] All navigation buttons visible
- [ ] "Entire Play" button works
- [ ] Act buttons show only that act's scenes
- [ ] Scene buttons show individual scenes
- [ ] Current selection tracked properly

---

## Phase 9: Content Display
**Duration:** 4 hours

**Tasks:**
- Display full play when "Entire Play" selected
- Display single act when Act selected
- Display single scene when Scene selected
- Proper headers and formatting for each view

**Success Criteria:**
- [ ] Entire play displays with all acts/scenes
- [ ] Individual acts show only their scenes
- [ ] Individual scenes show only that content
- [ ] Proper headers at each level

---

## Phase 10: Error Handling & Polish
**Duration:** 2 hours

**Tasks:**
- Add try/except for file loading
- Add error messages for missing/corrupt XML
- Clean up any UI issues
- Final testing of all functionality

**Success Criteria:**
- [ ] Missing file shows clear error message
- [ ] Corrupt XML shows helpful error
- [ ] No unhandled exceptions
- [ ] All navigation paths work smoothly

---

## Final Validation

**Manual Testing Checklist:**
- [ ] All acts accessible
- [ ] All scenes accessible
- [ ] Text formatting correct throughout
- [ ] No console errors
- [ ] Smooth navigation experience

**User Testing:**
- [ ] Test with 10 users
- [ ] Average rating 8/10 or higher

---

## Total Timeline

**Estimated Total:** 28 hours of development

**Suggested Schedule:**
- Week 1: Phases 1-4 (Setup and basic parsing)
- Week 2: Phases 5-7 (Complete parser and basic UI)
- Week 3: Phases 8-10 (Navigation and polish)
- Week 4: User testing and feedback

---

## Risk Mitigation

**Biggest Risks:**
1. TEI XML structure different than expected
   - Mitigation: Test parser early with actual file
   
2. Streamlit navigation complexity
   - Mitigation: Start with simple button clicks before optimization

3. Text formatting issues
   - Mitigation: Test with various scenes early

**If Behind Schedule:**
- Simplify formatting (skip italics for stage directions)
- Show only scenes (skip act-level navigation)
- Reduce error handling to basic try/except