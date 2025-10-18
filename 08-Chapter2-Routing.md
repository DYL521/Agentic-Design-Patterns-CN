- 原文链接：https://docs.google.com/document/d/1ux_n8n3T4bYndOjs1DKW5ccpC802KISdy2IWnlvYbas/edit?tab=t.0#heading=h.4z8lmx41zi0a

# Chapter 2: Routing 路由

## Routing Pattern Overview 路由模式概述


While sequential processing via prompt chaining is a foundational technique for executing deterministic, linear workflows with language models, its applicability is limited in scenarios requiring adaptive responses. Real-world agentic systems must often arbitrate between multiple potential actions based on contingent factors, such as the state of the environment, user input, or the outcome of a preceding operation. This capacity for dynamic decision-making, which governs the flow of control to different specialized functions, tools, or sub-processes, is achieved through a mechanism known as routing.
虽然通过提示链进行顺序处理是使用语言模型执行确定性线性工作流的基础技术，但在需要自适应响应的场景中，其适用性有限。现实世界中的代理系统通常必须根据偶然因素（例如环境状态、用户输入或先前操作的结果）在多个潜在操作之间进行仲裁。这种动态决策能力通过一种称为路由的机制实现，它控制着流向不同专用功能、工具或子流程的控制流。

Routing introduces conditional logic into an agent's operational framework, enabling a shift from a fixed execution path to a model where the agent dynamically evaluates specific criteria to select from a set of possible subsequent actions. This allows for more flexible and context-aware system behavior.
路由将条件逻辑引入代理的操作框架，使其能够从固定的执行路径转变为代理动态评估特定条件并从一系列可能的后续操作中进行选择的模型。这使得系统行为更加灵活，并能够感知上下文。

For instance, an agent designed for customer inquiries, when equipped with a routing function, can first classify an incoming query to determine the user's intent. Based on this classification, it can then direct the query to a specialized agent for direct question-answering, a database retrieval tool for account information, or an escalation procedure for complex issues, rather than defaulting to a single, predetermined response pathway.  Therefore, a more sophisticated agent using routing could:
虽然通过提示链进行顺序处理是使用语言模型执行确定性线性工作流的基础技术，但在需要自适应响应的场景中，其适用性有限。现实世界中的代理系统通常必须根据偶然因素（例如环境状态、用户输入或先前操作的结果）在多个潜在操作之间进行仲裁。这种动态决策能力通过一种称为路由的机制实现，它控制着流向不同专用功能、工具或子流程的控制流。

1.  Analyze the user's query. 
    分析用户的查询。
2.  Route the query based on its intent:
    根据查询意图进行路由

    a. If the intent is "check order status", route to a sub-agent or tool chain that interacts with the order database.
    如果意图是“检查订单状态”，则路由到与订单数据库交互的子代理或工具链。

     b.If the intent is "product information", route to a sub-agent or chain that searches the product catalog.
       如果意图是“产品信息”，则路由到搜索产品目录的子代理或链。
     
     c.If the intent is "technical support", route to a different chain that accesses troubleshooting guides or escalates to a human.
       如果意图是“技术支持”，则路由到访问故障排除指南或升级到人工的不同链。
       
     d.If the intent is unclear, route to a clarification sub-agent or prompt chain.
        如果意图不明确，则转至澄清子代理或提示链。

The core component of the Routing pattern is a mechanism that performs the evaluation and directs the flow. This mechanism can be implemented in several ways:
路由模式的核心组件是一种执行评估并引导流程的机制。该机制可以通过多种方式实现：

+   **LLM-based Routing**: The language model itself can be prompted to analyze the input and output a specific identifier or instruction that indicates the next step or destination. For example, a prompt might ask the LLM to "Analyze the following user query and output only the category: 'Order Status', 'Product Info', 'Technical Support', or 'Other'." The agentic system then reads this output and directs the workflow accordingly.
    **基于 LLM 的路由**: 语言模型本身可以接受提示，分析输入并输出指示下一步或目标的特定标识符或指令。例如，提示可能会要求 LLM“分析以下用户查询并仅输出类别：‘订单状态’、‘产品信息’、‘技术支持’或‘其他’”。然后，代理系统会读取此输出并相应地指导工作流程。

