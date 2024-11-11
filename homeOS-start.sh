#!/bin/bash
echo "Activating virtual environment..."
source /home/jo/Projects/homeOS/venv/bin/activate
echo "Virtual Environment started Successfully!"
echo "Starting Streamlit application"
cd /home/jo/Projects/homeOS/
streamlit run app.py --server.port 8001