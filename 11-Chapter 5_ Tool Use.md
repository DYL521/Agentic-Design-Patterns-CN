# Chapter 5: Tool Use (Function Calling)
# 第5章：工具使用（函数调用）

# Tool Use Pattern Overview
# 工具使用模式概述

So far, we've discussed agentic patterns that primarily involve orchestrating interactions between language models and managing the flow of information within the agent's internal workflow (Chaining, Routing, Parallelization, Reflection). However, for agents to be truly useful and interact with the real world or external systems, they need the ability to use Tools.
到目前为止，我们已经讨论了主要涉及编排语言模型之间交互和管理智能体内部工作流中信息流的智能体模式（链式、路由、并行化、反射）。然而，为了让智能体真正有用并与现实世界或外部系统交互，它们需要使用工具的能力。

The Tool Use pattern, often implemented through a mechanism called Function Calling, enables an agent to interact with external APIs, databases, services, or even execute code. It allows the LLM at the core of the agent to decide when and how to use a specific external function based on the user's request or the current state of the task.
工具使用模式通常通过一种称为函数调用的机制实现，使智能体能够与外部API、数据库、服务交互，甚至执行代码。它允许智能体核心的LLM根据用户的请求或任务的当前状态来决定何时以及如何使用特定的外部函数。

The process typically involves:
这个过程通常包括：

1. **Tool Definition:** External functions or capabilities are defined and described to the LLM. This description includes the function's purpose, its name, and the parameters it accepts, along with their types and descriptions.  
1. **工具定义：** 向LLM定义和描述外部函数或功能。这个描述包括函数的目的、名称以及它接受的参数，以及它们的类型和描述。

2. **LLM Decision:** The LLM receives the user's request and the available tool definitions. Based on its understanding of the request and the tools, the LLM decides if calling one or more tools is necessary to fulfill the request.  
2. **LLM决策：** LLM接收用户的请求和可用的工具定义。基于对请求和工具的理解，LLM决定是否需要调用一个或多个工具来满足请求。

3. **Function Call Generation:** If the LLM decides to use a tool, it generates a structured output (often a JSON object) that specifies the name of the tool to call and the arguments (parameters) to pass to it, extracted from the user's request.  
3. **函数调用生成：** 如果LLM决定使用工具，它会生成一个结构化输出（通常是JSON对象），指定要调用的工具名称和要传递给它的参数，这些参数从用户的请求中提取。

4. **Tool Execution:** The agentic framework or orchestration layer intercepts this structured output. It identifies the requested tool and executes the actual external function with the provided arguments.  
4. **工具执行：** 智能体框架或编排层拦截这个结构化输出。它识别请求的工具并使用提供的参数执行实际的外部函数。

5. **Observation/Result:** The output or result from the tool execution is returned to the agent.  
5. **观察/结果：** 工具执行的输出或结果返回给智能体。

6. **LLM Processing (Optional but common):** The LLM receives the tool's output as context and uses it to formulate a final response to the user or decide on the next step in the workflow (which might involve calling another tool, reflecting, or providing a final answer).
6. **LLM处理（可选但常见）：** LLM接收工具的输出作为上下文，并使用它来制定对用户的最终响应或决定工作流中的下一步（可能涉及调用另一个工具、反思或提供最终答案）。

This pattern is fundamental because it breaks the limitations of the LLM's training data and allows it to access up-to-date information, perform calculations it can't do internally, interact with user-specific data, or trigger real-world actions. Function calling is the technical mechanism that bridges the gap between the LLM's reasoning capabilities and the vast array of external functionalities available.
这种模式是基础性的，因为它打破了LLM训练数据的限制，允许它访问最新信息、执行内部无法完成的计算、与用户特定数据交互或触发现实世界的行动。函数调用是连接LLM推理能力和大量可用外部功能之间差距的技术机制。

While "function calling" aptly describes invoking specific, predefined code functions, it's useful to consider the more expansive concept of "tool calling." This broader term acknowledges that an agent's capabilities can extend far beyond simple function execution. A "tool" can be a traditional function, but it can also be a complex API endpoint, a request to a database, or even an instruction directed at another specialized agent. This perspective allows us to envision more sophisticated systems where, for instance, a primary agent might delegate a complex data analysis task to a dedicated "analyst agent" or query an external knowledge base through its API. Thinking in terms of "tool calling" better captures the full potential of agents to act as orchestrators across a diverse ecosystem of digital resources and other intelligent entities.
虽然"函数调用"恰当地描述了调用特定的、预定义的代码函数，但考虑更广泛的"工具调用"概念是有用的。这个更广泛的术语承认智能体的能力可以远远超出简单的函数执行。"工具"可以是传统函数，但也可以是复杂的API端点、对数据库的请求，甚至是针对另一个专门智能体的指令。这种观点允许我们设想更复杂的系统，例如，主要智能体可能将复杂的数据分析任务委托给专门的"分析师智能体"或通过其API查询外部知识库。从"工具调用"的角度思考更好地捕捉了智能体作为跨越多样化数字资源和其他智能实体生态系统的编排者的全部潜力。

