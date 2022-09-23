mkdir -p ~/.streamlit/
echo
"\
[serve]\n\
headless=true\n\
port=$PORT\n\
enableCORS=false\n\
\n\
" > ~/.streamlit/config.toml
