import time
import streamlit as st
import psutil
import subprocess
import os

def get_cpu_usage():
    return [cpu for cpu in psutil.cpu_percent(percpu=True, interval=1)]

def get_cpu_temp():
    result = subprocess.run(["vcgencmd", "measure_temp"], capture_output=True, text=True)
    temp_str = result.stdout.strip()
    return float(temp_str.replace("temp=", "").replace("'C", ""))

def bytes_to_gb(bytes):
    return round(bytes / (1024 * 1024 * 1024), 2)

def get_system_details():
    # Get CPU usage
    cpu_usage = get_cpu_usage()

    # Get memory info
    total_mem = psutil.virtual_memory().total
    free_mem = psutil.virtual_memory().available
    used_mem = total_mem - free_mem

    cpu_temp = get_cpu_temp()

    return {
        "cpu_temp": cpu_temp,
        "cpu_usage": cpu_usage,
        "memory_usage": {
            "total": bytes_to_gb(total_mem),
            "used": bytes_to_gb(used_mem),
            "free": bytes_to_gb(free_mem),
        },
        "hostname": os.uname().nodename,
        "platform": os.uname().sysname,
        "architecture": os.uname().machine
    }

# Streamlit app
st.set_page_config(page_title="System Details", layout="centered")
st.title("🛟 System Monitor")

# Button to refresh system details
if st.button("Refresh System Details"):
    with st.spinner("Fetching system details..."):
    #    time.sleep(1)  # Simulate delay for fetching data
         system_details = get_system_details()

    # Display system information
    st.header("System Information")
    st.write(f"**Hostname:** {system_details['hostname']}")
    st.write(f"**Platform:** {system_details['platform']}")
    st.write(f"**Architecture:** {system_details['architecture']}")
    st.write(f"**CPU Temperature:** {system_details['cpu_temp']:.1f} °C")

    # CPU Usage
    st.subheader("CPU Usage")
    for index, usage in enumerate(system_details['cpu_usage']):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"Core {index}: {usage}%")
        with col2:
            st.progress(usage / 100)

    # Memory Usage
    st.subheader("Memory Usage")
    used_memory = system_details['memory_usage']['used']
    total_memory = system_details['memory_usage']['total']
    
    st.write(f"**Used Memory:** {used_memory:.2f} GB / {total_memory:.2f} GB")
    st.progress(used_memory / total_memory)