# import streamlit as st
# from openai import OpenAI
# import os

# # -------------------------------
# # 🔑 OPENAI CLIENT
# # -------------------------------
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # -------------------------------
# # 💾 SESSION HISTORY
# # -------------------------------
# if "history" not in st.session_state:
#     st.session_state.history = []

# # -------------------------------
# # 🔧 PAGE CONFIG
# # -------------------------------
# st.set_page_config(page_title="PromptForge AI", page_icon="⚡", layout="centered")

# # -------------------------------
# # 🎨 CUSTOM STYLING
# # -------------------------------
# st.markdown("""
# <style>
# .main {
#     background-color: #0e1117;
# }
# h1, h2, h3 {
#     color: #ffffff;
# }
# .stButton>button {
#     background-color: #4CAF50;
#     color: white;
#     border-radius: 10px;
# }
# </style>
# """, unsafe_allow_html=True)

# # -------------------------------
# # 📌 SIDEBAR
# # -------------------------------
# st.sidebar.title("⚡ PromptForge AI")

# page = st.sidebar.radio(
#     "Navigate",
#     ["🏠 Home", "📜 History", "ℹ️ About"]
# )

# # -------------------------------
# # 🧠 FUNCTION: DYNAMIC QUESTIONS
# # -------------------------------
# def generate_questions(intent):

#     if "resume" in intent or "cv" in intent:
#         return [
#             ("1. Basic Info", "Are you a student, fresher, or experienced professional?", "e.g. Fresher"),
#             ("2. Industry", "What is your field/industry?", "e.g. IT, Mechanical"),
#             ("3. Target Role", "What role are you targeting?", "e.g. Software Engineer"),
#             ("4. Background", "Education / projects / experience?", "e.g. B.Tech + ML project"),
#             ("4. Skills", "Key skills?", "e.g. Python, SQL, Communication"),
#             ("6. Style", "Resume style?", "ATS-friendly or creative"),
#             ("7. Output", "1-page or 2-page?", "e.g. 1-page concise"),
#             ("8. Tone", "Tone?", "Formal / Professional")
#         ]

#     elif "image" in intent:
#         return [
#             ("1. Image Type", "What type of image?", "e.g. realistic, cartoon, 3D"),
#             ("2. Subject", "Main subject?", "e.g. person, product, landscape"),
#             ("3. Style", "Art style?", "e.g. cinematic, anime, photorealistic"),
#             ("4. Colors", "Color theme?", "e.g. dark, vibrant, pastel"),
#             ("5. Usage", "Where will it be used?", "e.g. Instagram, thumbnail"),
#             ("6. Details", "Extra details?", "e.g. lighting, background elements"),
#             ("7. Quality", "Resolution?", "HD, 4K, ultra realistic")
#         ]

#     elif "youtube" in intent:
#         return [
#             ("1. Topic", "Video topic?", "e.g. AI tools that save time"),
#             ("2. Audience", "Target audience?", "e.g. students, beginners"),
#             ("3. Duration", "Video length?", "Short or long"),
#             ("4. Style", "Video style?", "Storytelling, educational"),
#             ("5. Goal", "Purpose?", "Views, engagement"),
#             ("6. Platform", "Platform?", "YouTube Shorts / Long"),
#             ("7. Tone", "Tone?", "Energetic, fun")
#         ]

#     else:
#         return [
#             ("1. Goal", "What do you want to achieve?", "e.g. Build a startup idea"),
#             ("2. Context", "Topic or domain?", "e.g. fintech, AI"),
#             ("3. Audience", "Target users?", "e.g. developers"),
#             ("4. Format", "Output format?", "e.g. steps, list"),
#             ("5. Tone", "Tone?", "Professional, casual"),
#             ("6. Constraints", "Any limits?", "e.g. 60 sec, simple language")
#         ]

# # =========================================================
# # 🏠 HOME PAGE
# # =========================================================
# if page == "🏠 Home":

#     st.markdown("## ⚡ ganEEEE Prompt Magic")
#     st.caption("Generate powerful AI prompts with smart guided questions.")

#     st.success("🚀 AI-Powered Prompt Generator | Built by Ganesh")

#     st.markdown("""
# ### ✨ Features
# - 🧠 Smart question-based input
# - 🤖 AI-generated prompts
# - 📜 Prompt history tracking
# - 🌍 Works for multiple use cases
# """)

#     user_input = st.text_input(
#         "What do you want to create?",
#         placeholder="e.g. resume, image, youtube script..."
#     )

#     intent = user_input.strip().lower() if user_input else ""

#     if intent != "":

#         st.info(f"🧠 Smart Mode Activated for: {user_input}")

#         questions = generate_questions(intent)
#         answers = {}

#         st.markdown(f"""
# ### 👋 Let's build your prompt step-by-step

# You said: **{user_input}**

# Answer a few questions to generate a powerful prompt 👇
# """)

#         for title, question, example in questions:
#             st.markdown(f"### {title}")
#             answers[title] = st.text_input(question, placeholder=example, key=title)
#             st.caption(f"👉 Example: {example}")

#         if st.button("🚀 Generate Prompts", use_container_width=True):

#             with st.spinner("Generating AI-powered prompts..."):

#                 prompt_input = f"User wants: {user_input}\n\nDetails:\n"

#                 for key, value in answers.items():
#                     prompt_input += f"{key}: {value}\n"

#                 try:
#                     response = client.chat.completions.create(
#                         model="gpt-4o-mini",
#                         messages=[
#                             {
#                                 "role": "system",
#                                 "content": "You are PromptForge AI. Generate 4 high-quality prompts in Creative, Analytical, Minimal, and Expert styles."
#                             },
#                             {
#                                 "role": "user",
#                                 "content": prompt_input
#                             }
#                         ],
#                         temperature=0.7
#                     )

#                     output = response.choices[0].message.content

#                 except Exception as e:
#                     output = "⚠️ Error: API limit reached or issue occurred. Please try again later."

#             st.markdown("### 🔥 Generated Prompts")
#             st.code(output)

#             st.session_state.history.append(output)

#             col1, col2 = st.columns(2)

#             with col1:
#                 st.download_button("📥 Download", output, file_name="prompts.txt")

#             with col2:
#                 if st.button("🔄 Regenerate"):
#                     st.rerun()

# # =========================================================
# # 📜 HISTORY PAGE
# # =========================================================
# elif page == "📜 History":

#     st.title("📜 Prompt History")

#     if st.session_state.history:
#         for item in st.session_state.history[::-1]:
#             st.code(item)
#     else:
#         st.info("No prompts generated yet.")

# # =========================================================
# # ℹ️ ABOUT PAGE
# # =========================================================
# elif page == "ℹ️ About":

#     st.title("ℹ️ About PromptForge AI")

#     st.markdown("""
# PromptForge AI is an intelligent prompt generator that helps users create high-quality AI prompts.

# ### 🚀 Use Cases
# - Resume Building  
# - YouTube Scripts  
# - Image Generation  
# - Coding & Business Ideas  

# ### 🛠 Tech Stack
# - Streamlit  
# - OpenAI API  

# Built with ❤️ by Ganesh Goddilla
# """)



# import streamlit as st

# # -------------------------------
# # 💾 SESSION HISTORY
# # -------------------------------
# if "history" not in st.session_state:
#     st.session_state.history = []

