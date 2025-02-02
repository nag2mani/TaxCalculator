# Income Tax Calculator
According to the new tax regime presented on February 1, 2025, in the Union Budget by Union Finance Minister Nirmala Sitharaman.

## Overview
This is a **Streamlit-based Income Tax Calculator** designed to help users estimate their tax liability under the **New Income Tax Regime (FY 2025-26)** in India. The app provides an easy-to-use interface for entering income details and applying deductions while presenting results in a structured and visually appealing manner.

## Features
- **User-Friendly Interface**: Built with Streamlit, featuring an intuitive layout.
- **Tax Calculation**: Calculates income tax based on the **new tax slabs** and **rebates** applicable for FY 2025-26.
- **Standard Deduction**: Option to apply a **₹75,000 standard deduction**.
- **Dynamic Tax Breakdown**: Shows estimated tax amount based on given inputs.

## Tax Slabs and Rates
| Income Range (₹) | Tax Rate |
|------------------|---------|
| 0 - ₹4,00,000    | No Tax  |
| ₹4,00,001 - ₹8,00,000 | 5% |
| ₹8,00,001 - ₹12,00,000 | 10% |
| ₹12,00,001 - ₹16,00,000 | 15% |
| ₹16,00,001 - ₹20,00,000 | 20% |
| ₹20,00,001 - ₹24,00,000 | 25% |
| Above 24,00,000 | 30% |

## Rebate Details (Section 87A)
### New Tax Regime
- A **full rebate for taxable income of up to ₹12 lakhs** or an amount of **₹60,000** is available for taxpayers opting for the new tax regime under **Section 115 BAC(1A)**.
- This means a resident individual with taxable income up to ₹12,00,000 can avail of a rebate of **100% of payable income tax**.

### Important Note
- The rebate applies **only if taxable income does not exceed ₹12 lakh (new regime).
- If income exceeds the rebate limit, tax is applicable based on slab rates without rebate benefits.

## Installation and Usage
### Prerequisites
Ensure you have Python installed on your system.

### Steps to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/nag2mani/TaxCalculator
   ```
2. Navigate to the project directory:
   ```bash
   cd TaxCalculator
   ```
3. Install required dependencies:
   ```bash
   pip install streamlit
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Technologies Used
- **Python**: Backend logic
- **Streamlit**: Frontend UI
- **CSS**: Styling elements

## Author
Developed by **Nagmani Kumar and ChatGpt**
