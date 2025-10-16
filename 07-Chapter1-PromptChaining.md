- 原文链接：https://docs.google.com/document/d/1flxKGrbnF2g8yh3F-oVD5Xx7ZumId56HbFpIiPdkqLI/edit?tab=t.0#heading=h.fxiksssjx6aj

# Chapter 1: Prompt Chaining
  第 1 章：提示链接

## Prompt Chaining Pattern Overview
   提示链接模式概述

Prompt chaining, sometimes referred to as Pipeline pattern, represents a powerful paradigm for handling intricate tasks when leveraging large language models (LLMs). Rather than expecting an LLM to solve a complex problem in a single, monolithic step, prompt chaining advocates for a divide-and-conquer strategy. The core idea is to break down the original, daunting problem into a sequence of smaller, more manageable sub-problems. Each sub-problem is addressed individually through a specifically designed prompt, and the output generated from one prompt is strategically fed as input into the subsequent prompt in the chain.
提示链，有时也称为管道模式，代表了利用大型语言模型（LLM）处理复杂任务的强大范例。   与其期望法学硕士能够通过单一、整体的步骤解决复杂问题，不如采用分而治之的策略。   其核心思想是将原始的、令人畏惧的问题分解为一系列更小、更易于管理的子问题 。   每个子问题都通过专门设计的提示单独解决，并且一个提示生成的输出被策略性地作为输入输入到链中的后续提示中。

This sequential processing technique inherently introduces modularity and clarity into the interaction with LLMs. By decomposing a complex task, it becomes easier to understand and debug each individual step, making the overall process more robust and interpretable. Each step in the chain can be meticulously crafted and optimized to focus on a specific aspect of the larger problem, leading to more accurate and focused outputs.
这种顺序处理技术本质上为与 LLM 的交互引入了模块化和清晰度。通过分解复杂的任务，每个步骤都变得更容易理解和调试，从而使整个过程更加健壮且易于解释。   链中的每一步都可以精心设计和优化，以专注于更大问题的特定方面，从而获得更准确和更集中的输出。

The output of one step acting as the input for the next is crucial. This passing of information establishes a dependency chain, hence the name, where the context and results of previous operations guide the subsequent processing. This allows the LLM to build on its previous work, refine its understanding, and progressively move closer to the desired solution.
一个步骤的输出作为下一个步骤的输入至关重要。   这种信息传递建立了依赖链，因此得名，其中先前操作的上下文和结果指导后续处理。   这使得 LLM 能够在之前的工作基础上进一步完善其理解，并逐步接近所需的解决方案。

Furthermore, prompt chaining is not just about breaking down problems; it also enables the integration of external knowledge and tools. At each step, the LLM can be instructed to interact with external systems, APIs, or databases, enriching its knowledge and abilities beyond its internal training data. This capability dramatically expands the potential of LLMs, allowing them to function not just as isolated models but as integral components of broader, more intelligent systems.
此外，快速链接不仅仅是分解问题，它还能整合外部知识和工具。 在每一步中，LLM 都可以被指示与外部系统、API 或数据库进行交互，从而丰富其内部训练数据以外的知识和能力。   这种能力极大地扩展了 LLM 的潜力，使它们不仅可以作为独立的模型发挥作用，而且可以作为更广泛、更智能的系统的组成部分。

The significance of prompt chaining extends beyond simple problem-solving. It serves as a foundational technique for building sophisticated AI agents. These agents can utilize prompt chains to autonomously plan, reason, and act in dynamic environments. By strategically structuring the sequence of prompts, an agent can engage in tasks requiring multi-step reasoning, planning, and decision-making. Such agent workflows can mimic human thought processes more closely, allowing for more natural and effective interactions with complex domains and systems.
提示链的意义不仅限于简单的解决问题。   它是构建复杂 AI 代理的基础技术。   这些代理可以利用提示链在动态环境中自主规划、推理和行动。   通过策略性地构建提示序列，代理可以参与需要多步骤推理、规划和决策的任务。   这种代理工作流程可以更紧密地模仿人类的思维过程，从而实现与复杂领域和系统更自然、更有效的交互。


**Limitations of single prompts**: For multifaceted tasks, using a single, complex prompt for an LLM can be inefficient, causing the model to struggle with constraints and instructions, potentially leading to instruction neglect where parts of the prompt are overlooked, contextual drift where the model loses track of the initial context, error propagation where early errors amplify, prompts which require a longer context window where the model gets insufficient information to respond back and hallucination where the cognitive load increases the chance of incorrect information. For example, a query asking to analyze a market research report, summarize findings, identify trends with data points, and draft an email risks failure as the model might summarize well but fail to extract data or draft an email properly.
**单一提示的局限性** ：   对于多方面的任务，使用单一、复杂的 LLM 提示可能效率低下，导致模型难以应对约束和指令，可能导致指令忽略（即忽略提示的部分内容）、上下文漂移（即模型失去对初始上下文的跟踪）、错误传播（即早期错误被放大）、 提示需要更长的上下文窗口（即模型获得的信息不足以做出回应） 以及幻觉（即认知负荷增加了错误信息的机会）。   例如，要求分析市场研究报告、总结调查结果、用数据点识别趋势以及起草电子邮件的查询可能会失败，因为模型可能会很好地总结，但无法正确提取数据或起草电子邮件。

