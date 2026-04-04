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



import streamlit as st

# -------------------------------
# 🔧 PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="PromptForge AI", page_icon="⚡", layout="centered")

# -------------------------------
# 💾 SESSION STATE
# -------------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -------------------------------
# 🔐 LOGIN SYSTEM (FREE)
# -------------------------------
def login():
    st.title("🔐 Login to PromptForge AI")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Simple free login (you can change credentials)
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("Login successful 🚀")
            st.rerun()
        else:
            st.error("Invalid credentials")

# -------------------------------
# 🎨 STYLING
# -------------------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.main {
    background: linear-gradient(180deg, #0e1117 0%, #111827 100%);
}
.card {
    background: #1f2937;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
}
.stButton>button {
    background: linear-gradient(90deg, #4CAF50, #22c55e);
    color: white;
    border-radius: 12px;
    height: 45px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# 🧠 STYLE PROMPT ENGINE
# -------------------------------
def get_style_prompt(style):
    if style == "Cinematic":
        return "cinematic lighting, dramatic shadows, ultra realistic, 8k, depth of field, movie still, high contrast"
    elif style == "Anime":
        return "anime style, vibrant colors, sharp lines, highly detailed, dynamic pose"
    elif style == "Realistic":
        return "photorealistic, ultra detailed, 8k resolution, realistic textures, natural lighting"
    elif style == "Marvel Style":
        return "Marvel cinematic universe style, superhero aesthetics, epic pose, glowing energy, dramatic lighting"

# -------------------------------
# 🧠 PROMPT ENGINE
# -------------------------------
def generate_prompts(user_input, answers):

    intent = user_input.lower()

    # 🎯 ROLE-BASED PROMPTS (NEW LOGIC)
    if "youtube" in intent:

        topic = answers.get("Goal", "")
        audience = answers.get("Audience", "")

        return f"""
🔹 Prompt 1 – Expert Script Writer  
Act as an experienced YouTube content creator.  
Create an engaging script about "{topic}" for {audience}.  
Include a strong hook, storytelling, and a clear structure (intro, main content, conclusion).  

🔹 Prompt 2 – Growth Focused  
Act as a YouTube growth strategist.  
Write a viral-ready script on "{topic}" targeting {audience}.  
Focus on retention, curiosity gaps, and engagement techniques.  

🔹 Prompt 3 – Minimal  
Write a YouTube script about "{topic}" for {audience}.  

🔹 Prompt 4 – Professional  
Act as a professional scriptwriter.  
Create a high-quality, well-structured YouTube script on "{topic}" tailored for {audience}.  
Ensure clarity, engagement, and audience retention.
"""

    elif "resume" in intent:

        role = answers.get("Role", "job role")
        skills = answers.get("Skills", "")

        return f"""
🔹 Prompt 1 – Career Coach  
You are an experienced career coach.  
Review my resume for a "{role}" position and suggest improvements.  
Focus on clarity, impact, and ATS optimization.  

🔹 Prompt 2 – Recruiter Perspective  
Act as a recruiter hiring for "{role}".  
Evaluate my resume and suggest what to improve to stand out.  

🔹 Prompt 3 – Minimal  
Review my resume for {role}.  

🔹 Prompt 4 – Expert  
Act as a senior hiring manager.  
Provide detailed feedback on my resume for a "{role}" role, focusing on achievements, structure, and keywords.
"""

    elif "image" in intent:

        character = answers.get("Character", "")
        pose = answers.get("Pose", "")
        background = answers.get("Background", "")
        colors = answers.get("Colors", "")
        style = answers.get("Style", "")

        style_prompt = get_style_prompt(style)

        return f"""
🔹 Prompt 1 – Professional AI Artist  
Act as a professional AI artist.  
Create a highly detailed image of a {character}, {pose}, in a {background}.  
Use {colors} color palette and {style} style.  
Apply cinematic lighting, depth of field, and ultra-high resolution (8K).

🔹 Prompt 2 – Creative Direction  
Act as a creative director.  
Design a visually stunning {character} performing {pose} in {background},  
with {colors} tones and {style} aesthetics.  

🔹 Prompt 3 – Minimal  
{character}, {pose}, {background}, {colors}, {style}, high quality  

🔹 Prompt 4 – Expert-Level Prompt  
Act as an expert prompt engineer.  
Generate a production-quality AI image prompt for a {character} in {background},  
with {pose}, {colors}, and {style}.  
Include lighting, composition, textures, and realism enhancements.
"""

    # 🔥 DEFAULT (SMART GENERIC)
    return f"""
🔹 Prompt 1 – Expert  
Act as an expert in the field.  
Help me with: "{user_input}".  
Provide clear, structured, and actionable output.

🔹 Prompt 2 – Creative  
Act as a creative professional.  
Generate innovative ideas for: "{user_input}".

🔹 Prompt 3 – Minimal  
{user_input}

🔹 Prompt 4 – Professional  
Act as an industry expert.  
Deliver high-quality output for: "{user_input}" with clarity and depth.
"""

    # DEFAULT
    base = f"Task: {user_input}\n"
    for k, v in answers.items():
        base += f"- {k}: {v}\n"

    return f"""
🔹 Prompt 1 – Creative  
{base}

🔹 Prompt 2 – Analytical  
Break step-by-step:
{base}

🔹 Prompt 3 – Minimal  
{user_input}

🔹 Prompt 4 – Expert  
{base}
"""

# -------------------------------
# 🔐 LOGIN CHECK
# -------------------------------
if not st.session_state.logged_in:
    login()
    st.stop()

# -------------------------------
# 📌 SIDEBAR
# -------------------------------
st.sidebar.title("⚡ PromptForge AI")

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📜 History", "ℹ️ About"]
)

# =========================================================
# 🏠 HOME
# =========================================================
if page == "🏠 Home":

    st.title("⚡ PromptForge AI")
    st.markdown("Generate powerful prompts like a pro 🚀")

    user_input = st.text_input(
        "What do you want to create?",
        placeholder="e.g. image, resume, youtube..."
    )

    if user_input:

        answers = {}

        # 🔥 IMAGE UI (NEW)
        if "image" in user_input.lower():

            st.markdown("### 🎨 Image Settings")

            answers["Character"] = st.text_input("Character Type", "male superhero")
            answers["Pose"] = st.text_input("Pose", "standing confidently")
            answers["Background"] = st.text_input("Background", "space")
            answers["Colors"] = st.text_input("Color Theme", "pastel colors")

            answers["Style"] = st.selectbox(
                "Style",
                ["Cinematic", "Anime", "Realistic", "Marvel Style"]
            )

        else:
            answers["Goal"] = st.text_input("Goal", "startup idea")
            answers["Audience"] = st.text_input("Audience", "developers")

        if st.button("🚀 Generate Prompts"):

            output = generate_prompts(user_input, answers)

            st.markdown("### 🔥 Your Prompts")
            st.code(output)

            st.session_state.history.append(output)

# =========================================================
# 📜 HISTORY
# =========================================================
elif page == "📜 History":

    st.markdown("## 📜 Prompt History")

    if st.session_state.history:
        for item in st.session_state.history[::-1]:
            st.code(item)
    else:
        st.info("No prompts yet.")

# =========================================================
# ℹ️ ABOUT
# =========================================================
else:

    st.markdown("## ℹ️ About")

    st.write("""
PromptForge AI is a smart prompt generator.

🚀 Built by Ganesh Goddilla
⚡ Free version  
💡 Supports image, resume, YouTube prompts  
""")