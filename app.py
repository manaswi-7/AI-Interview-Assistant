import streamlit as st

from resume_parser import extract_resume_text
from resume_analyzer import analyze_resume
from question_generator import generate_questions
from answer_evaluator import evaluate_answer

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI Interview Assistant",
    page_icon="🤖",
    layout="wide"
)

st.markdown(
    """
    <h1 style='text-align:center; color:#4F8BF9;'>
        🤖 AI Interview Preparation Assistant
    </h1>
    <p style='text-align:center; font-size:20px; color:gray;'>
        Upload your resume, practice interview questions,
        and get AI-powered feedback.
    </p>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")
# -----------------------------------
# SESSION STATE
# -----------------------------------

if "resume_summary" not in st.session_state:
    st.session_state.resume_summary = ""

if "questions" not in st.session_state:
    st.session_state.questions = ""

# -----------------------------------
# RESUME UPLOAD
# -----------------------------------

left, center, right = st.columns([1, 2, 1])

with center:
    st.subheader("📄 Upload Resume")

    uploaded_file = st.file_uploader(
        "",
        type=["pdf"],
        label_visibility="collapsed"
    )
if uploaded_file:

    st.success("Resume selected successfully.")

    if st.button("🚀 Submit Resume", use_container_width=True):

        with st.spinner("Reading Resume..."):
            resume_text = extract_resume_text(uploaded_file)

        with st.spinner("Analyzing Resume..."):
            st.session_state.resume_summary = analyze_resume(
                resume_text
            )

        st.success("Resume analyzed successfully!")

    # -----------------------------------
    # TABS
    # -----------------------------------

    if st.session_state.resume_summary:

        tab1, tab2, tab3 = st.tabs(
            [
                "📋 Resume Analysis",
                "🎯 Interview Questions",
                "📝 Answer Evaluation"
            ]
        )

    # ===================================
    # TAB 1 - RESUME ANALYSIS
    # ===================================

        with tab1:

            st.subheader("Resume Analysis")

            st.write(
                st.session_state.resume_summary
            )

    # ===================================
    # TAB 2 - QUESTIONS
    # ===================================

        with tab2:

            st.subheader(
                "Generate Interview Questions"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                if st.button(
                    "Technical Questions"
                ):

                    with st.spinner(
                        "Generating Technical Questions..."
                    ):

                        st.session_state.questions = (
                            generate_questions(
                                st.session_state.resume_summary,
                                "technical"
                            )
                        )

            with col2:

                if st.button(
                    "Project Questions"
                ):

                    with st.spinner(
                        "Generating Project Questions..."
                    ):

                        st.session_state.questions = (
                            generate_questions(
                                st.session_state.resume_summary,
                                "project"
                            )
                        )

            with col3:

                if st.button(
                    "HR Questions"
                ):

                    with st.spinner(
                        "Generating HR Questions..."
                    ):

                        st.session_state.questions = (
                            generate_questions(
                                st.session_state.resume_summary,
                                "hr"
                            )
                        )

            st.markdown("---")

            if st.session_state.questions:

                st.subheader("Generated Questions")

                cleaned_questions = (
                    st.session_state.questions
                    .replace("**", "")
                    .replace('"', "")
                )

                for line in cleaned_questions.split("\n"):
                    if line.strip():
                        st.write(line)

    # ===================================
    # TAB 3 - ANSWER EVALUATION
    # ===================================

        with tab3:

            st.subheader(
                "Evaluate Your Answer"
            )

            question = st.text_area(
                "Interview Question",
                height=120
            )

            answer = st.text_area(
                "Your Answer",
                height=250
            )

            if st.button(
                "Evaluate Answer"
            ):

                if not question.strip():

                    st.warning(
                        "Please enter a question."
                    )

                elif not answer.strip():

                    st.warning(
                        "Please enter your answer."
                    )

                else:

                    with st.spinner(
                        "Evaluating Answer..."
                    ):

                        feedback = evaluate_answer(
                            question,
                            answer
                        )

                    st.success(
                        "Evaluation Complete!"
                    )

                    st.markdown(
                        "### AI Feedback"
                    )

                    st.write(feedback)

elif not uploaded_file:

    st.info(
        "Please upload a resume to get started."
    )