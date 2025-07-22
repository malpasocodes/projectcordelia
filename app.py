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
        st.write("Select a section to read:")
        
        # Navigation options
        view_mode = st.radio(
            "View Mode",
            ["Entire Play", "By Act", "By Scene"],
            key="view_mode"
        )
        
        st.divider()
        
        # Act selection
        if view_mode == "By Act":
            st.subheader("Select Act")
            # Use vertical layout for better readability in narrow sidebar
            for act in play.acts:
                if st.button(f"Act {act.number}", key=f"act_{act.number}", use_container_width=True):
                    st.session_state.current_view = "act"
                    st.session_state.current_act = act.number
                    st.rerun()
        
        # Scene selection
        elif view_mode == "By Scene":
            st.subheader("Select Act")
            # Use vertical layout for act selection in narrow sidebar
            for act in play.acts:
                if st.button(f"Act {act.number}", key=f"scene_act_{act.number}", use_container_width=True):
                    st.session_state.current_act = act.number
                    st.rerun()
            
            st.divider()
            
            # Scene buttons for selected act
            current_act = play.get_act(st.session_state.current_act)
            if current_act and current_act.scenes:
                st.subheader(f"Act {current_act.number} Scenes")
                
                # Use vertical layout for scene buttons too for consistency
                for scene in current_act.scenes:
                    if st.button(f"Scene {scene.number}", 
                               key=f"scene_{current_act.number}_{scene.number}", 
                               use_container_width=True):
                        st.session_state.current_view = "scene"
                        st.session_state.current_act = current_act.number
                        st.session_state.current_scene = scene.number
                        st.rerun()
    
    # Main content area
    with main_area:
        st.title(play.title)
        
        # Display content based on current view and selection
        if view_mode == "Entire Play":
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
            
        elif view_mode == "By Act":
            if st.session_state.current_view == "act":
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
            else:
                st.info("Select an act from the sidebar to view its content")
                
        elif view_mode == "By Scene":
            if st.session_state.current_view == "scene":
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
            else:
                st.info("Select an act and scene from the sidebar to view content")

if __name__ == "__main__":
    main()