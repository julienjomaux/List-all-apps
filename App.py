import streamlit as st

st.set_page_config(page_title="Streamlit App Launcher", page_icon="🔗")

st.title("📊 Streamlit App Launcher")
st.write("Welcome! Here are quick links to other Streamlit dashboards:")

# You can add as many links as you want in this list
apps = [
    {
        "name": "Belgian Balancing Dashboard",
        "url": "https://balancing-be.streamlit.app",
        "desc": "Visualize and explore Belgian grid balancing data, metrics, and insights."
    },
    # Add more apps below as needed!
    # {
    #     "name": "Another Streamlit App",
    #     "url": "https://another-app-url",
    #     "desc": "Short description of what this app does."
    # },
]

for app in apps:
    st.markdown(
        f"<a href='{app['url']}' target='_blank' style='font-size:1.15em; font-weight:bold;'>{app['name']}</a>",
        unsafe_allow_html=True
    )
    st.write(f"_{app['desc']}_")  # Description in italic
    st.markdown("---")  # Separator line
