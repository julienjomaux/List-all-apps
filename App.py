import streamlit as st

st.set_page_config(page_title="Streamlit App Launcher", page_icon="🔗")

st.title("Streamlit App Launcher")
st.write("Welcome! Here are quick links to other Streamlit dashboards:")
st.markdown(
    """
Welcome! Here are quick links to all the apps of GEM Energy Analytics

**Data source:** [Regelleistung.net](https://www.regelleistung.net/)

**More insights:** [GEM Energy Analytics](https://gemenergyanalytics.substack.com/)  
**Connect with me:** [Julien Jomaux](https://www.linkedin.com/in/julien-jomaux/)  
**Email me:** [julien.jomaux@gmail.com](mailto:julien.jomaux@gmail.com)
"""
)


# You can add as many links as you want in this list
apps = [
    {
        "name": "Belgian Balancing Dashboard",
        "url": "https://balancing-be.streamlit.app",
        "desc": "Visualize and explore Belgian grid balancing data, metrics, and insights."
    },

     {
         "name": "FCR capacity prices",
        "url": "https://fcr-heatmap.streamlit.app/",
         "desc": "Display FCR capacity prices from 2021 to 2025"
     }
]

for app in apps:
    st.markdown(
        f"<a href='{app['url']}' target='_blank' style='font-size:1.15em; font-weight:bold;'>{app['name']}</a>",
        unsafe_allow_html=True
    )
    st.write(f"_{app['desc']}_")  # Description in italic
    st.markdown("---")  # Separator line



