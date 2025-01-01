import streamlit as st
from src.pipeline.query_pipeline import get_query_engine

# Initialize session state
if 'session' not in st.session_state:
    st.session_state['session'] = False
if 'query_engine' not in st.session_state:
    st.session_state['query_engine'] = None

st.title("Document Q/A System")
document=st.file_uploader("Upload PDF document here")
# Submit button
if st.button("Submit & Process"):
    if document is not None:
        with st.spinner("Processing..."):
            st.session_state['session'] = True
            st.session_state['query_engine'] = get_query_engine(document)
    else:
        st.error("Please upload a document before submitting.")

# Show text input and Ask Query button if session is active
if st.session_state['session']:
    query = st.text_input("Enter your Question from Document here:")
    if st.button("Ask Query"):
        if query.strip() == "":
            st.error("Please enter a valid query.")
        else:
            with st.spinner("Fetching the response..."):
                response = st.session_state['query_engine'].query(str(query))
                st.write(response.response)