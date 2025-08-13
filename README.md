    AI Research Agent 

This project is an AI-powered research agent designed to provide a comprehensive, summarized report on a company and a specific job role. The application features a simple web interface built with Streamlit, where users can input a company name and a job role. In the backend, the agent uses a multi-step process to gather information from the web and an LLM to synthesize the findings into a clear, structured report. This project demonstrates API integration, agentic workflow design, and data summarization.

Features: <br>
Company Overview: Provides details on the company's domain, size, work-life balance, and latest news.<br>
Job-Specific Details: Gathers information on the required skills, experience, and typical salary range for a given role.<br>

Tech Stack: <br>
Frontend: Streamlit <br>
Backend & Core Logic: Python<br>
Web Search: Google Custom Search API<br>
AI Model: Groq API and Gemini API<br>

Initialization and Run:<br>
1. Prerequisites<br>
   Python 3.8+ installed on your system.<br>
   API Keys: You will need to obtain the following API keys:<br>
   Google Custom Search API Key and a Search Engine ID (cx).<br>
   Groq API Key.<br>


2. Cloning the repository:<br>
   git clone https://github.com/your-username/your-repository-name.git<br>
   cd your-repository-name<br>
   
3. pip install -r requirements.txt<br>


I have deployed this in Render. <br>
The URL is https://ai-job-agent-sbhc.onrender.com <br>

4. Creating .env file with following content:<br>
  GOOGLE_API_KEY="your_google_api_key_here"
  SEARCH_ENGINE_ID="your_custom_search_engine_id_here"
  GROQ_API_KEY="your_groq_api_key_here"

4. streamlit run app.py
