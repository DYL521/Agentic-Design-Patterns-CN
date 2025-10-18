# Appendix C \- Quick overview of Agentic Frameworks
# 附录 C - 智能体框架快速概览

# LangChain 

LangChain is a framework for developing applications powered by LLMs. Its core strength lies in its LangChain Expression Language (LCEL), which allows you to "pipe" components together into a chain. This creates a clear, linear sequence where the output of one step becomes the input for the next. It's built for workflows that are Directed Acyclic Graphs (DAGs), meaning the process flows in one direction without loops.
LangChain 是一个用于开发由大语言模型（LLM）驱动的应用程序的框架。其核心优势在于 LangChain 表达式语言（LCEL），它允许你将组件"管道"连接成一个链。这创建了一个清晰的线性序列，其中一个步骤的输出成为下一个步骤的输入。它是为有向无环图（DAG）工作流构建的，意味着流程单向流动，没有循环。

Use it for:
适用场景：

* Simple RAG: Retrieve a document, create a prompt, get an answer from an LLM.  
* 简单的检索增强生成（RAG）：检索文档，创建提示词，从大语言模型获取答案。
* Summarization: Take user text, feed it to a summarization prompt, and return the output.  
* 摘要生成：获取用户文本，将其输入摘要提示词，并返回输出。
* Extraction: Extract structured data (like JSON) from a block of text.
* 提取：从文本块中提取结构化数据（如 JSON）。

Python

|| `# A simple LCEL chain conceptually # (This is not runnable code, just illustrates the flow) chain = prompt | model | output_parse` |
|| :---- |

### LangGraph 

LangGraph is a library built on top of LangChain to handle more advanced agentic systems. It allows you to define your workflow as a graph with nodes (functions or LCEL chains) and edges (conditional logic). Its main advantage is the ability to create cycles, allowing the application to loop, retry, or call tools in a flexible order until a task is complete. It explicitly manages the application state, which is passed between nodes and updated throughout the process.
LangGraph 是建立在 LangChain 之上的库，用于处理更高级的智能体系统。它允许你将工作流定义为具有节点（函数或 LCEL 链）和边（条件逻辑）的图。其主要优势是能够创建循环，允许应用程序循环、重试或以灵活的顺序调用工具，直到任务完成。它显式地管理应用程序状态，该状态在节点之间传递并在整个过程中更新。

Use it for:
适用场景：

* Multi-agent Systems: A supervisor agent routes tasks to specialized worker agents, potentially looping until the goal is met.  
* 多智能体系统：监督智能体将任务路由到专门的工作智能体，可能会循环直到达成目标。
* Plan-and-Execute Agents: An agent creates a plan, executes a step, and then loops back to update the plan based on the result.  
* 计划-执行智能体：智能体创建计划，执行一个步骤，然后根据结果循环回来更新计划。
* Human-in-the-Loop: The graph can wait for human input before deciding which node to go to next.
* 人机交互：图可以在决定下一个节点之前等待人类输入。

|| Feature | LangChain | LangGraph |
|| :---- | :---- | :---- |
|| Core Abstraction | Chain (using LCEL) | Graph of Nodes |
|| 核心抽象 | 链（使用 LCEL） | 节点图 |
|| Workflow Type | Linear (Directed Acyclic Graph) | Cyclical (Graphs with loops) |
|| 工作流类型 | 线性（有向无环图） | 循环（带循环的图） |
|| State Management | Generally stateless per run | Explicit and persistent state object |
|| 状态管理 | 通常每次运行都是无状态的 | 显式和持久的状态对象 |
|| Primary Use | Simple, predictable sequences | Complex, dynamic, stateful agents |
|| 主要用途 | 简单、可预测的序列 | 复杂、动态、有状态的智能体 |

### Which One Should You Use?
### 你应该选择哪一个？

* Choose LangChain when your application has a clear, predictable, and linear flow of steps. If you can define the process from A to B to C without needing to loop back, LangChain with LCEL is the perfect tool.  
* 当你的应用程序有清晰、可预测和线性的步骤流程时，选择 LangChain。如果你可以从 A 到 B 到 C 定义流程而不需要回溯，那么使用 LCEL 的 LangChain 是完美的工具。
* Choose LangGraph when you need your application to reason, plan, or operate in a loop. If your agent needs to use tools, reflect on the results, and potentially try again with a different approach, you need the cyclical and stateful nature of LangGraph.
* 当你需要应用程序进行推理、规划或在循环中运行时，选择 LangGraph。如果你的智能体需要使用工具、反思结果，并可能尝试不同的方法，那么你需要 LangGraph 的循环和有状态特性。

