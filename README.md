
This project is an AI-powered chatbot built with Streamlit for an interactive UI and integrates with the OpenAI API to generate smart responses. 
It manages dependencies in a virtual environment, uses Weaviate for vector database storage, and follows secure practices by storing sensitive credentials in a `.env` file (ignored by Git).
Features include a conversational interface built with Streamlit, OpenAI API integration, vector storage with Weaviate for better query handling, dependency isolation via a virtual environment, and secure config management using environment variables. 
To install, clone the repository with `git clone <your-repo-url>` and `cd chatbot_backend`. Set up a virtual environment: on macOS/Linux, run `python3 -m venv venv` and `source venv/bin/activate`; on Windows PowerShell, run `python -m venv venv` and `.\venv\Scripts\Activate.ps1`. 
Install dependencies with `pip install -r requirements.txt`; if `requirements.txt` is missing, generate it using `pip freeze > requirements.txt`. Configure environment variables by copying `.env.example` to `.env` and adding your OpenAI API key and Weaviate URL: `OPENAI_API_KEY=your_api_key_here` and `WEAVIATE_URL=your_weaviate_instance_url`.
To run the chatbot, activate your virtual environment and execute `streamlit run main.py`, which will open the app in your default browser.
The project structure includes `.env` for environment variables (ignored by Git), `.env.example` as a template, `.gitignore` to exclude unnecessary files, `main.py` as the Streamlit entry point, `requirements.txt` for Python dependencies, and `venv/` as the virtual environment directory.
<img width="1086" height="686" alt="image" src="https://github.com/user-attachments/assets/5019969e-2cb3-47d1-a65c-0591a07f1708" />
<img width="832" height="575" alt="image" src="https://github.com/user-attachments/assets/04a4d0b2-0b1d-40c6-aad3-2a16f6e54ec4" />
<img width="735" height="638" alt="image" src="https://github.com/user-attachments/assets/40dc32d3-17a7-4b8a-af84-0d5172cef7d8" />

