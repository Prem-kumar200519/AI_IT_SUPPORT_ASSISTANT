import streamlit as st
import time


def show(llm):

    st.title("📄 AI Log Analyzer")
    st.caption("Upload Windows or Linux log files for AI-powered troubleshooting.")

    uploaded_file = st.file_uploader(
        "Choose a log file",
        type=["txt", "log"]
    )

    if uploaded_file is not None:

        # ==========================================
        # Read Uploaded File
        # ==========================================

        log_content = uploaded_file.read().decode("utf-8")

        total_lines = len(log_content.splitlines())
        file_size = round(uploaded_file.size / 1024, 2)

        # ==========================================
        # File Information
        # ==========================================

        st.markdown("---")
        st.subheader("📁 File Information")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("📄 File Name", uploaded_file.name)

        with col2:
            st.metric("📦 File Size", f"{file_size} KB")

        with col3:
            st.metric("📑 Total Lines", total_lines)

        # ==========================================
        # View Log File
        # ==========================================

        with st.expander("📄 View Uploaded Log File"):

            st.text_area(
                "Log Content",
                log_content,
                height=250
            )

        # ==========================================
        # Detect Errors & Warnings
        # ==========================================

        errors = []
        warnings = []

        for line in log_content.splitlines():

            upper = line.upper()

            if "ERROR" in upper:
                errors.append(line)

            elif "WARNING" in upper:
                warnings.append(line)

        # ==========================================
        # Summary
        # ==========================================

        st.markdown("---")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("❌ Errors", len(errors))

        with c2:
            st.metric("⚠️ Warnings", len(warnings))

        with c3:
            st.metric("📄 Lines", total_lines)

        # ==========================================
        # Severity
        # ==========================================

        st.subheader("🚨 Severity")

        if len(errors) == 0:
            st.success("🟢 LOW")

        elif len(errors) <= 5:
            st.warning("🟡 MEDIUM")

        else:
            st.error("🔴 HIGH")

        # ==========================================
        # Errors
        # ==========================================

        st.markdown("---")
        st.subheader("❌ Errors Found")

        if errors:
            for error in errors:
                st.error(error)
        else:
            st.success("No errors detected.")

        # ==========================================
        # Warnings
        # ==========================================

        st.subheader("⚠️ Warnings Found")

        if warnings:
            for warning in warnings:
                st.warning(warning)
        else:
            st.success("No warnings detected.")

        # ==========================================
        # AI Prompt
        # ==========================================

        analysis_prompt = f"""
You are a Senior IT Support Engineer.

Analyze the following log file.

Provide:

1. Summary
2. Errors Found
3. Warnings Found
4. Possible Causes
5. Step-by-step Troubleshooting
6. Final Recommendation

Log File:

{log_content}
"""

        # ==========================================
        # AI Analysis
        # ==========================================

        st.markdown("---")
        st.subheader("🤖 AI Analysis")

        start = time.time()

        with st.spinner("🔍 AI is analyzing the log file..."):
            analysis = llm.invoke(analysis_prompt)

        end = time.time()

        st.write(analysis.content)

        # ==========================================
        # Footer
        # ==========================================

        col1, col2 = st.columns([3, 1])

        with col1:
            st.caption(
                f"⏱️ Analysis completed in {end - start:.2f} seconds"
            )

        with col2:
            st.download_button(
                label="📥 Download Report",
                data=analysis.content,
                file_name="AI_Log_Analysis_Report.txt",
                mime="text/plain"
            )