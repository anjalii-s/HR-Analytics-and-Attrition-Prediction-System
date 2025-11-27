# app.py - IBM HR Analytics Dashboard
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="IBM HR Analytics",
    page_icon="🏢",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    font-size: 2.5rem;
    color: #1f77b4;
    text-align: center;
    margin-bottom: 2rem;
}
.metric-card {
    background-color: #f0f2f6;
    padding: 1rem;
    border-radius: 10px;
    margin: 0.5rem;
}
.risk-high { color: #DC143C; font-weight: bold; }
.risk-medium { color: #FF8C00; font-weight: bold; }
.risk-low { color: #2E8B57; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_sample_data():
    """Create sample HR data for demonstration"""
    np.random.seed(42)
    n_employees = 500
    data = {
        'EmployeeID': range(1, n_employees + 1),
        'Age': np.random.randint(22, 60, n_employees),
        'Department': np.random.choice(['Sales','Research & Development','Human Resources'], n_employees, p=[0.4,0.5,0.1]),
        'JobRole': np.random.choice(['Sales Executive','Research Scientist','Manager','Developer'], n_employees),
        'MonthlyIncome': np.random.normal(6500, 2000, n_employees).astype(int),
        'YearsAtCompany': np.random.randint(1, 15, n_employees),
        'JobSatisfaction': np.random.randint(1, 5, n_employees),
        'Overtime': np.random.choice(['Yes','No'], n_employees, p=[0.3,0.7]),
        'BusinessTravel': np.random.choice(['Travel_Rarely','Travel_Frequently','Non-Travel'], n_employees),
        'Attrition': np.random.choice(['Yes','No'], n_employees, p=[0.16,0.84])
    }
    df = pd.DataFrame(data)
    df['MonthlyIncome'] = np.abs(df['MonthlyIncome'])
    return df

def create_dashboard_overview(filtered_df):
    """Main dashboard overview"""
    st.markdown('<h1 class="main-header">🏢 IBM HR Analytics Dashboard</h1>', unsafe_allow_html=True)

    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Total Employees", f"{len(filtered_df):,}")
    with col2: st.metric("Attrition Rate", f"{(filtered_df['Attrition']=='Yes').mean():.1%}")
    with col3: st.metric("Avg Monthly Income", f"${filtered_df['MonthlyIncome'].mean():,.0f}")
    with col4: st.metric("Avg Job Satisfaction", f"{filtered_df['JobSatisfaction'].mean():.1f}/4")

    st.markdown("---")

    # Charts
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📊 Attrition by Department")
        dept_data = filtered_df.groupby('Department')['Attrition'].apply(lambda x: (x=='Yes').mean()).reset_index()
        fig = px.bar(dept_data, x='Department', y='Attrition', title='Department-wise Attrition Rates')
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.subheader("💰 Salary Distribution")
        fig = px.box(filtered_df, x='Attrition', y='MonthlyIncome', color='Attrition', title='Monthly Income by Attrition Status')
        st.plotly_chart(fig, use_container_width=True)

def create_employee_explorer(filtered_df):
    """Interactive employee explorer"""
    st.header("🔍 Employee Data Explorer")
    search_term = st.text_input("Search employees", placeholder="Enter department, job role, etc.")
    sort_by = st.selectbox("Sort by", ['MonthlyIncome','Age','YearsAtCompany','JobSatisfaction'])
    sort_order = st.radio("Order", ["Descending","Ascending"], horizontal=True)
    ascending = (sort_order=="Ascending")
    if search_term:
        mask = filtered_df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)
        display_df = filtered_df[mask].copy()
    else:
        display_df = filtered_df.copy()
    display_df = display_df.sort_values(sort_by, ascending=ascending)
    st.dataframe(display_df[['EmployeeID','Age','Department','JobRole','MonthlyIncome','YearsAtCompany','JobSatisfaction','Attrition']], use_container_width=True, height=400)

def main():
    df = load_sample_data()
    page = st.sidebar.radio("📊 Navigation", ["Dashboard Overview","Employee Explorer"])
    if page=="Dashboard Overview":
        create_dashboard_overview(df)
    elif page=="Employee Explorer":
        create_employee_explorer(df)
    st.markdown("---")
    st.caption("**IBM HR Analytics Dashboard** | Prototype | Built with Streamlit")

if __name__ == "__main__":
    main()