# # -------------------------------
# # 🔧 PAGE CONFIG
# # -------------------------------
# st.set_page_config(page_title="PromptForge AI", page_icon="⚡", layout="centered")

# # -------------------------------
# # 🎨 PREMIUM STYLING
# # -------------------------------
# st.markdown("""
# <style>
# body {
#     background-color: #0e1117;
# }
# .main {
#     background: linear-gradient(180deg, #0e1117 0%, #111827 100%);
# }
# h1 {
#     font-size: 42px;
#     font-weight: 700;
#     text-align: center;
# }
# .subtext {
#     text-align: center;
#     color: #9ca3af;
#     margin-bottom: 20px;
# }
# .card {
#     background: #1f2937;
#     padding: 15px;
#     border-radius: 12px;
#     margin-bottom: 10px;
# }
# .stButton>button {
#     background: linear-gradient(90deg, #4CAF50, #22c55e);
#     color: white;
#     border-radius: 12px;
#     height: 45px;
#     font-size: 16px;
# }
# </style>
# """, unsafe_allow_html=True)

# # -------------------------------
# # 📌 SIDEBAR
# # -------------------------------
# st.sidebar.markdown("""
# <h2 style='margin-bottom:0;'>⚡ PromptForge AI</h2>
# <p style='color:#6b7280; font-size:11px; margin-top:0;'>By Ganesh Goddilla</p>
# """, unsafe_allow_html=True)

# page = st.sidebar.radio(
#     "Navigation",
#     ["🏠 Home", "📜 History", "ℹ️ About"]
# )

# # -------------------------------
# # 🧠 FUNCTION: DYNAMIC QUESTIONS
# # -------------------------------
# def generate_questions(intent):

#     if "resume" in intent:
#         return [
#             ("Role", "Target job role?", "Software Engineer"),
#             ("Experience", "Experience level?", "Fresher"),
#             ("Skills", "Key skills?", "Python, SQL"),
#             ("Education", "Education?", "B.Tech"),
#         ]

#     elif "image" in intent:
#         return [
#             ("Type", "Image type?", "realistic"),
#             ("Subject", "Main subject?", "robot"),
#             ("Style", "Style?", "cinematic"),
#             ("Mood", "Mood?", "dark"),
#         ]

#     elif "youtube" in intent:
#         return [
#             ("Topic", "Video topic?", "AI tools"),
#             ("Audience", "Audience?", "students"),
#             ("Length", "Length?", "short"),
#             ("Tone", "Tone?", "fun"),
#         ]

#     else:
#         return [
#             ("Goal", "What do you want?", "startup idea"),
#             ("Context", "Topic?", "AI"),
#             ("Audience", "Target?", "developers"),
#             ("Tone", "Tone?", "professional"),
#         ]

# # -------------------------------
# # 🧠 SMART PROMPT ENGINE
# # -------------------------------
# def generate_prompts(user_input, answers):

#     intent = user_input.lower()

#     # 🔥 IMAGE LOGIC (SMART)
#     if "image" in intent:

#         subject = answers.get("Subject", "")
#         style = answers.get("Style", "")
#         mood = answers.get("Mood", "")
#         type_ = answers.get("Type", "")

#         base = f"{type_} {style} {mood} {subject}".strip()

#         creative = f"""
# 🔹 Prompt 1 – Creative Style  
# Create a highly detailed {type_} image of {subject} in a {style} style with a {mood} mood.  
# Include cinematic lighting, rich textures, and dynamic composition.  
# Make it visually stunning and unique.
# """

#         analytical = f"""
# 🔹 Prompt 2 – Analytical Style  
# Generate an image with the following structured details:
# - Subject: {subject}
# - Style: {style}
# - Mood: {mood}
# - Type: {type_}

# Ensure clarity, proper composition, and balanced visual elements.
# """

#         minimal = f"""
# 🔹 Prompt 3 – Minimal Style  
# {base}, high quality, detailed
# """

#         expert = f"""
# 🔹 Prompt 4 – Expert-Level Style  
# Create a {type_} {style} image of {subject} with a {mood} atmosphere.  
# Use professional photography techniques, depth of field, realistic lighting, and high-resolution detail (4K/8K).  
# Focus on composition, shadows, and cinematic realism.
# """

#         return creative + analytical + minimal + expert

#     # 🔥 DEFAULT LOGIC (OTHER USE CASES)
#     base = f"Task: {user_input}\n"
#     for k, v in answers.items():
#         base += f"- {k}: {v}\n"

#     return f"""
# 🔹 Prompt 1 – Creative  
# Act as a creative expert and generate output for:

# {base}

# 🔹 Prompt 2 – Analytical  
# Break this down step-by-step:

# {base}

# 🔹 Prompt 3 – Minimal  
# Create a short prompt for: {user_input}

# 🔹 Prompt 4 – Expert  
# Act as an industry expert and generate a high-quality prompt:

# {base}
# """

# # =========================================================
# # 🏠 HOME
# # =========================================================
# if page == "🏠 Home":

#     st.markdown("<h1>⚡ PromptForge AI</h1>", unsafe_allow_html=True)
#     st.markdown('<p class="subtext">Generate powerful prompts like a pro 🚀</p>', unsafe_allow_html=True)

#     st.markdown("""
# <div class="card">
# ✨ Create prompts for Resume, YouTube, Images, Startups & more  
# ⚡ 100% Free  
# 🧠 Smart guided system  
# </div>
# """, unsafe_allow_html=True)

#     user_input = st.text_input("What do you want to create?", placeholder="e.g. image, resume, youtube...")

#     if user_input:

#         questions = generate_questions(user_input.lower())
#         answers = {}

#         st.markdown("### ⚙️ Customize your prompt")

#         for title, question, example in questions:
#             answers[title] = st.text_input(question, placeholder=example)

#         if st.button("🚀 Generate Prompts"):

#             output = generate_prompts(user_input, answers)

#             st.markdown("### 🔥 Your Prompts")
#             st.code(output)

#             st.session_state.history.append(output)

# # =========================================================
# # 📜 HISTORY
# # =========================================================
# elif page == "📜 History":

#     st.markdown("## 📜 Prompt History")

#     if st.session_state.history:
#         for item in st.session_state.history[::-1]:
#             st.code(item)
#     else:
#         st.info("No prompts yet.")

# # =========================================================
# # ℹ️ ABOUT
# # =========================================================
# else:

#     st.markdown("## ℹ️ About")

#     st.write("""
# PromptForge AI is a smart prompt generator.
# Created By GANESH GODDILLA

# 🚀 Built for creators, developers, and entrepreneurs  
# ⚡ 100% Free version  
# 💡 Upgrade to AI-powered version anytime  
# """)


# import streamlit as st

# # -------------------------------
# # 💾 SESSION HISTORY
# # -------------------------------
# if "history" not in st.session_state:
#     st.session_state.history = []

# # -------------------------------
# # 🔧 PAGE CONFIG
# # -------------------------------
# st.set_page_config(page_title="PromptForge AI", page_icon="⚡", layout="centered")