**Enhanced Reliability Through Sequential Decomposition**: Prompt chaining addresses these challenges by breaking the complex task into a focused, sequential workflow, which significantly improves reliability and control. Given the example above, a pipeline or chained approach can be described as follows:
**通过顺序分解增强可靠性**： 快速链接通过将复杂任务分解为集中的、顺序的工作流程来解决这些挑战，从而显著提高可靠性和控制力 。 基于上述示例，流水线或链接方法可以描述如下 ：

- Initial Prompt (Summarization): "Summarize the key findings of the following market research report: [text]." The model's sole focus is summarization, increasing the accuracy of this initial step.
    初始提示（总结）：“总结以下市场研究报告的主要发现：[文本]。”该模型的唯一重点是总结，从而提高了此初始步骤的准确性。

- Second Prompt (Trend Identification): "Using the summary, identify the top three emerging trends and extract the specific data points that support each trend: [output from step 1]." This prompt is now more constrained and builds directly upon a validated output.
  第二个提示（趋势识别）：“使用摘要，确定三大新兴趋势，并提取支持每个趋势的具体数据点：[步骤 1 的输出]。” 此提示现在更加严格，并直接建立在经过验证的输出之上。

- Third Prompt (Email Composition): "Draft a concise email to the marketing team that outlines the following trends and their supporting data: [output from step 2]."
  第三个提示（电子邮件撰写）：“起草一封简明的电子邮件给营销团队，概述以下趋势及其支持数据：[步骤 2 的输出]。”

- This decomposition allows for more granular control over the process. Each step is simpler and less ambiguous, which reduces the cognitive load on the model and leads to a more accurate and reliable final output. This modularity is analogous to a computational pipeline where each function performs a specific operation before passing its result to the next. To ensure an accurate response for each specific task, the model can be assigned a distinct role at every stage. For example, in the given scenario, the initial prompt could be designated as "Market Analyst," the subsequent prompt as "Trade Analyst," and the third prompt as "Expert Documentation Writer," and so forth.
  这种分解方式可以更精细地控制整个流程。每个步骤都更简单、更少歧义，从而减轻了模型的认知负担，并最终获得更准确、更可靠的输出。这种模块化类似于计算流水线，其中每个函数执行特定的操作，然后再将其结果传递给下一个函数。 为了确保对每个特定任务的准确响应，可以在每个阶段为模型分配不同的角色。   例如，在给定场景中，初始提示可以指定为“市场分析师”，后续提示可以指定为“贸易分析师”，第三个提示可以指定为“专家文档撰写者”，依此类推。

**The Role of Structured Output**: The reliability of a prompt chain is highly dependent on the integrity of the data passed between steps. If the output of one prompt is ambiguous or poorly formatted, the subsequent prompt may fail due to faulty input. To mitigate this, specifying a structured output format, such as JSON or XML, is crucial.
结构化输出的作用： 提示链的可靠性高度依赖于步骤间传递数据的完整性。如果一个提示的输出含糊不清或格式错误，后续提示可能会因输入错误而失败。为了缓解这种情况，指定结构化输出格式（例如 JSON 或 XML）至关重要。

For example, the output from the trend identification step could be formatted as a JSON object:
例如， 趋势识别步骤的输出可以格式化为 JSON 对象：
```json
{
  "trends": [
    {
      "trend_name": "AI-Powered Personalization",
      "supporting_data": "73% of consumers prefer to do business with brands that use personal information to make their shopping experiences more relevant."
    },
    {
      "trend_name": "Sustainable and Ethical Brands",
      "supporting_data": "Sales of products with ESG-related claims grew 28% over the last five years, compared to 20% for products without."
    }
  ]
}
```



This structured format ensures that the data is machine-readable and can be precisely parsed and inserted into the next prompt without ambiguity. This practice minimizes errors that can arise from interpreting natural language and is a key component in building robust, multi-step LLM-based systems.
这种结构化格式确保数据是机器可读的，能够被精确解析并插入到下一个提示中，而不会产生歧义。这种做法可以最大限度地减少解释自然语言时可能出现的错误，是构建强大的、多步骤的基于 LLM 的系统的关键组成部分。

## Practical Applications & Use Cases
   实际应用和用例
Prompt chaining is a versatile pattern applicable in a wide range of scenarios when building agentic systems. Its core utility lies in breaking down complex problems into sequential, manageable steps. Here are several practical applications and use cases:
提示链是一种通用模式，适用于构建代理系统的各种场景。其核心功能在于将复杂问题分解为连续且可管理的步骤。以下是一些实际应用和用例：

1. **Information Processing Workflows**: Many tasks involve processing raw information through multiple transformations. For instance, summarizing a document, extracting key entities, and then using those entities to query a database or generate a report. A prompt chain could look like:
   **信息处理工作流**： 许多任务涉及通过多种转换来处理原始信息。例如，汇总文档，提取关键实体，然后使用这些实体查询数据库或生成报告。提示链可能如下所示：

