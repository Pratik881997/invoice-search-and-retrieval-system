from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
import json
import re


llm = ChatOllama(
    model="mistral",
    temperature=0
)


def clean_json_response(text):
    match = re.search(r'\{.*\}', text, re.DOTALL)
    return match.group(0) if match else "{}"


def parse_invoice(text: str):
    """
    Returns:
    {
        "page_content": "...",
        "metadata": {...}
    }
    """

    prompt = ChatPromptTemplate.from_template("""
You are an expert invoice parser.

Extract structured data and also create a clean readable summary.

Return JSON with EXACT structure:

{{
  "page_content": "Create a clean, readable invoice summary for LLM understanding. Format it well.",
  "metadata": {{
    "invoice_no": "...",
    "date": "...",
    "client_name": "...",
    "seller_name": "...",
    "total_amount": "..."
  }}
}}

Rules:
- If any field is missing, return null
- Do NOT hallucinate
- Ensure valid JSON only

Invoice Text:
{text}
""")

    chain = prompt | llm
    response = chain.invoke({"text": text})

    raw = response.content
    cleaned = clean_json_response(raw)

    try:
        return json.loads(cleaned)
    except:
        return {
            "page_content": text[:1000],  # fallback
            "metadata": {}
        }