# # -------------------------------
# # 🎨 STYLING
# # -------------------------------
# st.markdown("""
# <style>
# body {
#     background-color: #0e1117;
# }
# .main {
#     background: linear-gradient(180deg, #0e1117 0%, #111827 100%);
# }
# h1 {
#     font-size: 42px;
#     text-align: center;
# }
# .subtext {
#     text-align: center;
#     color: #9ca3af;
# }
# .stButton>button {
#     background: linear-gradient(90deg, #4CAF50, #22c55e);
#     color: white;
#     border-radius: 10px;
# }
# </style>
# """, unsafe_allow_html=True)

# # -------------------------------
# # 📌 SIDEBAR
# # -------------------------------
# st.sidebar.markdown("""
# <h2 style='margin-bottom:0;'>⚡ PromptForge AI</h2>
# <p style='color:#6b7280; font-size:11px; margin-top:0;'>By Ganesh Goddilla</p>
# """, unsafe_allow_html=True)

# page = st.sidebar.radio("Navigation", ["🏠 Home", "📜 History", "ℹ️ About"])

# # -------------------------------
# # 🧠 QUESTIONS
# # -------------------------------
# def generate_questions(intent):

#     if "image" in intent:
#         return [
#             ("Type", "Image type?", "realistic"),
#             ("Subject", "Main subject?", "robot"),
#             ("Style", "Style?", "cinematic"),
#             ("Mood", "Mood?", "dark"),
#         ]

#     elif "youtube" in intent:
#         return [
#             ("Topic", "Video topic?", "AI tools"),
#             ("Audience", "Audience?", "students"),
#             ("Length", "Length?", "short"),
#             ("Tone", "Tone?", "fun"),
#         ]

#     elif "resume" in intent:
#         return [
#             ("Role", "Target role?", "Software Engineer"),
#             ("Experience", "Experience?", "Fresher"),
#             ("Skills", "Skills?", "Python, SQL"),
#         ]

#     else:
#         return [
#             ("Goal", "Goal?", "startup idea"),
#             ("Context", "Context?", "AI"),
#             ("Audience", "Audience?", "developers"),
#             ("Tone", "Tone?", "professional"),
#         ]

# # -------------------------------
# # 🧠 DYNAMIC EXAMPLES
# # -------------------------------
# def get_examples(intent, field):

#     intent = intent.lower()
#     field = field.lower()

#     if "image" in intent:
#         return {
#             "type": ["realistic", "cartoon", "3D", "illustration"],
#             "subject": ["robot", "astronaut", "lion", "product"],
#             "style": ["cinematic", "anime", "photorealistic", "cyberpunk"],
#             "mood": ["dark", "vibrant", "futuristic", "dreamy"],
#         }.get(field, [])

#     elif "youtube" in intent:
#         return {
#             "topic": ["AI tools", "motivation", "finance"],
#             "audience": ["students", "beginners", "developers"],
#             "length": ["short", "long"],
#             "tone": ["fun", "educational", "serious"],
#         }.get(field, [])

#     elif "resume" in intent:
#         return {
#             "role": ["Software Engineer", "Data Analyst", "HR"],
#             "experience": ["Fresher", "1 year", "3+ years"],
#             "skills": ["Python, SQL", "Excel, Power BI"],
#         }.get(field, [])

#     return []

# # -------------------------------
# # 🧠 PROMPT ENGINE
# # -------------------------------
# def generate_prompts(user_input, answers):

#     if "image" in user_input.lower():

#         subject = answers.get("Subject", "")
#         style = answers.get("Style", "")
#         mood = answers.get("Mood", "")
#         type_ = answers.get("Type", "")

#         return f"""
# 🔹 Prompt 1 – Creative  
# Create a highly detailed {type_} image of {subject} in a {style} style with a {mood} mood.

# 🔹 Prompt 2 – Analytical  
# Subject: {subject}, Style: {style}, Mood: {mood}, Type: {type_}

# 🔹 Prompt 3 – Minimal  
# {type_} {style} {mood} {subject}, high quality

# 🔹 Prompt 4 – Expert  
# Professional {type_} {style} image of {subject}, cinematic lighting, ultra realistic.
# """

#     # default
#     return f"Generate prompts for {user_input}"

# # =========================================================
# # 🏠 HOME
# # =========================================================
# if page == "🏠 Home":

#     st.markdown("<h1>⚡ PromptForge AI</h1>", unsafe_allow_html=True)
#     st.markdown('<p class="subtext">Generate prompts like a pro 🚀</p>', unsafe_allow_html=True)

#     user_input = st.text_input("What do you want to create?")

#     if user_input:

#         questions = generate_questions(user_input.lower())
#         answers = {}

#         st.markdown("### ⚙️ Customize your prompt")

#         for title, question, example in questions:

#             key = f"{title}_{user_input}"

#             # input
#             answers[title] = st.text_input(
#                 question,
#                 placeholder=example,
#                 key=key
#             )

#             # examples
#             examples = get_examples(user_input, title)

#             if examples:
#                 cols = st.columns(len(examples))

#                 for i, ex in enumerate(examples):
#                     with cols[i]:
#                         if st.button(ex, key=f"{key}_{ex}"):
#                             st.session_state[key] = ex
#                             st.rerun()

#         # generate
#         if st.button("🚀 Generate Prompts"):

#             output = generate_prompts(user_input, answers)

#             st.markdown("### 🔥 Output")
#             st.code(output)

#             st.session_state.history.append(output)

# # =========================================================
# # 📜 HISTORY
# # =========================================================
# elif page == "📜 History":

#     for item in st.session_state.history[::-1]:
#         st.code(item)

# # =========================================================
# # ℹ️ ABOUT
# # =========================================================
# else:

#     st.write("PromptForge AI - Free prompt generator 🚀")



# import streamlit as st

# # -------------------------------
# # 🔧 PAGE CONFIG
# # -------------------------------
# st.set_page_config(page_title="PromptForge AI", page_icon="⚡", layout="centered")

# # -------------------------------
# # 💾 SESSION STATE
# # -------------------------------
# if "history" not in st.session_state:
#     st.session_state.history = []

# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# # -------------------------------
# # 🔐 LOGIN SYSTEM (FREE)
# # -------------------------------
# def login():
#     st.title("🔐 Login to PromptForge AI")

#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         # Simple free login (you can change credentials)
#         if username == "admin" and password == "1234":
#             st.session_state.logged_in = True
#             st.success("Login successful 🚀")
#             st.rerun()
#         else:
#             st.error("Invalid credentials")

# # -------------------------------
# # 🎨 STYLING
# # -------------------------------
# st.markdown("""
# <style>
# body {
#     background-color: #0e1117;
# }
# .main {
#     background: linear-gradient(180deg, #0e1117 0%, #111827 100%);
# }
# .card {
#     background: #1f2937;
#     padding: 15px;
#     border-radius: 12px;
#     margin-bottom: 10px;
# }
# .stButton>button {
#     background: linear-gradient(90deg, #4CAF50, #22c55e);
#     color: white;
#     border-radius: 12px;
#     height: 45px;
#     font-size: 16px;
# }
# </style>
# """, unsafe_allow_html=True)

# # -------------------------------
# # 🧠 STYLE PROMPT ENGINE
# # -------------------------------
# def get_style_prompt(style):
#     if style == "Cinematic":
#         return "cinematic lighting, dramatic shadows, ultra realistic, 8k, depth of field, movie still, high contrast"
#     elif style == "Anime":
#         return "anime style, vibrant colors, sharp lines, highly detailed, dynamic pose"
#     elif style == "Realistic":
#         return "photorealistic, ultra detailed, 8k resolution, realistic textures, natural lighting"
#     elif style == "Marvel Style":
#         return "Marvel cinematic universe style, superhero aesthetics, epic pose, glowing energy, dramatic lighting"

