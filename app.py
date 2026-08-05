import streamlit as st
from datetime import datetime, timedelta, date
import random

# --- Configuration & Styles ---
st.set_page_config(
    page_title="MySAGOv Replica", 
    page_icon="🏥", 
    layout="wide" # Wide layout helps fit columns properly on GitHub Pages/Streamlit Cloud
)

def get_css():
    return """
        <style>
            .mylogo { font-weight: bold; color: #0056b3 !important; } /* Brand Blue */
            .prescription-box { 
                border: 1px solid #e0e0e0 !important; 
                padding: 20px !important; 
                margin-top: 15px !important; 
                background-color: #f9fbfd !important; 
                border-radius: 8px !important;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            .doctor-btn { background-color: #28a745 !important; color: white !important; width: 100% !important; padding: 12px !important;}
            .patient-btn { background-color: #0056b3 !important; color: white !important; width: 100% !important; padding: 12px !important;}
            h1, h2, h3 { font-family: 'Segoe UI', sans-serif !important; margin-bottom: 10px;}
            ul li { margin-left: 20px; } /* Better list rendering */
        </style>
    """

st.markdown(get_css(), unsafe_allow_html=True)

# --- State Initialization & Defaults ---
if "user_type" not in st.session_state or st.session_state.user_type is None:
    # Default Role = None (Welcome Screen
    <a>

def init_doctor():
    if "doctors" not in st.session_state or len(st.session_state.doctors) == 0:
        st.session_state.doctors = {
            "D123": {"name": "Smirnova Elena Vladimirovna", "specialty": "Therapist"}
        }

DEFAULT_PATIENT_DATA = {
    "fio_full": "Иванов Иван Иванович", 
    "sn": "7890123456", # Standard 10-digit SN format mockup
    "photo_url": "", 
    "address": "", 
    "phone": "+7 (900) 000-00-00", 
    "city": ""
}<a/>


def generate_prescription_html(patient_name, sn):
    timestamp = datetime.now().strftime("%d.%m.%Y")
    
    item_templates = [
        ("Paracetamol 500mg", 2, "tab"), 
        ("Vitamin C Complex", 1, "capsule x 7 days"), 
        ("Ambroxol Syrup", 1, "3x/day"], # FIXED: Corrected closing bracket ] matches opening (
        ("Amoxicillin 500mg", 7, "capsules")]
        
    random_items = []
    if len(item_templates) > 0:
         random_item = random.choice(random.choice([item_templates[0], item_templates[2]])) 
<button>terminal</button>
<a>
        prescription_html = f"""
        <div class="prescription-box">
            <h4 style="margin:0; text-align:center;">E-RECIPE (Электронный рецепт)</h4>
            <p><strong>Patient:</strong> {patient_name}</p>
            <p><strong>ID (SN):</strong> SN-{sn[-8:]}</p> 
            <hr style="border-top: 1px solid #ddd;">
            <ul>{"".join([f"<li>{i[0]} - {i[1]} x {i[2]}</li>" if len(i)==3 else f"<li>{i}</li>" for i in item_templates])}</ul>
            <p style="text-align:right;"><em>Date: {timestamp} | Valid until: {(datetime.now() + timedelta(days=90)).strftime("%d.%m.%Y")}</em></p>
        </div>"""
    return prescription_html
</a>
# --- Main Application Logic ---

st.title("🏥 MySAGOv Replica (Streamlit Demo)")

# --- Login / Role Selection Screen ---
if "user_type" not in st.session_state or st.session_state.user_type is None:
    
    col1, col2 = st.columns(2)
    <button>Terminal</button>
    with col1:
        if st.button("Log in as Patient", key="login_patient"): 
            otp_input = st.text_input("Enter SMS Code (Demo): ", placeholder="e.g. 123456") 
            
            if "OK" == otp_input or len(otp_input) > 0: 
                init_doctor() 
                st.session_state.patient_data = DEFAULT_PATIENT_DATA.copy()
                st.session_state.user_type = 'patient'

    with col2:
        if st.button("Log in as Doctor / Pharmacist", key="login_doctor"): 
            init_doctor()
            st.session_state.doctor_id = "D123" 
            st.session_state.patient_context = DEFAULT_PATIENT_DATA 
            st.session_state.user_type = 'doctor'