+  **Embedding-based Routing**: The input query can be converted into a vector embedding (see RAG, Chapter 14). This embedding is then compared to embeddings representing different routes or capabilities. The query is routed to the route whose embedding is most similar. This is useful for semantic routing, where the decision is based on the meaning of the input rather than just keywords.
   **基于嵌入的路由**： 输入查询可以转换为向量嵌入（参见 RAG，第 14 章）。然后，将此嵌入与代表不同路由或功能的嵌入进行比较。查询将被路由到嵌入最相似的路由。这对于语义路由非常有用，因为决策基于输入的含义，而不仅仅是关键字

+  **Rule-based Routing**: This involves using predefined rules or logic (e.g., if-else statements, switch cases) based on keywords, patterns, or structured data extracted from the input. This can be faster and more deterministic than LLM-based routing, but is less flexible for handling nuanced or novel inputs.
   **基于规则的路由**：   这涉及使用基于关键字、模式或从输入中提取的结构化数据的预定义规则或逻辑（例如，if-else 语句、switch case）。这比基于 LLM 的路由更快、更确定 ， 但在处理细微差别或新颖的输入时灵活性较差。

+ **Machine Learning Model\-Based Routing**: it employs a discriminative model, such as a classifier, that has been specifically trained on a small corpus of labeled data to perform a routing task. While it shares conceptual similarities with embedding-based methods, its key characteristic is the supervised fine-tuning process, which adjusts the model's parameters to create a specialized routing function. This technique is distinct from LLM-based routing because the decision-making component is not a generative model executing a prompt at inference time. Instead, the routing logic is encoded within the fine-tuned model's learned weights. While LLMs may be used in a pre-processing step to generate synthetic data for augmenting the training set, they are not involved in the real-time routing decision itself.
  **基于机器学习模型的路由** ：它采用一个判别模型（例如分类器），该模型已在小型标记数据语料库上进行专门训练，以执行路由任务。虽然它与基于嵌入的方法在概念上相似，但其关键特征在于监督式微调过程，该过程会调整模型参数以创建专门的路由功能。该技术不同于基于 LLM 的路由，因为决策组件不是在推理时执行提示的生成模型。相反，路由逻辑被编码在微调模型的学习权重中。虽然 LLM 可用于预处理步骤以生成用于扩充训练集的合成数据，但它们本身并不参与实时路由决策。

Routing mechanisms can be implemented at multiple junctures within an agent's operational cycle. They can be applied at the outset to classify a primary task, at intermediate points within a processing chain to determine a subsequent action, or during a subroutine to select the most appropriate tool from a given set.
路由机制可以在代理操作周期的多个环节实现。它们可以在一开始就应用于对主要任务进行分类，也可以在处理链的中间点应用于确定后续操作，或者在子程序运行过程中应用于从给定集合中选择最合适的工具。


Computational frameworks such as LangChain, LangGraph, and Google's Agent Developer Kit (ADK) provide explicit constructs for defining and managing such conditional logic. With its state-based graph architecture, LangGraph is particularly well-suited for complex routing scenarios where decisions are contingent upon the accumulated state of the entire system. Similarly, Google's ADK provides foundational components for structuring an agent's capabilities and interaction models, which serve as the basis for implementing routing logic. Within the execution environments provided by these frameworks, developers define the possible operational paths and the functions or model-based evaluations that dictate the transitions between nodes in the computational graph.
LangChain、LangGraph 和 Google 的 Agent Developer Kit (ADK) 等计算框架提供了用于定义和管理此类条件逻辑的显式结构。LangGraph 凭借其基于状态的图架构，尤其适用于决策取决于整个系统累积状态的复杂路由场景。同样，Google 的 ADK 提供了用于构建代理功能和交互模型的基础组件，这些组件是实现路由逻辑的基础。在这些框架提供的执行环境中，开发者可以定义可能的操作路径以及用于指示计算图中节点之间转换的函数或基于模型的评估。


