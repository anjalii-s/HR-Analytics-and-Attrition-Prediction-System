**📊 HR Analytics Dashboard – Interactive Data Visualization & Attrition Prediction**

**🔎 Overview**

This project delivers an interactive HR Analytics dashboard built with Python and Jupyter widgets. It enables data exploration, machine learning model training, and employee attrition prediction. The system is designed with Human-Computer Interaction (HCI) principles to make advanced analytics accessible to both technical and non-technical HR professionals.

**Features**

Data Exploration Tab

Dataset overview, statistics, and visualizations (attrition distribution, age histogram)

Model Training Tab

One-click training of a Random Forest classifier

Feedback on available/missing features

Accuracy and confidence scoring

Prediction Tab

Sliders and dropdowns for employee attributes

Real-time attrition risk prediction with confidence scores

Color-coded risk indicators (🔴 High / 🟢 Low)

**🏗️ Technical Stack**

Python

Pandas / NumPy – Data processing

Scikit-learn – Machine learning

Matplotlib / Seaborn – Visualization

ipywidgets – Interactive UI

🚀 **How to Run**
Place your dataset file as HR_IBM_dataset.csv in the project folder.

Run the script:

bash
python hr_analytics.py
Use the interactive UI to explore data, train models, and predict attrition.

👥 **Target Users**

HR Managers needing quick attrition insights

Team Leads monitoring employee retention risks

Data Analysts exploring HR metrics patterns

📈 **Usability Highlights**

Tab-based workflow for logical progression

Real-time feedback with emojis and status messages

Error handling for missing data or invalid inputs

Tested with HR professionals (high satisfaction scores)

🔮 **Future Enhancements**

Feature importance visualization

Batch processing for multiple employees

Advanced model comparison

HRIS integration for enterprise use

## 🌐 Streamlit + ngrok Version (Colab)

In addition to the Jupyter widgets prototype, I have also created a **Streamlit notebook version** that demonstrates deployment using **ngrok tunneling**.  

This version includes:
- A modern Streamlit UI with sidebar navigation (Dashboard Overview & Employee Explorer)
- Interactive charts built with Plotly
- Search and sorting functionality for employee data
- Secure public access via ngrok (Colab → web browser)

### How to Run (ngrok version)
1. Place your dataset file as `HR_IBM_dataset.csv` in the project folder.  
2. Open the notebook `HR_Analytics_Streamlit_ngrok.ipynb`.  
3. Run all cells.  
4. Copy the generated ngrok public URL and open it in your browser to interact with the dashboard.  

⚠️ **Note:** For security reasons, the ngrok authtoken is not included in the notebook. Please replace the placeholder `"YOUR_NGROK_TOKEN"` with your own token from the [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken).


📜 **License**

This project is licensed under the MIT License – free to use, modify, and distribute.
Dataset used : https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset/data
