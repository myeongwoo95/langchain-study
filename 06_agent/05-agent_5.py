from langchain.agents import AgentType, initialize_agent
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory  #←ConversationBufferMemory 가져오기
from langchain.retrievers import WikipediaRetriever