Python

|| `# Graph state class State(TypedDict):    topic: str    joke: str    story: str    poem: str    combined_output: str # Nodes def call_llm_1(state: State):    """First LLM call to generate initial joke"""    msg = llm.invoke(f"Write a joke about {state['topic']}")    return {"joke": msg.content} def call_llm_2(state: State):    """Second LLM call to generate story"""    msg = llm.invoke(f"Write a story about {state['topic']}")    return {"story": msg.content} def call_llm_3(state: State):    """Third LLM call to generate poem"""    msg = llm.invoke(f"Write a poem about {state['topic']}")    return {"poem": msg.content} def aggregator(state: State):    """Combine the joke and story into a single output"""    combined = f"Here's a story, joke, and poem about {state['topic']}!\n\n"    combined += f"STORY:\n{state['story']}\n\n"    combined += f"JOKE:\n{state['joke']}\n\n"    combined += f"POEM:\n{state['poem']}"    return {"combined_output": combined} # Build workflow parallel_builder = StateGraph(State) # Add nodes parallel_builder.add_node("call_llm_1", call_llm_1) parallel_builder.add_node("call_llm_2", call_llm_2) parallel_builder.add_node("call_llm_3", call_llm_3) parallel_builder.add_node("aggregator", aggregator) # Add edges to connect nodes parallel_builder.add_edge(START, "call_llm_1") parallel_builder.add_edge(START, "call_llm_2") parallel_builder.add_edge(START, "call_llm_3") parallel_builder.add_edge("call_llm_1", "aggregator") parallel_builder.add_edge("call_llm_2", "aggregator") parallel_builder.add_edge("call_llm_3", "aggregator") parallel_builder.add_edge("aggregator", END) parallel_workflow = parallel_builder.compile() # Show workflow display(Image(parallel_workflow.get_graph().draw_mermaid_png())) # Invoke state = parallel_workflow.invoke({"topic": "cats"}) print(state["combined_output"])` |
|| :---- |

This code defines and runs a LangGraph workflow that operates in parallel. Its main purpose is to simultaneously generate a joke, a story, and a poem about a given topic and then combine them into a single, formatted text output.
这段代码定义并运行了一个并行操作的 LangGraph 工作流。其主要目的是同时生成关于给定主题的笑话、故事和诗歌，然后将它们组合成一个格式化的文本输出。

# Google's ADK

Google's Agent Development Kit, or ADK, provides a high-level, structured framework for building and deploying applications composed of multiple, interacting AI agents. It contrasts with LangChain and LangGraph by offering a more opinionated and production-oriented system for orchestrating agent collaboration, rather than providing the fundamental building blocks for an agent's internal logic.
Google 的智能体开发工具包（ADK）提供了一个高级、结构化的框架，用于构建和部署由多个交互式 AI 智能体组成的应用程序。它与 LangChain 和 LangGraph 的不同之处在于，它提供了一个更加固执己见和面向生产的系统来编排智能体协作，而不是提供智能体内部逻辑的基本构建块。

LangChain operates at the most foundational level, offering the components and standardized interfaces to create sequences of operations, such as calling a model and parsing its output. LangGraph extends this by introducing a more flexible and powerful control flow; it treats an agent's workflow as a stateful graph. Using LangGraph, a developer explicitly defines nodes, which are functions or tools, and edges, which dictate the path of execution. This graph structure allows for complex, cyclical reasoning where the system can loop, retry tasks, and make decisions based on an explicitly managed state object that is passed between nodes. It gives the developer fine-grained control over a single agent's thought process or the ability to construct a multi-agent system from first principles.
LangChain 在最基础的层面上运作，提供组件和标准化接口来创建操作序列，如调用模型和解析其输出。LangGraph 通过引入更灵活和强大的控制流来扩展这一点；它将智能体的工作流视为有状态图。使用 LangGraph，开发者明确定义节点（作为函数或工具）和边（决定执行路径）。这种图结构允许复杂的循环推理，系统可以循环、重试任务，并基于在节点之间传递的显式管理的状态对象做出决策。它为开发者提供了对单个智能体思考过程的细粒度控制，或从头构建多智能体系统的能力。

