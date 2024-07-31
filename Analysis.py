import streamlit as st

def compute_cagr(initial_value, final_value, years):
    cagr = (final_value / initial_value) ** (1 / years) - 1
    return cagr

# Streamlit app
def main():
    st.title("CAGR Calculator")
    
    st.write("""
    This app calculates the Compound Annual Growth Rate (CAGR) given the initial value, final value, and the number of years.
    """)
    
    initial_value = st.number_input("Initial Value", min_value=0.0, format="%.2f")
    final_value = st.number_input("Final Value", min_value=0.0, format="%.2f")
    years = st.number_input("Number of Years", min_value=0, format="%d")
    
    if st.button("Calculate CAGR"):
        if initial_value <= 0 or final_value <= 0 or years <= 0:
            st.error("Please enter positive values for all inputs.")
        else:
            cagr = compute_cagr(initial_value, final_value, years)
            st.success(f"The Compound Annual Growth Rate (CAGR) is: {cagr * 100:.2f}%")

if __name__ == "__main__":
    main()