The implementation of routing enables a system to move beyond deterministic sequential processing. It facilitates the development of more adaptive execution flows that can respond dynamically and appropriately to a wider range of inputs and state changes.
路由的实现使系统能够超越确定性的顺序处理。它有助于开发更具自适应性的执行流程，从而能够动态且适当地响应更广泛的输入和状态变化。


## Practical Applications & Use Cases 实际应用和用例

The routing pattern is a critical control mechanism in the design of adaptive agentic systems, enabling them to dynamically alter their execution path in response to variable inputs and internal states. Its utility spans multiple domains by providing a necessary layer of conditional logic.
路由模式是自适应代理系统设计中的关键控制机制，使系统能够根据可变输入和内部状态动态地调整执行路径。它通过提供必要的条件逻辑层，跨越多个领域。


In human-computer interaction, such as with virtual assistants or AI-driven tutors, routing is employed to interpret user intent. An initial analysis of a natural language query determines the most appropriate subsequent action, whether it is invoking a specific information retrieval tool, escalating to a human operator, or selecting the next module in a curriculum based on user performance. This allows the system to move beyond linear dialogue flows and respond contextually.
在人机交互中，例如与虚拟助手或人工智能导师的互动，路由机制用于解读用户意图。对自然语言查询的初步分析将决定最合适的后续操作，无论是调用特定的信息检索工具、升级到人工客服，还是根据用户表现选择课程中的下一个模块。这使得系统能够超越线性对话流程，根据情境做出响应。


Within automated data and document processing pipelines, routing serves as a classification and distribution function. Incoming data, such as emails, support tickets, or API payloads, is analyzed based on content, metadata, or format. The system then directs each item to a corresponding workflow, such as a sales lead ingestion process, a specific data transformation function for JSON or CSV formats, or an urgent issue escalation path.
在自动化数据和文档处理流程中，路由功能起着分类和分发的作用。系统会根据内容、元数据或格式分析传入的数据，例如电子邮件、支持工单或 API 负载。然后，系统会将每项数据引导至相应的工作流，例如销售线索提取流程、针对 JSON 或 CSV 格式的特定数据转换功能，或紧急问题升级路径。


In complex systems involving multiple specialized tools or agents, routing acts as a high-level dispatcher. A research system composed of distinct agents for searching, summarizing, and analyzing information would use a router to assign tasks to the most suitable agent based on the current objective. Similarly, an AI coding assistant uses routing to identify the programming language and user's intent—to debug, explain, or translate—before passing a code snippet to the correct specialized tool.
在涉及多个专用工具或代理的复杂系统中，路由充当高级调度程序。一个由用于搜索、汇总和分析信息的不同代理组成的研究系统，会使用路由器根据当前目标将任务分配给最合适的代理。同样，人工智能编码助手会使用路由来识别编程语言和用户的意图（调试、解释或翻译），然后将代码片段传递给正确的专用工具。


Ultimately, routing provides the capacity for logical arbitration that is essential for creating functionally diverse and context-aware systems. It transforms an agent from a static executor of pre-defined sequences into a dynamic system that can make decisions about the most effective method for accomplishing a task under changing conditions.
最终，路由提供了逻辑仲裁的能力，这对于创建功能多样化且具有上下文感知能力的系统至关重要。它将代理从预定义序列的静态执行器转变为一个动态系统，能够在不断变化的条件下，做出关于完成任务的最有效方法的决策。


## Hands-On Code Example (LangChain) 实际代码示例（LangChain）

Implementing routing in code involves defining the possible paths and the logic that decides which path to take. Frameworks like LangChain and LangGraph provide specific components and structures for this. LangGraph's state-based graph structure is particularly intuitive for visualizing and implementing routing logic.
在代码中实现路由涉及定义可能的路径以及决定采用哪条路径的逻辑。LangChain 和 LangGraph 等框架为此提供了特定的组件和结构。LangGraph 基于状态的图结构对于路由逻辑的可视化和实现尤其直观。


