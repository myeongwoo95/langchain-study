from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import DatetimeOutputParser
from langchain.schema import HumanMessage

output_parser = DatetimeOutputParser() # 초기화