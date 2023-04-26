import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        m.split_map(
            left_layer='ESA WorldCover 2020 S2 FCC', right_layer='ESA WorldCover 2020'
        )
        m.add_legend(title='ESA Land Cover', builtin_legend='ESA_WorldCover')

m.to_streamlit(height=700)
