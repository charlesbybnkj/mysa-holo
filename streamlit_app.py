import streamlit as st
from time import sleep
import random

# --- 1. Initialize Session State (Tracks if user is logged in) ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False 
    st.session_state['user_email'] = "" # Store email for display later

# --- 2. Define Custom CSS (Official MySA Gov Look + Holo Effects) ---
st.markdown("""
    <style>
        body { background-color: #f4fbf9; font-family: -apple-system, BlinkMacSystemFont, 'Roboto', sans-serif; padding-top: 60px; } 
        
        .my-sa-header { text-align: center; color:white; font-size:3rem; letter-spacing: -1.5px; position:relative; z-index:2; top:-50px;} 

        /* The Card Container */
        .card-wrapper { 
            max-width: 80%; margin:auto; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,139,79,0.15);
            display:flex; flex-direction:column; align-items:center; justify-content:center;padding-top:-80px;margin-top:-40px;width:95%}
            
        @keyframes holog-shake { 
            0%,100% { transform: translateX(0) rotateY(0deg); }
            1%   { transform: translateX(-1px) rotateY(-1deg); }
            2%   { transform: translateX(2px) rotateY(1deg); }
            5%   { transform: translateX(-3px) rotateY(-1.5deg); }
            6%   { transform: translateX(3px) rotateY(1.5deg);}
        }

        /* License Card Styles */
        .license-card { 
            width: 90%; height: auto; background:#fff; border-radius:8px; overflow:hidden; position:relative; 
            box-shadow: inset 0 0 20px rgba(0,0,0,0.1), 0 4px 20px rgba(0,139,79,0.2); 
            animation:holog-shake 6s infinite ease-in-out; transition: all 0.3s;
        }

        /* Holo Overlay (The "Scanning" Lines) */
        .holo-scan { 
            position:absolute; top:-5%; left:-5%; right:-5%; bottom:-5%; border-radius:8px; 
            background: linear-gradient(rgba(18, 255, 18, 0), rgba(18, 255, 18, 0)), 
                        repeating-linear-gradient(90deg, transparent, transparent 4%, #fff 4%, #fff 6%),
                        repeating-linear-gradient(0deg, rgba(255,230,230,.1), rgba(255,230,230,.1) 4px ,transparent); 
            mix-blend-mode: overlay; pointer-events:none; z-index:10; opacity:0.7; }

        /* License Content (Face + Barcode) */
        .card-face { padding: 1rem; display:flex; gap:1rem;}
        .photo-area { width: 90px; height: 110px; background:#eee; border-radius:4px; object-fit:center; position:relative;}
        .barcode-area { flex-grow:1; text-align:left; font-family:'Consolas', monospace;}
        
        #face-img{width:100%;height:100%;object-fit:cover;border-radius:3px;}

        .bar-code-line { color:#008B4F; font-size:.65rem; line-height:1.2; letter-spacing:-1px;}
        .qr-placeholder { float:right; width:90px;height:auto;background:url('https://api.qrserver.com/v1/create-qr-code/?size=90x90&data=demo') no-repeat center/contain }

    </style>
""", unsafe_allow_html=True)

# --- 3. Header (Logo/Title) ---
st.markdown('<h1 class="my-sa-header">MySA Gov</h1>', unsafe_allow_html=True)

# --- 4. Main Logic Flow (The "If/Else" Switch) ---

if not st.session_state['logged_in']:
    # === LOGIN FORM VIEW ===
    custom_title = "<h2>Welcome back</h2>" + "<p style='color:#6E7C8C;margin-bottom:2rem;'>Sign in securely using your registered MySA ID credentials.</p>"
    st.markdown(custom_title, unsafe_allow_html=True)

    user_email = st.text_input("Email or Mobile Number", key="email")
    # === LOGIN FORM VIEW (if not logged_in) ===
    custom_title = "<h2>Welcome back</h2>" + "<p style='color:#6E7C8C;margin-bottom:2rem;'>Sign in securely using your registered MySA ID credentials.</p>"
    st.markdown(custom_title, unsafe_allow_html=True)

    user_email = st.text_input("Email or Mobile Number", key="email")
    
    if st.button('Sign In', use_container_width=True):
        if not user_email: # No email entered yet
            st.error("Please enter your email/mobile number.")
            
        elif len(user_email) < 5: # Optional fallback for short emails (e.g., "abc1")  
            demo_mail = "demo_user"
        else: 
            # Clean up dummy name
            demo_mail = user_email.split('@')[0] + "@sa.gov.au" 

# === Simulate Loading/Scanning Effect ===
for i in range(3): 
    st.write(f"Authenticating... {i+1}...")
    sleep(0.5) 

# Mark as logged-in and rerun to show dashboard + generated license
st.session_state['logged_in'] = True
st.rerun()


else: # === DASHBOARD VIEW (Shows Realistic License After Login) ---
    with st.container(border=False): 
         custom_title = "<h2>Driver's License Verified ✅</h2>" + "<p style='color:#6E7C8C;margin-bottom:2rem;'>Welcome back, your secure session is active.</p>"
         st.markdown(custom_title, unsafe_allow_html=True)

        if not user_email or len(user_email) < 5:
             demo_mail = "demo_user"
        else:
            demo_mail = user_email.split('@')[0] + "@sa.gov.au" # Clean up dummy name
            
        def generate_realistic_license():
            """Generates random but consistent attributes to simulate a real SA driver."""
            
            first_name = f"{random.choice(['J','M','S','R'])}{random.randint(1,9)}{chr(random.randint(65,87))}" 
            last_name = "SMITH" 
