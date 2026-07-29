import streamlit as st
from time import sleep # Import needed for loading animation

# Set up page config for "App-like" feel
st.set_page_config(page_title="MySA Gov - Secure Digital ID", layout='centered')

# Custom CSS to match MySA design exactly (Wrapped in markdown with unsafe flag)
st.markdown("""
    <style>
        body { background-color: #f4fbf9; font-family: 'Roboto', sans-serif; padding-top: 60px; } 
        
        .my-sa-header { 
            text-align: center; 
            color:white; 
            font-size:3rem;
            letter-spacing: -1.5px;
            position:relative; z-index:2; top:-50px;} 

        .login-card-container {
            background:#fff; padding-top:-80px; /* Overlap effect */
            max-width: 420px; margin-top:-40px; width:95%;
            border-radius: var(--border-radius-lg); box-shadow: 0 4px 20px rgba(0,139,79,0.15);
            display:flex; flex-direction:column; align-items:center; justify-content:center;
            animation:holog-shake 6s infinite ease-in-out; 
        }

        @keyframes holog-shake { 
            0%,100% { transform: translateX(0) rotateY(0deg); }
            1%   { transform: translateX(-1px) rotateY(-1deg); }
            2%   { transform: translateX(2px) rotateY(1deg); }
            5%   { transform: translateX(-3px) rotateY(-1.5deg); }
            6%   { transform: translateX(3px) rotateY(1.5deg);}
        }

        .custom-title { margin-bottom:0.5rem; font-weight:700; color:#1D2936;} 
        .desc-text { color:#6E7C8C;margin-bottom:2rem;font-size:1rem;line-height:1.4;text-align:center;}

        /* Input Styles */
        input[type="text"],input[type="password"]{ 
            width: 95%; padding:1rem 1.2rem;margin-bottom:1rem;border:none; outline:none; 
            background:white;border-radius:8px;font-size:1rem;color:#333;letter-spacing:0.5px;box-shadow:inset 0 -3px 0 #EAEAEA;transition:border-color 0.2s;}
            
            input:focus { transform:translateY(-2px); box-shadow: inset 0 -4px 0 var(--sage-green);} 
            
        :root { --sage-green: #008B4F; }

        /* Button Styles */
        .btn-login { 
            width:97%; padding:1rem;background:#008B4F; color:white; 
            border:none;font-weight:bold;font-size:1.1rem;border-radius:8px;display:flex;justify-content:center;align-items:center;gap:0.5rem;cursor:pointer;margin-top:-6px; transition:all 0.2s ease;}
            
            .btn-login:hover,.btn-login:focus{ background:#E6F3ED;color:black;} 

        /* Footer Links */
        .footer-links { text-align:right;margin-top:2rem;font-size:0.9rem;padding-right:4%; } 
        a.link{ color:#6E7C8C;text-decoration:none;font-weight:500;} 
        a.link:hover { color:#008B4F}

    </style>
""", unsafe_allow_html=True)

# Header (Logo/Title) - Use HTML tags wrapped in markdown for Streamlit compatibility
st.markdown('<h1 class="my-sa-header">MySA Gov</h1>', unsafe_allow_html=True)

# Login Form Container
with st.container(border=False): # Removes default Streamlit border
    
    custom_title = "<h2>Welcome back</h2>" + "<p class='desc-text'>Sign in securely using your registered MySA ID credentials.</p>"
    st.markdown(custom_title, unsafe_allow_html=True)

    user_email = st.text_input("Email or Mobile Number", key="email")
    
    password = st.password_input("Password", key="pass")

    if st.button('Sign In', use_container_width=True):
        if not user_email and not password:
            st.error("Please enter both email/mobile and password.")
        else:
            # Simulate Loading/Scanning Effect (Replace with real auth later)
            for i in range(3): 
                st.write(f"Authenticating... {i+1}...")
                sleep(0.5) # Use 'sleep' instead of time.sleep() for Streamlit compatibility
            
            st.success("Welcome back! Redirecting to dashboard...")


