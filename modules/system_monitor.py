import streamlit as st
import psutil
import platform
from datetime import datetime


def show():

    st.title("🖥️ System Monitor")
    st.caption("Monitor the health and performance of your system in real time.")

    st.markdown("---")

    # ==========================================
    # Collect System Information
    # ==========================================

    cpu = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()

    disk = psutil.disk_usage('/')

    boot_time = datetime.fromtimestamp(
        psutil.boot_time()
    )

    # ==========================================
    # Top Metrics
    # ==========================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "💻 CPU Usage",
            f"{cpu}%"
        )

    with col2:
        st.metric(
            "🧠 RAM Usage",
            f"{memory.percent}%"
        )

    with col3:
        st.metric(
            "💾 Disk Usage",
            f"{disk.percent}%"
        )

    st.markdown("---")

    # ==========================================
    # Usage Bars
    # ==========================================

    st.subheader("📊 Resource Utilization")

    st.write("💻 CPU Usage")
    st.progress(int(cpu))

    st.write("🧠 RAM Usage")
    st.progress(int(memory.percent))

    st.write("💾 Disk Usage")
    st.progress(int(disk.percent))

    st.markdown("---")

    # ==========================================
    # System Details
    # ==========================================

    st.subheader("🖥️ System Information")

    info1, info2 = st.columns(2)

    with info1:

        st.info(
            f"""
**Operating System**

{platform.system()} {platform.release()}
"""
        )

        st.info(
            f"""
**Processor**

{platform.processor()}
"""
        )

        st.info(
            f"""
**Machine**

{platform.machine()}
"""
        )

    with info2:

        st.info(
            f"""
**Python Version**

{platform.python_version()}
"""
        )

        st.info(
            f"""
**Boot Time**

{boot_time.strftime("%d-%m-%Y %H:%M:%S")}
"""
        )

        st.info(
            f"""
**Architecture**

{platform.architecture()[0]}
"""
        )

    st.markdown("---")

    # ==========================================
    # Health Status
    # ==========================================

    st.subheader("🟢 System Health")

    if cpu < 70 and memory.percent < 80 and disk.percent < 90:

        st.success("✅ System is running normally.")

    elif cpu < 90:

        st.warning("⚠️ Moderate system load detected.")

    else:

        st.error("❌ High system usage detected.")

    st.markdown("---")

    # ==========================================
    # Refresh
    # ==========================================

    if st.button("🔄 Refresh System Status"):

        st.rerun()