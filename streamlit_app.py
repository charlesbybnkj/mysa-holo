import streamlit as st
from datetime import datetime
import random
import json

# --- Configuration & Styles (Simulating the UI) ---
st.set_page_config(page_title="MySAGOv Replica", page_icon="🏥", layout="wide")

# Custom CSS to mimic the clean, medical look of MySAGOv
def get_css():
    return """
    <style>
        .mylogo { font-weight: bold; color: #0056b3; } /* Approximate brand blue */
        .prescription-box { 
            border: 1px solid #e0e0e0; 
            padding: 20px; 
            margin-top: 10px; 
            background-color: #f9fbfd; 
            border-radius: 8px;
        }
        .doctor-btn { background-color: #28a745; color: white; width: 100%; padding: 12px;}
        .patient-btn { background-color: #0056b3; color: white; width: 100%; padding: 12px;}
        h1, h2, h3 { font-family: 'Segoe UI', sans-serif; }
    </style>
    """

st.markdown(get_css(), unsafe_allow_html=True)

# --- State Management (Simulating Database) ---
if "user_type" not in st.session_state:
    st.session_state.user_type = None
if "doctor_id" not in st.session_state or patient_data not in st.session_state.get("doctors", {}):
    if "patient_data" not in st.session_state:
        # Default Patient Data for Demo Login
        default_patient = {
            "name": "Ivanov Ivan Ivanovich", 
            "sn": "1234567890", 
            "fio_full": "Иванов Иван Иванович", 
            "photo_url": "",
            "address": "",
            "phone": "+7 (900) 000-00-00",
            "city": ""
        }

# --- Helper Functions ---
def init_doctor():
    if st.session_state.doctor_id == None:
        st.session_state.doctors["D123"] = {"name": "Smirnova Elena Vladimirovna", "specialty": "Therapist"}

def get_patient_record(sn):
    # In a real app, this queries the backend. Here we use session state or defaults.
    return st.session_state.patient_data

def generate_prescription(patient_fio, sn):
    timestamp = datetime.now().strftime("%d.%m.%Y")
    
    items = ["Paracetamol 500mg - 2 tabs", "Vitamin C - 1 capsule x 7 days", "Ambroxol - 5ml x 3 times/day"]
    random_items = random.sample(items, min(2, len(items)))
    
    prescription_html = f"""
    <div class="prescription-box">
        <h4 style="margin:0; text-align:center;">E-RECIPE (Электронный рецепт)</h4>
        <p><strong>Patient:</strong> {patient_fio}</p>
        <p><strong>ID:</strong> SN-{sn[-8:]}</p> <!-- Shortened for demo -->
        <hr>
        <ul>{"".join([f"<li>{i}</li>" for i in random_items])}</ul>
        <p style="text-align:right;"><em>Date: {timestamp} | Valid until: {datetime.now().year + 1}.12.31</em></p>
    </div>
    """
    return prescription_html

# --- Main Application Logic ---

st.title("🏥 MySAGOv Replica")

# --- Login / Role Selection Screen ---
if st.session_state.user_type is None:
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Log in as Patient", key="login_patient"):
            # Simulating OTP entry (skipping for brevity, defaulting to demo data)
            otp = st.text_input("Enter SMS Code (Demo): ", placeholder="123456")
            
            if "OK" == otp or len(otp) > 0: 
                init_doctor() # Ensure doctor exists so we can switch later
                st.session_state.patient_data = {
                    "name": "Ivanov Ivan Ivanovich", 
                    "sn": "7890123456", 
                    "fio_full": "Иванов Иван Иванович", 
                    "photo_url": "",
                    "address": "",
                    "phone": "+7 (900) 000-00-00",
                    "city": ""
                }
                st.session_state.user_type = 'patient'
                
    with col2:
        if st.button("Log in as Doctor / Pharmacist", key="login_doctor"):
            init_doctor()
            # Simulate doctor login screen briefly or direct access for demo
            st.session_state.doctor_id = "D123" 
            st.session_state.patient_data = { # Assume same patient context for demo ease, or separate state later
                 "name": "Ivanov Ivan Ivanovich", 
                 "sn": "7890123456", 
                 "fio_full": "Иванов Иван Иванович", 
                 "photo_url": "",
                 "address": "",
                 "phone": "+7 (900) 000-00-00",
                 "city": ""
            }
            st.session_state.user_type = 'doctor'

    st.divider()

