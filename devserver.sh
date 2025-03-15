#!/bin/sh
##check once https://docs.streamlit.io/knowledge-base/deploy/remote-start
source .venv/bin/activate
python -m streamlit run app.py --server.port $PORT --server.enableCORS=false --server.enableXsrfProtection=false