Google's ADK abstracts away much of this low-level graph construction. Instead of asking the developer to define every node and edge, it provides pre-built architectural patterns for multi-agent interaction. For instance, ADK has built-in agent types like SequentialAgent or ParallelAgent, which manage the flow of control between different agents automatically. It is architected around the concept of a "team" of agents, often with a primary agent delegating tasks to specialized sub-agents. State and session management are handled more implicitly by the framework, providing a more cohesive but less granular approach than LangGraph's explicit state passing. Therefore, while LangGraph gives you the detailed tools to design the intricate wiring of a single robot or a team, Google's ADK gives you a factory assembly line designed to build and manage a fleet of robots that already know how to work together.
Google 的 ADK 抽象掉了大部分低级图构建工作。它不要求开发者定义每个节点和边，而是提供了多智能体交互的预构建架构模式。例如，ADK 有内置的智能体类型，如 SequentialAgent 或 ParallelAgent，它们自动管理不同智能体之间的控制流。它围绕"智能体团队"的概念进行架构设计，通常有一个主要智能体将任务委派给专门的子智能体。状态和会话管理由框架更隐式地处理，提供了比 LangGraph 显式状态传递更加内聚但粒度更低的方法。因此，虽然 LangGraph 为你提供了设计单个机器人或团队复杂布线的详细工具，但 Google 的 ADK 为你提供了一个工厂装配线，旨在构建和管理已经知道如何协同工作的机器人舰队。

Python

|| `from google.adk.agents import LlmAgent from google.adk.tools import google_Search dice_agent = LlmAgent(    model="gemini-2.0-flash-exp",     name="question_answer_agent",    description="A helpful assistant agent that can answer questions.",    instruction="""Respond to the query using google search""",    tools=[google_search], )` |
|| :---- |

This code creates a search-augmented agent. When this agent receives a question, it will not just rely on its pre-existing knowledge. Instead, following its instructions, it will use the Google Search tool to find relevant, real-time information from the web and then use that information to construct its answer.
这段代码创建了一个搜索增强的智能体。当这个智能体收到问题时，它不仅仅依赖于其预先存在的知识。相反，按照其指令，它将使用 Google 搜索工具从网络上查找相关的实时信息，然后使用这些信息构建答案。

Crew.AI
Crew.AI

CrewAI offers an orchestration framework for building multi-agent systems by focusing on collaborative roles and structured processes. It operates at a higher level of abstraction than foundational toolkits, providing a conceptual model that mirrors a human team. Instead of defining the granular flow of logic as a graph, the developer defines the actors and their assignments, and CrewAI manages their interaction.
CrewAI 通过关注协作角色和结构化流程，提供了一个用于构建多智能体系统的编排框架。它在比基础工具包更高的抽象层次上运作，提供了一个镜像人类团队的概念模型。开发者不是将逻辑流定义为图，而是定义执行者及其任务，CrewAI 管理它们的交互。

The core components of this framework are Agents, Tasks, and the Crew. An Agent is defined not just by its function but by a persona, including a specific role, a goal, and a backstory, which guides its behavior and communication style. A Task is a discrete unit of work with a clear description and expected output, assigned to a specific Agent. The Crew is the cohesive unit that contains the Agents and the list of Tasks, and it executes a predefined Process. This process dictates the workflow, which is typically either sequential, where the output of one task becomes the input for the next in line, or hierarchical, where a manager-like agent delegates tasks and coordinates the workflow among other agents.
该框架的核心组件是智能体（Agents）、任务（Tasks）和团队（Crew）。智能体不仅由其功能定义，还由一个角色定义，包括特定的角色、目标和背景故事，这些指导其行为和沟通风格。任务是具有明确描述和预期输出的离散工作单元，分配给特定智能体。团队是包含智能体和任务列表的内聚单元，它执行预定义的流程。这个流程决定了工作流，通常是顺序的（一个任务的输出成为下一个任务的输入）或层级的（类似管理者的智能体委派任务并在其他智能体之间协调工作流）。

When compared to other frameworks, CrewAI occupies a distinct position. It moves away from the low-level, explicit state management and control flow of LangGraph, where a developer wires together every node and conditional edge. Instead of building a state machine, the developer designs a team charter. While Googlés ADK provides a comprehensive, production-oriented platform for the entire agent lifecycle, CrewAI concentrates specifically on the logic of agent collaboration and for simulating a team of specialists
与其他框架相比，CrewAI 占据了一个独特的位置。它远离了 LangGraph 的低级、显式状态管理和控制流，在那里开发者将每个节点和条件边连接在一起。与构建状态机不同，开发者设计了一个团队章程。虽然 Google 的 ADK 为整个智能体生命周期提供了全面的、面向生产的平台，但 CrewAI 专注于智能体协作的逻辑，并模拟专家团队。

Python

|| `@crew def crew(self) -> Crew:    """Creates the research crew"""    return Crew(      agents=self.agents,      tasks=self.tasks,      process=Process.sequential,      verbose=True,    )` |
|| :---- |