# # -------------------------------
# # 🧠 PROMPT ENGINE
# # -------------------------------
# def generate_prompts(user_input, answers):

#     intent = user_input.lower()

#     # 🎯 ROLE-BASED PROMPTS (NEW LOGIC)
#     if "youtube" in intent:

#         topic = answers.get("Goal", "")
#         audience = answers.get("Audience", "")

#         return f"""
# 🔹 Prompt 1 – Expert Script Writer  
# Act as an experienced YouTube content creator.  
# Create an engaging script about "{topic}" for {audience}.  
# Include a strong hook, storytelling, and a clear structure (intro, main content, conclusion).  

# 🔹 Prompt 2 – Growth Focused  
# Act as a YouTube growth strategist.  
# Write a viral-ready script on "{topic}" targeting {audience}.  
# Focus on retention, curiosity gaps, and engagement techniques.  

# 🔹 Prompt 3 – Minimal  
# Write a YouTube script about "{topic}" for {audience}.  

# 🔹 Prompt 4 – Professional  
# Act as a professional scriptwriter.  
# Create a high-quality, well-structured YouTube script on "{topic}" tailored for {audience}.  
# Ensure clarity, engagement, and audience retention.
# """

#     elif "resume" in intent:

#         role = answers.get("Role", "job role")
#         skills = answers.get("Skills", "")

#         return f"""
# 🔹 Prompt 1 – Career Coach  
# You are an experienced career coach.  
# Review my resume for a "{role}" position and suggest improvements.  
# Focus on clarity, impact, and ATS optimization.  

# 🔹 Prompt 2 – Recruiter Perspective  
# Act as a recruiter hiring for "{role}".  
# Evaluate my resume and suggest what to improve to stand out.  

# 🔹 Prompt 3 – Minimal  
# Review my resume for {role}.  

# 🔹 Prompt 4 – Expert  
# Act as a senior hiring manager.  
# Provide detailed feedback on my resume for a "{role}" role, focusing on achievements, structure, and keywords.
# """

#     elif "image" in intent:

#         character = answers.get("Character", "")
#         pose = answers.get("Pose", "")
#         background = answers.get("Background", "")
#         colors = answers.get("Colors", "")
#         style = answers.get("Style", "")

#         style_prompt = get_style_prompt(style)

#         return f"""
# 🔹 Prompt 1 – Professional AI Artist  
# Act as a professional AI artist.  
# Create a highly detailed image of a {character}, {pose}, in a {background}.  
# Use {colors} color palette and {style} style.  
# Apply cinematic lighting, depth of field, and ultra-high resolution (8K).

# 🔹 Prompt 2 – Creative Direction  
# Act as a creative director.  
# Design a visually stunning {character} performing {pose} in {background},  
# with {colors} tones and {style} aesthetics.  

# 🔹 Prompt 3 – Minimal  
# {character}, {pose}, {background}, {colors}, {style}, high quality  

# 🔹 Prompt 4 – Expert-Level Prompt  
# Act as an expert prompt engineer.  
# Generate a production-quality AI image prompt for a {character} in {background},  
# with {pose}, {colors}, and {style}.  
# Include lighting, composition, textures, and realism enhancements.
# """

#     # 🔥 DEFAULT (SMART GENERIC)
#     return f"""
# 🔹 Prompt 1 – Expert  
# Act as an expert in the field.  
# Help me with: "{user_input}".  
# Provide clear, structured, and actionable output.

# 🔹 Prompt 2 – Creative  
# Act as a creative professional.  
# Generate innovative ideas for: "{user_input}".

# 🔹 Prompt 3 – Minimal  
# {user_input}

# 🔹 Prompt 4 – Professional  
# Act as an industry expert.  
# Deliver high-quality output for: "{user_input}" with clarity and depth.
# """

#     # DEFAULT
#     base = f"Task: {user_input}\n"
#     for k, v in answers.items():
#         base += f"- {k}: {v}\n"

#     return f"""
# 🔹 Prompt 1 – Creative  
# {base}

# 🔹 Prompt 2 – Analytical  
# Break step-by-step:
# {base}

# 🔹 Prompt 3 – Minimal  
# {user_input}

# 🔹 Prompt 4 – Expert  
# {base}
# """

# # -------------------------------
# # 🔐 LOGIN CHECK
# # -------------------------------
# if not st.session_state.logged_in:
#     login()
#     st.stop()

# # -------------------------------
# # 📌 SIDEBAR
# # -------------------------------
# st.sidebar.title("⚡ PromptForge AI")

# page = st.sidebar.radio(
#     "Navigation",
#     ["🏠 Home", "📜 History", "ℹ️ About"]
# )

# # =========================================================
# # 🏠 HOME
# # =========================================================
# if page == "🏠 Home":

#     st.title("⚡ PromptForge AI")
#     st.markdown("Generate powerful prompts like a pro 🚀")

#     user_input = st.text_input(
#         "What do you want to create?",
#         placeholder="e.g. image, resume, youtube..."
#     )

#     if user_input:

#         answers = {}

#         # 🔥 IMAGE UI (NEW)
#         if "image" in user_input.lower():

#             st.markdown("### 🎨 Image Settings")

#             answers["Character"] = st.text_input("Character Type", "male superhero")
#             answers["Pose"] = st.text_input("Pose", "standing confidently")
#             answers["Background"] = st.text_input("Background", "space")
#             answers["Colors"] = st.text_input("Color Theme", "pastel colors")

#             answers["Style"] = st.selectbox(
#                 "Style",
#                 ["Cinematic", "Anime", "Realistic", "Marvel Style"]
#             )

#         else:
#             answers["Goal"] = st.text_input("Goal", "startup idea")
#             answers["Audience"] = st.text_input("Audience", "developers")

#         if st.button("🚀 Generate Prompts"):

#             output = generate_prompts(user_input, answers)

#             st.markdown("### 🔥 Your Prompts")
#             st.code(output)

#             st.session_state.history.append(output)

# # =========================================================
# # 📜 HISTORY
# # =========================================================
# elif page == "📜 History":

#     st.markdown("## 📜 Prompt History")

#     if st.session_state.history:
#         for item in st.session_state.history[::-1]:
#             st.code(item)
#     else:
#         st.info("No prompts yet.")

# # =========================================================
# # ℹ️ ABOUT
# # =========================================================
# else:

#     st.markdown("## ℹ️ About")

#     st.write("""
# PromptForge AI is a smart prompt generator.

# 🚀 Built by Ganesh Goddilla
# ⚡ Free version  
# 💡 Supports image, resume, YouTube prompts  
# """)





# import streamlit as st
# from openai import OpenAI
# import os

# # -------------------------------
# # 🔑 OPENAI CLIENT
# # -------------------------------
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # -------------------------------
# # 💾 SESSION HISTORY
# # -------------------------------
# if "history" not in st.session_state:
#     st.session_state.history = []

# # -------------------------------
# # 🔧 PAGE CONFIG
# # -------------------------------
# st.set_page_config(
#     page_title="PromptForge AI",
#     page_icon="⚡",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # -------------------------------
# # 🎨 PREMIUM CHATGPT-LIKE UI
# # -------------------------------
# st.markdown("""
# <style>
# /* Global */
# html, body, [class*="css"] {
#     font-family: "Inter", sans-serif;
# }

