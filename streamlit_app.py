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
    
    if st.button('Sign In', use_container_width=True):
        if not user_email:
            st.error("Please enter your email/mobile number.")
        else:
            # Simulate Loading/Scanning Effect (Like reading a chip/card)
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
             # Fallback for demo purposes if email was short during test
             demo_mail = "demo_user"
        else:
            demo_mail = user_email.split('@')[0] + "@sa.gov.au" # Clean up dummy name
            
        # Generate a REALISTIC-looking license using Python strings (No external images needed!)
        
        def generate_realistic_license():
            """Generates random but consistent attributes to simulate a real SA driver."""
            
            # Randomize realistic data ranges
            first_name = f"{random.choice(['J','M','S','R'])}{random.randint(1,9)}{chr(random.randint(65,87))}" # 2-3 chars start like JH1
            last_name = "SMITH" 
            dob_year = str(random.randint(1950, 2004)) + "-" + "".join([str(random.randint(0,9)) for _ in range(2)])+"-" + "".join([str(random.randint(0,9)) for _ in range(2)])
            
            expiry = f"{int(dob_year[0:4]) + random.choice(range(8,16))}-{random.sample('012345', k=1)[0]}-{random.sample('01',k=1)[0]}" # Y-M-D format roughly

            return first_name, last_name, dob_year, expiry

        fname, lname, dob_str, exp_str = generate_realistic_license()

        st.write(f"### Simulated License Data")
        
        col_photo, col_data = st.columns([1.5, 3])
        
        with col_photo:
            st.markdown("""
                <div class="license-card">
                    <!-- Holo Effect -->
                    <div class="holo-scan"></div>
                    
                    <!-- Face Photo (Random realistic face from placeholder service) -->
                    <img id="face-img" src="https://randomuser.me/api/portraits/men/40.jpg" alt="Driver Face">
                </div>
            """, unsafe_allow_html=True)

        with col_data:
            # Create the classic SA License layout text + barcode style
            st.write(f"**Full Name**<br><span style='font-size:1.2rem; font-weight:bold;'>{fname} {lname}</span>")
            st.markdown(f"<p><b>Date of Birth:</b> {dob_str}<br><b>Expires:</b> {exp_str}</p>", unsafe_allow_html=True)
            
            # Simulated Barcode (Visual only, uses CSS to look like a scanner strip)
            bar_width = 300 # Approx width in px for this container size
            bar_height = 50
            bg_color = "#ffffff" # White background typical for SA barcode area
            
            # Generate random bars pattern 
            bar_pattern = "".join([f"{random.choice(['#',' '])}" * random.randint(2,4)] * 15)[:bar_width]
            
            st.markdown(f"<div class='barcode-line' style='width:{bar_width}px; height:{bar_height}px; display:flex; align-items:center;'>{bar_pattern}</div>", unsafe_allow_html=True)