- Prompt 1: Extract text content from a given URL or document.
            从给定的 URL 或文档中提取文本内容。
- Prompt 2: Summarize the cleaned text.
            总结清理后的文本。
- Prompt 3: Extract specific entities (e.g., names, dates, locations) from the summary or original text.
            从摘要或原文中提取特定实体（例如，名称、日期、位置）。
- Prompt 4: Use the entities to search an internal knowledge base.
            使用实体搜索内部知识库。
- Prompt 5: Generate a final report incorporating the summary, entities, and search results.
            生成包含摘要、实体和搜索结果的最终报告。
This methodology is applied in domains such as automated content analysis, the development of AI-driven research assistants, and complex report generation.
该方法应用于自动内容分析、人工智能驱动的研究助手的开发和复杂报告生成等领域。

2. **Complex Query Answering**: Answering complex questions that require multiple steps of reasoning or information retrieval is a prime use case. For example, "What were the main causes of the stock market crash in 1929, and how did government policy respond?"
    **复杂查询应答**： 回答需要多步推理或信息检索的复杂问题是其主要用例。例如，“1929 年股市崩盘的主要原因是什么？政府政策如何应对？”

- Prompt 1: Identify the core sub-questions in the user's query (causes of crash, government response).
           确定用户查询中的核心子问题（事故原因、政府反应）。
- Prompt 2: Research or retrieve information specifically about the causes of the 1929 crash.
            研究或检索有关 1929 年崩盘原因的具体信息。
- Prompt 3: Research or retrieve information specifically about the government's policy response to the 1929 stock market crash.
            研究或检索有关政府对 1929 年股市崩盘的政策反应的具体信息 。
Prompt 4: Synthesize the information from steps 2 and 3 into a coherent answer to the original query.
           将步骤 2 和 3 中的信息综合成对原始查询的连贯答案。
This sequential processing methodology is integral to developing AI systems capable of multi-step inference and information synthesis. Such systems are required when a query cannot be answered from a single data point but instead necessitates a series of logical steps or the integration of information from diverse sources.
这种顺序处理方法对于开发能够进行多步骤推理和信息综合的人工智能系统至关重要。当查询无法从单个数据点得到解答，而是需要一系列逻辑步骤或整合来自不同来源的信息时，就需要这样的系统。

For example, an automated research agent designed to generate a comprehensive report on a specific topic executes a hybrid computational workflow. Initially, the system retrieves numerous relevant articles. The subsequent task of extracting key information from each article can be performed concurrently for each source. This stage is well-suited for parallel processing, where independent sub-tasks are run simultaneously to maximize efficiency.
例如，一个旨在生成特定主题综合报告的自动化研究代理会执行混合计算工作流。首先，系统会检索大量相关文章。随后，从每篇文章中提取关键信息的任务可以针对每个来源同时执行。此阶段非常适合并行处理，即同时运行独立的子任务以最大限度地提高效率。

However, once the individual extractions are complete, the process becomes inherently sequential. The system must first collate the extracted data, then synthesize it into a coherent draft, and finally review and refine this draft to produce a final report. Each of these later stages is logically dependent on the successful completion of the preceding one. This is where prompt chaining is applied: the collated data serves as the input for the synthesis prompt, and the resulting synthesized text becomes the input for the final review prompt. Therefore, complex operations frequently combine parallel processing for independent data gathering with prompt chaining for the dependent steps of synthesis and refinement.
然而，一旦各个提取步骤完成，整个过程就变得本质上是连续的。系统必须首先整理提取的数据，然后将其合成为连贯的草稿，最后审查并完善该草稿以生成最终报告。从逻辑上讲，每个后续阶段都依赖于前一个阶段的成功完成。这时就需要应用提示链：整理后的数据作为合成提示的输入，而生成的合成文本则成为最终审查提示的输入。因此，复杂的操作通常会将并行处理（用于独立数据收集）与提示链（用于合成和完善这些相互依赖的步骤）结合起来。

3. Data Extraction and Transformation: The conversion of unstructured text into a structured format is typically achieved through an iterative process, requiring sequential modifications to improve the accuracy and completeness of the output.
  数据提取和转换： 非结构化文本向结构化格式的转换通常通过迭代过程实现，需要进行连续修改以提高输出的准确性和完整性。

- Prompt 1: Attempt to extract specific fields (e.g., name, address, amount) from an invoice document.
           尝试从发票文件中提取特定字段（例如姓名、地址、金额）。
- Processing: Check if all required fields were extracted and if they meet format requirements.
        处理： 检查是否提取了所有必填字段以及它们是否符合格式要求。

- Prompt 2 (Conditional): If fields are missing or malformed, craft a new prompt asking the model to specifically find the missing/malformed information, perhaps providing context from the failed attempt.
                        如果字段缺失或格式错误，则制作一个新提示，要求模型专门查找缺失/格式错误的信息，或许提供失败尝试的背景。
