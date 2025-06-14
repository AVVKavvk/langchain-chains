from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatDeepSeek(model="deepseek-chat",max_tokens=100)

prompt = PromptTemplate(
  template="Tell me 4 point about {topic}",
  input_variables=["topic"],
)
parser =StrOutputParser()
chain = prompt | model | parser
result = chain.invoke({"topic": "Music"})

chain.get_graph().print_ascii()