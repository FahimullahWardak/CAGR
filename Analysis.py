import streamlit as st
import pandas as pd

def compute_cagr(data):
    cagr_results = {}
    years = len(data) - 1
    for column in data.columns:
        initial_value = data[column].iloc[0]
        final_value = data[column].iloc[-1]
        if initial_value > 0 and final_value > 0:
            cagr = (final_value / initial_value) ** (1 / years) - 1
            cagr_results[column] = cagr * 100  # converting to percentage
        else:
            cagr_results[column] = None
    return cagr_results

# Streamlit app
def main():
    st.title("CAGR Calculator for Multiple Columns")
    
    st.write("""
    This app calculates the Compound Annual Growth Rate (CAGR) for all columns in a provided CSV file.
    """)
    
    uploaded_file = st.file_uploader("Choose a CSV file", type=("xls", "xlsx", "csv")
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.write(data)
        
        if st.button("Calculate CAGR"):
            cagr_results = compute_cagr(data)
            cagr_df = pd.DataFrame(list(cagr_results.items()), columns=['Variable', 'CAGR (%)'])
            st.write("CAGR Results:")
            st.write(cagr_df)

if __name__ == "__main__":
    main()