- Processing: Validate the results again. Repeat if necessary.
  处理：再次验证结果。如有必要，请重复。
- Output: Provide the extracted, validated structured data.
输出：提供提取的、验证的结构化数据。

This sequential processing methodology is particularly applicable to data extraction and analysis from unstructured sources like forms, invoices, or emails. For example, solving complex Optical Character Recognition (OCR) problems, such as processing a PDF form, is more effectively handled through a decomposed, multi-step approach.
这种顺序处理方法尤其适用于从表单、发票或电子邮件等非结构化数据中提取和分析数据。例如，解决复杂的光学字符识别 (OCR) 问题（例如处理 PDF 表单），可以通过分解、多步骤的方法更有效地处理。

Initially, a large language model is employed to perform the primary text extraction from the document image. Following this, the model processes the raw output to normalize the data, a step where it might convert numeric text, such as "one thousand and fifty," into its numerical equivalent, 1050. A significant challenge for LLMs is performing precise mathematical calculations. Therefore, in a subsequent step, the system can delegate any required arithmetic operations to an external calculator tool. The LLM identifies the necessary calculation, feeds the normalized numbers to the tool, and then incorporates the precise result. This chained sequence of text extraction, data normalization, and external tool use achieves a final, accurate result that is often difficult to obtain reliably from a single LLM query.
首先，使用大型语言模型从文档图像中提取主要文本。之后，该模型处理原始输出以规范化数据，此步骤可能会将数字文本（例如“一千零五十”）转换为其对应的数字 1050。LLM 面临的一个重大挑战是执行精确的数学计算。因此，在后续步骤中，系统可以将任何所需的算术运算委托给外部计算工具。LLM 识别必要的计算，将规范化的数字输入到该工具，然后合并精确的结果。这种文本提取、数据规范化和外部工具使用的链式流程最终能够获得准确的结果，而这通常很难通过单个 LLM 查询获得可靠的结果。

4. Content Generation Workflows: The composition of complex content is a procedural task that is typically decomposed into distinct phases, including initial ideation, structural outlining, drafting, and subsequent revision
   内容生成工作流程： 复杂内容的创作是一个程序性任务，通常分解为不同的阶段，包括初步构思、结构概述、起草和后续修订

- Prompt 1: Generate 5 topic ideas based on a user's general interest.
提示 1：根据用户的一般兴趣产生 5 个主题想法。

- Processing: Allow the user to select one idea or automatically choose the best one.
  处理：允许用户选择一个想法或自动选择最佳想法。

- Prompt 2: Based on the selected topic, generate a detailed outline.
提示 2：根据选定的主题，生成详细的大纲。

- Prompt 3: Write a draft section based on the first point in the outline.
提示 3：根据大纲中的第一点写一个草稿部分。

- Prompt 4: Write a draft section based on the second point in the outline, providing the previous section for context. Continue this for all outline points.
提示 4：根据提纲中的第二点，撰写一个草稿部分，并提供前一部分作为背景。对所有提纲要点都重复此操作。

- Prompt 5: Review and refine the complete draft for coherence, tone, and grammar.
提示 5：审查并完善完整草稿的连贯性、语气和语法。
This methodology is employed for a range of natural language generation tasks, including the automated composition of creative narratives, technical documentation, and other forms of structured textual content.
该方法适用于一系列自然语言生成任务，包括创意叙述、技术文档和其他形式的结构化文本内容的自动创作。

5. Conversational Agents with State: Although comprehensive state management architectures employ methods more complex than sequential linking, prompt chaining provides a foundational mechanism for preserving conversational continuity. This technique maintains context by constructing each conversational turn as a new prompt that systematically incorporates information or extracted entities from preceding interactions in the dialogue sequence.
    具有状态的对话代理： 尽管全面的状态管理架构采用的方法比顺序链接更为复杂，但提示链提供了保持对话连续性的基础机制。该技术通过将每个对话轮次构建为新的提示来维护上下文，该提示系统地整合对话序列中先前交互中的信息或提取的实体。

- Prompt 1: Process User Utterance 1, identify intent and key entities.
提示 1：处理用户话语 1，识别意图和关键实体。
- Processing: Update conversation state with intent and entities.
处理：使用意图和实体更新对话状态。
-  Prompt 2: Based on current state, generate a response and/or identify the next required piece of information.
提示 2：根据当前状态，生成响应和/或识别下一个所需的信息。
Repeat for subsequent turns, with each new user utterance initiating a chain that leverages the accumulating conversation history (state).
重复后续轮次，每个新用户话语都会启动一个利用累积对话历史（状态）的链。
This principle is fundamental to the development of conversational agents, enabling them to maintain context and coherence across extended, multi-turn dialogues. By preserving the conversational history, the system can understand and appropriately respond to user inputs that depend on previously exchanged information.
这一原则是对话代理开发的基础，使其能够在扩展的多轮对话中保持语境和连贯性。通过保存对话历史记录，系统可以理解并根据先前交换的信息做出适当的响应。