Frameworks like LangChain, LangGraph, and Google Agent Developer Kit (ADK) provide robust support for defining tools and integrating them into agent workflows, often leveraging the native function calling capabilities of modern LLMs like those in the Gemini or OpenAI series. On the "canvas" of these frameworks, you define the tools and then configure agents (typically LLM Agents) to be aware of and capable of using these tools.
像LangChain、LangGraph和Google Agent Developer Kit (ADK)这样的框架为定义工具并将其集成到智能体工作流中提供了强大的支持，通常利用现代LLM（如Gemini或OpenAI系列）的原生函数调用能力。在这些框架的"画布"上，你定义工具，然后配置智能体（通常是LLM智能体）以了解并能够使用这些工具。

Tool Use is a cornerstone pattern for building powerful, interactive, and externally aware agents.
工具使用是构建强大的、交互式的、具有外部感知能力的智能体的基石模式。

# Practical Applications & Use Cases
# 实际应用和用例

The Tool Use pattern is applicable in virtually any scenario where an agent needs to go beyond generating text to perform an action or retrieve specific, dynamic information:
工具使用模式几乎适用于任何智能体需要超越生成文本来执行操作或检索特定、动态信息的场景：

1\. Information Retrieval from External Sources:  
1\. 从外部源检索信息：

Accessing real-time data or information that is not present in the LLM's training data.
访问LLM训练数据中不存在的实时数据或信息。

* **Use Case:** A weather agent.  
* **用例：** 天气智能体。

  * **Tool:** A weather API that takes a location and returns the current weather conditions.  
  * **工具：** 接收位置并返回当前天气状况的天气API。

  * **Agent Flow:** User asks, "What's the weather in London?", LLM identifies the need for the weather tool, calls the tool with "London", tool returns data, LLM formats the data into a user-friendly response.
  * **智能体流程：** 用户询问"伦敦的天气如何？"，LLM识别需要使用天气工具，使用"London"调用工具，工具返回数据，LLM将数据格式化为用户友好的响应。

2\. Interacting with Databases and APIs:  
2\. 与数据库和API交互：

Performing queries, updates, or other operations on structured data.
对结构化数据执行查询、更新或其他操作。

* **Use Case:** An e-commerce agent.  
* **用例：** 电子商务智能体。

  * **Tools:** API calls to check product inventory, get order status, or process payments.  
  * **工具：** 用于检查产品库存、获取订单状态或处理支付的API调用。

  * **Agent Flow:** User asks "Is product X in stock?", LLM calls the inventory API, tool returns stock count, LLM tells the user the stock status.
  * **智能体流程：：** 用户询问"产品X有库存吗？"，LLM调用库存API，工具返回库存数量，LLM告诉用户库存状态。

3\. Performing Calculations and Data Analysis:  
3\. 执行计算和数据分析：

Using external calculators, data analysis libraries, or statistical tools.
使用外部计算器、数据分析库或统计工具。

* **Use Case:** A financial agent.  
* **用例：** 金融智能体。

  * **Tools:** A calculator function, a stock market data API, a spreadsheet tool.  
  * **工具：** 计算器函数、股票市场数据API、电子表格工具。

  * **Agent Flow:** User asks "What's the current price of AAPL and calculate the potential profit if I bought 100 shares at $150?", LLM calls stock API, gets current price, then calls calculator tool, gets result, formats response.
  * **智能体流程：** 用户询问"AAPL的当前价格是多少，如果我以150美元买入100股的潜在利润是多少？"，LLM调用股票API，获取当前价格，然后调用计算器工具，获取结果，格式化响应。

# Hands-On Code Example (LangChain)
# 实践代码示例（LangChain）

The following example demonstrates how to create an agent that can use tools in LangChain. We'll create a research agent that can search the web and summarize information:
以下示例演示了如何在LangChain中创建一个可以使用工具的智能体。我们将创建一个可以搜索网络和总结信息的研究智能体：

