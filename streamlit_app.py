<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0"> <!-- Supports scaling on smaller screens -->
    <title>MySA Gov | Secure Digital ID</title>
    
    <!-- Icons & Fonts (Standard Roboto/Apple System) -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet" />

    <style>
        :root {
            --sage-green: #008B4F; /* Official MySA Green */
            --bg-color: #FFFFFF;   /* Pure White Background like the real app */
            --text-dark: #1D2936;  /* Dark slate text */
            --text-grey: #6E7C8C;  /* Subtle grey for hints */
            --border-radius-lg: 16px; 
            --shadow-soft: 0 4px 20px rgba(0,0,0,0.05);
        }

        body { 
            margin: 0; padding: 20px; 
            background-color: var(--bg-color); 
            font-family: -apple-system, BlinkMacSystemFont, 'Roboto', sans-serif;
            display: flex; justify-content: center; align-items: center; min-height: 100vh;
            color: var(--text-dark); overflow-x:hidden;
        }

        /* --- Top Header Bar (Like Real App) --- */
        .app-header {
            width: 100%; max-width: 480px; height: 64px;
            display:flex; align-items:center; justify-content:center; position:relative; z-index:2;
        }
        
        .header-logo { font-size: 3rem; letter-spacing: -1.5px;} /* Big Bold Logo Text */

        /* --- Main Login Card (The "App" Container) --- */
        .login-card { 
            background:white; padding-top:-80px; /* Overlap the header slightly for app feel */
            margin-top:-40px; width:100%; max-width:420px; border-radius:var(--border-radius-lg);
            box-shadow: var(--shadow-soft), 0 20px 60px rgba(0,139,79,0.15); /* SAGE Shadow */
            display:flex; flex-direction:column; position:relative; overflow:hidden;
            animation:holog-shake 6s infinite ease-in-out; /* Subtle "Holo" tremble */
        }

        @keyframes holog-shake { 
            0%,100% { transform: translateX(0) rotateY(0deg); }
            1%   { transform: translateX(-1px) rotateY(-1deg); }
            2%   { transform: translateX(2px) rotateY(1deg); }
            5%   { transform: translateX(-3px) rotateY(-1.5deg); }
            6%   { transform: translateX(3px) rotateY(1.5deg);}
            ... /* Simulated continuous micro-tremble */
        }

        .card-content { padding-top:-48px;} 

        h2 { margin-bottom:0.5rem; font-weight:700; color:#1D2936; line-height:1.2; letter-spacing:-0.5px;} 
        p.desc { color:var(--text-grey); margin-bottom:2rem;font-size:1rem;line-height:1.4;}

        /* --- Inputs & Button (Exact MySA Style) --- */
        input[type="text"],input[type="password"]{ 
            width: 95%; padding:1rem 1.2rem;margin-bottom:1rem; border:none; outline:none; 
            background:white;border-radius:8px;font-size:1rem;color:#333;letter-spacing:0.5px;box-shadow:inset 0 -3px 0 #EAEAEA;transition:border-color 0.2s;}
            
            /* Focus ring matches Sage Green exactly like real app */
            input:focus { transform:translateY(-2px); box-shadow: inset 0 -4px 0 var(--sage-green);} 

        .btn-login { 
            width:97%; padding:1rem;background:var(--sage-green); color:white; 
            border:none;font-weight:bold;font-size:1.1rem;border-radius:8px;display:flex;justify-content:center;align-items:center;gap:0.5rem;cursor:pointer;margin-top:-6px; transition:all 0.2s ease;}
        
        .btn-login:hover,.btn-login:focus{ background:#E6F3ED;color:black;} /* Slight darken on hover */

        /* --- Footer Links (Small Text) --- */
        .footer-links { text-align:right;margin-top:2rem;font-size:0.9rem;padding-right:4%; } 
        a.link{ color:var(--text-grey);text-decoration:none;font-weight:500;} 
        a.link:hover { color:var(--sage-green)}


    </style>
</head>
<body id="body-root">

<!-- Top Header Bar -->
<div class="app-header">
     <h1 style="margin:0; font-style:bold;">MySA Gov</h1> <!-- Simple but bold title like app icon -->
</div>

<!-- Main Login Card (Overlapping Effect) -->
<div class="login-card" id="mainCard">

    <div class="card-content">
        
        <!-- OFFICIAL LOGO SVG REPLACEMENT (White Shield, Gold Cross) -->
         <svg viewBox="0 0 256 348.75" xmlns="http://www.w3.org/2000/svg" style="width:180px;height:auto;margin:-2rem auto -1rem;display:block;filter:drop-shadow(0px 4px 6px rgba(0,139,79,0.4)); z-index:1;"> 
             <!-- White Background Base -->
            <circle cx="128" cy="174.37" r="128" fill="#ffffff"/> 
            
            <!-- Inner Shield Shape (Simplified Victoria Arms Style but Cleaned up for SA) -->
            <path d="M128,22 L231.5,99 v118 c0,14-11.3,25.3-25.3,25.3 H89.8 C75.8,264 64.5,252 64.5,238 V99 l103.5,-77 z M64.5,174.37c0,8 6.5,14.6 14.6,14.6h93c8 0 14.5-6.6 14.5-14.6V99l-102,73v75 z" fill="#ffffff"/>
            
            <!-- Red Lions (The Core of SA Arms) -->
            <path d="M128,22 L231.5,99 v118 c0,14-11.3,25.3-25.3,25.3 H89.8 C75.8,264 64.5,252 64.5,238 V99 l103.5,-77 z M64.5,174.37c0,8 6.5,14.6 14.6,14.6h93c8 0 14.5-6.6 14.5-14.6V99l-102,73v75 z" fill="#ffffff"/>
            
            <!-- Gradient Overlay for "Digital" Feel (Subtle Blue Tint) -->
             <defs>
                <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:#EFFFFF; stop-opacity:1" />
                    <stop offset="50%" style="stop-color:#ffffff;" /> 
                    <stop offset="100%" style="stop-color:#D4EDDA;" />
                </linearGradient>
                
                 <!-- Simplified Lion/Cross Icon (Red/Gold - Mimics Victoria Arms but used as decorative border) -->
                 <path d="M96,72h64v38c-5.3,-3.8,-12.5,-6,-20,-6s-14.7,2.2,-20,6V72H96z" fill="#DC2626"/> <!-- Red field base for digital contrast -->
                 <rect x="118" y="70" width="12" height="44" rx="2" fill="#FBBF24"/> <!-- Gold Cross Center -->
            </defs>

             <!-- Shine Effect for Holographic Look (Cyan Overlay) -->
            <path d="M64,99 L76,99 L73,130 L85,130 Z M235,99 L235,130 L214.5,130 L214.5,99 Z " stroke="#ffffff" stroke-width="3" opacity="0.8"/>
         </svg>

        <h2>Welcome back</h2>
        <p class="desc">Sign in securely using your registered MySA ID credentials.</p>

        <form onsubmit="handleLogin(event)">
            <!-- MySA Style: Email Input -->
            <input type="text" id="id" placeholder="Email or mobile number" required autocomplete="username"/>

            <!-- MySA Style: Password Input -->
            <input type="password" id="pass" placeholder="Password" required autocomplete="current-password"/>

             <!-- Holographic Button Effect (Sage Green) -->
            <button class="btn-login" onclick="handleLogin(event)">
                Sign in 
                 <!-- Simple SVG Arrow Icon inside button -->
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M13 7l5.5-4.5m0 13L8.5 17" stroke="#fff"/></svg>
            </button>

            <!-- Footer Links (Exact Placement like Real App) -->
            <div style="text-align:right;margin-top:2rem;padding-right:4%;">
                <a href="#" class="link">Forgot your password?</a><br><br>
                 <span style="font-size:0.8rem; color:#99aaad;">© Government of South Australia | Secure Session</span>
            </div>
        </form>
    </div>

    <!-- Script for simple interaction + Splash Screen Logic -->
    
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script> 
    
    <script>
        // Simple Interaction Handler (Simulates network request) 
        function handleLogin(e) { 
            e.preventDefault(); 
            
            const id = $('#id').val().trim(); 
            
            // Visual feedback: Add a "scanning" animation effect to the button border
            $('.btn-login').html('<svg width="18" height="18" style="margin-left:5px;animation:pulse 1s infinite"><circle cx="9" cy="9" r="7" fill="#fff"/></svg>').css('opacity', '0.8');

            setTimeout(() => { 
                alert(`Success! \nLogged in as: ${id}\n\n(This is your MySA Gov Holographic Clone)`); 
                
                 // Reset button for next time
                const btn = $('.btn-login')[0];
                btn.innerHTML = '<span>Sign In Securely</span><svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M13 7l5.5-4.5m0 13L8.5 17" stroke="#fff"/></svg>';
            }, 1500); 
        }

        $(document).ready(function(){
            let x = -window.scrollX / window.innerWidth; 
            
             // Fade out splash screen after loading to simulate native app behavior
            setTimeout(() => { 
                document.getElementById('app-splash').style.opacity = '0'; 
                setTimeout(() => {
                    document.getElementById('app-splash').remove(); 
                    $('body, .holo-container').css({ opacity:1 }); 
                }, 800);
            }, 2500); // ~2.5 sec delay like real apps
            
             // Add subtle parallax effect (simulated tilt) if mouse moves
             document.querySelector('.form-side').addEventListener('mousemove', function(e){
                 let xAxis = (window.innerWidth / 2 - e.pageX) / 30,
                     yAxis = (window.innerHeight / 2 - e.pageY) / 30;
                 
                  // Apply slight rotation based on cursor position to enhance "Holo" feel
                  this.style.transform = `rotateX(${yAxis}deg) rotateY(${-xAxis}deg)`; 
              });

        });

    </script>

</body>
</html>
