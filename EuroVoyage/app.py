import streamlit as st
from pathlib import Path
from datetime import date
import pandas as pd

# ============================================================
# EUROVOYAGE — EUROPE TRAVEL FINDER
# GitHub-ready Streamlit app
# ============================================================

st.set_page_config(
    page_title="EuroVoyage — Europe Travel Finder",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "trips.csv"


# ------------------------------------------------------------
# Styling
# ------------------------------------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: "Inter", sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 0%, #17365b 0, transparent 35%),
        linear-gradient(135deg, #07111f, #091727 55%, #070d18);
    color: #eef6ff;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

.logo {
    font-size: 25px;
    font-weight: 900;
    letter-spacing: -1px;
}
.logo span { color: #6ee7ff; }

.header-line {
    border-bottom: 1px solid #18304a;
    padding-bottom: 20px;
    margin-bottom: 42px;
}

.eyebrow {
    color: #6ee7ff;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 2px;
}

.hero-title {
    font-size: clamp(45px, 7vw, 78px);
    font-weight: 900;
    line-height: .95;
    letter-spacing: -5px;
    max-width: 850px;
    margin-top: 15px;
}

.hero-text {
    color: #91a5bc;
    font-size: 17px;
    line-height: 1.6;
    max-width: 680px;
    margin-top: 20px;
}

.search-box {
    background: #0d1b2c;
    border: 1px solid #29435f;
    border-radius: 24px;
    padding: 24px;
    margin-top: 35px;
    box-shadow: 0 25px 80px rgba(0,0,0,.45);
}

.travel-card {
    background: linear-gradient(145deg, #0d1b2d, #0a1625);
    border: 1px solid #203852;
    border-radius: 20px;
    padding: 22px;
    margin-bottom: 16px;
    min-height: 285px;
}

.travel-card:hover {
    border-color: #3e668d;
}

.mode {
    color: #6ee7ff;
    font-size: 12px;
    font-weight: 800;
}

.route {
    font-size: 21px;
    font-weight: 850;
    margin-top: 16px;
}

.operator {
    color: #91a5bc;
    font-size: 12px;
    margin-top: 5px;
}

.meta {
    color: #b7c7d8;
    font-size: 13px;
    margin-top: 18px;
}

.price-label {
    color: #91a5bc;
    font-size: 11px;
    margin-top: 18px;
}

.price {
    font-size: 30px;
    font-weight: 900;
}

.direct {
    background: #113a2b;
    color: #67e8a5;
    padding: 5px 9px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 700;
}

.stButton > button {
    border-radius: 12px;
    border: 1px solid #29435f;
    background: #0b1828;
    color: #eef6ff;
    font-weight: 700;
}

.stButton > button:hover {
    border-color: #6ee7ff;
    color: #6ee7ff;
}

.footer {
    border-top: 1px solid #18304a;
    margin-top: 50px;
    padding-top: 25px;
    color: #71869d;
    font-size: 12px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


# ------------------------------------------------------------
# Data
# ------------------------------------------------------------

@st.cache_data
def load_trips():
    if not DATA_FILE.exists():
        st.error("The data/trips.csv file is missing.")
        return pd.DataFrame()

    return pd.read_csv(DATA_FILE)


df = load_trips()


def format_duration(minutes):
    minutes = int(minutes)
    hours, mins = divmod(minutes, 60)

    if hours == 0:
        return f"{mins}m"
    if mins == 0:
        return f"{hours}h"
    return f"{hours}h {mins}m"


def format_price(price):
    return f"€{float(price):.2f}"


# ------------------------------------------------------------
# Header
# ------------------------------------------------------------

st.markdown("""
<div class="header-line">
    <div style="display:flex;justify-content:space-between;align-items:center;">
        <div class="logo">Euro<span>Voyage</span> ✦</div>
        <div style="color:#91a5bc;font-size:14px;">
            Explore &nbsp; Trains &nbsp; Buses &nbsp; Flights
            &nbsp;&nbsp;
            <span style="border:1px solid #2a4867;border-radius:999px;padding:8px 13px;color:#eef6ff;">
                EUR · Europe
            </span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ------------------------------------------------------------
# Hero
# ------------------------------------------------------------

st.markdown('<div class="eyebrow">ONE SEARCH · EVERY WAY TO GO</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="hero-title">Find your fastest way across Europe.</div>',
    unsafe_allow_html=True,
)

st.markdown("""
<div class="hero-text">
Compare flights, high-speed trains and coaches in one clean view.
Prices in this prototype are sample/indicative fares. A production
version should replace them with live carrier or travel-provider data.
</div>
""", unsafe_allow_html=True)


# ------------------------------------------------------------
# Search
# ------------------------------------------------------------

st.markdown('<div class="search-box">', unsafe_allow_html=True)

c1, c2, c3, c4, c5 = st.columns([1.2, 1.2, 1, 1, .8])

with c1:
    from_city = st.text_input("FROM", value="London",
                              placeholder="City or airport")

with c2:
    to_city = st.text_input("TO", value="Paris",
                            placeholder="City or airport")

with c3:
    travel_date = st.date_input("DATE", value=date.today())

with c4:
    passengers = st.selectbox(
        "PASSENGERS",
        ["1 traveller", "2 travellers", "3 travellers", "4 travellers"],
    )

with c5:
    st.markdown("<br>", unsafe_allow_html=True)
    search_clicked = st.button(
        "Search trips",
        type="primary",
        use_container_width=True,
    )

st.markdown("</div>", unsafe_allow_html=True)


# ------------------------------------------------------------
# Filters
# ------------------------------------------------------------

filter_col, sort_col = st.columns([3, 1])

with filter_col:
    transport = st.radio(
        "TRANSPORT",
        ["All", "✈ Flights", "🚆 Trains", "🚌 Buses"],
        horizontal=True,
    )

with sort_col:
    sorting = st.selectbox(
        "SORT BY",
        ["Recommended", "Lowest price", "Shortest trip"],
    )


# ------------------------------------------------------------
# Filtering
# ------------------------------------------------------------

filtered = df.copy()

if search_clicked:
    f = from_city.strip().lower()
    t = to_city.strip().lower()

    if f:
        filtered = filtered[
            filtered["from"].str.lower().str.contains(f, na=False)
        ]

    if t:
        filtered = filtered[
            filtered["to"].str.lower().str.contains(t, na=False)
        ]

if transport == "✈ Flights":
    filtered = filtered[filtered["mode"] == "Flight"]
elif transport == "🚆 Trains":
    filtered = filtered[filtered["mode"] == "Train"]
elif transport == "🚌 Buses":
    filtered = filtered[filtered["mode"] == "Bus"]

if sorting == "Lowest price":
    filtered = filtered.sort_values("price")
elif sorting == "Shortest trip":
    filtered = filtered.sort_values("duration_minutes")


# ------------------------------------------------------------
# Results
# ------------------------------------------------------------

st.markdown(
    f"""
    <div style="color:#91a5bc;font-size:13px;margin:20px 0;">
        {len(filtered)} options · one-way indicative fares ·
        travel date: {travel_date.strftime("%d %b %Y")} · {passengers}
    </div>
    """,
    unsafe_allow_html=True,
)

if filtered.empty:
    st.markdown("""
    <div class="travel-card" style="text-align:center;padding-top:55px;">
        <div style="font-size:42px;">🌍</div>
        <h3>No trips found</h3>
        <p style="color:#91a5bc;">
            Try another city or switch the transport filter.
        </p>
    </div>
    """, unsafe_allow_html=True)

else:
    cols = st.columns(3)

    for i, (_, trip) in enumerate(filtered.iterrows()):
        with cols[i % 3]:

            st.markdown(f"""
            <div class="travel-card">

                <div style="display:flex;justify-content:space-between;">
                    <div class="mode">
                        {trip["icon"]} {trip["mode"].upper()}
                    </div>
                    <div class="direct">DIRECT</div>
                </div>

                <div class="route">
                    {trip["from"]} → {trip["to"]}
                </div>

                <div class="operator">
                    {trip["operator"]} · {trip["note"]}
                </div>

                <div class="meta">
                    ◷ {format_duration(trip["duration_minutes"])}
                    &nbsp;&nbsp; ↪ {trip["stops"]}
                </div>

                <div class="price-label">FROM</div>
                <div class="price">{format_price(trip["price"])}</div>

            </div>
            """, unsafe_allow_html=True)

            if st.button(
                f"View {trip['operator']} deal",
                key=f"deal_{i}_{trip['from']}_{trip['to']}",
                use_container_width=True,
            ):
                st.info(
                    f"Demo selection: {trip['operator']} · "
                    f"{trip['from']} → {trip['to']} · "
                    f"{format_price(trip['price'])}"
                )


# ------------------------------------------------------------
# Feature section
# ------------------------------------------------------------

st.markdown("---")
st.markdown("## Why EuroVoyage?")

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    ### ⚡ Compare instantly
    See flights, trains and buses together instead of checking
    multiple websites.
    """)

with f2:
    st.markdown("""
    ### 💶 Find better fares
    Sort results by price and quickly identify lower-cost options.
    """)

with f3:
    st.markdown("""
    ### 🗺️ Travel smarter
    Compare journey duration and direct connections before choosing.
    """)


# ------------------------------------------------------------
# Footer
# ------------------------------------------------------------

st.markdown("""
<div class="footer">
EuroVoyage prototype · Sample fares only. Verify final price,
availability, baggage and booking conditions with the provider.
</div>
""", unsafe_allow_html=True)