# --- Patient Interface ---
elif st.session_state.user_type == 'patient':
    p_data = st.session_state.patient_data
    
    # Header Profile Info
    col_name, _ = st.columns([3, 1])
    
    with col_name:
        if len(p_data.get("name")) > 2: 
             st.write(f"**{p_data['fio_full']}**")
        else:
             st.write("**Patient Name (Demo)**")
             
    with col_name[0]: # Placeholder for photo logic if needed
        
    c1, c2, c3 = st.columns(3)
    
    with c1:
        s_tab1 = c1.selectbox("View", ["My Profile", "Search Prescriptions"])

    if s_tab1 == "My Profile":
        p_tabs = st.tabs(["General Info", "Documents"])
        
        with p_tabs[0]:
            st.markdown(f"""
            <div class="mylogo">Profile Data</div>
            <ul>
                <li><strong>Name:</strong> {p_data['fio_full']}</li>
                <li><strong>ID (SN):</strong> {p_data['sn']}</li> 
                <li><strong>Phone:</strong> {p_data.get('phone', 'N/A')}</li> 
                <li><strong>POLIS / E-Karta Status:</strong> Active</li>
            </ul>
            """, unsafe_allow_html=True)

        with p_tabs[1]:
            st.info("In a full replica, this tab would show uploaded scans of physical prescriptions.")

    elif s_tab1 == "Search Prescriptions":
        query = st.text_input("Enter SN (e.g., 7890123456)")
        if st.button("Check Validity"):
            # Simulate API check against the backend database
            if len(query.strip()) > 0: 
                status = random.choice(["Valid until Dec 2026", "Expired on Jan 2024"]) 
                
                if "Valid" in status:
                    p_fio = p_data['fio_full']
                    sn_short = f"{p_data['sn']}"[:6] + "**" # Masking demo
                    
                    col_r, _ = st.columns([1,1])
                    with col_r[0]: 
                        st.markdown(generate_prescription(p_fio, sn_short))
                    
                    with col_r[1]:
                         st.success("Status: **ACTIVE**")
                         st.info(f"Seller info would appear here (Pharmacy Name, Address).")
                else:
                     st.error("Status: **EXPIRED / NOT FOUND**")

# --- Doctor Interface ---
elif st.session_state.user_type == 'doctor':
    init_doctor()
    d_id = st.session_state.doctor_id
    
    # Simple Doctor Dashboard Simulation
    c1, c2, c3 = st.columns(3)
    
    with c1: 
        s_d_tab = c1.selectbox("Action", ["Issue Prescription", "Verify Patient Data"])

    if s_d_tab == "Issue Prescription":
        # Simulate selecting patient (in real app, this fetches from registry)
        selected_patient_name = p_data['fio_full'] + " (" + str(p_data.get('sn','')) + ")"
        
        col_s, _ = st.columns([3, 1])
        with col_s:
            p_details = st.text(f"Selecting for: **{selected_patient_name}**")
            
            sub_tabs = st.tabs(["Diagnostics", "Prescription Items", "Sign & Send"])

            with sub_tabs[0]:
                d_text = st.text_area("Diagnosis / Description:", placeholder="e.g. Acute respiratory viral infection...", height=100)
                
            with sub_tabs[1]:
                # Simple list builder simulation
                items_list = ["Amoxicillin 500mg"]
                add_item = st.text_input("Add item (Demo): ", key="addmeds") 
                if add_item and len(add_item) > 0:
                    items_list.append(add_item)
                    
                for idx, i in enumerate(items_list[:-1]): # Show all except the new empty one
                    st.write(f"- {i}")

            with sub_tabs[2]:
                st.info("Review signature:")
                s_sig = st.checkbox("Sign digital prescription")
                
                if st.button("Send to Pharmacy Operator", use_container_width=True):
                    if s_sig:
                        temp_sn = "D" + p_data['sn'][-6:] # Generate fake SN fragment for demo
                        
                        col_res, _ = st.columns(2)
                        with col_res[0]: 
                            st.markdown(generate_prescription(p_details.split(' (')[0], f"{p_data['sn']}")) # Simplified call)
                        
                        with col_res[1]:
                             success_msg = """✅ **Success!**
                             Prescription created.
                             
                             - ID: D-7890...
                             - Status: Sent to Operator (Megafon/MTS/Baikal)
                             - SMS Code generated."""
                            
                             st.info(success_msg)

    elif s_d_tab == "Verify Patient Data":
        query_sn = st.text_input("Enter Patient SN")
        if st.button("Find"):
            if len(query_sn.strip()) > 0:
                st.success(f"Found record for SN-{query_sn}") 
                # In real app, load data from backend into session state here

# Footer simulation matching MySAGOv style
st.divider()
with st.columns(3):
    c1,middle,c2= st.columns([1,5,1])
