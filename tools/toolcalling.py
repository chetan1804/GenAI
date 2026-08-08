from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain.tools import tool 
from langchain_core.messages import HumanMessage, ToolMessage
from rich import print 

#1 creating a tool 

@tool
def get_text_length(text: str) -> int:
    """Returns the number of character in a given text"""
    return len(text)

tools = {
    "get_text_length" : get_text_length
}
llm = ChatMistralAI(model = "mistral-small-2603")

#tool binding 
llm_with_tool = llm.bind_tools([get_text_length])

message = []
prompt = input("You: ")
query = HumanMessage(prompt)
message.append(query)

result = llm_with_tool.invoke(message)

message.append(result)

if result.tool_calls:
    tool_call = result.tool_calls[0]
    tool_name = tool_call["name"]
    tool_result = tools[tool_name].invoke(tool_call["args"])
    message.append(
        ToolMessage(
            content=str(tool_result),
            tool_call_id=tool_call["id"],
        )
    )

    result = llm_with_tool.invoke(message)

print(result.content)