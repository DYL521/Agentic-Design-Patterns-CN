# Appendix E \- AI Agents on the CLI
# 附录 E - 命令行界面上的 AI 智能体

# Introduction
# 引言

​​The developer's command line, long a bastion of precise, imperative commands, is undergoing a profound transformation. It is evolving from a simple shell into an intelligent, collaborative workspace powered by a new class of tools: AI Agent Command-Line Interfaces (CLIs). These agents move beyond merely executing commands; they understand natural language, maintain context about your entire codebase, and can perform complex, multi-step tasks that automate significant parts of the development lifecycle. 
开发者的命令行，这个长期以来精确的命令式指令的堡垒，正在经历深刻的转变。它正在从一个简单的 shell 演变为由一类新工具驱动的智能协作工作空间：AI 智能体命令行界面（CLI）。这些智能体超越了仅仅执行命令的范畴；它们能理解自然语言，维护整个代码库的上下文，并能执行复杂的多步骤任务，从而实现开发生命周期中重要部分的自动化。

This guide provides an in-depth look at four leading players in this burgeoning field, exploring their unique strengths, ideal use cases, and distinct philosophies to help you determine which tool best fits your workflow. It is important to note that many of the example use cases provided for a specific tool can often be accomplished by the other agents as well. The key differentiator between these tools frequently lies in the quality, efficiency, and nuance of the results they are able to achieve for a given task. There are specific benchmarks designed to measure these capabilities, which will be discussed in the following sections.
本指南深入探讨了这个新兴领域的四个主要参与者，探索了它们的独特优势、理想用例和不同理念，以帮助你确定哪个工具最适合你的工作流程。需要注意的是，为特定工具提供的许多示例用例通常也可以由其他智能体完成。这些工具之间的关键区别通常在于它们在给定任务中能够实现的结果的质量、效率和细微差别。有专门的基准测试用于衡量这些能力，这将在后续章节中讨论。

# Claude CLI (Claude Code)
# Claude CLI（Claude 代码）

Anthropic's Claude CLI is engineered as a high-level coding agent with a deep, holistic understanding of a project's architecture. Its core strength is its "agentic" nature, allowing it to create a mental model of your repository for complex, multi-step tasks. The interaction is highly conversational, resembling a pair programming session where it explains its plans before executing. This makes it ideal for professional developers working on large-scale projects involving significant refactoring or implementing features with broad architectural impacts.
Anthropic 的 Claude CLI 被设计为一个高级编码智能体，对项目架构有深入、全面的理解。它的核心优势在于其"智能体"特性，使其能够为复杂的多步骤任务创建仓库的心智模型。交互高度对话化，类似于结对编程会话，在执行之前会解释其计划。这使其非常适合专业开发人员处理涉及重大重构或实现具有广泛架构影响的功能的大型项目。

**Example Use Cases:**
**示例用例：**

1. **Large-Scale Refactoring:** You can instruct it: "Our current user authentication relies on session cookies. Refactor the entire codebase to use stateless JWTs, updating the login/logout endpoints, middleware, and frontend token handling." Claude will then read all relevant files and perform the coordinated changes.  
1. **大规模重构：** 你可以指示它："我们当前的用户认证依赖于会话 cookie。重构整个代码库以使用无状态 JWT，更新登录/登出端点、中间件和前端令牌处理。" Claude 随后会读取所有相关文件并执行协调的更改。

2. **API Integration:** After being provided with an OpenAPI specification for a new weather service, you could say: "Integrate this new weather API. Create a service module to handle the API calls, add a new component to display the weather, and update the main dashboard to include it."  
2. **API 集成：** 在提供了新天气服务的 OpenAPI 规范后，你可以说："集成这个新的天气 API。创建一个服务模块来处理 API 调用，添加一个新组件来显示天气，并更新主仪表板以包含它。"

3. **Documentation Generation**: Pointing it to a complex module with poorly documented code, you can ask: "Analyze the ./src/utils/data\_processing.js file. Generate comprehensive TSDoc comments for every function, explaining its purpose, parameters, and return value."
3. **文档生成**：指向一个文档不完善的复杂模块，你可以要求："分析 ./src/utils/data\_processing.js 文件。为每个函数生成全面的 TSDoc 注释，解释其目的、参数和返回值。"