6. Code Generation and Refinement: The generation of functional code is typically a multi-stage process, requiring a problem to be decomposed into a sequence of discrete logical operations that are executed progressively
   代码生成和细化： 功能代码的生成通常是一个多阶段的过程，需要将问题分解为一系列离散的逻辑操作，并逐步执行

- Prompt 1: Understand the user's request for a code function. Generate pseudocode or an outline.
提示 1：了解用户对代码功能的请求。生成伪代码或概要。

- Prompt 2: Write the initial code draft based on the outline.
提示 2：根据大纲编写初始代码草稿。

- Prompt 3: Identify potential errors or areas for improvement in the code (perhaps using a static analysis tool or another LLM call).
提示 3：识别代码中的潜在错误或需要改进的地方（可能使用静态分析工具或其他 LLM 调用）。

- Prompt 4: Rewrite or refine the code based on the identified issues.
提示 4：根据发现的问题重写或改进代码。

- Prompt 5: Add documentation or test cases.
提示 5：添加文档或测试用例。

- In applications such as AI-assisted software development, the utility of prompt chaining stems from its capacity to decompose complex coding tasks into a series of manageable sub-problems. This modular structure reduces the operational complexity for the large language model at each step. Critically, this approach also allows for the insertion of deterministic logic between model calls, enabling intermediate data processing, output validation, and conditional branching within the workflow. By this method, a single, multifaceted request that could otherwise lead to unreliable or incomplete results is converted into a structured sequence of operations managed by an underlying execution framework.
在人工智能辅助软件开发等应用中，提示链的实用性源于其能够将复杂的编码任务分解为一系列可管理的子问题。这种模块化结构降低了大型语言模型每一步的操作复杂性。至关重要的是，这种方法还允许在模型调用之间插入确定性逻辑，从而支持工作流中的中间数据处理、输出验证和条件分支。通过这种方法，原本可能导致不可靠或不完整结果的单一、多方面请求将被转换为由底层执行框架管理的结构化操作序列。

7. Multimodal and multi-step reasoning: Analyzing datasets with diverse modalities necessitates breaking down the problem into smaller, prompt-based tasks. For example, interpreting an image that contains a picture with embedded text, labels highlighting specific text segments, and tabular data explaining each label, requires such an approach.
 多模式和多步骤推理： 分析具有多种模式的数据集需要将问题分解为更小的、基于提示的任务。   例如，解释包含嵌入文本的图片、突出显示特定文本段的标签以及解释每个标签的表格数据的图像需要这种方法。

- Prompt 1: Extract and comprehend the text from the user's image request.
提示 1：从用户的图像请求中提取并理解文本。

- Prompt 2: Link the extracted image text with its corresponding labels.
提示 2：将提取的图像文本与其对应的标签链接起来。

- Prompt 3: Interpret the gathered information using a table to determine the required output.
提示 3：使用表格解释收集到的信息以确定所需的输出 。


## Hands-On Code Example  实际操作代码示例
Implementing prompt chaining ranges from direct, sequential function calls within a script to the utilization of specialized frameworks designed to manage control flow, state, and component integration. Frameworks such as LangChain, LangGraph, Crew AI, and the Google Agent Development Kit (ADK) offer structured environments for constructing and executing these multi-step processes, which is particularly advantageous for complex architectures.
实现即时链接的方式多种多样，从脚本中的直接顺序函数调用，到利用专门用于管理控制流、状态和组件集成的框架。诸如 LangChain、LangGraph、Crew AI 和 Google Agent Development Kit (ADK) 之类的框架提供了用于构建和执行这些多步骤流程的结构化环境，这对于复杂的架构尤其有利。

For the purpose of demonstration, LangChain and LangGraph are suitable choices as their core APIs are explicitly designed for composing chains and graphs of operations. LangChain provides foundational abstractions for linear sequences, while LangGraph extends these capabilities to support stateful and cyclical computations, which are necessary for implementing more sophisticated agentic behaviors. This example will focus on a fundamental linear sequence.
为了演示的目的，LangChain 和 LangGraph 是合适的选择，因为它们的核心 API 是专门为组合操作链和操作图而设计的。LangChain 提供了线性序列的基础抽象，而 LangGraph 扩展了这些功能以支持状态计算和循环计算，这对于实现更复杂的代理行为至关重要。本示例将重点介绍一个基本的线性序列。

The following code implements a two-step prompt chain that functions as a data processing pipeline. The initial stage is designed to parse unstructured text and extract specific information. The subsequent stage then receives this extracted output and transforms it into a structured data format.
以下代码实现了一个两步提示链，它充当数据处理管道。初始阶段旨在解析非结构化文本并提取特定信息。后续阶段接收提取的输出并将其转换为结构化数据格式。

To replicate this procedure, the required libraries must first be installed. This can be accomplished using the following command:
要复制此过程，必须首先安装所需的库。可以使用以下命令完成此操作：

```bash 
pip install langchain langchain-community langchain-openai langgraph
```

