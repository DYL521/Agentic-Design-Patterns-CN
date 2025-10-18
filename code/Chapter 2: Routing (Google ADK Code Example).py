# Copyright (c) 2025 Marco Fago
# 版权所有 (c) 2025 Marco Fago
#
# This code is licensed under the MIT License.
# 本代码根据 MIT 许可证授权。
# See the LICENSE file in the repository for the full license text.
# 请参阅仓库中的 LICENSE 文件获取完整许可证文本。

import uuid
from typing import Dict, Any, Optional

from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from google.adk.tools import FunctionTool
from google.genai import types
from google.adk.events import Event

# --- Define Tool Functions ---
# --- 定义工具函数 ---
# These functions simulate the actions of the specialist agents.
# 这些函数模拟专业代理的操作。

def booking_handler(request: str) -> str:
    """
    Handles booking requests for flights and hotels.
    处理航班和酒店预订请求。
    Args:
        request: The user's request for a booking.
        request: 用户的预订请求。
    Returns:
        A confirmation message that the booking was handled.
        一条确认预订已处理的消息。
    """
    print("-------------------------- Booking Handler Called ----------------------------")
    return f"Booking action for '{request}' has been simulated."

def info_handler(request: str) -> str:
    """
    Handles general information requests.
    处理一般信息请求。
    Args:
        request: The user's question.
        request: 用户的问题。
    Returns:
        A message indicating the information request was handled.
        一条指示信息请求已处理的消息。
    """
    print("-------------------------- Info Handler Called ----------------------------")
    return f"Information request for '{request}'. Result: Simulated information retrieval."

def unclear_handler(request: str) -> str:
    """Handles requests that couldn't be delegated."""
    """处理无法委派的请求。"""
    return f"Coordinator could not delegate request: '{request}'. Please clarify."

# --- Create Tools from Functions ---
# --- 从函数创建工具 ---
booking_tool = FunctionTool(booking_handler)
info_tool = FunctionTool(info_handler)

# Define specialized sub-agents equipped with their respective tools
# 定义配备各自工具的专业子代理
booking_agent = Agent(
    name="Booker",
    model="gemini-2.0-flash",
    description="A specialized agent that handles all flight and hotel booking requests by calling the booking tool.",
    description="一个专门的代理，通过调用预订工具处理所有航班和酒店预订请求。",
    tools=[booking_tool]
)

info_agent = Agent(
    name="Info",
    model="gemini-2.0-flash",
    description="A specialized agent that provides general information and answers user questions by calling the info tool.",
    description="一个通过调用信息工具提供一般信息并回答用户问题的专业代理。",
    tools=[info_tool]
)

# Define the parent agent with explicit delegation instructions
# 定义带有明确委派指令的父代理
coordinator = Agent(
    name="Coordinator",
    model="gemini-2.0-flash",
    instruction=(
        "你是主协调员。你唯一的任务是分析传入的用户请求，并将其委派给适当的专业代理。不要直接尝试回答用户。\n"
        "- 对于任何与预订航班或酒店相关的请求，委派给'Booker'代理。\n"
        "- 对于所有其他一般信息问题，委派给'Info'代理。"
    ),
    instruction=(
        "你是主协调员。你唯一的任务是分析传入的用户请求，并将其委派给适当的专业代理。不要直接尝试回答用户。\n"
        "- 对于任何与预订航班或酒店相关的请求，委派给'Booker'代理。\n"
        "- 对于所有其他一般信息问题，委派给'Info'代理。"
    ),
    description="A coordinator that routes user requests to the correct specialist agent.",
    description="一个将用户请求路由到正确专业代理的协调器。",
    # The presence of sub_agents enables LLM-driven delegation (Auto-Flow) by default.
    # 子代理的存在默认启用了由大语言模型驱动的委派（自动流）。
    sub_agents=[booking_agent, info_agent]
)

# --- Execution Logic ---
# --- 执行逻辑 ---

def run_coordinator(runner: InMemoryRunner, request: str):
    """Runs the coordinator agent with a given request and delegates."""
    """使用给定的请求运行协调器代理并进行委派。"""
    print(f"\n--- Running Coordinator with request: '{request}' ---")
    final_result = ""
    try:
        user_id = "user_123"
        session_id = str(uuid.uuid4())
        runner.session_service.create_session(
            app_name=runner.app_name, user_id=user_id, session_id=session_id
        )

        for event in runner.run(
            user_id=user_id,
            session_id=session_id,
            new_message=types.Content(
                role='user',
                parts=[types.Part(text=request)]
            ),
        ):
            if event.is_final_response() and event.content:
                # Try to get text directly from event.content to avoid iterating parts
                # 尝试直接从 event.content 获取文本以避免迭代部分
                if hasattr(event.content, 'text') and event.content.text:
                     final_result = event.content.text
                elif event.content.parts:
                    # Fallback: Iterate through parts and extract text (might trigger warning)
                    # 回退：遍历部分并提取文本（可能触发警告）
                    text_parts = [part.text for part in event.content.parts if part.text]
                    final_result = "".join(text_parts)
                # Assuming the loop should break after the final response
                # 假设循环应在最终响应后中断
                break

        print(f"Coordinator Final Response: {final_result}")
        return final_result
    except Exception as e:
        print(f"An error occurred while processing your request: {e}")
        return f"An error occurred while processing your request: {e}"

def main():
    """Main function to run the ADK example."""
    """运行 ADK 示例的主函数。"""
    print("--- Google ADK Routing Example (ADK Auto-Flow Style) ---")
    print("Note: This requires Google ADK installed and authenticated.")
    print("注意：这需要已安装和认证的 Google ADK。")

    runner = InMemoryRunner(coordinator)
    # Example Usage
    # 示例用法
    result_a = run_coordinator(runner, "Book me a hotel in Paris.")
    print(f"Final Output A: {result_a}")
    result_b = run_coordinator(runner, "What is the highest mountain in the world?")
    print(f"Final Output B: {result_b}")
    result_c = run_coordinator(runner, "Tell me a random fact.") # Should go to Info
    print(f"Final Output C: {result_c}")
    result_d = run_coordinator(runner, "Find flights to Tokyo next month.") # Should go to Booker
    print(f"Final Output D: {result_d}")


if __name__ == "__main__":
    main()