This code demonstrates a simple agent-like system using LangChain and Google's Generative AI. It sets up a "coordinator" that routes user requests to different simulated "sub-agent" handlers based on the request's intent (booking, information, or unclear). The system uses a language model to classify the request and then delegates it to the appropriate handler function, simulating a basic delegation pattern often seen in multi-agent architectures.
此代码演示了一个使用 LangChain 和 Google 生成式人工智能 (Generative AI) 的简单类代理系统。它设置了一个“协调器”，根据请求的意图（预​​订、信息或不明确），将用户请求路由到不同的模拟“子代理”处理程序。系统使用语言模型对请求进行分类，然后将其委托给相应的处理程序函数，模拟了多代理架构中常见的基本委托模式。


First, ensure you have the necessary libraries installed:
首先，确保已安装必要的库：

```bash
pip install langchain langgraph google-cloud-aiplatform langchain-google-genai google-adk deprecated pydantic
```

You will also need to set up your environment with your API key for the language model you choose (e.g., OpenAI, Google Gemini, Anthropic).
您还需要使用 API 密钥为您选择的语言模型（例如，OpenAI、Google Gemini、Anthropic）设置环境。

```python
# Copyright (c) 2025 Marco Fago
#
# This code is licensed under the MIT License.
# See the LICENSE file in the repository for the full license text.

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableBranch

# --- Configuration ---
# Ensure your API key environment variable is set (e.g., GOOGLE_API_KEY)
try:
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    print(f"Language model initialized: {llm.model}")
except Exception as e:
    print(f"Error initializing language model: {e}")
    llm = None

# --- Define Simulated Sub-Agent Handlers (equivalent to ADK sub_agents) ---

def booking_handler(request: str) -> str:
    """Simulates the Booking Agent handling a request."""
    print("\n--- DELEGATING TO BOOKING HANDLER ---")
    return f"Booking Handler processed request: '{request}'. Result: Simulated booking action."

def info_handler(request: str) -> str:
    """Simulates the Info Agent handling a request."""
    print("\n--- DELEGATING TO INFO HANDLER ---")
    return f"Info Handler processed request: '{request}'. Result: Simulated information retrieval."

def unclear_handler(request: str) -> str:
    """Handles requests that couldn't be delegated."""
    print("\n--- HANDLING UNCLEAR REQUEST ---")
    return f"Coordinator could not delegate request: '{request}'. Please clarify."

# --- Define Coordinator Router Chain (equivalent to ADK coordinator's instruction) ---
# This chain decides which handler to delegate to.
coordinator_router_prompt = ChatPromptTemplate.from_messages([
    ("system", """Analyze the user's request and determine which specialist handler should process it.
     - If the request is related to booking flights or hotels, output 'booker'.
     - For all other general information questions, output 'info'.
     - If the request is unclear or doesn't fit either category, output 'unclear'.
     ONLY output one word: 'booker', 'info', or 'unclear'."""),
    ("user", "{request}")
])

if llm:
    coordinator_router_chain = coordinator_router_prompt | llm | StrOutputParser()

# --- Define the Delegation Logic (equivalent to ADK's Auto-Flow based on sub_agents) ---
# Use RunnableBranch to route based on the router chain's output.

# Define the branches for the RunnableBranch
branches = {
    "booker": RunnablePassthrough.assign(output=lambda x: booking_handler(x['request']['request'])),
    "info": RunnablePassthrough.assign(output=lambda x: info_handler(x['request']['request'])),
    "unclear": RunnablePassthrough.assign(output=lambda x: unclear_handler(x['request']['request'])),
}

# Create the RunnableBranch. It takes the output of the router chain
# and routes the original input ('request') to the corresponding handler.
delegation_branch = RunnableBranch(
    (lambda x: x['decision'].strip() == 'booker', branches["booker"]), # Added .strip()
    (lambda x: x['decision'].strip() == 'info', branches["info"]),     # Added .strip()
    branches["unclear"] # Default branch for 'unclear' or any other output
)

# Combine the router chain and the delegation branch into a single runnable
# The router chain's output ('decision') is passed along with the original input ('request')
# to the delegation_branch.
coordinator_agent = {
    "decision": coordinator_router_chain,
    "request": RunnablePassthrough()
} | delegation_branch | (lambda x: x['output']) # Extract the final output

# --- Example Usage ---
def main():
    if not llm:
        print("\nSkipping execution due to LLM initialization failure.")
        return

    print("--- Running with a booking request ---")
    request_a = "Book me a flight to London."
    result_a = coordinator_agent.invoke({"request": request_a})
    print(f"Final Result A: {result_a}")

    print("\n--- Running with an info request ---")
    request_b = "What is the capital of Italy?"
    result_b = coordinator_agent.invoke({"request": request_b})
    print(f"Final Result B: {result_b}")

    print("\n--- Running with an unclear request ---")
    request_c = "Tell me about quantum physics."
    result_c = coordinator_agent.invoke({"request": request_c})
    print(f"Final Result C: {result_c}")

if __name__ == "__main__":
    main()
```


