- 原文链接：https://docs.google.com/document/d/1K5jwqB6jh20uHL0TTWxqWOxFk-dzFxRvHzrRRV79hrg/edit?tab=t.0#heading=h.jyvbxtbusz8t

# Preface  前言
Welcome to "Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems." As we look across the landscape of modern artificial intelligence, we see a clear evolution from simple, reactive programs to sophisticated, autonomous entities capable of understanding context, making decisions, and interacting dynamically with their environment and other systems. These are the intelligent agents and the agentic systems they comprise.
欢迎阅读《代理设计模式：构建智能系统实用指南》。纵观现代人工智能的发展历程，我们可以看到它从简单的反应式程序，进化为能够理解上下文、做出决策并与环境和其他系统动态交互的复杂自主实体。这些就是智能代理及其组成的代理系统。

The advent of powerful large language models (LLMs) has provided unprecedented capabilities for understanding and generating human-like content such as text and media, serving as the cognitive engine for many of these agents. However, orchestrating these capabilities into systems that can reliably achieve complex goals requires more than just a powerful model. It requires structure, design, and a thoughtful approach to how the agent perceives, plans, acts, and interacts.
强大的大型语言模型 (LLM) 的出现，为理解和生成类似人类的内容（例如文本和媒体）提供了前所未有的能力，并成为许多智能体的认知引擎。然而，要将这些能力编排到能够可靠地实现复杂目标的系统中，仅仅拥有一个强大的模型是不够的。它需要结构、设计，以及对智能体如何感知、计划、行动和交互的深思熟虑的方法。

Think of building intelligent systems as creating a complex work of art or engineering on a canvas. This canvas isn't a blank visual space, but rather the underlying infrastructure and frameworks that provide the environment and tools for your agents to exist and operate. It's the foundation upon which you'll build your intelligent application, managing state, communication, tool access, and the flow of logic.
构建智能系统就像在画布上创作一件复杂的艺术品或工程作品。这块画布并非一片空白的视觉空间，而是为代理提供生存和运行环境和工具的底层基础架构和框架。它是您构建智能应用、管理状态、通信、工具访问和逻辑流程的基础。

Building effectively on this agentic canvas demands more than just throwing components together. It requires understanding proven techniques – patterns – that address common challenges in designing and implementing agent behavior. Just as architectural patterns guide the construction of a building, or design patterns structure software, agentic design patterns provide reusable solutions for the recurring problems you'll face when bringing intelligent agents to life on your chosen canvas.
要想在这个代理画布上高效构建，需要的不仅仅是将组件随意组合。它需要理解成熟的技术—— 模式 ——来解决设计和实现代理行为时常见的挑战。正如建筑模式指导建筑建造，设计模式构建软件结构一样，代理设计模式为您在所选画布上创建智能代理时可能遇到的反复出现的问题提供了可复用的解决方案。

# What are Agentic Systems? 
# 什么是代理系统？

At its core, an agentic system is a computational entity designed to perceive its environment (both digital and potentially physical), make informed decisions based on those perceptions and a set of predefined or learned goals, and execute actions to achieve those goals autonomously. Unlike traditional software, which follows rigid, step-by-step instructions, agents exhibit a degree of flexibility and initiative.
代理系统的核心是一个计算实体，旨在感知其环境（包括数字环境和潜在的物理环境），并基于这些感知和一系列预先定义或学习到的目标做出明智的决策，并自主执行操作以实现这些目标。与遵循严格的、循序渐进指令的传统软件不同，代理系统展现出一定的灵活性和主动性。

Imagine you need a system to manage customer inquiries. A traditional system might follow a fixed script. An agentic system, however, could perceive the nuances of a customer's query, access knowledge bases, interact with other internal systems (like order management), potentially ask clarifying questions, and proactively resolve the issue, perhaps even anticipating future needs. These agents operate on the canvas of your application's infrastructure, utilizing the services and data available to them.
假设您需要一个系统来管理客户咨询。传统系统可能遵循固定的脚本。而代理系统则可以感知客户查询的细微差别，访问知识库，与其他内部系统（例如订单管理）交互，提出必要的澄清问题，并主动解决问题，甚至预测未来的需求。这些代理系统在应用程序基础设施的画布上运行，利用可用的服务和数据。

Agentic systems are often characterized by features like autonomy, allowing them to act without constant human oversight; proactiveness, initiating actions towards their goals; and reactiveness, responding effectively to changes in their environment. They are fundamentally goal-oriented, constantly working towards objectives. A critical capability is tool use, enabling them to interact with external APIs, databases, or services – effectively reaching out beyond their immediate canvas. They possess memory, retain information across interactions, and can engage in communication with users, other systems, or even other agents operating on the same or connected canvases.
代理系统通常具有以下特征： 自主性 ，使其无需持续的人工监督即可行动； 主动性 ，使其主动采取行动以实现目标；以及反应性 ，使其能够有效地响应环境的变化。它们本质上是以目标为导向的，不断努力实现目标。一项关键能力是工具使用 ，使它们能够与外部 API、数据库或服务进行交互，从而有效地超越其直接画布。它们拥有记忆能力 ，能够在交互过程中保留信息，并能够与用户、其他系统，甚至在同一画布或连接画布上运行的其他代理进行通信 。

