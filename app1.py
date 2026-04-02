import streamlit as st

# -------------------------------
# 🔧 PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="PromptForge AI", page_icon="⚡", layout="centered")

# -------------------------------
# 🎨 UI HEADER
# -------------------------------
st.markdown("## ⚡ ganEEEE Prompt Magic")
st.caption("Generate powerful AI prompts with smart guided questions.")

# -------------------------------
# 🧠 FUNCTION: DYNAMIC QUESTIONS
# -------------------------------
def generate_questions(intent):

    if "resume" in intent or "cv" in intent:
        return [
            ("1. Basic Info", "Are you a student, fresher, or experienced professional?", "e.g. Fresher"),
            ("2. Industry", "What is your field/industry?", "e.g. IT, Mechanical"),
            ("3. Target Role", "What role are you targeting?", "e.g. Software Engineer"),
            ("4. Background", "Education / projects / experience?", "e.g. B.Tech + ML project"),
            ("5. Skills", "Key skills?", "e.g. Python, SQL, Communication"),
            ("6. Style", "Resume style?", "ATS-friendly or creative"),
            ("7. Output", "1-page or 2-page?", "e.g. 1-page concise"),
            ("8. Tone", "Tone?", "Formal / Professional")
        ]

    elif "image" in intent:
        return [
            ("1. Image Type", "What type of image?", "e.g. realistic, cartoon, 3D"),
            ("2. Subject", "Main subject?", "e.g. person, product, landscape"),
            ("3. Style", "Art style?", "e.g. cinematic, anime, photorealistic"),
            ("4. Colors", "Color theme?", "e.g. dark, vibrant, pastel"),
            ("5. Usage", "Where will it be used?", "e.g. Instagram, thumbnail"),
            ("6. Details", "Extra details?", "e.g. lighting, background elements"),
            ("7. Quality", "Resolution?", "HD, 4K, ultra realistic")
        ]

    elif "youtube" in intent:
        return [
            ("1. Topic", "Video topic?", "e.g. AI tools that save time"),
            ("2. Audience", "Target audience?", "e.g. students, beginners"),
            ("3. Duration", "Video length?", "Short or long"),
            ("4. Style", "Video style?", "Storytelling, educational"),
            ("5. Goal", "Purpose?", "Views, engagement"),
            ("6. Platform", "Platform?", "YouTube Shorts / Long"),
            ("7. Tone", "Tone?", "Energetic, fun")
        ]

    else:
        return [
            ("1. Goal", "What do you want to achieve?", "e.g. Build a startup idea"),
            ("2. Context", "Topic or domain?", "e.g. fintech, AI"),
            ("3. Audience", "Target users?", "e.g. developers"),
            ("4. Format", "Output format?", "e.g. steps, list"),
            ("5. Tone", "Tone?", "Professional, casual"),
            ("6. Constraints", "Any limits?", "e.g. 60 sec, simple language")
        ]

# -------------------------------
# 🧠 MAIN INPUT
# -------------------------------
user_input = st.text_input(
    "What do you want to create?",
    placeholder="e.g. resume, image, youtube script..."
)

intent = user_input.strip().lower() if user_input else ""

# -------------------------------
# 🤖 SMART INTERACTIVE MODE
# -------------------------------
if intent != "":

    st.info(f"🧠 Smart Mode Activated for: {user_input}")

    questions = generate_questions(intent)
    answers = {}

    st.markdown(f"""
### 👋 Let's build your prompt step-by-step

You said: **{user_input}**

Answer a few questions to generate a powerful prompt 👇
""")

    for title, question, example in questions:
        st.markdown(f"### {title}")
        answers[title] = st.text_input(question, placeholder=example, key=title)
        st.caption(f"👉 Example: {example}")

    # -------------------------------
    # 🚀 GENERATE PROMPTS
    # -------------------------------
    if st.button("🚀 Generate Prompts", use_container_width=True):

        with st.spinner("Generating high-quality prompts..."):

            response = f"""
🔹 Prompt 1 – Creative Style  
Act as a creative expert. Generate content for "{user_input}" considering:
"""

            for key, value in answers.items():
                response += f"- {key}: {value}\n"

            response += """

🔹 Prompt 2 – Analytical Style  
Break down the task step-by-step with structured reasoning.

🔹 Prompt 3 – Minimal Style  
Create a short, direct, and actionable prompt.

🔹 Prompt 4 – Expert-Level Style  
Act as an industry expert. Generate a high-performance, optimized prompt with advanced techniques.
"""

        st.markdown("### 🔥 Generated Prompts")
        st.code(response)

        col1, col2 = st.columns(2)

        with col1:
            st.download_button("📥 Download", response, file_name="prompts.txt")

        with col2:
            if st.button("🔄 Regenerate"):
                st.rerun()

# -------------------------------
# 💤 EMPTY STATE
# -------------------------------
else:
    st.info("👋 Start by typing what you want to create (resume, image, youtube, etc.)")