Note that langchain-openai can be substituted with the appropriate package for a different model provider. Subsequently, the execution environment must be configured with the necessary API credentials for the selected language model provider, such as OpenAI, Google Gemini, or Anthropic.
请注意，langchain-openai 可以用其他模型提供商的相应包替换。随后，必须为执行环境配置所选语言模型提供商（例如 OpenAI、Google Gemini 或 Anthropic）所需的 API 凭据。

```python
import os  

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# For better security, load environment variables from a .env file
# from dotenv import load_dotenv
# load_dotenv()

# Make sure your OPENAI_API_KEY is set in the .env file
# Initialize the Language Model (using ChatOpenAI is recommended)

llm = ChatOpenAI(temperature=0)

# --- Prompt 1: Extract Information ---
prompt_extract = ChatPromptTemplate.from_template(
   "Extract the technical specifications from the following text:\n\n{text_input}"

)

# --- Prompt 2: Transform to JSON ---
prompt_transform = ChatPromptTemplate.from_template(
   "Transform the following specifications into a JSON object with 'cpu', 'memory', and 'storage' as keys:\n\n{specifications}"
)


# --- Build the Chain using LCEL ---
# The StrOutputParser() converts the LLM's message output to a simple string.

extraction_chain = prompt_extract | llm | StrOutputParser()
# The full chain passes the output of the extraction chain into the 'specifications'
# variable for the transformation prompt.
full_chain = (
   {"specifications": extraction_chain}
   | prompt_transform
   | llm
   | StrOutputParser()
)


# --- Run the Chain ---
input_text = "The new laptop model features a 3.5 GHz octa-core processor, 16GB of RAM, and a 1TB NVMe SSD."


# Execute the chain with the input text dictionary.
final_result = full_chain.invoke({"text_input": input_text})
print("\n--- Final JSON Output ---")
print(final_result)
```

This Python code demonstrates how to use the LangChain library to process text. It utilizes two separate prompts: one to extract technical specifications from an input string and another to format these specifications into a JSON object. The ChatOpenAI model is employed for language model interactions, and the StrOutputParser ensures the output is in a usable string format. The LangChain Expression Language (LCEL) is used to elegantly chain these prompts and the language model together. The first chain, extraction_chain, extracts the specifications. The full_chain then takes the output of the extraction and uses it as input for the transformation prompt. A sample input text describing a laptop is provided. The full_chain is invoked with this text, processing it through both steps. The final result, a JSON string containing the extracted and formatted specifications, is then printed.
这段 Python 代码演示了如何使用 LangChain 库处理文本。它使用两个独立的提示：一个从输入字符串中提取技术规范，另一个将这些规范格式化为 JSON 对象。ChatOpenAI 模型用于语言模型交互，StrOutputParser 确保输出为可用的字符串格式。LangChain 表达式语言 (LCEL) 用于优雅地将这些提示和语言模型链接在一起。第一个链 Extraction_chain 用于提取规范。然后，full_chain 获取提取的输出并将其用作转换提示的输入。提供了一个描述笔记本电脑的示例输入文本。full_chain 使用此文本调用，并通过两个步骤对其进行处理。最终结果是一个包含提取和格式化规范的 JSON 字符串，并被打印出来。


## Context Engineering and Prompt Engineering
情境工程和提示工程
Context Engineering (see Fig.1) is the systematic discipline of designing, constructing, and delivering a complete informational environment to an AI model prior to token generation. This methodology asserts that the quality of a model's output is less dependent on the model's architecture itself and more on the richness of the context provided.
情境工程（见图 1）是一门系统性学科，在生成令牌之前，设计、构建并向 AI 模型提供完整的信息环境。该方法论认为，模型输出的质量较少依赖于模型架构本身，而更多地取决于所提供情境的丰富性。



Fig.1: Context Engineering is the discipline of building a rich, comprehensive informational environment for an AI, as the quality of this context is a primary factor in enabling advanced Agentic performance.
图 1：   情境工程是一门为人工智能构建丰富、全面的信息环境的学科，因为这种情境的质量是实现高级代理性能的主要因素。

It represents a significant evolution from traditional prompt engineering, which focuses primarily on optimizing the phrasing of a user's immediate query. Context Engineering expands this scope to include several layers of information, such as the system prompt, which is a foundational set of instructions defining the AI's operational parameters—for instance, "You are a technical writer; your tone must be formal and precise." The context is further enriched with external data. This includes retrieved documents, where the AI actively fetches information from a knowledge base to inform its response, such as pulling technical specifications for a project. It also incorporates tool outputs, which are the results from the AI using an external API to obtain real-time data, like querying a calendar to determine a user's availability. This explicit data is combined with critical implicit data, such as user identity, interaction history, and environmental state. The core principle is that even advanced models underperform when provided with a limited or poorly constructed view of the operational environment.
它代表了传统提示工程的重大进化，传统提示工程主要侧重于优化用户即时查询的措辞。情境工程扩展了这一范围，涵盖了多个信息层，例如系统提示 ，它是一组定义 AI 操作参数的基础指令——例如， “您是一名技术作家；您的语气必须正式且准确。” 情境工程通过外部数据进一步丰富。这包括检索到的文档，AI 会主动从知识库中获取信息以指导其响应，例如提取项目的技术规范。它还包含工具输出，这些输出是 AI 使用外部 API 获取实时数据的结果，例如查询日历以确定用户的可用性。这些显式数据与关键的隐式数据（例如用户身份、交互历史记录和环境状态）相结合。其核心原则是，即使是先进的模型，如果提供的是对操作环境的有限或构建不良的视图，其性能也会不佳。