Effectively realizing these characteristics introduces significant complexity. How does the agent maintain state across multiple steps on its canvas? How does it decide when and how to use a tool? How is communication between different agents managed? How do you build resilience into the system to handle unexpected outcomes or errors?
有效地实现这些特性会带来巨大的复杂性。代理如何在画布上的多个步骤之间保持状态？它如何决定何时以及如何使用工具？如何管理不同代理之间的通信？如何在系统中构建弹性以应对意外结果或错误？

# Why Patterns Matter in Agent Development 
# 为什么模式在代理开发中很重要

This complexity is precisely why agentic design patterns are indispensable. They are not rigid rules, but rather battle-tested templates or blueprints that offer proven approaches to standard design and implementation challenges in the agentic domain. By recognizing and applying these design patterns, you gain access to solutions that enhance the structure, maintainability, reliability, and efficiency of the agents you build on your canvas.
这种复杂性正是代理设计模式不可或缺的原因。它们并非僵化的规则，而是久经考验的模板或蓝图，为代理领域的标准设计和实现挑战提供了行之有效的方法。通过识别和应用这些设计模式，您可以获得增强在画布上构建的代理的结构、可维护性、可靠性和效率的解决方案。

Using design patterns helps you avoid reinventing fundamental solutions for tasks like managing conversational flow, integrating external capabilities, or coordinating multiple agent actions. They provide a common language and structure that makes your agent's logic clearer and easier for others (and yourself in the future) to understand and maintain. Implementing patterns designed for error handling or state management directly contributes to building more robust and reliable systems. Leveraging these established approaches accelerates your development process, allowing you to focus on the unique aspects of your application rather than the foundational mechanics of agent behavior.
使用设计模式可以帮助您避免为管理对话流、集成外部功能或协调多个代理操作等任务重新设计基础解决方案。它们提供了一种通用的语言和结构，使您的代理逻辑更清晰，更易于他人（以及您自己）理解和维护。实施专为错误处理或状态管理而设计的模式，可直接帮助您构建更稳健、更可靠的系统。利用这些成熟的方法可以加速您的开发流程，让您能够专注于应用程序的独特之处，而不是代理行为的基本机制。

This book extracts 21 key design patterns that represent fundamental building blocks and techniques for constructing sophisticated agents on various technical canvases. Understanding and applying these patterns will significantly elevate your ability to design and implement intelligent systems effectively.
本书精选了21个关键设计模式，这些模式代表了在各种技术框架下构建复杂智能体的基本构建块和技术。理解并运用这些模式将显著提升你有效设计和实现智能系统的能力。

# Overview of the Book and How to Use It
# 本书概述及其使用方法
This book, "Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems," is crafted to be a practical and accessible resource. Its primary focus is on clearly explaining each agentic pattern and providing concrete, runnable code examples to demonstrate its implementation. Across 21 dedicated chapters, we will explore a diverse range of design patterns, from foundational concepts like structuring sequential operations (Prompt Chaining) and external interaction (Tool Use) to more advanced topics like collaborative work (Multi-Agent Collaboration) and self-improvement (Self-Correction).
本书名为《 智能体设计模式 ：构建智能系统的实用指南》，旨在成为一本实用易懂的资源。本书主要侧重于清晰地解释每个智能体模式，并提供具体的、可运行的代码示例来演示其实现。本书共 21 个章节，将探讨各种设计模式，从构建顺序操作（快速链接）和外部交互（工具使用）等基础概念，到协作工作（多智能体协作）和自我提升（自我修正）等更高级的主题。

The book is organized chapter by chapter, with each chapter delving into a single agentic pattern. Within each chapter, you will find:
本书按章节组织，每章深入探讨一个代理模式。在每一章中，你将找到：

- A detailed Pattern Overview providing a clear explanation of the pattern and its role in agentic design.
- 详细的模式概述提供了对模式及其在代理设计中的作用的清晰解释。

- A section on Practical Applications & Use Cases illustrating real-world scenarios where the pattern is invaluable and the benefits it brings.
- 关于实际应用和用例的部分说明了现实世界场景中该模式的宝贵价值及其带来的好处。

- A Hands-On Code Example offering practical, runnable code that demonstrates the pattern's implementation using prominent agent development frameworks. This is where you'll see how to apply the pattern within the context of a technical canvas.
动手代码示例提供了实用且可运行的代码，演示了如何使用知名的代理开发框架实现该模式。在这里，您将了解如何在技术画布中应用该模式。