# .stApp {
#     background: linear-gradient(180deg, #0b1020 0%, #111827 100%);
#     color: #ffffff;
# }

# /* Main container */
# .block-container {
#     padding-top: 2rem;
#     padding-bottom: 2rem;
#     max-width: 1200px;
# }

# /* Sidebar */
# section[data-testid="stSidebar"] {
#     background: #0b1220;
#     border-right: 1px solid rgba(255,255,255,0.08);
# }

# /* Headings */
# h1, h2, h3, h4 {
#     color: #ffffff !important;
# }

# /* Hero Card */
# .hero-card {
#     background: linear-gradient(135deg, rgba(99,102,241,0.18), rgba(16,185,129,0.12));
#     border: 1px solid rgba(255,255,255,0.08);
#     border-radius: 24px;
#     padding: 26px;
#     margin-bottom: 22px;
#     box-shadow: 0 10px 30px rgba(0,0,0,0.25);
# }

# .hero-title {
#     font-size: 2.1rem;
#     font-weight: 800;
#     margin-bottom: 8px;
# }

# .hero-sub {
#     color: #cbd5e1;
#     font-size: 1rem;
#     line-height: 1.7;
# }

# /* Section Cards */
# .glass-card {
#     background: rgba(17, 24, 39, 0.78);
#     border: 1px solid rgba(255,255,255,0.08);
#     backdrop-filter: blur(10px);
#     border-radius: 22px;
#     padding: 22px;
#     margin-bottom: 18px;
#     box-shadow: 0 10px 24px rgba(0,0,0,0.22);
# }

# /* Feature grid */
# .feature-item {
#     background: rgba(255,255,255,0.03);
#     border: 1px solid rgba(255,255,255,0.06);
#     border-radius: 16px;
#     padding: 14px 16px;
#     margin-bottom: 10px;
#     color: #e5e7eb;
#     line-height: 1.6;
# }

# /* Prompt Output */
# .chat-shell {
#     background: #0f172a;
#     border: 1px solid rgba(255,255,255,0.08);
#     border-radius: 22px;
#     padding: 18px;
#     margin-top: 14px;
#     box-shadow: 0 10px 24px rgba(0,0,0,0.22);
# }

# .user-bubble {
#     background: #1e293b;
#     border-left: 4px solid #60a5fa;
#     padding: 16px 18px;
#     border-radius: 16px;
#     margin-bottom: 14px;
#     color: #e2e8f0;
#     line-height: 1.7;
# }

# .assistant-bubble {
#     background: #111827;
#     border-left: 4px solid #34d399;
#     padding: 18px 20px;
#     border-radius: 16px;
#     color: #f9fafb;
#     line-height: 1.9;
#     white-space: pre-wrap;
#     font-size: 15px;
# }

# /* Labels */
# .tag {
#     display: inline-block;
#     padding: 6px 10px;
#     margin-right: 8px;
#     margin-bottom: 8px;
#     border-radius: 999px;
#     background: rgba(255,255,255,0.06);
#     color: #dbeafe;
#     font-size: 13px;
#     border: 1px solid rgba(255,255,255,0.08);
# }

# /* Buttons */
# .stButton > button {
#     width: 100%;
#     background: linear-gradient(90deg, #2563eb, #7c3aed);
#     color: white;
#     border: none;
#     border-radius: 14px;
#     padding: 0.85rem 1rem;
#     font-weight: 700;
#     font-size: 15px;
#     box-shadow: 0 8px 18px rgba(37,99,235,0.25);
# }

# .stDownloadButton > button {
#     width: 100%;
#     border-radius: 14px;
#     padding: 0.85rem 1rem;
#     font-weight: 700;
#     border: 1px solid rgba(255,255,255,0.08);
#     background: #0f172a;
#     color: white;
# }

# /* Inputs */
# .stTextInput > div > div > input {
#     border-radius: 14px !important;
#     background: #0f172a !important;
#     color: white !important;
#     border: 1px solid rgba(255,255,255,0.09) !important;
#     padding: 0.8rem 1rem !important;
# }

# .small-note {
#     color: #94a3b8;
#     font-size: 13px;
#     line-height: 1.6;
# }

# hr {
#     border: none;
#     border-top: 1px solid rgba(255,255,255,0.07);
#     margin: 18px 0;
# }
# </style>
# """, unsafe_allow_html=True)

# # -------------------------------
# # 📌 SIDEBAR
# # -------------------------------
# st.sidebar.markdown("## ⚡ PromptForge AI")
# st.sidebar.caption("Premium prompt generation workspace")

# page = st.sidebar.radio(
#     "Navigate",
#     ["🏠 Home", "📜 History", "ℹ️ About"]
# )

# st.sidebar.markdown("---")
# st.sidebar.markdown("### Quick Use Cases")
# st.sidebar.markdown("""
# - Resume prompts  
# - Image prompts  
# - Midjourney prompts  
# - YouTube scripts  
# - Marketing copy  
# - Coding prompts  
# - Startup ideas  
# - LinkedIn content  
# """)

# # -------------------------------
# # 🧠 FUNCTION: DYNAMIC QUESTIONS
# # -------------------------------
# def generate_questions(intent):
#     if "resume" in intent or "cv" in intent:
#         return [
#             ("1. Basic Info", "Are you a student, fresher, or experienced professional?", "e.g. Fresher"),
#             ("2. Industry", "What is your field/industry?", "e.g. IT, Mechanical"),
#             ("3. Target Role", "What role are you targeting?", "e.g. Software Engineer"),
#             ("4. Background", "Education / projects / experience?", "e.g. B.Tech + ML project"),
#             ("5. Skills", "Key skills?", "e.g. Python, SQL, Communication"),
#             ("6. Style", "Resume style?", "ATS-friendly or creative"),
#             ("7. Output", "1-page or 2-page?", "e.g. 1-page concise"),
#             ("8. Tone", "Tone?", "Formal / Professional")
#         ]

#     elif "image" in intent or "midjourney" in intent or "art" in intent:
#         return [
#             ("1. Image Type", "What type of image?", "e.g. realistic, cartoon, 3D"),
#             ("2. Subject", "Main subject?", "e.g. person, product, landscape"),
#             ("3. Style", "Art style?", "e.g. cinematic, anime, photorealistic"),
#             ("4. Colors", "Color theme?", "e.g. dark, vibrant, pastel"),
#             ("5. Usage", "Where will it be used?", "e.g. Instagram, thumbnail"),
#             ("6. Details", "Extra details?", "e.g. lighting, background elements"),
#             ("7. Quality", "Resolution?", "HD, 4K, ultra realistic")
#         ]

#     elif "youtube" in intent or "video" in intent or "reel" in intent:
#         return [
#             ("1. Topic", "Video topic?", "e.g. AI tools that save time"),
#             ("2. Audience", "Target audience?", "e.g. students, beginners"),
#             ("3. Duration", "Video length?", "Short or long"),
#             ("4. Style", "Video style?", "Storytelling, educational"),
#             ("5. Goal", "Purpose?", "Views, engagement"),
#             ("6. Platform", "Platform?", "YouTube Shorts / Long"),
#             ("7. Tone", "Tone?", "Energetic, fun")
#         ]