Claude CLI functions as a specialized coding assistant, with inherent tools for core development tasks, including file ingestion, code structure analysis, and edit generation. Its deep integration with Git facilitates direct branch and commit management. The agent's extensibility is mediated by the Multi-tool Control Protocol (MCP), enabling users to define and integrate custom tools. This allows for interactions with private APIs, database queries, and execution of project-specific scripts. This architecture positions the developer as the arbiter of the agent's functional scope, effectively characterizing Claude as a reasoning engine augmented by user-defined tooling.
Claude CLI 作为一个专门的编码助手运作，具有用于核心开发任务的固有工具，包括文件摄取、代码结构分析和编辑生成。它与 Git 的深度集成便于直接的分支和提交管理。智能体的可扩展性由多工具控制协议（MCP）调解，使用户能够定义和集成自定义工具。这允许与私有 API、数据库查询和执行项目特定脚本进行交互。这种架构将开发者定位为智能体功能范围的仲裁者，有效地将 Claude 描述为一个由用户定义工具增强的推理引擎。

# Gemini CLI
# Gemini 命令行界面

Google's Gemini CLI is a versatile, open-source AI agent designed for power and accessibility. It stands out with the advanced Gemini 2.5 Pro model, a massive context window, and multimodal capabilities (processing images and text). Its open-source nature, generous free tier, and "Reason and Act" loop make it a transparent, controllable, and excellent all-rounder for a broad audience, from hobbyists to enterprise developers, especially those within the Google Cloud ecosystem.
Google 的 Gemini CLI 是一个功能多样的开源 AI 智能体，专为强大功能和可访问性而设计。它以先进的 Gemini 2.5 Pro 模型、巨大的上下文窗口和多模态能力（处理图像和文本）而脱颖而出。其开源特性、慷慨的免费层级和"推理和行动"循环使其成为一个透明、可控且优秀的全能工具，适用于从业余爱好者到企业开发者的广泛受众，尤其是那些在 Google Cloud 生态系统中的用户。

**Example Use Cases:**
**示例用例：**

1. **Multimodal Development:** You provide a screenshot of a web component from a design file (gemini describe component.png) and instruct it: "Write the HTML and CSS code to build a React component that looks exactly like this. Make sure it's responsive."  
1. **多模态开发：** 你提供一个来自设计文件的网页组件截图（gemini describe component.png）并指示它："编写 HTML 和 CSS 代码来构建一个看起来完全一样的 React 组件。确保它是响应式的。"

2. **Cloud Resource Management:** Using its built-in Google Cloud integration, you can command: "Find all GKE clusters in the production project that are running versions older than 1.28 and generate a gcloud command to upgrade them one by one."  
2. **云资源管理：** 使用其内置的 Google Cloud 集成，你可以命令："找出生产项目中所有运行版本低于 1.28 的 GKE 集群，并生成一个 gcloud 命令来逐个升级它们。"

3. **Enterprise Tool Integration (via MCP):** A developer provides Gemini with a custom tool called get-employee-details that connects to the company's internal HR API. The prompt is: "Draft a welcome document for our new hire. First, use the get-employee-details \--id=E90210 tool to fetch their name and team, and then populate the welcome\_template.md with that information."  
3. **企业工具集成（通过 MCP）：** 开发者为 Gemini 提供了一个名为 get-employee-details 的自定义工具，该工具连接到公司的内部人力资源 API。提示是："为我们的新员工起草一份欢迎文档。首先，使用 get-employee-details \--id=E90210 工具获取他们的姓名和团队，然后用这些信息填充 welcome\_template.md。"

4. **Large-Scale Refactoring**: A developer needs to refactor a large Java codebase to replace a deprecated logging library with a new, structured logging framework. They can use Gemini with a prompt like: Read all \*.java files in the 'src/main/java' directory. For each file, replace all instances of the 'org.apache.log4j' import and its 'Logger' class with 'org.slf4j.Logger' and 'LoggerFactory'. Rewrite the logger instantiation and all .info(), .debug(), and .error() calls to use the new structured format with key-value pairs.
4. **大规模重构**：开发者需要重构一个大型 Java 代码库，将一个已弃用的日志库替换为新的结构化日志框架。他们可以使用类似这样的提示来使用 Gemini：读取 'src/main/java' 目录中的所有 \*.java 文件。对于每个文件，将所有 'org.apache.log4j' 导入及其 'Logger' 类的实例替换为 'org.slf4j.Logger' 和 'LoggerFactory'。重写日志记录器实例化和所有 .info()、.debug() 和 .error() 调用，使用带有键值对的新结构化格式。

