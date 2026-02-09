import streamlit as st

st.set_page_config(page_title="All Apps from GEM Energy Analytics", page_icon="GEM.webp")
st.title("All Apps from GEM Energy Analytics")
st.markdown("---")  # Separator line

st.markdown(
    """
Welcome! Here are quick links to all the apps of GEM Energy Analytics.

**More insights:** [GEM Energy Analytics](https://gemenergyanalytics.substack.com/)  
**Connect with me:** [Julien Jomaux](https://www.linkedin.com/in/julien-jomaux/)  
**Email me:** [julien.jomaux@gmail.com](mailto:julien.jomaux@gmail.com)

More apps are being created at the moment. If you want to support, please consider becoming a paying member of GEM Energy Analytics. 

Thanks for reading [GEM Energy Analytics](https://gemenergyanalytics.substack.com/).
"""
)
st.markdown("---")

# Categorized Apps

european_balancing = [
    {
        "name": "FCR capacity prices",
        "url": "https://fcr-heatmap.streamlit.app/",
        "desc": "Display FCR capacity prices from 2021 to 2025."
    },
    {
        "name": "German aFRR capacity prices",
        "url": "https://german-capacity-afrr-prices.streamlit.app/",
        "desc": "Display aFRR German capacity prices from 2021 to 2025."
    },
        {
        "name": "Picasso Visualizer - all countries",
        "url": "https://afrr-cbmp-all.streamlit.app/",
        "desc": "Visualize Picasso CBMP data For all European countries."
    },
    {
        "name": "Picasso Visualizer (BE, NL, FR, DE)",
        "url": "https://afrr-cbmp.streamlit.app/",
        "desc": "Visualize Picasso CBMP data for Belgium, Netherlands, France, and Germany."
    }

]
belgian_balancing = [
    {
        "name": "Belgian Balancing Dashboard (Free)",
        "url": "https://balancing-be.streamlit.app",
        "desc": "Visualize and explore Belgian grid balancing data, metrics, and insights."
    },
    {
        "name": "Belgian Imbalance Prices - Real-Time (Free)",
        "url": "https://balancing-be-rt.streamlit.app/",
        "desc": "Show in Real-Time the imbalance prices in Belgium."
    },
    {
        "name": "Belgian FRR capacity auction Results (Free)",
        "url": "https://frr-auctions-be.streamlit.app/",
        "desc": "Show the results of the FRR capacity auctions in Belgium."
    },
    {
        "name": "Imbalance Price 1 minute Belgium (Free)",
        "url": "https://ip1-be.streamlit.app/",
        "desc": "One-minute resolution view of Belgian imbalance price."
    }
]
analytics_day_ahead = [
    {
        "name": "Capture Prices Analytics (NEW!)",
        "url": "https://capture-prices.streamlit.app/",
        "desc": "App for analytics on day-ahead prices and capture rates across European markets."
    }
]

### Helper function for categories
def app_category(title, apps, color, desc_color="#222"):
    st.markdown(
        f"<div style='background-color:{color}; padding: 1rem; border-radius:8px; margin-bottom:2rem;'>"
        f"<h3 style='color:white'>{title}</h3>",
        unsafe_allow_html=True
    )
    for app in apps:
        st.markdown(
            f"<a href='{app['url']}' target='_blank' style='font-size:1.18em; font-weight:bold; color:blue;'>{app['name']}</a>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<span style='color:{desc_color}; font-style: italic; background-color:rgba(255,255,255,0.7); padding:2px 5px; border-radius:4px;'>{app['desc']}</span>"
            "<br><br>",
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)


# Display each category with a different color for clear visual separation
app_category("Belgian Balancing (Free)", belgian_balancing, "#F76A1A")  # Elia/Orange
app_category("European Balancing", european_balancing, "#378986") # Petrol blue
app_category("Analytics on Day-ahead prices", analytics_day_ahead, "#222") # Dark grey/black

st.markdown("---")

st.info("More categories will be added soon! If you have suggestions, please get in touch.")





