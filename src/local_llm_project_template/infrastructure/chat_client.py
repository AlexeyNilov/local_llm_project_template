from openai import AsyncOpenAI

from local_llm_project_template.config import LLM_BASE_URL, LLM_API_KEY

chat_client = AsyncOpenAI(
    api_key=LLM_BASE_URL,
    base_url=LLM_API_KEY,
)
