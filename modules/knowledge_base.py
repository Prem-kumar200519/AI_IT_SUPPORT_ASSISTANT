import streamlit as st
import os


def show():

    st.title("📚 Company Knowledge Base")
    st.caption("Browse the documents used by the AI Assistant for Retrieval-Augmented Generation (RAG).")

    DATA_FOLDER = "data"

    # ==========================================
    # Check Folder
    # ==========================================

    if not os.path.exists(DATA_FOLDER):
        st.error(f"Folder '{DATA_FOLDER}' not found.")
        return

    files = sorted(os.listdir(DATA_FOLDER))

    # Remove hidden/system files
    files = [f for f in files if not f.startswith(".")]

    # ==========================================
    # Statistics
    # ==========================================

    st.markdown("---")

    total_files = len(files)

    txt_count = len([f for f in files if f.lower().endswith(".txt")])
    pdf_count = len([f for f in files if f.lower().endswith(".pdf")])
    docx_count = len([f for f in files if f.lower().endswith(".docx")])

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("📄 Total Files", total_files)

    with c2:
        st.metric("📝 TXT", txt_count)

    with c3:
        st.metric("📕 PDF", pdf_count)

    with c4:
        st.metric("📘 DOCX", docx_count)

    # ==========================================
    # Description
    # ==========================================

    st.markdown("---")

    st.info(
        """
This repository contains company manuals, troubleshooting guides,
standard operating procedures, and technical documentation.

These files are indexed into the vector database and used by the
AI IT Support Assistant to provide company-specific answers.
"""
    )

    # ==========================================
    # Search
    # ==========================================

    st.markdown("---")

    search = st.text_input(
        "🔍 Search Documents",
        placeholder="Example: Linux, VPN, Windows..."
    )

    if search:

        filtered = [
            file for file in files
            if search.lower() in file.lower()
        ]

    else:
        filtered = files

    # ==========================================
    # Documents
    # ==========================================

    st.markdown("---")

    st.subheader("📂 Available Documents")

    if len(filtered) == 0:

        st.warning("No matching documents found.")

    else:

        for file in filtered:

            path = os.path.join(DATA_FOLDER, file)

            if file.lower().endswith(".pdf"):
                icon = "📕"

            elif file.lower().endswith(".docx"):
                icon = "📘"

            elif file.lower().endswith(".txt"):
                icon = "📄"

            else:
                icon = "📁"

            with st.expander(f"{icon} {file}"):

                try:

                    if file.lower().endswith(".txt"):

                        with open(path, "r", encoding="utf-8") as f:
                            content = f.read()

                        st.text_area(
                            "Preview",
                            content,
                            height=250
                        )

                    else:

                        st.info(
                            "Preview is currently available for TXT files.\n\n"
                            "PDF and DOCX support can be added later."
                        )

                    with open(path, "rb") as download_file:

                        st.download_button(
                            label="📥 Download",
                            data=download_file,
                            file_name=file
                        )

                except Exception as e:

                    st.error(f"Unable to open file.\n\n{e}")

    # ==========================================
    # Footer
    # ==========================================

    st.markdown("---")

    st.success(
        f"Knowledge Base Ready • {total_files} document(s) available."
    )