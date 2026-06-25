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

st.title("🤖 AI Interview Preparation Assistant")
st.markdown("Upload your resume and prepare for interviews using AI.")

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

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    # Extract Resume Text
    with st.spinner("Reading Resume..."):
        resume_text = extract_resume_text(uploaded_file)

    # Analyze Resume
    with st.spinner("Analyzing Resume..."):
        st.session_state.resume_summary = analyze_resume(
            resume_text
        )

    st.success("Resume Uploaded Successfully!")

    # -----------------------------------
    # TABS
    # -----------------------------------

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

            st.subheader(
                "Generated Questions"
            )

            st.text_area(
                "Questions",
                value=st.session_state.questions,
                height=350
            )

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

else:

    st.info(
        "Please upload a resume to get started."
    )