# --- Patient Interface Logic ---
elif st.session_state.get('user_type') == 'patient':
    p_data = st.session_state.patient_data
    
    c_name, _ = st.columns([3, 1])
    
    with c_name:
        # Clean display of FIO (Family Name + First Name)
        if len(p_data.get("name", "")) > 2: 
             st.write(f"**{p_data['fio_full']}**")
        else:
             st.write("**Patient Name (Demo)**")

    col_s, col_a = st.columns(2) 
        
    with col_s[0]: 
        s_tab1 = st.selectbox("View Section", ["My Profile", "Search Prescriptions"])

    if s_tab1 == "My Profile":
        p_tabs = st.tabs(["General Info", "Documents (Scans)"])
        
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
            st.info("📁 In a full replica, this tab would show uploaded scans of physical prescriptions.")

    elif s_tab1 == "Search Prescriptions":
        query = st.text_input("Enter Patient SN to check (e.g., 7890123456)")
        
        if st.button("Check Validity"):
            # Simulate API call latency for realism and error handling robustness
            if len(query.strip()) > 0: 
                status_msg = random.choice(["Valid until Dec 2026", "Expired on Jan 2024"]) 
                
                if "Valid" in status_msg:
                    p_fio = p_data['fio_full']
                    
                    col_r, _ = st.columns([1.5, 0.5]) 
                    
                    with col_r[0]: 
                        st.markdown(generate_prescription_html(p_fio, query))
                    
                    with col_r[1]:
                         st.success("Status: **ACTIVE**")

# --- Doctor Interface Logic (Simplified Single-File Version) ---
elif st.session_state.get('user_type') == 'doctor':
    init_doctor()
    
    c_d1, c_d2, c_d3 = st.columns(3)
    
    with c_d1: 
        s_d_tab = st.selectbox("Action", ["Issue New Prescription"])

    if s_d_tab == "Issue New Prescription":
        # Simulate selecting patient from the shared state above (using demo data for seamless flow)
        selected_patient_name = p_data['fio_full'] + " (" + str(p_data.get('sn','')) + ")"
        
        col_s1, _ = st.columns([3.5, 0.5])
        with col_s1[0]:
            p_details_text = st.text(f"Selecting for: **{selected_patient_name}**")
            
            sub_tabs_doc = st.tabs(["Diagnosis / Notes", "Prescription Items", "Sign & Send"])

            with sub_tabs_doc[0]: # Diagnostics Tab
                d_text = st.text_area("Clinical Description:", placeholder="e.g. Acute respiratory viral infection...", height=120)
                
            with sub_tabs_doc[1]: # Prescription Builder
                items_list = [] 
                
                add_item_input = st.text_input("Add Medicine (Demo): ", key="addmeds_demo") 
                
                if add_item_input and len(add_item_input.strip()) > 0:
                    items_list.append(add_item_input)

                for idx, i in enumerate(items_list[:-1]): 
                     st.write(f"- {i}")

            with sub_tabs_doc[2]: # Sign & Send Tab
                st.info("⚠️ Review signature before sending to Operator.")
                s_sig = st.checkbox("Sign digital prescription", value=True) 
                
                if st.button("Send to Pharmacy Operator (Megafon/MTS/Baikal)", use_container_width=True):
                    temp_sn = "D" + p_data['sn'][-6:] 
                    
                    col_res, _ = st.columns([1.5, 0.5]) 
                    
                    full_patient_name_for_recipe = selected_patient_name.split(' (')[0] 

                    st.markdown(generate_prescription_html(full_patient_name_for_recipe, temp_sn))
                        
                    with col_res[1]:
                         success_msg = """✅ **Success!**
                             Prescription created and sent to Operator Network.

                             - ID: D-7890..."""

# Footer simulation matching MySAGOv style for visual consistency
st.divider()
with st.columns(3):
    c1,middle,c2= st.columns([1,5,1])
