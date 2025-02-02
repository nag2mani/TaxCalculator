import streamlit as st

def calculate_new_tax(income, apply_standard_deduction):
    standard_deduction = 75000 if apply_standard_deduction else 0
    taxable_income = max(0, income - standard_deduction)
    tax = 0
    
    tax_slabs = [
        (400000, 0.00),
        (800000, 0.05),
        (1200000, 0.10),
        (1600000, 0.15),
        (2000000, 0.20),
        (2400000, 0.25),
        (float('inf'), 0.30),
    ]
    
    previous_slab = 0
    for slab, rate in tax_slabs:
        if taxable_income > previous_slab:
            tax += (min(taxable_income, slab) - previous_slab) * rate
        else:
            break
        previous_slab = slab
    
    rebate = 60000 if taxable_income <= 1200000 else 0
    final_tax = max(0, tax - rebate)
    
    return final_tax

st.title("New Income Tax Regime Calculator")

# Styling the main layout
st.markdown(
    """
    <style>
        .box {
            background-color: #f9f9f9;
            padding: 5px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
            margin-bottom: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Calculator Box
st.markdown("<div class='box'>", unsafe_allow_html=True)
income = st.number_input("Enter Your Total Annual Income (₹):", min_value=0, value=1200000, step=10000)
apply_standard_deduction = st.checkbox("Apply Standard Deduction of ₹75,000")

if st.button("Calculate Tax"):
    tax = calculate_new_tax(income, apply_standard_deduction)
    st.subheader("Your Estimated Tax:")
    st.write(f"**₹ {tax:,.2f}**")
st.markdown("</div>", unsafe_allow_html=True)

# Information Box
st.markdown("<div class='box'>", unsafe_allow_html=True)
st.subheader("Tax Slabs and Rates")
st.markdown("""
- **0 - ₹4,00,000**: No Tax
- **₹4,00,001 - ₹8,00,000**: 5%
- **₹8,00,001 - ₹12,00,000**: 10%
- **₹12,00,001 - ₹16,00,000**: 15%
- **₹16,00,001 - ₹20,00,000**: 20%
- **₹20,00,001 - ₹24,00,000**: 25%
- **₹24,00,001 and Above**: 30%
""")

st.subheader("Tax Rebate under the New Tax Regime")
st.markdown("""
A full rebate for taxable income of up to ₹12 lakhs or an amount of ₹60,000 for the taxpayers opting for the new tax regime under Section 115 BAC(1A).
""")
st.markdown("</div>", unsafe_allow_html=True)


st.markdown("""
---
Author: Nagmani and ChatGpt.  
Let's connect on [LinkedIn](https://www.linkedin.com/in/nag2mani/)
""")