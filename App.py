import streamlit as st

st.set_page_config(page_title="All Apps from GEM Energy Analytics", page_icon="GEM.webp")
st.title("All Apps from GEM Energy Analytics")
st.markdown("---")  # Separator line

st.markdown(
    """
Welcome! Here are quick links to all the apps of GEM Energy Analytics.

**More insights:** GEM Energy Analytics  
**Connect with me:** [Julien Jomaux 
**Email me:** julien.jomaux@gmail.com

More apps are being created at the moment. Register here. 

Thanks for reading GEM Energy Analytics and for supporting the GEM Energy Apps.
"""
)
st.markdown("---")

# Categorized Apps
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
        "name": "Imbalance Price 1 minute Belgium",
        "url": "https://ip1-be.streamlit.app/",
        "desc": "One-minute resolution view of Belgian imbalance price."
    }
]

european_balancing = [
