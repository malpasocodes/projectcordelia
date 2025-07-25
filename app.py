import streamlit as st
from pathlib import Path
from parser import TEIParser, Play

# King Lear Synopsis (from dataset)
KING_LEAR_SYNOPSIS = """
King Lear dramatizes the story of an aged king of ancient Britain, whose plan to divide his kingdom among his three daughters ends tragically. When he tests each by asking how much she loves him, the older daughters, Goneril and Regan, flatter him. The youngest, Cordelia, does not, and Lear disowns and banishes her. She marries the king of France. Goneril and Regan turn on Lear, leaving him to wander madly in a furious storm.

Meanwhile, the Earl of Gloucester's illegitimate son Edmund turns Gloucester against his legitimate son, Edgar. Gloucester, appalled at the daughters' treatment of Lear, gets news that a French army is coming to help Lear. Edmund betrays Gloucester to Regan and her husband, Cornwall, who puts out Gloucester's eyes and makes Edmund the Earl of Gloucester.

Cordelia and the French army save Lear, but the army is defeated. Edmund imprisons Cordelia and Lear. Edgar then mortally wounds Edmund in a trial by combat. Dying, Edmund confesses that he has ordered the deaths of Cordelia and Lear. Before they can be rescued, Lear brings in Cordelia's body and then he himself dies.
"""

@st.cache_resource
def load_play() -> Play:
    """Load and parse the King Lear XML file."""
    xml_path = Path("data/king-lear_TEIsimple_FolgerShakespeare.xml")
    parser = TEIParser(xml_path)
    return parser.parse()