```python
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent
from langchain.prompts import StringPromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI

# Initialize our search tool
search = DuckDuckGoSearchRun()

# Define the tools our agent can use
tools = [
    Tool(
        name="Web Search",
        func=search.run,
        description="Useful for searching the internet to find information on current events and topics."
    )
]

# Create a custom prompt template
class CustomPromptTemplate(StringPromptTemplate):
    template = """You are a research assistant. Use the following tools to find information and answer the user's question:

{tools}

Question: {input}
Let's approach this step by step:
1) First, determine if we need to search for information
2) If yes, use the search tool to find relevant information
3) Finally, provide a clear and concise answer

{agent_scratchpad}"""

    def format(self, **kwargs):
        # Get the intermediate steps (AgentAction, Observation tuples)
        intermediate_steps = kwargs.pop("intermediate_steps")
        
        # Format the list of tools
        tools_str = "
".join([f"{tool.name}: {tool.description}" for tool in kwargs["tools"]])
        
        # Format the agent scratchpad
        thoughts = ""
        for action, observation in intermediate_steps:
            thoughts += f"Action: {action.tool}
Action Input: {action.tool_input}
Observation: {observation}
"
        
        kwargs["agent_scratchpad"] = thoughts
        kwargs["tools"] = tools_str
        
        return self.template.format(**kwargs)

# Initialize the LLM
llm = ChatOpenAI(temperature=0)

# Create and run the agent
agent = LLMSingleActionAgent(
    llm_chain=llm,
    prompt=CustomPromptTemplate(tools=tools),
    tools=tools,
    verbose=True
)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    verbose=True
)

# Example usage
result = agent_executor.run("What are the latest developments in quantum computing?")
print(result)
```

This example showcases several key aspects of tool use:
这个示例展示了工具使用的几个关键方面：

1. **Tool Definition:** We define a web search tool using DuckDuckGo's search API.
1. **工具定义：** 我们使用DuckDuckGo的搜索API定义了一个网络搜索工具。

2. **Prompt Engineering:** The custom prompt template provides clear instructions to the agent about how to use the tools.
2. **提示工程：** 自定义提示模板为智能体提供了关于如何使用工具的清晰指令。

3. **Step-by-Step Reasoning:** The prompt encourages the agent to break down its approach into clear steps.
3. **逐步推理：** 提示鼓励智能体将其方法分解为清晰的步骤。

4. **Tool Integration:** The agent can seamlessly use the search tool as part of its reasoning process.
4. **工具集成：** 智能体可以将搜索工具无缝地集成到其推理过程中。

# Hands-On Code Example (CrewAI)
# 实践代码示例（CrewAI）

The following example demonstrates how to create a research agent using CrewAI that can use multiple tools to gather and analyze information:
以下示例演示了如何使用CrewAI创建一个可以使用多个工具来收集和分析信息的研究智能体：

```python
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools.file_management import ReadFileTool, WriteFileTool

# Initialize tools
search_tool = DuckDuckGoSearchRun()
read_tool = ReadFileTool()
write_tool = WriteFileTool()

# Create specialized agents
researcher = Agent(
    role='Research Analyst',
    goal='Find and analyze information about specific topics',
    backstory='You are an expert research analyst with years of experience in gathering and analyzing information.',
    tools=[search_tool],
    verbose=True
)

writer = Agent(
    role='Technical Writer',
    goal='Write clear and comprehensive reports based on research findings',
    backstory='You are a skilled technical writer who can transform complex information into clear, readable content.',
    tools=[read_tool, write_tool],
    verbose=True
)

# Define tasks
research_task = Task(
    description='Research the latest advancements in artificial intelligence and their potential impact on society.',
    agent=researcher
)

writing_task = Task(
    description='Write a comprehensive report based on the research findings. The report should be clear, well-structured, and accessible to a general audience.',
    agent=writer
)

# Create and run the crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    verbose=2
)

result = crew.kickoff()
```

This example demonstrates several advanced aspects of tool use:
这个示例展示了工具使用的几个高级方面：

1. **Multiple Agents with Different Tools:** Each agent has access to specific tools that match their role and expertise.
1. **具有不同工具的多个智能体：** 每个智能体都可以访问与其角色和专业知识相匹配的特定工具。

2. **Task Coordination:** The crew orchestrates the sequential execution of tasks, with the writer using the researcher's output.
2. **任务协调：** 团队编排任务的顺序执行，写作者使用研究者的输出。

3. **Specialized Tool Sets:** The researcher uses search tools while the writer uses file management tools.
3. **专门的工具集：** 研究者使用搜索工具，而写作者使用文件管理工具。

4. **Process Control:** The sequential process ensures that research is completed before writing begins.
4. **过程控制：** 顺序过程确保在写作开始之前完成研究。

# Hands-on code (Google ADK)
# 实践代码（Google ADK）

The Google Agent Developer Kit (ADK) includes a library of natively integrated tools that can be directly incorporated into an agent's capabilities. Here's an example demonstrating tool use with Google ADK:
Google Agent Developer Kit (ADK)包含一个原生集成的工具库，可以直接集成到智能体的功能中。以下是一个演示使用Google ADK进行工具使用的示例：