#     elif "business" in intent or "startup" in intent:
#         return [
#             ("1. Business Type", "What type of business idea do you want?", "e.g. SaaS, local business"),
#             ("2. Industry", "Which industry?", "e.g. AI, fintech, e-commerce"),
#             ("3. Target Audience", "Who is it for?", "e.g. students, founders"),
#             ("4. Goal", "What outcome do you want?", "e.g. startup idea, pitch"),
#             ("5. Format", "Output format?", "e.g. roadmap, strategy, pitch deck"),
#             ("6. Tone", "Tone?", "Professional, persuasive")
#         ]

#     elif "coding" in intent or "code" in intent or "app" in intent or "streamlit" in intent:
#         return [
#             ("1. Project Type", "What do you want to build?", "e.g. Streamlit app, website, API"),
#             ("2. Language", "Preferred language/stack?", "e.g. Python, React"),
#             ("3. Purpose", "What should it do?", "e.g. generate prompts"),
#             ("4. Users", "Who will use it?", "e.g. developers, general users"),
#             ("5. Features", "Important features?", "e.g. login, export, history"),
#             ("6. Style", "Code style?", "Beginner-friendly / production-ready")
#         ]

#     elif "marketing" in intent or "copy" in intent or "linkedin" in intent:
#         return [
#             ("1. Content Type", "What do you want to create?", "e.g. ad copy, email, landing page"),
#             ("2. Product/Service", "What are you promoting?", "e.g. AI tool"),
#             ("3. Audience", "Who is the target audience?", "e.g. founders, students"),
#             ("4. Goal", "Main objective?", "e.g. sales, clicks, signups"),
#             ("5. Tone", "Brand tone?", "e.g. bold, premium, friendly"),
#             ("6. Platform", "Where will it be used?", "e.g. Instagram, website")
#         ]

#     else:
#         return [
#             ("1. Goal", "What do you want to achieve?", "e.g. Build a startup idea"),
#             ("2. Context", "Topic or domain?", "e.g. fintech, AI"),
#             ("3. Audience", "Target users?", "e.g. developers"),
#             ("4. Format", "Output format?", "e.g. steps, list"),
#             ("5. Tone", "Tone?", "Professional, casual"),
#             ("6. Constraints", "Any limits?", "e.g. 60 sec, simple language")
#         ]


# def build_prompt_input(user_input, answers):
#     prompt_input = f"User wants: {user_input}\n\nDetails:\n"
#     for key, value in answers.items():
#         prompt_input += f"{key}: {value}\n"
#     return prompt_input


# def format_prompt_output(raw_text):
#     if not raw_text:
#         return ""
#     return raw_text.strip().replace("```", "")


# # =========================================================
# # 🏠 HOME PAGE
# # =========================================================
# if page == "🏠 Home":

#     st.markdown("""
#     <div class="hero-card">
#         <div class="hero-title">⚡ ganEEEE Prompt Magic</div>
#         <div class="hero-sub">
#             Create premium AI prompts with smart guided questions, polished output,
#             and a modern interface that feels closer to real AI conversation tools.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     colA, colB = st.columns([1.4, 1])

#     with colA:
#         st.markdown('<div class="glass-card">', unsafe_allow_html=True)
#         st.markdown("### ✨ Features")
#         st.markdown("""
#         <div class="feature-item">🧠 Smart question-based input flow</div>
#         <div class="feature-item">🤖 Multi-style prompt generation</div>
#         <div class="feature-item">💬 ChatGPT-style conversation layout</div>
#         <div class="feature-item">🎨 Midjourney-style image prompt writing</div>
#         <div class="feature-item">📹 YouTube, Reels, and Shorts prompt creation</div>
#         <div class="feature-item">💻 Coding, app-building, and debugging prompts</div>
#         <div class="feature-item">📈 Business, startup, and marketing prompts</div>
#         <div class="feature-item">🧾 Copywriting and brand messaging prompts</div>
#         <div class="feature-item">📜 Prompt history with cleaner display</div>
#         <div class="feature-item">📥 Export generated prompts instantly</div>
#         """, unsafe_allow_html=True)
#         st.markdown("</div>", unsafe_allow_html=True)

#     with colB:
#         st.markdown('<div class="glass-card">', unsafe_allow_html=True)
#         st.markdown("### 🚀 Popular Categories")
#         st.markdown("""
#         <span class="tag">Resume</span>
#         <span class="tag">Image</span>
#         <span class="tag">Midjourney</span>
#         <span class="tag">YouTube</span>
#         <span class="tag">Coding</span>
#         <span class="tag">Marketing</span>
#         <span class="tag">Business</span>
#         <span class="tag">LinkedIn</span>
#         """, unsafe_allow_html=True)
#         st.markdown("<p class='small-note'>Tip: type something like <b>resume</b>, <b>image</b>, <b>youtube script</b>, <b>business idea</b>, or <b>coding app</b>.</p>", unsafe_allow_html=True)
#         st.markdown("</div>", unsafe_allow_html=True)

#     st.markdown('<div class="glass-card">', unsafe_allow_html=True)
#     user_input = st.text_input(
#         "What do you want to create?",
#         placeholder="e.g. resume, image, youtube script, startup idea, coding prompt..."
#     )

#     intent = user_input.strip().lower() if user_input else ""

#     if intent:
#         st.success(f"🧠 Smart Mode Activated for: {user_input}")

#         questions = generate_questions(intent)
#         answers = {}

#         st.markdown("### 👋 Let’s build your prompt step-by-step")
#         st.markdown(f"<p class='small-note'>You selected: <b>{user_input}</b></p>", unsafe_allow_html=True)

#         qcol1, qcol2 = st.columns(2)
#         for i, (title, question, example) in enumerate(questions):
#             with qcol1 if i % 2 == 0 else qcol2:
#                 st.markdown(f"**{title}**")
#                 answers[title] = st.text_input(question, placeholder=example, key=title)
#                 st.caption(f"Example: {example}")

#         if st.button("🚀 Generate Prompts"):
#             with st.spinner("Generating premium prompts..."):
#                 prompt_input = build_prompt_input(user_input, answers)

#                 try:
#                     response = client.chat.completions.create(
#                         model="gpt-4o-mini",
#                         messages=[
#                             {
#                                 "role": "system",
#                                 "content": """
# You are PromptForge AI, a world-class prompt engineer.

# Generate exactly 4 prompt versions:
# 1. Creative Prompt
# 2. Analytical Prompt
# 3. Minimal Prompt
# 4. Expert Prompt

# Rules:
# - Write each version as a polished professional paragraph.
# - Make the output feel premium, natural, and ready to copy-paste.
# - Use role assignment, context, goal, constraints, tone, and output instructions.
# - Keep each version distinct in quality and style.
# - For image prompts, make them highly visual and cinematic like Midjourney-quality prompts.
# - For writing, coding, business, or resume prompts, make them structured like elite ChatGPT prompts.
# - Do not return JSON.
# - Do not wrap the answer in code fences.
# - Use clean headings for each version.
# """
#                             },
#                             {
#                                 "role": "user",
#                                 "content": prompt_input
#                             }
#                         ],
#                         temperature=0.8
#                     )

#                     output = format_prompt_output(response.choices[0].message.content)

