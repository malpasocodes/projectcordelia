import streamlit as st
from pathlib import Path
from parser import TEIParser, Play

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
        st.session_state.current_view = "full"
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
        st.title(play.title)
        
        # Display content based on current view and selection
        if st.session_state.current_view == "full":
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