Gemini CLI is equipped with a suite of built-in tools that allow it to interact with its environment. These include tools for file system operations (like reading and writing), a shell tool for running commands, and tools for accessing the internet via web fetching and searching. For broader context, it uses specialized tools to read multiple files at once and a memory tool to save information for later sessions. This functionality is built on a secure foundation: sandboxing isolates the model's actions to prevent risk, while MCP servers act as a bridge, enabling Gemini to safely connect to your local environment or other APIs.
Gemini CLI 配备了一套内置工具，允许它与其环境交互。这些工具包括用于文件系统操作（如读写）的工具、用于运行命令的 shell 工具，以及通过网络获取和搜索来访问互联网的工具。为了获得更广泛的上下文，它使用专门的工具一次读取多个文件，并使用内存工具保存信息以供后续会话使用。这些功能建立在安全的基础之上：沙箱隔离模型的操作以防止风险，而 MCP 服务器充当桥梁，使 Gemini 能够安全地连接到你的本地环境或其他 API。

# Aider
# Aider

Aider is an open-source AI coding assistant that acts as a true pair programmer by working directly on your files and committing changes to Git. Its defining feature is its directness; it applies edits, runs tests to validate them, and automatically commits every successful change. Being model-agnostic, it gives users complete control over cost and capabilities. Its git-centric workflow makes it perfect for developers who value efficiency, control, and a transparent, auditable trail of all code modifications.
Aider 是一个开源的 AI 编码助手，通过直接在你的文件上工作并将更改提交到 Git 来充当真正的结对编程伙伴。它的显著特点是直接性；它应用编辑、运行测试来验证它们，并自动提交每个成功的更改。由于它与模型无关，它给予用户对成本和功能的完全控制。其以 git 为中心的工作流程使其非常适合那些重视效率、控制和所有代码修改的透明、可审计跟踪的开发者。

**Example Use Cases:**
**示例用例：**

1. **Test-Driven Development (TDD):** A developer can say: "Create a failing test for a function that calculates the factorial of a number." After Aider writes the test and it fails, the next prompt is: "Now, write the code to make the test pass." Aider implements the function and runs the test again to confirm.  
1. **测试驱动开发（TDD）：** 开发者可以说："为一个计算数字阶乘的函数创建一个失败的测试。" 在 Aider 编写测试并且它失败后，下一个提示是："现在，编写代码使测试通过。" Aider 实现该函数并再次运行测试以确认。

2. **Precise Bug Squashing:** Given a bug report, you can instruct Aider: "The calculate\_total function in billing.py fails on leap years. Add the file to the context, fix the bug, and verify your fix against the existing test suite."  
2. **精确的错误修复：** 给定一个错误报告，你可以指示 Aider："billing.py 中的 calculate\_total 函数在闰年时失败。将文件添加到上下文中，修复错误，并根据现有的测试套件验证你的修复。"

3. **Dependency Updates:** You could instruct it: "Our project uses an outdated version of the 'requests' library. Please go through all Python files, update the import statements and any deprecated function calls to be compatible with the latest version, and then update requirements.txt."
3. **依赖更新：** 你可以指示它："我们的项目使用了过时版本的 'requests' 库。请检查所有 Python 文件，更新导入语句和任何已弃用的函数调用以与最新版本兼容，然后更新 requirements.txt。"

# GitHub Copilot CLI
# GitHub Copilot 命令行界面

GitHub Copilot CLI extends the popular AI pair programmer into the terminal, with its primary advantage being its native, deep integration with the GitHub ecosystem. It understands the context of a project *within GitHub*. Its agent capabilities allow it to be assigned a GitHub issue, work on a fix, and submit a pull request for human review.
GitHub Copilot CLI 将流行的 AI 结对编程伙伴扩展到终端，其主要优势在于与 GitHub 生态系统的原生、深度集成。它理解项目在 GitHub 内的上下文。其智能体能力允许它被分配一个 GitHub 问题，处理修复，并提交拉取请求供人工审查。

**Example Use Cases:**
**示例用例：**

1. **Automated Issue Resolution:** A manager assigns a bug ticket (e.g., "Issue \#123: Fix off-by-one error in pagination") to the Copilot agent. The agent then checks out a new branch, writes the code, and submits a pull request referencing the issue, all without manual developer intervention.  
1. **自动问题解决：** 管理者将一个错误工单（例如，"问题 \#123：修复分页中的差一错误"）分配给 Copilot 智能体。智能体然后检出一个新分支，编写代码，并提交引用该问题的拉取请求，所有这些都无需开发者手动干预。

2. **Repository-Aware Q\&A:** A new developer on the team can ask: "Where in this repository is the database connection logic defined, and what environment variables does it require?" Copilot CLI uses its awareness of the entire repo to provide a precise answer with file paths.  
2. **仓库感知问答：** 团队中的新开发者可以问："在这个仓库中，数据库连接逻辑定义在哪里，它需要哪些环境变量？" Copilot CLI 使用其对整个仓库的感知来提供带有文件路径的精确答案。

