mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
[theme]\n\
base=\"dark\"\n\
primaryColor=\"white\"\n\
\n\
" > ~/.streamlit/config.toml
