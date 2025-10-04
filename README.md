 🩺 CTG Guardian: AI for Fetal Health Monitoring

CTG Guardian is a machine learning tool designed to assist clinicians in detecting fetal distress using cardiotocography (CTG) data. It classifies fetal health into **Normal**, **Suspect**, or **Pathologic** categories and provides interpretable insights to support decision-making during labor.


📊 Problem Statement

Every year, thousands of mothers undergo CTG monitoring during labor. These recordings are complex, and subtle signs of fetal distress can be missed. CTG Guardian acts as a second pair of eyes, using machine learning to detect patterns that may indicate risk — potentially saving lives.


💡 Features

- ✅ Classifies CTG data into Normal, Suspect, Pathologic
- ✅ Uses Random Forest for robust performance
- ✅ SHAP-based interpretability for clinical trust
- ✅ Streamlit app for real-time predictions
- ✅ Clean codebase with modular notebooks


📦 Installation & Usage

1. Clone the Repository

```bash
git clone https://github.com/yourusername/ctg_guardian.git
cd ctg_guardian
2. Install Dependencies

Make sure you have Python 3.8+ installed. Then run:

`bash
pip install -r requirements.txt
`

3. Download the Dataset

Download the CTG dataset from Kaggle  
Extract the ZIP and place fetal_health.csv inside the data/ folder:

`
ctg_guardian/
├── data/
│   └── fetal_health.csv
`

4. Train the Model

Run the notebooks in order:

- notebooks/1datapreprocessing.ipynb
- notebooks/2modeltraining.ipynb
- notebooks/3modelevaluation.ipynb
- notebooks/4_interpretability.ipynb

This will save the trained model as ctg_model.pkl in app/model/.

5. Launch the App

Run the Streamlit app:

`bash
streamlit run app/streamlit_app.py
`

6. Use the App

- Enter 21 CTG feature values as comma-separated numbers (e.g., 120,0.5,0.3,...)
- Click submit to get a prediction: Normal, Suspect, or Pathologic
- The app will display the result and highlight any input errors

🛠️ Tech Stack

| Layer         | Tools Used                      |
|---------------|----------------------------------|
| Data Science  | Pandas, Scikit-learn, SHAP       |
| Modeling      | Random Forest                    |
| App Interface | Streamlit                        |
| Deployment    | Local or Streamlit Cloud         |

📬 Contact

Built by SULEIMAN  
📍 Jigawa State, Nigeria  
📧 suleimanidris04@gmail.com.com  