As mentioned, this Python code constructs a simple agent-like system using the LangChain library and Google's Generative AI model, specifically gemini-2.5-flash. In detail, It defines three simulated sub-agent handlers: booking\_handler, info\_handler, and unclear\_handler, each designed to process specific types of requests.
如上所述，这段 Python 代码使用 LangChain 库和 Google 的生成式 AI 模型（具体来说是 gemini-2.5-flash）构建了一个简单的类代理系统。具体来说，它定义了三个模拟子代理处理程序：booking_handler、info_handler 和 unknown_handler，每个处理程序都用于处理特定类型的请求。

A core component is the coordinator\_router\_chain, which utilizes a ChatPromptTemplate to instruct the language model to categorize incoming user requests into one of three categories: 'booker', 'info', or 'unclear'. The output of this router chain is then used by a RunnableBranch to delegate the original request to the corresponding handler function. The RunnableBranch checks the decision from the language model and directs the request data to either the booking\_handler, info\_handler, or unclear\_handler. The coordinator\_agent combines these components, first routing the request for a decision and then passing the request to the chosen handler. The final output is extracted from the handler's response.
核心组件是 coordinator_router_chain，它利用 ChatPromptTemplate 指示语言模型将传入的用户请求分为以下三个类别之一：“booker”、“info”或“unclear”。然后，RunnableBranch 会使用此路由链的输出将原始请求委托给相应的处理函数。RunnableBranch 会检查语言模型的决策，并将请求数据定向到 booking_handler、info_handler 或 unknown_handler。coordinator_agent 会将这些组件组合起来，首先路由请求进行决策，然后将请求传递给所选的处理函数。最终输出从处理函数的响应中提取。

The main function demonstrates the system's usage with three example requests, showcasing how different inputs are routed and processed by the simulated agents. Error handling for language model initialization is included to ensure robustness. The code structure mimics a basic multi-agent framework where a central coordinator delegates tasks to specialized agents based on intent.
主函数通过三个示例请求演示了系统的使用方法，展示了模拟代理如何路由和处理不同的输入。为了确保系统的稳健性，还包含语言模型初始化的错误处理。代码结构模拟了一个基本的多代理框架，其中中央协调器根据意图将任务委托给专门的代理。

## Hands-On Code Example (Google ADK)
实际操作代码示例（Google ADK）

The Agent Development Kit (ADK) is a framework for engineering agentic systems, providing a structured environment for defining an agent's capabilities and behaviours. In contrast to architectures based on explicit computational graphs, routing within the ADK paradigm is typically implemented by defining a discrete set of "tools" that represent the agent's functions. The selection of the appropriate tool in response to a user query is managed by the framework's internal logic, which leverages an underlying model to match user intent to the correct functional handler.
代理开发套件 (ADK) 是一个用于设计代理系统的框架，它提供了一个结构化的环境来定义代理的功能和行为。与基于显式计算图的架构不同，ADK 范式中的路由通常通过定义一组代表代理功能的离散“工具”来实现。框架的内部逻辑负责管理如何根据用户查询选择合适的工具，该逻辑利用底层模型将用户意图与正确的功能处理程序进行匹配。

