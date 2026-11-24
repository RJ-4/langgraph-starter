# langgraph-starter
Test flight fare application for langgraph practice

# Setup
Create a new project using UV:
<code>uv init --no-package </code>

Add dependencies using UV:
<code>uv add langchain langchain-openai langchain-google-genai langgraph python-dotenv black isort </code>

To create virtual env. and download dependencies
<code>uv sync</code>

# .env file:

<li>GEMINI_API_KEY=gemini api key</li>
<li>LANGSMITH_TRACING=true</li>
<li>LANGSMITH_ENDPOINT=https://apac.api.smith.langchain.com</li>
<li>LANGSMITH_API_KEY=langsmith api key</li>