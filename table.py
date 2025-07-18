import streamlit as st

# ✅ Set page config
st.set_page_config(page_title="Calculate your Bodyshop Potential", layout="centered", initial_sidebar_state="collapsed")

# Read the URL parameter (?page=...)
page = st.query_params.get("page", "home")

# ---------------- HOME PAGE ----------------
if page == "home":
    st.header("Unlock your BodyShop's True Revenue Potential", divider="gray")
    st.subheader("Are you setting the right revenue goals for your BodyShop?")
    st.subheader("Are your targets achievable, profitable and sustainable?")
    st.markdown(
        """
        This calculator will help you set realistic revenue targets for your BodyShop based on your current performance and industry benchmarks.

        **Key Features:**
        - Set Realistic Revenue Goals
        - Plan the Right Growth Path
        - Control Costs and Maximize Profitability
        - Align and Optimize Resources

        **Why use this Tool?**

        - Because most BodyShops chase vague KPIs, suffer from under-performance and overspending.
        - BodyShopGuru helps you fix the math before it breaks the business.
        - Contact us to learn more about how we can help you optimize your BodyShop's performance and profitability.
        """
    )

    # Add red "Get Started" button at the bottom
    st.markdown(
        """
        <div style='text-align: center; margin-top: 2rem;'>
            <a href="/?page=calculator" target="_self">
                <button style='background-color: #e53935; color: white; padding: 0.75rem 2rem; font-size: 1.1rem; border: none; border-radius: 8px; cursor: pointer;'>
                    Get Started
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- CALCULATOR PAGE ----------------
elif page == "calculator":

    st.markdown("<h1 style='text-align: center;'>BodyShop Potential Calculator</h1>", unsafe_allow_html=True)

    # 💅 Calculator Styling
    st.markdown("""
        <style>
        .input-title, .output-title {
            font-size: 1.4rem;
            font-weight: 700;
            margin-top: 20px;
            margin-bottom: 10px;
            text-align: center;
        }
        .input-title {
            color: #3f51b5;
        }
        .output-title {
            color: #2e7d32;
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
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    # 💼 Calculator Logic
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

    # 📥 Input Form
    st.markdown("<div class='input-title'>📥 Input </div>", unsafe_allow_html=True)

    with st.form("calculator_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            brand = st.selectbox("Car Brand Type", ["Luxury", "Mass Market"])
        with col2:
            city = st.selectbox("City Category", ["City A", "City B", "City C", "City D", "City E"])
        with col3:
            service_load = st.number_input("Last 6 Months Service (PMGR + B&P)", min_value=0)

        submitted = st.form_submit_button("Submit")

        if submitted:
            if brand == "Luxury" and city == "City E":
                st.error("🚫 'Luxury' brand is not available in City E.")
            else:
                annual_load = service_load * 12
                divisor = 2.3 if brand == "Luxury" else 2.2
                units = round(annual_load / divisor)
                vars = data[brand][city]
                repairs = round((vars["collision_rate"] * units) / 12)
                labour_sales = round(repairs * vars["per_car_labour"])
                parts_sales = round(repairs * vars["per_car_sales"])

                def to_indian_notation(x):
                    if x >= 1_00_00_000:
                        return f"{x // 1_00_00_000}Cr"
                    elif x >= 1_00_000:
                        return f"{x // 1_00_000}L"
                    elif x >= 1_000:
                        return f"{x // 1_000}K"
                    return str(x)

                # 📤 Output Section
                st.markdown("<div class='output-title'>📤 Potential</div>", unsafe_allow_html=True)
                col4, col5, col6 = st.columns(3)
                with col4:
                    st.markdown("Repairs / Month")
                    st.markdown(f"<div class='data-box'>{repairs}</div>", unsafe_allow_html=True)
                with col5:
                    st.markdown("Labour Sales / Month")
                    st.markdown(f"<div class='data-box'>₹{to_indian_notation(labour_sales)}</div>", unsafe_allow_html=True)
                with col6:
                    st.markdown("Parts Sales / Month")
                    st.markdown(f"<div class='data-box'>₹{to_indian_notation(parts_sales)}</div>", unsafe_allow_html=True)