This Python code demonstrates an example of an Agent Development Kit (ADK) application using Google's ADK library. It sets up a "Coordinator" agent that routes user requests to specialized sub-agents ("Booker" for bookings and "Info" for general information) based on defined instructions. The sub-agents then use specific tools to simulate handling the requests, showcasing a basic delegation pattern within an agent system
这段 Python 代码演示了一个使用 Google ADK 库的代理开发套件 (ADK) 应用程序示例。它设置了一个“协调器”代理，该代理根据定义的指令将用户请求路由到专门的子代理（“Booker”用于预订，“Info”用于一般信息）。然后，子代理使用特定的工具来模拟处理请求，展示了代理系统中的基本委托模式。

```python
# Copyright (c) 2025 Marco Fago
#
# This code is licensed under the MIT License.
# See the LICENSE file in the repository for the full license text.

import uuid
from typing import Dict, Any, Optional

from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from google.adk.tools import FunctionTool
from google.genai import types
from google.adk.events import Event

# --- Define Tool Functions ---
# These functions simulate the actions of the specialist agents.

def booking_handler(request: str) -> str:
    """
    Handles booking requests for flights and hotels.
    Args:
        request: The user's request for a booking.
    Returns:
        A confirmation message that the booking was handled.
    """
    print("-------------------------- Booking Handler Called ----------------------------")
    return f"Booking action for '{request}' has been simulated."

def info_handler(request: str) -> str:
    """
    Handles general information requests.
    Args:
        request: The user's question.
    Returns:
        A message indicating the information request was handled.
    """
    print("-------------------------- Info Handler Called ----------------------------")
    return f"Information request for '{request}'. Result: Simulated information retrieval."

def unclear_handler(request: str) -> str:
    """Handles requests that couldn't be delegated."""
    return f"Coordinator could not delegate request: '{request}'. Please clarify."

# --- Create Tools from Functions ---
booking_tool = FunctionTool(booking_handler)
info_tool = FunctionTool(info_handler)

# Define specialized sub-agents equipped with their respective tools
booking_agent = Agent(
    name="Booker",
    model="gemini-2.0-flash",
    description="A specialized agent that handles all flight and hotel booking requests by calling the booking tool.",
    tools=[booking_tool]
)

info_agent = Agent(
    name="Info",
    model="gemini-2.0-flash",
    description="A specialized agent that provides general information and answers user questions by calling the info tool.",
    tools=[info_tool]
)

# Define the parent agent with explicit delegation instructions
coordinator = Agent(
    name="Coordinator",
    model="gemini-2.0-flash",
    instruction=(
        "You are the main coordinator. Your only task is to analyze incoming user requests "
        "and delegate them to the appropriate specialist agent. Do not try to answer the user directly.\n"
        "- For any requests related to booking flights or hotels, delegate to the 'Booker' agent.\n"
        "- For all other general information questions, delegate to the 'Info' agent."
    ),
    description="A coordinator that routes user requests to the correct specialist agent.",
    # The presence of sub_agents enables LLM-driven delegation (Auto-Flow) by default.
    sub_agents=[booking_agent, info_agent]
)

# --- Execution Logic ---

def run_coordinator(runner: InMemoryRunner, request: str):
    """Runs the coordinator agent with a given request and delegates."""
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
                if hasattr(event.content, 'text') and event.content.text:
                     final_result = event.content.text
                elif event.content.parts:
                    # Fallback: Iterate through parts and extract text (might trigger warning)
                    text_parts = [part.text for part in event.content.parts if part.text]
                    final_result = "".join(text_parts)
                # Assuming the loop should break after the final response
                break

        print(f"Coordinator Final Response: {final_result}")
        return final_result
    except Exception as e:
        print(f"An error occurred while processing your request: {e}")
        return f"An error occurred while processing your request: {e}"

def main():
    """Main function to run the ADK example."""
    print("--- Google ADK Routing Example (ADK Auto-Flow Style) ---")
    print("Note: This requires Google ADK installed and authenticated.")

    runner = InMemoryRunner(coordinator)
    # Example Usage
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
```

