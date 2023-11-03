import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from xhtml2pdf import pisa
from io import BytesIO
import base64

# Load models
diabetes_model = pickle.load(open('D:\diseaseML\diseaseML/saved models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('D:\diseaseML\diseaseML/saved models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('D:\diseaseML\diseaseML/saved models/parkinsons_model.sav', 'rb'))

diab_diagnosis = ''
heart_diagnosis = ''
parkinsons_diagnosis = ''

# Function to authenticate user
def authenticate(username, password):
    if username == "user" and password == "123":
        return True
    return False

def download_pdf(inputs, diagnosis):
    report_content = f"""
    <html>
        <head>
            <title>Disease Prediction Report</title>pip
        </head>
        <body>
            <h1>User Inputs</h1>
            {inputs}
            <h1>Diagnosis Output</h1>
            {diagnosis}
        </body>
    </html>
    """

    pdf = BytesIO()
    pisa.CreatePDF(report_content, dest=pdf)
    return pdf


# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Main page
st.title("Disease Prediction System")

# Sidebar login section
with st.sidebar:
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password")

# If logged in, show the disease prediction options in the main area
if st.session_state.logged_in:
    selected = option_menu(
        "Multiple Disease Prediction System",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction"],
        icons=["activity", "heart", "person"],
        default_index=0,
    )

    # Diabetes Prediction Page
    if selected == "Diabetes Prediction":
        st.title('Diabetes Prediction using ML')
        
        # Getting the input data from the user
        col1, col2, col3 = st.columns(3)
            
        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')
            
        with col2:
            Glucose = st.text_input('Glucose Level')
        
        with col3:
            BloodPressure = st.text_input('Blood Pressure value')
        
        with col1:
            SkinThickness = st.text_input('Skin Thickness value')
        
        with col2:
            Insulin = st.text_input('Insulin Level')
        
        with col3:
            BMI = st.text_input('BMI value')
        
        with col1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
        with col2:
            Age = st.text_input('Age of the Person')
        
    
    # Code for Prediction
        diab_diagnosis = ''
        if st.button('Diabetes Test Result'):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        st.success(diab_diagnosis)

    # Heart Disease Prediction Page
    if (selected == 'Heart Disease Prediction'):
            
            # page title
        st.title('Heart Disease Prediction using ML')
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            age = st.text_input('Age')
            
        with col2:
            sex = st.text_input('Sex')
            
        with col3:
            cp = st.text_input('Chest Pain types')
            
        with col1:
            trestbps = st.text_input('Resting Blood Pressure')
            
        with col2:
            chol = st.text_input('Serum Cholestoral in mg/dl')
            
        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
            
        with col1:
            restecg = st.text_input('Resting Electrocardiographic results')
            
        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved')
            
        with col3:
            exang = st.text_input('Exercise Induced Angina')
            
        with col1:
            oldpeak = st.text_input('ST depression induced by exercise')
            
        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')
            
        with col3:
            ca = st.text_input('Major vessels colored by flourosopy')
            
        with col1:
            thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')    
            
        age = float(age)
        sex = float(sex)
        cp = float(cp)
        trestbps = float(trestbps)
        chol = float(chol)
        fbs = float(fbs)
        restecg = float(restecg)
        thalach = float(thalach)
        exang = float(exang)
        oldpeak = float(oldpeak)
        slope = float(slope)
        ca = float(ca)
        thal = float(thal)    

            
        # code for Prediction
        heart_diagnosis = ''
        
        # creating a button for Prediction
        
        if st.button('Heart Disease Test Result'):
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
            
            if (heart_prediction[0] == 1):
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        st.success(heart_diagnosis)
            

    if (selected == "Parkinsons Prediction"):
            
            # page title
            st.title("Parkinson's Disease Prediction using ML")
            
            col1, col2, col3, col4, col5 = st.columns(5)  
            
            with col1:
                fo = st.text_input('MDVP:Fo(Hz)')
                
            with col2:
                fhi = st.text_input('MDVP:Fhi(Hz)')
                
            with col3:
                flo = st.text_input('MDVP:Flo(Hz)')
                
            with col4:
                Jitter_percent = st.text_input('MDVP:Jitter(%)')
                
            with col5:
                Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
                
            with col1:
                RAP = st.text_input('MDVP:RAP')
                
            with col2:
                PPQ = st.text_input('MDVP:PPQ')
                
            with col3:
                DDP = st.text_input('Jitter:DDP')
                
            with col4:
                Shimmer = st.text_input('MDVP:Shimmer')
                
            with col5:
                Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
                
            with col1:
                APQ3 = st.text_input('Shimmer:APQ3')
                
            with col2:
                APQ5 = st.text_input('Shimmer:APQ5')
                
            with col3:
                APQ = st.text_input('MDVP:APQ')
                
            with col4:
                DDA = st.text_input('Shimmer:DDA')
                
            with col5:
                NHR = st.text_input('NHR')
                
            with col1:
                HNR = st.text_input('HNR')
                
            with col2:
                RPDE = st.text_input('RPDE')
                
            with col3:
                DFA = st.text_input('DFA')
                
            with col4:
                spread1 = st.text_input('spread1')
                
            with col5:
                spread2 = st.text_input('spread2')
                
            with col1:
                D2 = st.text_input('D2')
                
            with col2:
                PPE = st.text_input('PPE')

            # code for Prediction
            parkinsons_diagnosis = ''
            
            # creating a button for Prediction    
            if st.button("Parkinson's Test Result"):
                parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
                
                if (parkinsons_prediction[0] == 1):
                    parkinsons_diagnosis = "The person has Parkinson's disease"
                else:
                    parkinsons_diagnosis = "The person does not have Parkinson's disease"
                
            st.success(parkinsons_diagnosis)
            

            
def download_pdf(inputs, diagnosis):
    report_content = f"""
    <html>
        <head>
            <title>Disease Prediction Report</title>
        </head>
        <body>
            <h1>User Inputs</h1>
            {inputs}
            <h1>Diagnosis Output</h1>
            {diagnosis}
        </body>
    </html>
    """

    pdf = BytesIO()
    pisa.CreatePDF(report_content, dest=pdf)
    return pdf

# Button to trigger the PDF generation and download
if st.button("Generate PDF Report"):
    # Capture user inputs and diagnosis
    inputs = ""
    diagnosis = ""
    

    if selected == "Diabetes Prediction":
        inputs = f"""
           <h3> <p>Number of Pregnancies: {Pregnancies}</p>
            <p>Glucose Level: {Glucose}</p>
            <p>Blood Pressure Value: {BloodPressure}</p>
            <p>Skin Thickness Value: {SkinThickness}</p>
            <p>Insulin Level: {Insulin}</p>
            <p>BMI: {BMI}</p>
            <p>Diabetes Pedigree Function value: {DiabetesPedigreeFunction}</p>
            <p>Age of the Person: {Age}</p></h3>
        """
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        diagnosis = f"<h1><u><p>{diab_diagnosis}</p></u></h1>"
    elif selected == "Heart Disease Prediction":
        inputs = f"""
            <h3><p>Age: {age}</p>
            <p>Sex: {sex}</p>
            <p>Chest Pain types: {cp}</p>
            <p>Resting Blood Pressure: {trestbps}</p>
            <p>Serum Cholestoral in mg/dl: {chol}</p>
            <p>Fasting Blood Sugar > 120 mg/dl: {fbs}</p>
            <p>Resting Electrocardiographic results: {restecg}</p>
            <p>Maximum Heart Rate achieved: {thalach}</p>
            <p>Exercise Induced Angina: {exang}</p>
            <p>ST depression induced by exercise: {oldpeak}</p>
            <p>Slope of the peak exercise ST segment: {slope}</p>
            <p>Major vessels colored by flourosopy: {ca}</p>
            <p>thal: 0 = normal; 1 = fixed defect; 2 = reversable defect: {thal}</p></h3>
        """
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])
        heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
        diagnosis = f"<h1><u><p>{heart_diagnosis}</p></u></h1>"
    else:
        inputs = f"""
            <h3><p>MDVP:Fo(Hz): {fo}</p>
            <p>MDVP:Fhi(Hz): {fhi}</p>
            <p>MDVP:Flo(Hz): {flo}</p>
            <p>MDVP:Jitter(%): {Jitter_percent}</p>
            <p>MDVP:Jitter(Abs): {Jitter_Abs}</p>
            <p>MDVP:RAP: {RAP}</p>
            <p>MDVP:PPQ: {PPQ}</p>
            <p>Jitter:DDP: {DDP}</p>
            <p>MDVP:Shimmer: {Shimmer}</p>
            <p>MDVP:Shimmer(dB): {Shimmer_dB}</p>
            <p>Shimmer:APQ3: {APQ3}</p>
            <p>Shimmer:APQ5: {APQ5}</p>
            <p>MDVP:APQ: {APQ}</p>
            <p>Shimmer:DDA: {DDA}</p>
            <p>NHR: {NHR}</p>
            <p>HNR: {HNR}</p>
            <p>RPDE: {RPDE}</p>
            <p>DFA: {DFA}</p>
            <p>Spread1: {spread1}</p>
            <p>Spread2: {spread2}</p>
            <p>D2: {D2}</p>
            <p>PPE: {PPE}</p></h3>
        """
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        diagnosis = f"<h1><u><p>{parkinsons_diagnosis}</p></u></h1>"
        
    diab_diagnosis = ''
    heart_diagnosis = ''
    parkinsons_diagnosis = ''

    # Generate PDF with inputs and diagnosis, then download
    pdf = download_pdf(inputs, diagnosis)
    pdf_encoded = base64.b64encode(pdf.getvalue()).decode('utf-8')
    href = f'<a href="data:application/pdf;base64,{pdf_encoded}" download="disease_prediction_report.pdf">Download PDF</a>'
    st.markdown(href, unsafe_allow_html=True)