This code sets up a sequential workflow for a team of AI agents, where they tackle a list of tasks in a specific order, with detailed logging enabled to monitor their progress.
这段代码为一个 AI 智能体团队设置了顺序工作流，它们按特定顺序处理任务列表，并启用详细日志记录以监控其进度。

Other agent development framework
其他智能体开发框架

**Microsoft AutoGen**: AutoGen is a framework centered on orchestrating multiple agents that solve tasks through conversation. Its architecture enables agents with distinct capabilities to interact, allowing for complex problem decomposition and collaborative resolution. The primary advantage of AutoGen is its flexible, conversation-driven approach that supports dynamic and complex multi-agent interactions. However, this conversational paradigm can lead to less predictable execution paths and may require sophisticated prompt engineering to ensure tasks converge efficiently.
**Microsoft AutoGen**：AutoGen 是一个以通过对话编排多个智能体解决任务为中心的框架。其架构使具有不同能力的智能体能够交互，从而允许复杂问题的分解和协作解决。AutoGen 的主要优势是其灵活的、对话驱动的方法，支持动态和复杂的多智能体交互。然而，这种对话范式可能导致不太可预测的执行路径，并可能需要复杂的提示词工程以确保任务有效收敛。

**LlamaIndex**: LlamaIndex is fundamentally a data framework designed to connect large language models with external and private data sources. It excels at creating sophisticated data ingestion and retrieval pipelines, which are essential for building knowledgeable agents that can perform RAG. While its data indexing and querying capabilities are exceptionally powerful for creating context-aware agents, its native tools for complex agentic control flow and multi-agent orchestration are less developed compared to agent-first frameworks. LlamaIndex is optimal when the core technical challenge is data retrieval and synthesis.
**LlamaIndex**：LlamaIndex 本质上是一个数据框架，旨在将大型语言模型与外部和私有数据源连接。它擅长创建复杂的数据摄入和检索管道，这对于构建能执行检索增强生成（RAG）的知识型智能体至关重要。虽然其数据索引和查询能力对于创建上下文感知的智能体极其强大，但与面向智能体的框架相比，其用于复杂智能体控制流和多智能体编排的原生工具发展较少。当核心技术挑战是数据检索和综合时，LlamaIndex 是最佳选择。

**Haystac**k: Haystack is an open-source framework engineered for building scalable and production-ready search systems powered by language models. Its architecture is composed of modular, interoperable nodes that form pipelines for document retrieval, question answering, and summarization. The main strength of Haystack is its focus on performance and scalability for large-scale information retrieval tasks, making it suitable for enterprise-grade applications. A potential trade-off is that its design, optimized for search pipelines, can be more rigid for implementing highly dynamic and creative agentic behaviors.
**Haystack**：Haystack 是一个开源框架，专为构建由语言模型驱动的可扩展和生产就绪的搜索系统而设计。其架构由模块化、可互操作的节点组成，形成文档检索、问答和摘要的管道。Haystack 的主要优势在于其对大规模信息检索任务的性能和可扩展性的关注，使其适合企业级应用。潜在的权衡是，其为搜索管道优化的设计可能对实现高度动态和创造性的智能体行为更加僵化。

**MetaGPT**: MetaGPT implements a multi-agent system by assigning roles and tasks based on a predefined set of Standard Operating Procedures (SOPs). This framework structures agent collaboration to mimic a software development company, with agents taking on roles like product managers or engineers to complete complex tasks. This SOP-driven approach results in highly structured and coherent outputs, which is a significant advantage for specialized domains like code generation. The framework's primary limitation is its high degree of specialization, making it less adaptable for general-purpose agentic tasks outside of its core design.
**MetaGPT**：MetaGPT 通过基于预定义的标准操作程序（SOPs）分配角色和任务来实现多智能体系统。该框架构建智能体协作以模仿软件开发公司，智能体扮演产品经理或工程师等角色来完成复杂任务。这种基于 SOP 的方法产生高度结构化和一致的输出，这对于代码生成等专业领域是显著优势。该框架的主要局限性在于其高度专业化，使其在其核心设计之外的通用智能体任务中适应性较差。

**SuperAGI**: SuperAGI is an open-source framework designed to provide a complete lifecycle management system for autonomous agents. It includes features for agent provisioning, monitoring, and a graphical interface, aiming to enhance the reliability of agent execution. The key benefit is its focus on production-readiness, with built-in mechanisms to handle common failure modes like looping and to provide observability into agent performance. A potential drawback is that its comprehensive platform approach can introduce more complexity and overhead than a more lightweight, library-based framework.
**SuperAGI**：SuperAGI 是一个开源框架，旨在为自主智能体提供完整的生命周期管理系统。它包括智能体配置、监控和图形界面等功能，旨在提高智能体执行的可靠性。其关键优势在于专注于生产就绪性，具有内置机制来处理循环等常见故障模式，并提供对智能体性能的可观察性。潜在的缺点是，其全面的平台方法可能比更轻量级的基于库的框架引入更多复杂性和开销。

