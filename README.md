## Question/Answer System
- It is a RAG application which uses <**Gemini 1.5 pro**> LLM model and <**LLAMAINDEX**> for query retrieval and storage of information from user uploaded document.
- It is a question answer application which gives answers the user's question using user uploaded document.

## How to Use
- Currently, simply upload PDF document containing text information.
- Simply ask question from uploaded document which will be answered by the system.

## How to setup
- Create python virtual environment.
        
        virtualenv ./venv

- Activate environment

        - cd ./venv/Scripts
        - activate

- Now get back from the virtual environment directory

        - cd ../..

- Run application at local device

        - streamlit run app.py


## Requirements
- User must setup <**.env**> file in the directory where app.py file is present.

- Create **GEMINI** model API key and paste inside <**.env**> file as following typecase:

        GEMINI_KEY="YOUR API KEY"



