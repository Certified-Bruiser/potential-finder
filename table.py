import streamlit as st

st.set_page_config(page_title="🔧 Bodyshop Potential Dashboard", layout="centered")

# 🌈 Custom CSS Styling
st.markdown("""
    <style>
    body {
    .input-title, .output-title {
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 20px;
        text-align: center;
    }
    .input-title {
        color: #3f51b5;
    }
    .output-title {
        color: #2e7d32;
        margin-top: 40px;
    }
    .data-box {
        background-color: #e3f2fd;
        color: #0d47a1;
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        font-size: 1.2rem;
        font-weight: 600;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.05);
        margin-top: 10px;
    }
    .stSelectbox > div > div,
    .stNumberInput > div > input {
        font-weight: 600 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 🚗 Service Logic Data
data = {
    "Luxury": {
        "City A": {"collision_rate": 0.72, "per_car_labour": 45000, "per_car_sales": 85000},
        "City B": {"collision_rate": 0.60, "per_car_labour": 45000, "per_car_sales": 85000},
        "City C": {"collision_rate": 0.48, "per_car_labour": 35000, "per_car_sales": 100000},
        "City D": {"collision_rate": 0.36, "per_car_labour": 35000, "per_car_sales": 100000}
    },
    "Mass Market": {
        "City A": {"collision_rate": 0.84, "per_car_labour": 14000, "per_car_sales": 9000},
        "City B": {"collision_rate": 0.72, "per_car_labour": 125000, "per_car_sales": 9000},
        "City C": {"collision_rate": 0.60, "per_car_labour": 11500, "per_car_sales": 12000},
        "City D": {"collision_rate": 0.48, "per_car_labour": 11500, "per_car_sales": 14000},
        "City E": {"collision_rate": 0.36, "per_car_labour": 11500, "per_car_sales": 14000},
    }
}

# 💳 Main Dashboard Card
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    # 📥 Input Section
    st.markdown("<div class='input-title'>📥 Input Dashboard</div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        brand = st.selectbox("Car Brand", ["Luxury", "Mass Market"])
    with col2:
        city = st.selectbox("City", ["City A", "City B", "City C", "City D", "City E"])
    with col3:
        service_load = st.number_input("Number of Services", min_value=0)

    # 🚫 Invalid Check
    if brand == "Luxury" and city == "City E":
        st.error("🚫 'Luxury' brand is not available in City E.")
        st.stop()

    # 📊 Calculations
    annual_load = service_load * 12
    divisor = 2.3 if brand == "Luxury" else 2.2
    units = round(annual_load / divisor)
    vars = data[brand][city]
    repairs = round((vars["collision_rate"] * units) / 12)
    labour_sales = round(repairs * vars["per_car_labour"])
    parts_sales = round(repairs * vars["per_car_sales"])

    # 📤 Output Section
    st.markdown("<div class='output-title'>📤 Output Estimates</div>", unsafe_allow_html=True)
    col4, col5, col6 = st.columns(3)
    with col4:
        st.markdown("Repairs / Month")
        st.markdown(f"<div class='data-box'>{repairs}</div>", unsafe_allow_html=True)

    with col5:
        st.markdown("Labour Sales / Month")
        st.markdown(f"<div class='data-box'>₹{labour_sales:,}</div>", unsafe_allow_html=True)

    with col6:
        st.markdown("Parts Sales / Month")
        st.markdown(f"<div class='data-box'>₹{parts_sales:,}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