def main():
    st.set_page_config(
        page_title="King Lear - Shakespeare",
        page_icon="📖",
        layout="wide"
    )
    
    # Initialize session state
    if "current_view" not in st.session_state:
        st.session_state.current_view = "home"
    if "current_act" not in st.session_state:
        st.session_state.current_act = "1"
    if "current_scene" not in st.session_state:
        st.session_state.current_scene = "1"
    
    # Load the play data
    play = load_play()
    
    # Create two-column layout
    sidebar = st.sidebar
    main_area = st.container()
    
    # Sidebar navigation
    with sidebar:
        st.title("Navigation")
        
        # Custom CSS for box styling
        st.markdown("""
        <style>
        div.stButton > button {
            background-color: #f0f2f6;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 0.5rem 1rem;
            margin: 0.25rem 0;
            width: 100%;
            text-align: left;
            transition: all 0.2s;
        }
        div.stButton > button:hover {
            background-color: #e0e2e6;
            border-color: #999;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Home button
        if st.button("🏠 Home", key="home", use_container_width=True):
            st.session_state.current_view = "home"
            st.rerun()
        
        # Characters button
        if st.button("👥 Characters", key="characters", use_container_width=True):
            st.session_state.current_view = "characters"
            st.rerun()
        
        # Synopsis button
        if st.button("📜 Synopsis", key="synopsis", use_container_width=True):
            st.session_state.current_view = "synopsis"
            st.rerun()
        
        # Entire Play button
        if st.button("📖 Entire Play", key="entire_play", use_container_width=True):
            st.session_state.current_view = "full"
            st.rerun()
        
        # Act and Scene navigation
        for act in play.acts:
            # Expand only if this act is currently selected
            expanded = (
                (st.session_state.current_view == "act" and st.session_state.current_act == act.number) or
                (st.session_state.current_view == "scene" and st.session_state.current_act == act.number)
            )
            with st.expander(f"📁 Act {act.number}", expanded=expanded):
                # Act button
                if st.button(f"📄 Act {act.number} (All Scenes)", 
                           key=f"act_{act.number}", 
                           use_container_width=True):
                    st.session_state.current_view = "act"
                    st.session_state.current_act = act.number
                    st.rerun()
                
                # Scene buttons
                for scene in act.scenes:
                    if st.button(f"　　📄 Scene {scene.number}", 
                               key=f"scene_{act.number}_{scene.number}", 
                               use_container_width=True):
                        st.session_state.current_view = "scene"
                        st.session_state.current_act = act.number
                        st.session_state.current_scene = scene.number
                        st.rerun()
    
    # Main content area
    with main_area:
        # Display content based on current view and selection
        if st.session_state.current_view == "home":
            # Center the title with dark crimson color
            st.markdown("<h1 style='text-align: center; color: #8B0000;'>King Lear</h1>", unsafe_allow_html=True)
            
            # Add separator
            st.markdown("---")
            
            # Create two columns with adjusted proportions
            col1, col2 = st.columns([1, 1.5])
            
            with col1:
                # Add spacing to align image with paragraph
                st.markdown("<br><br>", unsafe_allow_html=True)
                # Center the image and resize to 75%
                _, center, _ = st.columns([1, 6, 1])
                with center:
                    st.image("images/shakespeare-houghton.jpg", width=300)
            
            with col2:
                # Display the synopsis
                st.markdown("### Synopsis")
                st.markdown(KING_LEAR_SYNOPSIS)
            
            # Add separator and acknowledgment
            st.markdown("---")
            st.markdown(
                "<p style='text-align: center; color: #666666; font-size: 0.9em;'>"
                "Text sourced from the <a href='https://www.folger.edu' target='_blank' style='color: #666666;'>Folger Shakespeare Library</a>. "
                "Any errors in presentation or formatting are not attributable to the Folger Shakespeare Library."
                "</p>", 
                unsafe_allow_html=True
            )
        
        elif st.session_state.current_view == "characters":
            st.markdown("<h1 style='text-align: center; color: #8B0000;'>King Lear</h1>", unsafe_allow_html=True)
            st.subheader("Characters")
            st.write(f"Total characters: {len(play.characters)}")
            
            # Display characters in a scrollable container
            with st.container(height=600, border=True):
                # Group characters by their groups if available
                main_characters = []
                grouped_characters = {}
                
                for char in play.characters:
                    if char.group:
                        if char.group not in grouped_characters:
                            grouped_characters[char.group] = []
                        grouped_characters[char.group].append(char)
                    else:
                        main_characters.append(char)
                
                # Display main characters first
                if main_characters:
                    st.markdown("### Main Characters")
                    for char in main_characters:
                        if char.description:
                            st.markdown(f"**{char.name}** - {char.description}")
                        else:
                            st.markdown(f"**{char.name}**")
                    st.markdown("")
                
                # Display grouped characters
                for group_name, chars in grouped_characters.items():
                    st.markdown(f"### {group_name}")
                    for char in chars:
                        if char.description:
                            st.markdown(f"**{char.name}** - {char.description}")
                        else:
                            st.markdown(f"**{char.name}**")
                    st.markdown("")
        
        elif st.session_state.current_view == "synopsis":
            st.markdown("<h1 style='text-align: center; color: #8B0000;'>King Lear</h1>", unsafe_allow_html=True)
            st.subheader("Synopsis")
            
            # Display synopsis in a scrollable container
            with st.container(height=600, border=True):
                st.markdown(KING_LEAR_SYNOPSIS)
        
        elif st.session_state.current_view == "full":
            st.markdown("<h1 style='text-align: center; color: #8B0000;'>King Lear</h1>", unsafe_allow_html=True)
            st.subheader(f"Complete text of {play.title}")
            st.write(f"Acts: {play.get_act_count()} | Total scenes: {play.get_total_scenes()}")
            
            # Display entire play with all acts and scenes
            with st.container(height=600, border=True):
                for act in play.acts:
                    st.markdown(f"# {act.get_formatted_title()}")
                    st.markdown("---")
                    
                    for scene in act.scenes:
                        st.markdown(f"## {scene.title}")
                        formatted_content = scene.get_formatted_content()
                        st.markdown(formatted_content)
                        st.markdown("")  # Add spacing between scenes
            
        elif st.session_state.current_view == "act":
            st.markdown("<h1 style='text-align: center; color: #8B0000;'>King Lear</h1>", unsafe_allow_html=True)
            current_act = play.get_act(st.session_state.current_act)
            if current_act:
                st.subheader(f"{current_act.get_formatted_title()}")
                st.write(f"Scenes: {current_act.get_scene_count()}")
                
                # Display all scenes in this act
                with st.container(height=600, border=True):
                    for scene in current_act.scenes:
                        st.markdown(f"## {scene.title}")
                        formatted_content = scene.get_formatted_content()
                        st.markdown(formatted_content)
                        st.markdown("---")  # Divider between scenes
            else:
                st.error("Act not found")
                
        elif st.session_state.current_view == "scene":
            st.markdown("<h1 style='text-align: center; color: #8B0000;'>King Lear</h1>", unsafe_allow_html=True)
            current_act = play.get_act(st.session_state.current_act)
            if current_act:
                current_scene = current_act.get_scene(st.session_state.current_scene)
                if current_scene:
                    st.subheader(current_scene.title)
                    st.write(f"Content: {len(current_scene.content)} items")
                    
                    # Display the selected scene with full formatting
                    with st.container(height=600, border=True):
                        formatted_content = current_scene.get_formatted_content()
                        st.markdown(formatted_content)
                else:
                    st.error("Scene not found")
            else:
                st.error("Act not found")

if __name__ == "__main__":
    main()