**Semantic Kernel**: Developed by Microsoft, Semantic Kernel is an SDK that integrates large language models with conventional programming code through a system of "plugins" and "planners." It allows an LLM to invoke native functions and orchestrate workflows, effectively treating the model as a reasoning engine within a larger software application. Its primary strength is its seamless integration with existing enterprise codebases, particularly in .NET and Python environments. The conceptual overhead of its plugin and planner architecture can present a steeper learning curve compared to more straightforward agent frameworks.
**Semantic Kernel**：由微软开发，Semantic Kernel 是一个通过"插件"和"规划器"系统将大型语言模型与传统编程代码集成的 SDK。它允许大语言模型调用原生函数并编排工作流，有效地将模型视为更大软件应用程序中的推理引擎。其主要优势在于与现有企业代码库的无缝集成，特别是在 .NET 和 Python 环境中。其插件和规划器架构的概念开销可能比更直接的智能体框架呈现更陡峭的学习曲线。

**Strands Agents:** An AWS lightweight and flexible SDK that uses a model-driven approach for building and running AI agents. It is designed to be simple and scalable, supporting everything from basic conversational assistants to complex multi-agent autonomous systems. The framework is model-agnostic, offering broad support for various LLM providers, and includes native integration with the MCP for easy access to external tools. Its core advantage is its simplicity and flexibility, with a customizable agent loop that is easy to get started with. A potential trade-off is that its lightweight design means developers may need to build out more of the surrounding operational infrastructure, such as advanced monitoring or lifecycle management systems, which more comprehensive frameworks might provide out-of-the-box.
**Strands Agents**：AWS 的一个轻量级且灵活的 SDK，使用模型驱动的方法构建和运行 AI 智能体。它被设计为简单和可扩展的，支持从基本对话助手到复杂的多智能体自主系统。该框架是模型不可知的，为各种大语言模型提供广泛支持，并包括与 MCP 的原生集成，以便轻松访问外部工具。其核心优势在于其简单性和灵活性，具有易于入门的可定制智能体循环。潜在的权衡是，其轻量级设计意味着开发者可能需要构建更多周边操作基础设施，如高级监控或生命周期管理系统，而更全面的框架可能开箱即用。

Conclusion
结论

The landscape of agentic frameworks offers a diverse spectrum of tools, from low-level libraries for defining agent logic to high-level platforms for orchestrating multi-agent collaboration. At the foundational level, LangChain enables simple, linear workflows, while LangGraph introduces stateful, cyclical graphs for more complex reasoning. Higher-level frameworks like CrewAI and Google's ADK shift the focus to orchestrating teams of agents with predefined roles, while others like LlamaIndex specialize in data-intensive applications. This variety presents developers with a core trade-off between the granular control of graph-based systems and the streamlined development of more opinionated platforms. Consequently, selecting the right framework hinges on whether the application requires a simple sequence, a dynamic reasoning loop, or a managed team of specialists. Ultimately, this evolving ecosystem empowers developers to build increasingly sophisticated AI systems by choosing the precise level of abstraction their project demands.
智能体框架的景观提供了从定义智能体逻辑的低级库到编排多智能体协作的高级平台的多样工具。在基础层面，LangChain 支持简单的线性工作流，而 LangGraph 引入了有状态、循环的图以实现更复杂的推理。像 CrewAI 和 Google 的 ADK 这样的高级框架将重点转移到使用预定义角色编排智能体团队，而像 LlamaIndex 这样的框架专注于数据密集型应用。这种多样性为开发者提供了图形系统的细粒度控制与更固执己见平台的简化开发之间的核心权衡。因此，选择正确的框架取决于应用程序是需要简单序列、动态推理循环还是受管理的专家团队。最终，这个不断发展的生态系统通过让开发者选择项目所需的精确抽象层次，使他们能够构建越来越复杂的人工智能系统。

References
参考文献

1. LangChain, [https://www.langchain.com/](https://www.langchain.com/)   
2. LangGraph, [https://www.langchain.com/langgraph](https://www.langchain.com/langgraph)   
3. Google's ADK, [https://google.github.io/adk-docs/](https://google.github.io/adk-docs/)   
4. Crew.AI, [https://docs.crewai.com/en/introduction](https://docs.crewai.com/en/introduction) 