3. **Shell Command Helper:** When unsure about a complex shell command, a user can ask: gh? find all files larger than 50MB, compress them, and place them in an archive folder. Copilot will generate the exact shell command needed to perform the task.
3. **Shell 命令助手：** 当对复杂的 shell 命令不确定时，用户可以问：gh？找出所有大于 50MB 的文件，压缩它们，并将它们放在一个归档文件夹中。Copilot 将生成执行该任务所需的确切 shell 命令。

# Terminal-Bench: A Benchmark for AI Agents in Command-Line Interfaces
# Terminal-Bench：命令行界面 AI 智能体的基准测试

Terminal-Bench is a novel evaluation framework designed to assess the proficiency of AI agents in executing complex tasks within a command-line interface. The terminal is identified as an optimal environment for AI agent operation due to its text-based, sandboxed nature. The initial release, Terminal-Bench-Core-v0, comprises 80 manually curated tasks spanning domains such as scientific workflows and data analysis. To ensure equitable comparisons, Terminus, a minimalistic agent, was developed to serve as a standardized testbed for various language models. The framework is designed for extensibility, allowing for the integration of diverse agents through containerization or direct connections. Future developments include enabling massively parallel evaluations and incorporating established benchmarks. The project encourages open-source contributions for task expansion and collaborative framework enhancement.
Terminal-Bench 是一个新颖的评估框架，旨在评估 AI 智能体在命令行界面中执行复杂任务的熟练程度。由于其基于文本、沙箱化的特性，终端被认定为 AI 智能体操作的最佳环境。初始版本 Terminal-Bench-Core-v0 包含 80 个手动策划的任务，涵盖科学工作流和数据分析等领域。为确保公平比较，开发了一个极简智能体 Terminus，作为各种语言模型的标准化测试平台。该框架设计具有可扩展性，允许通过容器化或直接连接集成各种智能体。未来的发展包括启用大规模并行评估和整合已建立的基准测试。该项目鼓励开源贡献以扩展任务和协作增强框架。

# Conclusion
# 结论

The emergence of these powerful AI command-line agents marks a fundamental shift in software development, transforming the terminal into a dynamic and collaborative environment. As we've seen, there is no single "best" tool; instead, a vibrant ecosystem is forming where each agent offers a specialized strength. The ideal choice depends entirely on the developer's needs: Claude for complex architectural tasks, Gemini for versatile and multimodal problem-solving, Aider for git-centric and direct code editing, and GitHub Copilot for seamless integration into the GitHub workflow. As these tools continue to evolve, proficiency in leveraging them will become an essential skill, fundamentally changing how developers build, debug, and manage software.
这些强大的 AI 命令行智能体的出现标志着软件开发的根本性转变，将终端转变为一个动态和协作的环境。正如我们所见，没有单一的"最佳"工具；相反，一个充满活力的生态系统正在形成，每个智能体都提供专门的优势。理想的选择完全取决于开发者的需求：Claude 用于复杂的架构任务，Gemini 用于多功能和多模态问题解决，Aider 用于以 git 为中心的直接代码编辑，GitHub Copilot 用于无缝集成到 GitHub 工作流中。随着这些工具继续发展，熟练利用它们将成为一项基本技能，从根本上改变开发者构建、调试和管理软件的方式。

# References
# 参考文献

1. Anthropic. *Claude*. [https://docs.anthropic.com/en/docs/claude-code/cli-reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference)   
   Anthropic. *Claude*. [https://docs.anthropic.com/en/docs/claude-code/cli-reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference)
2. Google Gemini Cli [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)   
   Google Gemini 命令行界面 [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
3. Aider. [https://aider.chat/](https://aider.chat/)  
   Aider. [https://aider.chat/](https://aider.chat/)
4. GitHub *Copilot CLI* [https://docs.github.com/en/copilot/github-copilot-enterprise/copilot-cli](https://docs.github.com/en/copilot/github-copilot-enterprise/copilot-cli)  
   GitHub *Copilot 命令行界面* [https://docs.github.com/en/copilot/github-copilot-enterprise/copilot-cli](https://docs.github.com/en/copilot/github-copilot-enterprise/copilot-cli)
5. Terminal Bench: [https://www.tbench.ai/](https://www.tbench.ai/) 
   Terminal Bench：[https://www.tbench.ai/](https://www.tbench.ai/)