#                 except Exception:
#                     output = "⚠️ Error: API limit reached or an unexpected issue occurred. Please try again later."

#             st.markdown("## 🔥 Prompt's Generation")

#             st.markdown(f"""
#             <div class="chat-shell">
#                 <div class="user-bubble">
#                     <b>You:</b><br>
#                     Create a premium prompt for: <b>{user_input}</b>
#                 </div>
#                 <div class="assistant-bubble">
#                     <b>PromptForge AI:</b><br><br>
#                     {output}
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)

#             st.session_state.history.append({
#                 "topic": user_input,
#                 "output": output
#             })

#             st.markdown("<br>", unsafe_allow_html=True)
#             col1, col2 = st.columns(2)

#             with col1:
#                 st.download_button(
#                     "📥 Download Prompt",
#                     output,
#                     file_name="prompts.txt",
#                     use_container_width=True
#                 )

#             with col2:
#                 if st.button("🔄 Regenerate", use_container_width=True):
#                     st.rerun()

#     st.markdown("</div>", unsafe_allow_html=True)

# # =========================================================
# # 📜 HISTORY PAGE
# # =========================================================
# elif page == "📜 History":

#     st.markdown("""
#     <div class="hero-card">
#         <div class="hero-title">📜 Prompt History</div>
#         <div class="hero-sub">
#             Review your previously generated prompts in a cleaner conversation-style layout.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     if st.session_state.history:
#         for item in reversed(st.session_state.history):
#             topic = item["topic"] if isinstance(item, dict) else "Prompt"
#             output = item["output"] if isinstance(item, dict) else str(item)

#             st.markdown(f"""
#             <div class="chat-shell">
#                 <div class="user-bubble">
#                     <b>You:</b><br>
#                     {topic}
#                 </div>
#                 <div class="assistant-bubble">
#                     <b>PromptForge AI:</b><br><br>
#                     {output}
#                 </div>
#             </div>
#             <br>
#             """, unsafe_allow_html=True)
#     else:
#         st.info("No prompts generated yet.")

# # =========================================================
# # ℹ️ ABOUT PAGE
# # =========================================================
# elif page == "ℹ️ About":

#     st.markdown("""
#     <div class="hero-card">
#         <div class="hero-title">ℹ️ About prompts for free</div>
#         <div class="hero-sub">
#             PromptForge AI helps users generate high-quality prompts for content, images,
#             coding, business, and more through an elegant guided experience.
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown('<div class="glass-card">', unsafe_allow_html=True)
#     st.markdown("""
# ### 🚀 Use Cases
# - Resume Building  
# - YouTube Scripts  
# - Image Generation  
# - Midjourney Prompt Writing  
# - Coding & App Building  
# - Business Ideas  
# - Startup Validation  
# - Marketing & Copywriting  
# - LinkedIn Content  
# - Product Descriptions  
# - Social Media Captions  
# - Email Writing Prompts  

# ### 🛠 Tech Stack
# - Streamlit  
# - OpenAI API  
# - Custom CSS UI  

# Built with ❤️ by Ganesh Goddilla
# """)
#     st.markdown("</div>", unsafe_allow_html=True)







import streamlit as st
import textwrap

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="PromptNexus AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# SESSION STATE
# -------------------------------
if "generated_prompt" not in st.session_state:
    st.session_state.generated_prompt = ""