```python
from google.adk import Agent, Tool
from google.adk.tools import web_search, calculator
from typing import AsyncGenerator

# Define a custom tool
class WeatherTool(Tool):
    """A tool for getting weather information."""
    name = "weather"
    description = "Gets current weather information for a location"
    
    async def _run_impl(self, location: str) -> AsyncGenerator[str, None]:
        # In a real implementation, this would call a weather API
        yield f"Getting weather for {location}..."
        yield "Sunny, 22°C"

# Create an agent with multiple tools
agent = Agent(
    name="MultiTool Agent",
    description="An agent that can use multiple tools to help users",
    tools=[
        web_search.WebSearchTool(),  # Built-in Google search tool
        calculator.CalculatorTool(),  # Built-in calculator tool
        WeatherTool()                # Our custom weather tool
    ],
    model="gemini-2.0-flash",
    instruction="""You are a helpful assistant that can search the web, perform calculations, 
                  and check the weather. Use the appropriate tool based on the user's request."""
)

# Example usage
async def main():
    # The agent will automatically choose and use the appropriate tool
    # based on the user's request
    response = await agent.run("What's the weather in London and what's 15% of 200?")
    print(response)

# Run the agent
import asyncio
asyncio.run(main())
```

This example demonstrates several key features of tool use in Google ADK:
这个示例展示了Google ADK中工具使用的几个关键特性：

1. **Built-in Tools:** ADK provides a set of pre-built tools like web search and calculator.
1. **内置工具：** ADK提供了一组预构建的工具，如网络搜索和计算器。

2. **Custom Tool Creation:** You can create custom tools by extending the Tool base class.
2. **自定义工具创建：** 你可以通过扩展Tool基类来创建自定义工具。

3. **Tool Integration:** Tools are seamlessly integrated into the agent's capabilities.
3. **工具集成：** 工具被无缝集成到智能体的功能中。

4. **Automatic Tool Selection:** The agent automatically selects the appropriate tool based on the user's request.
4. **自动工具选择：** 智能体根据用户的请求自动选择适当的工具。

# At a Glance
# 概览

**What:** The Tool Use pattern enables agents to interact with external systems and perform actions beyond text generation. Through function calling, agents can use APIs, databases, and other tools to access real-time information, perform calculations, and execute real-world actions.
**是什么：** 工具使用模式使智能体能够与外部系统交互并执行超出文本生成的操作。通过函数调用，智能体可以使用API、数据库和其他工具来访问实时信息、执行计算和执行现实世界的操作。

**Why:** Pure language models are limited by their training data and lack real-time information or the ability to perform specific actions. Tool use overcomes these limitations by allowing agents to access external capabilities and current information.
**为什么：** 纯语言模型受其训练数据的限制，缺乏实时信息或执行特定操作的能力。工具使用通过允许智能体访问外部功能和当前信息来克服这些限制。

**Rule of thumb:** Use this pattern when your agent needs to:
**经验法则：** 在以下情况下使用此模式：

1. Access real-time or external information
1. 访问实时或外部信息

2. Perform specific actions or calculations
2. 执行特定操作或计算

3. Interact with external systems or APIs
3. 与外部系统或API交互

4. Execute real-world operations
4. 执行现实世界的操作

# Key Takeaways
# 关键要点

* Tool use is essential for building agents that can interact with the real world and external systems.
* 工具使用对于构建能够与现实世界和外部系统交互的智能体至关重要。

* Function calling provides a structured way for agents to use external tools and capabilities.
* 函数调用为智能体使用外部工具和功能提供了一种结构化的方式。

* Modern frameworks like LangChain, CrewAI, and Google ADK provide robust support for tool integration.
* 现代框架如LangChain、CrewAI和Google ADK为工具集成提供了强大的支持。

* Tools can range from simple functions to complex APIs and even other specialized agents.
* 工具可以从简单的函数到复杂的API，甚至是其他专门的智能体。

# Conclusion
# 结论

The Tool Use pattern is fundamental to building practical, real-world AI agents. By enabling agents to interact with external systems and perform concrete actions, this pattern bridges the gap between language understanding and real-world capabilities. As we continue to develop more sophisticated tools and integration methods, the potential applications of tool-enabled agents will only grow.
工具使用模式是构建实用的、现实世界AI智能体的基础。通过使智能体能够与外部系统交互并执行具体操作，这种模式弥合了语言理解和现实世界能力之间的差距。随着我们继续开发更复杂的工具和集成方法，具有工具使用能力的智能体的潜在应用只会增加。

# References
# 参考文献

1. LangChain Documentation: [https://python.langchain.com/docs/modules/agents/tools](https://python.langchain.com/docs/modules/agents/tools)
2. CrewAI GitHub Repository: [https://github.com/joaomdmoura/crewAI](https://github.com/joaomdmoura/crewAI)
3. Google ADK Documentation: [https://google.github.io/adk-docs/](https://google.github.io/adk-docs/)