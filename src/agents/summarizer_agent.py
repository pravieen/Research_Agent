# agents/summarizer_agent.py
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

from src.core import constants

GEMINI_API_KEY = constants.CONFIGURATION['secrets']['GEMINI_API_KEY']

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=GEMINI_API_KEY)

# Prompt for summarizing full paper text
SUMMARIZE_FULL_TEXT_PROMPT = ChatPromptTemplate.from_template(
    "You are a research assistant and expert in scientific literature.\n"
    "Below is the full text of an academic paper:\n\n{full_text}\n\n"
    "Provide a comprehensive, paragraph-style summary including:\n"
    "- The main objective and problem addressed\n"
    "- Key methodologies or theoretical frameworks used\n"
    "- Major findings or contributions\n"
    "- Practical or theoretical implications\n\n"
    "Ensure the summary is detailed, well-structured, and suitable for researchers or students."
)

# Prompt for synthesizing across multiple papers
SYNTHESIZE_PROMPT = ChatPromptTemplate.from_template(
    "You are a senior researcher synthesizing findings from multiple academic papers.\n"
    "Here are summaries of several papers:\n\n{summaries}\n\n"
    "Write a detailed, paragraph-style synthesis that connects themes, identifies trends,\n"
    "highlights contrasting approaches, and outlines implications across the papers.\n"
    "Structure your output to be useful for understanding the field holistically."
)

def summarize_full_text(full_text: str) -> str:
    result = llm.invoke(SUMMARIZE_FULL_TEXT_PROMPT.format(full_text=full_text))
    return result.content.strip()

def synthesize_overview(summaries: list) -> str:
    summaries_str = "\n\n".join(summaries)
    result = llm.invoke(SYNTHESIZE_PROMPT.format(summaries=summaries_str))
    return result.content.strip()