- Key Takeaways summarizing the most crucial points for quick review.
关键要点总结了最重要的要点，以便快速审查。

- References for further exploration, providing resources for deeper learning on the pattern and related concepts.
- 进一步探索的参考资料 ，为更深入地学习模式和相关概念提供资源。


While the chapters are ordered to build concepts progressively, feel free to use the book as a reference, jumping to chapters that address specific challenges you face in your own agent development projects. The appendices provide a comprehensive look at advanced prompting techniques, principles for applying AI agents in real-world environments, and an overview of essential agentic frameworks. To complement this, practical online-only tutorials are included, offering step-by-step guidance on building agents with specific platforms like AgentSpace and for the command-line interface. The emphasis throughout is on practical application; we strongly encourage you to run the code examples, experiment with them, and adapt them to build your own intelligent systems on your chosen canvas. 
虽然本书的章节安排循序渐进，循序渐进地构建概念，但您也可以将本书作为参考，直接跳到解决您在自己的代理开发项目中遇到的具体挑战的章节。附录全面介绍了高级提示技术、在实际环境中应用人工智能代理的原则，并概述了基本的代理框架。此外，本书还包含实用的在线教程，提供使用 AgentSpace 等特定平台构建代理的分步指导以及命令行界面的指导。本书始终强调实际应用；我们强烈建议您运行代码示例，进行实验，并根据您选择的画布调整它们以构建您自己的智能系统。

A great question I hear is, 'With AI changing so fast, why write a book that could be quickly outdated?' My motivation was actually the opposite. It's precisely because things are moving so quickly that we need to step back and identify the underlying principles that are solidifying. Patterns like RAG, Reflection, Routing, Memory and the others I discuss, are becoming fundamental building blocks. This book is an invitation to reflect on these core ideas, which provide the foundation we need to build upon. Humans need these reflection moments on foundation patterns
我听到一个很好的问题是：“人工智能变化如此之快，为什么要写一本很快就会过时的书？” 我的动机实际上恰恰相反。正是因为事物发展如此之快，我们才需要退一步思考，找出那些正在固化的基本原则。像 RAG、反射、路由、内存以及我讨论的其他模式，正在成为基本的构建块。这本书邀请我们反思这些核心思想，它们为我们构建所需的基础奠定了基础。人类需要这些关于基础模式的反思时刻。

# Introduction to the Frameworks Used
# 所用框架简介

To provide a tangible "canvas" for our code examples (see also Appendix), we will primarily utilize three prominent agent development frameworks. LangChain, along with its stateful extension LangGraph, provides a flexible way to chain together language models and other components, offering a robust canvas for building complex sequences and graphs of operations. Crew AI provides a structured framework specifically designed for orchestrating multiple AI agents, roles, and tasks, acting as a canvas particularly well-suited for collaborative agent systems. The Google Agent Developer Kit (Google ADK) offers tools and components for building, evaluating, and deploying agents, providing another valuable canvas, often integrated with Google's AI infrastructure.
为了为我们的代码示例（另见附录）提供一个切实的“画布”，我们将主要利用三个著名的代理开发框架。LangChain 及其状态扩展 LangGraph 提供了一种灵活的方式 ， 可以将语言模型和其他组件链接在一起，从而为构建复杂的序列和操作图提供了一个强大的画布。Crew AI 提供了一个专门设计用于协调多个 AI 代理、角色和任务的结构化框架，可作为特别适合协作代理系统的画布。Google 代理开发套件 (Google ADK) 提供了用于构建、评估和部署代理的工具和组件，提供了另一个有价值的画布，通常与 Google 的 AI 基础架构集成。

These frameworks represent different facets of the agent development canvas, each with its strengths. By showing examples across these tools, you will gain a broader understanding of how the patterns can be applied regardless of the specific technical environment you choose for your agentic systems. The examples are designed to clearly illustrate the pattern's core logic and its implementation on the framework's canvas, focusing on clarity and practicality.
这些框架代表了代理开发画布的不同方面，各有优势。通过展示这些工具的示例，您将更广泛地了解如何应用这些模式，无论您为代理系统选择的具体技术环境如何。这些示例旨在清晰地说明模式的核心逻辑及其在框架画布上的实现，注重清晰度和实用性。

By the end of this book, you will not only understand the fundamental concepts behind 21 essential agentic patterns but also possess the practical knowledge and code examples to apply them effectively, enabling you to build more intelligent, capable, and autonomous systems on your chosen development canvas. Let's begin this hands-on journey!
读完本书，你不仅能理解 21 个基本代理模式背后的基本概念，还能掌握有效应用这些模式的实践知识和代码示例，从而能够在你选择的开发画布上构建更智能、更强大、更自主的系统。让我们开始这段实践之旅吧！

