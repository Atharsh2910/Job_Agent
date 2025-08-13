import os
import google.generativeai as genai
from googleapiclient.discovery import build
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

def google_search(query, num_results=5):
    """
    Performs a Google Custom Search and returns a list of results.
    
    Args:
        query (str): The search query string.
        num_results (int): The number of search results to return.
        
    Returns:
        list: A list of search result items with titles, snippets, and links.
    """
    try:
        service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
        res = service.cse().list(
            q=query,
            cx=SEARCH_ENGINE_ID,
            num=num_results
        ).execute()
        return res.get('items', [])
    except Exception as e:
        print(f"An error occurred during search: {e}")
        return []

def summarize_data(context, company_name, job_role):

    try:
        client = Groq(api_key=GROQ_API_KEY)
        prompt = f"""
        You are a highly skilled research analyst. Your task is to analyze the following
        information about {company_name} and the job role of {job_role}.
        
        Based on the provided context, generate a structured report that includes:
        
        ### Company Overview
        - **Domain/Industry:**
        - **Company Size:**
        - **Latest News/Updates:**
        - **Work-Life Balance & Culture:**
        
        ### Job Role Details for {job_role}
        - **Key Skills & Qualifications:**
        - **Expected Experience:**
        - **Typical Salary Range:**
        
        Use only the information provided below. If a detail is not available, state "Not specified in the available data."
        Make the final output easy to read using markdown formatting.

        ---
        Provided Context:
        {context}
        """
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred during summarization: {e}"


def run_research(company_name, job_role):
    """
    Orchestrates the entire research workflow.
    
    Args:
        company_name (str): The name of the company.
        job_role (str): The job role.
        
    Returns:
        str: The final research report.
    """

    company_queries = [
        f"{company_name} company overview industry",
        f"{company_name} company size employees",
        f"{company_name} work life balance culture",
        f"{company_name} latest news"
    ]
    
    job_queries = [
        f"{job_role} salary at {company_name}",
        f"{job_role} skills and qualifications at {company_name}",
        f"{job_role} experience requirements at {company_name}"
    ]
    
    all_queries = company_queries + job_queries

    all_snippets = []
    for query in all_queries:
        results = google_search(query)
        for item in results:
            snippet = item.get('snippet', '')
            link = item.get('link', '')
            all_snippets.append(f"Snippet: {snippet}\nLink: {link}\n\n")

    consolidated_context = "\n".join(all_snippets)

    if not consolidated_context:
        return "No information found. Please try a different company or job role."
    
    final_report = summarize_data(consolidated_context, company_name, job_role)
    return final_report