This script consists of a main Coordinator agent and two specialized sub\_agents: Booker and Info. Each specialized agent is equipped with a FunctionTool that wraps a Python function simulating an action. The booking\_handler function simulates handling flight and hotel bookings, while the info\_handler function simulates retrieving general information. The unclear\_handler is included as a fallback for requests the coordinator cannot delegate, although the current coordinator logic doesn't explicitly use it for delegation failure in the main run\_coordinator function.

The Coordinator agent's primary role, as defined in its instruction, is to analyze incoming user messages and delegate them to either the Booker or Info agent. This delegation is handled automatically by the ADK's Auto-Flow mechanism because the Coordinator has sub\_agents defined. The run\_coordinator function sets up an InMemoryRunner, creates a user and session ID, and then uses the runner to process the user's request through the coordinator agent. The runner.run method processes the request and yields events, and the code extracts the final response text from the event.content.

The main function demonstrates the system's usage by running the coordinator with different requests, showcasing how it delegates booking requests to the Booker and information requests to the Info agent.

## At a Glance

What: Agentic systems must often respond to a wide variety of inputs and situations that cannot be handled by a single, linear process. A simple sequential workflow lacks the ability to make decisions based on context. Without a mechanism to choose the correct tool or sub-process for a specific task, the system remains rigid and non-adaptive. This limitation makes it difficult to build sophisticated applications that can manage the complexity and variability of real-world user requests.

Why: The Routing pattern provides a standardized solution by introducing conditional logic into an agent's operational framework. It enables the system to first analyze an incoming query to determine its intent or nature. Based on this analysis, the agent dynamically directs the flow of control to the most appropriate specialized tool, function, or sub-agent. This decision can be driven by various methods, including prompting LLMs, applying predefined rules, or using embedding-based semantic similarity. Ultimately, routing transforms a static, predetermined execution path into a flexible and context-aware workflow capable of selecting the best possible action.

Rule of Thumb: Use the Routing pattern when an agent must decide between multiple distinct workflows, tools, or sub-agents based on the user's input or the current state. It is essential for applications that need to triage or classify incoming requests to handle different types of tasks, such as a customer support bot distinguishing between sales inquiries, technical support, and account management questions.

#### Visual Summary:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXebya1PTjQcs-iTMPdJhjw23bynnPvTURu21UyUKbvoTJsW-6Bs4N38CxMzQdipLbiFPYq4478QTJg2k0zc3sy01rDR8uc487SSffYqrUqyr4PCe_5uu35E553ztYN02A=s800?key=7vJcEhu1QiId0k62gPNSMw)

Fig.1: Router pattern, using an LLM as a Router

## Key Takeaways

## Conclusion

The Routing pattern is a critical step in building truly dynamic and responsive agentic systems. By implementing routing, we move beyond simple, linear execution flows and empower our agents to make intelligent decisions about how to process information, respond to user input, and utilize available tools or sub-agents.

We've seen how routing can be applied in various domains, from customer service chatbots to complex data processing pipelines. The ability to analyze input and conditionally direct the workflow is fundamental to creating agents that can handle the inherent variability of real-world tasks.

The code examples using LangChain and Google ADK demonstrate two different, yet effective, approaches to implementing routing. LangGraph's graph-based structure provides a visual and explicit way to define states and transitions, making it ideal for complex, multi-step workflows with intricate routing logic. Google ADK, on the other hand, often focuses on defining distinct capabilities (Tools) and relies on the framework's ability to route user requests to the appropriate tool handler, which can be simpler for agents with a well-defined set of discrete actions.

Mastering the Routing pattern is essential for building agents that can intelligently navigate different scenarios and provide tailored responses or actions based on context. It's a key component in creating versatile and robust agentic applications.

## References

1.  LangGraph Documentation: [https://www.langchain.com/](https://www.google.com/url?q=https://www.langchain.com/&sa=D&source=editors&ust=1760787973501914&usg=AOvVaw1r1m3zT6yBsSm2vLzcUBKz)  
2.  Google Agent Developer Kit Documentation: [https://google.github.io/adk-docs/](https://www.google.com/url?q=https://google.github.io/adk-docs/&sa=D&source=editors&ust=1760787973502294&usg=AOvVaw07KWXhRBQ8vB3WmMkw8olO)