This practice, therefore, reframes the task from merely answering a question to building a comprehensive operational picture for the agent. For example, a context-engineered agent would not just respond to a query but would first integrate the user's calendar availability (a tool output), the professional relationship with an email's recipient (implicit data), and notes from previous meetings (retrieved documents). This allows the model to generate outputs that are highly relevant, personalized, and pragmatically useful. The "engineering" component involves creating robust pipelines to fetch and transform this data at runtime and establishing feedback loops to continually improve context quality.
因此，这种做法将任务从单纯的回答问题重新定义为为代理构建全面的操作图景。例如，情境工程代理不仅会响应查询，还会首先整合用户的日历空闲时间（工具输出）、与电子邮件收件人的职业关系（隐式数据）以及之前会议的记录（检索到的文档）。这使得模型能够生成高度相关、个性化且实用的输出。“工程”部分包括创建强大的管道以在运行时获取和转换这些数据，并建立反馈循环以持续提升情境质量。

To implement this, specialized tuning systems can be used to automate the improvement process at scale. For example, tools like Google's Vertex AI prompt optimizer can enhance model performance by systematically evaluating responses against a set of sample inputs and predefined evaluation metrics. This approach is effective for adapting prompts and system instructions across different models without requiring extensive manual rewriting. By providing such an optimizer with sample prompts, system instructions, and a template, it can programmatically refine the contextual inputs, offering a structured method for implementing the feedback loops required for sophisticated Context Engineering.
为了实现这一点，可以使用专门的调优系统来大规模自动化改进过程。例如，像谷歌 Vertex AI 提示优化器这样的工具，可以通过系统地评估针对一组样本输入和预定义评估指标的响应来提升模型性能。这种方法可以有效地在不同模型之间调整提示和系统指令，而无需大量的手动重写。通过为此类优化器提供样本提示、系统指令和模板，它可以以编程方式优化上下文输入，从而提供一种结构化的方法来实现复杂的上下文工程所需的反馈循环。

This structured approach is what differentiates a rudimentary AI tool from a more sophisticated and contextually-aware system. It treats the context itself as a primary component, placing critical importance on what the agent knows, when it knows it, and how it uses that information. The practice ensures the model has a well-rounded understanding of the user's intent, history, and current environment. Ultimately, Context Engineering is a crucial methodology for advancing stateless chatbots into highly capable, situationally-aware systems.
这种结构化方法正是区分基础人工智能工具与更复杂、更具备情境感知能力的系统的关键所在。它将情境本身视为主要组成部分，并高度重视代理了解的内容、何时了解以及如何使用这些信息。这种做法确保模型能够全面理解用户的意图、历史记录和当前环境。最终，情境工程是将无状态聊天机器人发展为功能强大、情境感知系统的关键方法。

## At a Glance  概览
What: Complex tasks often overwhelm LLMs when handled within a single prompt, leading to significant performance issues. The cognitive load on the model increases the likelihood of errors such as overlooking instructions, losing context, and generating incorrect information. A monolithic prompt struggles to manage multiple constraints and sequential reasoning steps effectively. This results in unreliable and inaccurate outputs, as the LLM fails to address all facets of the multifaceted request.
问题： 复杂的任务在单一提示中处理时，往往会让法学硕士 (LLM) 不堪重负，从而导致严重的性能问题。模型的认知负荷会增加出错的可能性，例如忽略指令、丢失上下文以及生成错误信息。单一的提示难以有效地管理多个约束和顺序推理步骤。这会导致输出不可靠且不准确，因为法学硕士 (LLM) 无法涵盖多方面请求的所有方面。

Why: Prompt chaining provides a standardized solution by breaking down a complex problem into a sequence of smaller, interconnected sub-tasks. Each step in the chain uses a focused prompt to perform a specific operation, significantly improving reliability and control. The output from one prompt is passed as the input to the next, creating a logical workflow that progressively builds towards the final solution. This modular, divide-and-conquer strategy makes the process more manageable, easier to debug, and allows for the integration of external tools or structured data formats between steps. This pattern is foundational for developing sophisticated, multi-step Agentic systems that can plan, reason, and execute complex workflows.
原因： 提示链通过将复杂问题分解为一系列相互关联的小任务，提供标准化解决方案。链中的每一步都使用一个集中的提示来执行特定操作，从而显著提高可靠性和控制力。一个提示的输出将作为下一个提示的输入，从而创建一个逻辑工作流，逐步构建最终解决方案。这种模块化、分而治之的策略使流程更易于管理、更易于调试，并允许在步骤之间集成外部工具或结构化数据格式。此模式是开发能够规划、推理和执行复杂工作流的复杂多步骤 Agentic 系统的基础。