# -------------------------------
# CUSTOM CSS
# -------------------------------
st.markdown("""
<style>
/* Global */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0B0F19 0%, #111827 40%, #0F172A 100%);
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0F172A 0%, #111827 100%);
    border-right: 1px solid rgba(255,255,255,0.08);
}

.sidebar-logo {
    padding: 14px 10px 18px 10px;
    border-radius: 18px;
    background: linear-gradient(135deg, rgba(108,99,255,0.15), rgba(0,212,255,0.10));
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 0 18px rgba(108,99,255,0.18);
    margin-bottom: 18px;
}

.logo-title {
    font-size: 28px;
    font-weight: 800;
    line-height: 1.1;
    background: linear-gradient(90deg, #6C63FF, #00D4FF, #A855F7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.logo-subtitle {
    color: #9CA3AF;
    font-size: 13px;
    margin-top: 6px;
}

/* Main title */
.hero-card {
    padding: 28px;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(17,24,39,0.92), rgba(15,23,42,0.92));
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 0 30px rgba(0,212,255,0.08), 0 0 50px rgba(108,99,255,0.08);
    margin-bottom: 22px;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 10px;
    background: linear-gradient(90deg, #FFFFFF, #00D4FF, #A855F7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-desc {
    color: #cbd5e1;
    font-size: 16px;
    line-height: 1.6;
}

/* Cards */
.feature-card {
    background: rgba(17,24,39,0.85);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 20px;
    padding: 18px;
    margin-bottom: 16px;
    box-shadow: 0 0 20px rgba(0,0,0,0.18);
}

.feature-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 10px;
    color: #E5E7EB;
}

.feature-text {
    color: #9CA3AF;
    line-height: 1.7;
    font-size: 15px;
}

/* Prompt output box */
.prompt-box {
    background: linear-gradient(135deg, rgba(17,24,39,0.98), rgba(30,41,59,0.98));
    border: 1px solid rgba(0,212,255,0.22);
    border-radius: 22px;
    padding: 24px;
    box-shadow: 0 0 25px rgba(0,212,255,0.10), 0 0 35px rgba(168,85,247,0.10);
    margin-top: 18px;
    white-space: pre-wrap;
    line-height: 1.75;
    font-size: 16px;
    color: #F8FAFC;
}

.prompt-heading {
    font-size: 24px;
    font-weight: 800;
    margin-bottom: 14px;
    color: #FFFFFF;
}

/* Input labels */
label, .stSelectbox label, .stTextInput label, .stTextArea label {
    color: #E5E7EB !important;
    font-weight: 600 !important;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 16px;
    border: none;
    padding: 0.75rem 1rem;
    font-weight: 700;
    font-size: 15px;
    color: white;
    background: linear-gradient(90deg, #6C63FF, #00D4FF);
    box-shadow: 0 0 18px rgba(0,212,255,0.25);
    transition: all 0.25s ease-in-out;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 24px rgba(108,99,255,0.35);
}

/* Text area / inputs */
.stTextArea textarea,
.stTextInput input {
    background: rgba(17,24,39,0.95) !important;
    color: white !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"] > div {
    background: rgba(17,24,39,0.95) !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
}

/* Divider heading */
.section-title {
    font-size: 26px;
    font-weight: 800;
    margin-top: 12px;
    margin-bottom: 14px;
    color: #F8FAFC;
}

/* Small badge */
.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 999px;
    background: rgba(108,99,255,0.16);
    color: #dbeafe;
    border: 1px solid rgba(255,255,255,0.08);
    font-size: 13px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# PROMPT GENERATOR LOGIC
# -------------------------------
def build_prompt(use_case, topic, style, audience, extra_details):
    style_map = {
        "Professional": "Write in a polished, structured, professional tone with clarity and strong intent.",
        "Creative": "Write in an imaginative, engaging, high-impact style with expressive language and originality.",
        "Minimal": "Write in a concise, sharp, clean style with no fluff and maximum clarity.",
        "Cinematic": "Write in a vivid, dramatic, immersive cinematic style with rich visual detail and emotional depth.",
        "Anime": "Write in a visually expressive anime-inspired style with strong mood, dynamic imagery, and stylized details.",
        "Realistic": "Write in a grounded, highly realistic style with precise details and practical clarity.",
        "Expert": "Write in an advanced expert-level style with authority, precision, structure, and strategic detail."
    }

    base_templates = {
        "Content Writing": f"""
Act as an expert content strategist and professional writer. Create a high-quality prompt for {use_case.lower()} focused on "{topic}".

The prompt should be written for {audience.lower()} and should guide the AI to produce output that is clear, engaging, useful, and well-structured. {style_map[style]}

Make sure the final generated content includes:
- a strong objective
- the right tone for the target audience
- clear structure with logical flow
- practical, high-value output
- polished, natural language that feels professional

Additional context to include:
{extra_details if extra_details else "No extra constraints provided."}

Return the final prompt as one professional paragraph, ready to paste into ChatGPT or any advanced AI tool.
""",

        "Coding": f"""
Act as a senior software engineer and AI coding assistant. Create a high-quality prompt for {use_case.lower()} focused on "{topic}".

The prompt should help generate accurate, production-quality, well-explained output for {audience.lower()}. {style_map[style]}

Make sure the final generated result asks for:
- clean and correct code
- best practices
- clear explanations
- modular structure
- error handling where relevant
- readable formatting and maintainability

Additional context to include:
{extra_details if extra_details else "No extra constraints provided."}

Return the final prompt as one polished professional paragraph.
""",

        "Business": f"""
Act as a strategic business consultant and prompt engineer. Create a premium-quality prompt for {use_case.lower()} focused on "{topic}".

The prompt should be suitable for {audience.lower()} and should drive AI to produce useful, practical, and decision-oriented output. {style_map[style]}

Ensure the prompt asks for:
- strategic thinking
- clarity and business relevance
- actionable insights
- professional tone
- organized response structure
- realistic recommendations

Additional context to include:
{extra_details if extra_details else "No extra constraints provided."}

Return the final prompt as one refined paragraph that sounds premium and professional.
""",

        "Students": f"""
Act as an educational mentor and smart AI tutor. Create a high-quality prompt for {use_case.lower()} focused on "{topic}".

The prompt should be designed for {audience.lower()} and should help the AI deliver clear, accurate, easy-to-understand, and valuable educational support. {style_map[style]}

Ensure the prompt requests:
- step-by-step clarity
- simple but intelligent explanations
- structured output
- practical examples where useful
- beginner-friendly understanding without losing quality

Additional context to include:
{extra_details if extra_details else "No extra constraints provided."}

Return the final prompt as one polished and user-friendly paragraph.
""",

        "General Use": f"""
Act as a world-class AI assistant and prompt engineer. Create a premium-quality prompt for {use_case.lower()} focused on "{topic}".

The prompt should be useful for {audience.lower()} and should produce a clear, intelligent, high-quality result. {style_map[style]}

Ensure the prompt asks for:
- accurate output
- strong clarity
- professional structure
- relevant detail
- polished natural language
- a result that feels thoughtful and high-value

Additional context to include:
{extra_details if extra_details else "No extra constraints provided."}

Return the final prompt as one strong, professional paragraph ready for direct use.
"""
    }

    prompt = base_templates.get(use_case, base_templates["General Use"])
    return " ".join(prompt.split())


# -------------------------------
# SIDEBAR
# -------------------------------
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="logo-title">PromptNexus AI</div>
        <div class="logo-subtitle">Where prompts become intelligence.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### ⚡ Use Cases")
    st.markdown("""
    - Content Writing  
    - Coding  
    - Business Ideas  
    - Resume Building  
    - Marketing  
    - Startup Planning  
    - Study Help  
    - Social Media  
    - Product Descriptions  
    - Email Writing  
    - YouTube Scripts  
    - Image Generation Prompts  
    """)

    st.markdown("### 🎨 Prompt Styles")
    st.markdown("""
    - Professional  
    - Creative  
    - Minimal  
    - Cinematic  
    - Anime  
    - Realistic  
    - Expert  
    """)

# -------------------------------
# HERO SECTION
# -------------------------------
st.markdown("""
<div class="hero-card">
    <div class="badge">🚀 AI Prompt Workspace</div>
    <div class="hero-title">PromptNexus AI</div>
    <div class="hero-desc">
        Generate premium, professional, and ready-to-use prompts for content, coding, business, student needs, and more.
        Designed with a futuristic SaaS-style interface for a cleaner and smarter prompting experience.
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# INPUT SECTION
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    use_case = st.selectbox(
        "Select Use Case",
        ["Content Writing", "Coding", "Business", "Students", "General Use"]
    )

    topic = st.text_input("Topic / Goal", placeholder="e.g. YouTube script for AI tools, portfolio website, resume rewrite")

with col2:
    style = st.selectbox(
        "Prompt Style",
        ["Professional", "Creative", "Minimal", "Cinematic", "Anime", "Realistic", "Expert"]
    )

    audience = st.text_input("Target Audience", placeholder="e.g. beginners, developers, recruiters, startup founders")

extra_details = st.text_area(
    "Extra Details / Requirements",
    placeholder="Add constraints, tone, platform, format, keywords, output expectations, etc.",
    height=140
)

# -------------------------------
# BUTTONS
# -------------------------------
btn1, btn2 = st.columns([2, 1])

with btn1:
    if st.button("✨ Generate Prompt"):
        if topic.strip():
            st.session_state.generated_prompt = build_prompt(
                use_case=use_case,
                topic=topic,
                style=style,
                audience=audience if audience.strip() else "general users",
                extra_details=extra_details
            )
        else:
            st.warning("Please enter a topic or goal first.")

with btn2:
    if st.button("🗑 Clear"):
        st.session_state.generated_prompt = ""

# -------------------------------
# OUTPUT SECTION
# -------------------------------
st.markdown('<div class="section-title">Prompt’s Generation</div>', unsafe_allow_html=True)

if st.session_state.generated_prompt:
    st.markdown(
        f"""
        <div class="prompt-box">
            <div class="prompt-heading">🎯 Prompt</div>
            {st.session_state.generated_prompt}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.text_area(
        "Copy Prompt",
        value=st.session_state.generated_prompt,
        height=220
    )
else:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">No prompt generated yet</div>
        <div class="feature-text">
            Fill in your topic, choose a style, and click <b>Generate Prompt</b> to create a polished AI-ready prompt.
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# FEATURES SECTION
# -------------------------------
st.markdown('<div class="section-title">Why PromptNexus AI?</div>', unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">🧠 Smart Prompt Structuring</div>
        <div class="feature-text">
            Generates prompts that feel refined, goal-oriented, and professional instead of random one-line instructions.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">🎨 Multi-Style Output</div>
        <div class="feature-text">
            Switch between professional, creative, cinematic, anime, realistic, and expert styles based on your exact use case.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">⚡ Ready for Real Work</div>
        <div class="feature-text">
            Useful for content creators, developers, students, marketers, founders, freelancers, and AI enthusiasts.
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("""
<br>
<div style="text-align:center; color:#94A3B8; font-size:14px; padding-bottom:10px;">
    Built with ❤️ By Ganesh Goddilla for smarter prompting • <b>PromptNexus AI</b>
</div>
""", unsafe_allow_html=True)