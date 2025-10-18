import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# For better security, load environment variables from a .env file
# 为了更好的安全性，从 .env 文件加载环境变量
# from dotenv import load_dotenv
# load_dotenv()
# Make sure your OPENAI_API_KEY is set in the .env file
# 确保在 .env 文件中设置了 OPENAI_API_KEY

# Initialize the Language Model (using ChatOpenAI is recommended)
# 初始化语言模型（推荐使用 ChatOpenAI）
llm = ChatOpenAI(temperature=0)

# --- Prompt 1: Extract Information ---
# --- 提示 1：提取信息 ---
prompt_extract = ChatPromptTemplate.from_template(
    "Extract the technical specifications from the following text:\n\n{text_input}"
)

# --- Prompt 2: Transform to JSON ---
# --- 提示 2：转换为 JSON ---
prompt_transform = ChatPromptTemplate.from_template(
    "Transform the following specifications into a JSON object with 'cpu', 'memory', and 'storage' as keys:\n\n{specifications}"
)

# --- Build the Chain using LCEL ---
# --- 使用 LCEL 构建链 ---
# The StrOutputParser() converts the LLM's message output to a simple string.
# StrOutputParser() 将 LLM 的消息输出转换为简单字符串。
extraction_chain = prompt_extract | llm | StrOutputParser()

# The full chain passes the output of the extraction chain into the 'specifications'
# variable for the transformation prompt.
# 完整的链将提取链的输出传递到转换提示的 'specifications' 变量中。
full_chain = (
    {"specifications": extraction_chain}
    | prompt_transform
    | llm
    | StrOutputParser()
)

# --- Run the Chain ---
# --- 运行链 ---
input_text = "The new laptop model features a 3.5 GHz octa-core processor, 16GB of RAM, and a 1TB NVMe SSD."

# Execute the chain with the input text dictionary.
# 使用输入文本字典执行链。
final_result = full_chain.invoke({"text_input": input_text})

print("\n--- Final JSON Output ---")
print("\n--- 最终 JSON 输出 ---")
print(final_result)