Rule of thumb: Use this pattern when a task is too complex for a single prompt, involves multiple distinct processing stages, requires interaction with external tools between steps, or when building Agentic systems that need to perform multi-step reasoning and maintain state.
经验法则： 当任务对于单个提示来说太复杂、涉及多个不同的处理阶段、需要在步骤之间与外部工具进行交互，或者在构建需要执行多步骤推理和维持状态的 Agentic 系统时，使用此模式。

### Visual summary
视觉摘要



Fig. 2: Prompt Chaining Pattern: Agents receive a series of prompts from the user, with the output of each agent serving as the input for the next in the chain.
图 2：提示链模式： 代理从用户接收一系列提示，每个代理的输出作为链中下一个代理的输入。

## Key Takeaways  关键要点
Here are some key takeaways:
以下是一些关键要点：

- Prompt Chaining breaks down complex tasks into a sequence of smaller, focused steps. This is occasionally known as the Pipeline pattern.
  提示链将复杂的任务分解成一系列更小、更集中的步骤。 这有时被称为流水线模式。
- Each step in a chain involves an LLM call or processing logic, using the output of the previous step as input.
  链中的每一步都涉及 LLM 调用或处理逻辑，使用上一步的输出作为输入。
- This pattern improves the reliability and manageability of complex interactions with language models.
  这种模式提高了与语言模型的复杂交互的可靠性和可管理性。
- Frameworks like LangChain/LangGraph, and Google ADK  provide robust tools to define, manage, and execute these multi-step sequences.
LangChain/LangGraph 和 Google ADK 等框架提供了强大的工具来定义、管理和执行这些多步骤序列。

## Conclusion  结论
By deconstructing complex problems into a sequence of simpler, more manageable sub-tasks, prompt chaining provides a robust framework for guiding large language models. This "divide-and-conquer" strategy significantly enhances the reliability and control of the output by focusing the model on one specific operation at a time. As a foundational pattern, it enables the development of sophisticated AI agents capable of multi-step reasoning, tool integration, and state management. Ultimately, mastering prompt chaining is crucial for building robust, context-aware systems that can execute intricate workflows well beyond the capabilities of a single prompt.
通过将复杂问题分解为一系列更简单、更易于管理的子任务，提示链提供了一个用于指导大型语言模型的强大框架。这种“分而治之”的策略通过使模型每次专注于一项特定操作，显著提升了输出的可靠性和控制力。作为一种基础模式，它能够开发出能够进行多步推理、工具集成和状态管理的复杂 AI 代理。最终，掌握提示链对于构建强大的上下文感知系统至关重要，这些系统能够执行远远超出单个提示能力的复杂工作流程。

## References

1.  LangChain Documentation on LCEL : [https://python.langchain.com/v0.2/docs/core\_modules/expression\_language/](https://www.google.com/url?q=https://python.langchain.com/v0.2/docs/core_modules/expression_language/&sa=D&source=editors&ust=1760629338985831&usg=AOvVaw0rx-cKS4jxZjxe4CuZORpK)   
2.  LangGraph Documentation: [https://langchain-ai.github.io/langgraph/](https://www.google.com/url?q=https://langchain-ai.github.io/langgraph/&sa=D&source=editors&ust=1760629338986254&usg=AOvVaw0nycvPJlAqeoqJNJ4BZnx6)
3.  Prompt Engineering Guide - Chaining Prompts: [https://www.promptingguide.ai/techniques/chaining](https://www.google.com/url?q=https://www.promptingguide.ai/techniques/chaining&sa=D&source=editors&ust=1760629338986632&usg=AOvVaw1sVEOXn9U_nA3QAUlCuBFk)  
4.  OpenAI API Documentation (General Prompting Concepts): [https://platform.openai.com/docs/guides/gpt/prompting](https://www.google.com/url?q=https://platform.openai.com/docs/guides/gpt/prompting&sa=D&source=editors&ust=1760629338987080&usg=AOvVaw1XPRc9BjPiWvX3GsCWVjp1) 
5.  Crew AI Documentation (Tasks and Processes): [https://docs.crewai.com/](https://www.google.com/url?q=https://docs.crewai.com/&sa=D&source=editors&ust=1760629338987396&usg=AOvVaw0M3Zw_ziwYH_kPjJ9P3VPx)  
6.  Google AI for Developers (Prompting Guides): [https://cloud.google.com/discover/what-is-prompt-engineering?hl=en](https://www.google.com/url?q=https://cloud.google.com/discover/what-is-prompt-engineering?hl%3Den&sa=D&source=editors&ust=1760629338987846&usg=AOvVaw3iENYXkWnLtARreC_s6vrq) 
7.  Vertex Prompt Optimizer [https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-optimizer](https://www.google.com/url?q=https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-optimizer&sa=D&source=editors&ust=1760629338988256&usg=AOvVaw3VJwIaaG3jSipUVd_y0y1L)