# Appendix A: Advanced Prompting Techniques
# 附录 A：高级提示技术

# Introduction to Prompting
# 提示技术导论

Prompting is the art and science of communicating with large language models (LLMs) to elicit desired responses. It involves crafting input instructions that guide the model's behavior, understanding, and output generation. As AI technologies evolve, prompting has emerged as a critical skill for effectively leveraging the capabilities of advanced AI systems.
提示是与大型语言模型（LLM）进行交流以引发期望响应的艺术和科学。它涉及制定引导模型行为、理解和输出生成的输入指令。随着人工智能技术的发展，提示已成为有效利用先进人工智能系统能力的关键技能。

The complexity of prompting goes far beyond simply typing a question or command. It requires a nuanced understanding of how language models process and generate text, their strengths and limitations, and the intricate ways in which different prompt structures can dramatically influence the model's performance.
提示的复杂性远远超出简单地输入问题或命令。它需要对语言模型如何处理和生成文本、它们的优势和局限性，以及不同提示结构如何显著影响模型性能的细微理解。

# Core Prompting Principles
# 核心提示原则

Effective prompting is grounded in several fundamental principles that help maximize the potential of language models:
有效的提示基于几个基本原则，这些原则有助于最大化语言模型的潜力：

1. **Clarity and Specificity**: The more precise and unambiguous your instructions, the more likely the model will generate the desired output.
1. **清晰和具体性**：指令越精确和明确，模型生成期望输出的可能性就越高。

2. **Context Provision**: Providing relevant background information helps the model understand the task's nuances and constraints.
2. **上下文提供**：提供相关的背景信息有助于模型理解任务的细微差别和约束。

3. **Role Definition**: Explicitly defining the role or persona the model should adopt can significantly shape its response style and approach.
3. **角色定义**：明确定义模型应该采用的角色或人物可以显著塑造其响应风格和方法。

4. **Iterative Refinement**: Prompting is an iterative process. Initial responses can be improved through careful rephrasing and additional context.
4. **迭代改进**：提示是一个迭代过程。通过仔细重新表述和添加上下文，可以改进初始响应。

5. **Understanding Model Limitations**: Recognize that while powerful, language models have inherent limitations and can produce incorrect or biased information.
5. **理解模型局限性**：认识到尽管强大，语言模型仍有固有的局限性，可能产生不正确或有偏见的信息。

# Basic Prompting Techniques
# 基本提示技术

Building on core principles, foundational techniques provide language models with varying levels of information or examples to direct their responses. These methods serve as an initial phase in prompt engineering and are effective for a wide spectrum of applications.
基于核心原则，基础技术为语言模型提供不同程度的信息或示例，以引导其响应。这些方法是提示工程的初始阶段，并且对广泛的应用场景都有效。

## Zero-Shot Prompting 
## 零样本提示

Zero-shot prompting is the most basic form of prompting, where the language model is provided with an instruction and input data without any examples of the desired input-output pair. It relies entirely on the model's pre-training to understand the task and generate a relevant response. Essentially, a zero-shot prompt consists of a task description and initial text to begin the process.
零样本提示是最基本的提示形式，在这种方式中，语言模型被提供指令和输入数据，但没有任何期望的输入-输出对示例。它完全依赖模型的预训练来理解任务并生成相关响应。本质上，零样本提示由任务描述和初始文本组成，以启动处理过程。

* **When to use:** Zero-shot prompting is often sufficient for tasks that the model has likely encountered extensively during its training, such as simple question answering, text completion, or basic summarization of straightforward text. It's the quickest approach to try first.  
* **何时使用：** 零样本提示通常适用于模型在训练期间可能广泛遇到的任务，如简单的问答、文本补全或直接文本的基本摘要。这是首先尝试的最快方法。

* **Example:**  
  Translate the following English sentence to French: 'Hello, how are you?'
* **示例：**
  将以下英语句子翻译成法语：'Hello, how are you?'

## One-Shot Prompting
## 单样本提示

One-shot prompting involves providing the language model with a single example of the input and the corresponding desired output prior to presenting the actual task. This method serves as an initial demonstration to illustrate the pattern the model is expected to replicate. The purpose is to equip the model with a concrete instance that it can use as a template to effectively execute the given task.
单样本提示涉及在提出实际任务之前，向语言模型提供单个输入示例及其对应的期望输出。这种方法作为初始演示，说明模型预期复制的模式。目的是为模型提供一个具体实例，它可以将其用作模板来有效执行给定任务。

* **When to use:** One-shot prompting is useful when the desired output format or style is specific or less common. It gives the model a concrete instance to learn from. It can improve performance compared to zero-shot for tasks requiring a particular structure or tone.  
* **何时使用：** 当期望的输出格式或风格特定或不太常见时，单样本提示很有用。它为模型提供了一个具体的学习实例。对于需要特定结构或语气的任务，它可以比零样本提示提高性能。

* **Example:**  
  Translate the following English sentences to Spanish:  
  English: 'Thank you.'  
  Spanish: 'Gracias.'

  English: 'Please.'  
  Spanish:
* **示例：**
  将以下英语句子翻译成西班牙语：
  英语：'Thank you.'
  西班牙语：'Gracias.'

  英语：'Please.'
  西班牙语：

## Few-Shot Prompting 
## 少样本提示

Few-shot prompting enhances one-shot prompting by supplying several examples, typically three to five, of input-output pairs. This aims to demonstrate a clearer pattern of expected responses, improving the likelihood that the model will replicate this pattern for new inputs. This method provides multiple examples to guide the model to follow a specific output pattern.
少样本提示通过提供多个示例（通常是三到五个）输入-输出对来增强单样本提示。这旨在展示期望响应的更清晰模式，提高模型为新输入复制此模式的可能性。这种方法提供多个示例，引导模型遵循特定的输出模式。

* **When to use:** Few-shot prompting is particularly effective for tasks where the desired output requires adhering to a specific format, style, or exhibiting nuanced variations. It's excellent for tasks like classification, data extraction with specific schemas, or generating text in a particular style, especially when zero-shot or one-shot don't yield consistent results. Using at least three to five examples is a general rule of thumb, adjusting based on task complexity and model token limits.  
* **何时使用：** 少样本提示对于期望输出需要遵循特定格式、风格或展示细微变化的任务特别有效。它非常适合分类、使用特定模式的数据提取或以特定风格生成文本等任务，尤其是在零样本或单样本无法产生一致结果的情况下。使用至少三到五个示例是一般经验法则，根据任务复杂性和模型标记限制进行调整。

* **Importance of Example Quality and Diversity:** The effectiveness of few-shot prompting heavily relies on the quality and diversity of the examples provided. Examples should be accurate, representative of the task, and cover potential variations or edge cases the model might encounter. High-quality, well-written examples are crucial; even a small mistake can confuse the model and result in undesired output. Including diverse examples helps the model generalize better to unseen inputs.  
* **示例质量和多样性的重要性：** 少样本提示的有效性高度依赖于所提供示例的质量和多样性。示例应该准确、具有代表性，并涵盖模型可能遇到的潜在变化或边缘情况。高质量、精心编写的示例至关重要；即使是小小的错误也可能使模型混淆并导致不期望的输出。包含多样的示例有助于模型更好地泛化到未见过的输入。

* **Mixing Up Classes in Classification Examples:** When using few-shot prompting for classification tasks (where the model needs to categorize input into predefined classes), it's a best practice to mix up the order of the examples from different classes. This prevents the model from potentially overfitting to the specific sequence of examples and ensures it learns to identify the key features of each class independently, leading to more robust and generalizable performance on unseen data.  
* **分类示例中混合类别：** 在使用少样本提示进行分类任务（模型需要将输入分类到预定义类别）时，最佳实践是混合来自不同类别的示例顺序。这可以防止模型可能过度拟合到特定示例序列，并确保它独立地学习识别每个类别的关键特征，从而在未见过的数据上实现更强大和更具泛化性的性能。

* **Evolution to "Many-Shot" Learning:** As modern LLMs like Gemini get stronger with long context modeling, they are becoming highly effective at utilizing "many-shot" learning. This means optimal performance for complex tasks can now be achieved by including a much larger number of examples—sometimes even hundreds—directly within the prompt, allowing the model to learn more intricate patterns.  
* **演变为"多样本"学习：** 随着 Gemini 等现代大语言模型在长上下文建模方面变得更强，它们在利用"多样本"学习方面变得非常有效。这意味着对于复杂任务，现在可以通过直接在提示中包含大量示例（有时甚至是数百个）来实现最佳性能，使模型能够学习更复杂的模式。

* **Example:**  
  Classify the sentiment of the following movie reviews as POSITIVE, NEUTRAL, or NEGATIVE:

  Review: "The acting was superb and the story was engaging."  
  Sentiment: POSITIVE

  Review: "It was okay, nothing special."  
  Sentiment: NEUTRAL

  Review: "I found the plot confusing and the characters unlikable."  
  Sentiment: NEGATIVE

  Review: "The visuals were stunning, but the dialogue was weak."  
  Sentiment:
* **示例：**
  将以下电影评论的情感分类为正面（POSITIVE）、中性（NEUTRAL）或负面（NEGATIVE）：

  评论："The acting was superb and the story was engaging."
  情感：正面（POSITIVE）

  评论："It was okay, nothing special."
  情感：中性（NEUTRAL）

  评论："I found the plot confusing and the characters unlikable."
  情感：负面（NEGATIVE）

  评论："The visuals were stunning, but the dialogue was weak."
  情感：

Understanding when to apply zero-shot, one-shot, and few-shot prompting techniques, and thoughtfully crafting and organizing examples, are essential for enhancing the effectiveness of agentic systems. These basic methods serve as the groundwork for various prompting strategies.
了解何时应用零样本、单样本和少样本提示技术，并细心地制作和组织示例，对于增强代理系统的有效性至关重要。这些基本方法为各种提示策略奠定了基础。

# Structuring Prompts
# 构建提示

Beyond the basic techniques of providing examples, the way you structure your prompt plays a critical role in guiding the language model. Structuring involves using different sections or elements within the prompt to provide distinct types of information, such as instructions, context, or examples, in a clear and organized manner. This helps the model parse the prompt correctly and understand the specific role of each piece of text.
除了提供示例的基本技术，您构建提示的方式对引导语言模型起着关键作用。构建涉及在提示中使用不同的部分或元素，以清晰和有组织的方式提供不同类型的信息，如指令、上下文或示例。这有助于模型正确解析提示，并理解每段文本的具体角色。

## System Prompting
## 系统提示

System prompting sets the overall context and purpose for a language model, defining its intended behavior for an interaction or session. This involves providing instructions or background information that establish rules, a persona, or overall behavior. Unlike specific user queries, a system prompt provides foundational guidelines for the model's responses. It influences the model's tone, style, and general approach throughout the interaction. For example, a system prompt can instruct the model to consistently respond concisely and helpfully or ensure responses are appropriate for a general audience. System prompts are also utilized for safety and toxicity control by including guidelines such as maintaining respectful language.
系统提示为语言模型设置整体上下文和目的，定义其在交互或会话中的预期行为。这涉及提供建立规则、角色或整体行为的指令或背景信息。与特定用户查询不同，系统提示为模型的响应提供基础性指南。它影响模型在整个交互过程中的语气、风格和总体方法。例如，系统提示可以指示模型始终简洁且有帮助地响应，或确保响应适合普通受众。系统提示还通过包含诸如保持尊重性语言等准则来用于安全性和有害性控制。

Furthermore, to maximize their effectiveness, system prompts can undergo automatic prompt optimization through LLM-based iterative refinement. Services like the Vertex AI Prompt Optimizer facilitate this by systematically improving prompts based on user-defined metrics and target data, ensuring the highest possible performance for a given task.
此外，为了最大化其有效性，系统提示可以通过基于大语言模型的迭代优化进行自动优化。像 Vertex AI 提示优化器这样的服务通过根据用户定义的指标和目标数据系统地改进提示，确保给定任务的最高可能性能。

* **Example:**  
  You are a helpful and harmless AI assistant. Respond to all queries in a polite and informative manner. Do not generate content that is harmful, biased, or inappropriate
* **示例：**
  你是一个有帮助且无害的人工智能助手。以礼貌和信息丰富的方式回答所有查询。不要生成有害、有偏见或不恰当的内容

## Role Prompting
## 角色提示

Role prompting assigns a specific character, persona, or identity to the language model, often in conjunction with system or contextual prompting. This involves instructing the model to adopt the knowledge, tone, and communication style associated with that role. For example, prompts such as "Act as a travel guide" or "You are an expert data analyst" guide the model to reflect the perspective and expertise of that assigned role. Defining a role provides a framework for the tone, style, and focused expertise, aiming to enhance the quality and relevance of the output. The desired style within the role can also be specified, for instance, "a humorous and inspirational style."
角色提示为语言模型分配特定的角色、人物或身份，通常与系统或上下文提示结合使用。这涉及指示模型采用与该角色相关的知识、语气和交流风格。例如，诸如"扮演旅游导游"或"你是一位专家数据分析师"的提示引导模型反映所分配角色的视角和专业知识。定义角色为语气、风格和专注的专业知识提供框架，旨在提高输出的质量和相关性。还可以指定角色内的期望风格，例如"幽默且鼓舞人心的风格"。

* **Example:**  
  Act as a seasoned travel blogger. Write a short, engaging paragraph about the best hidden gem in Rome.
* **示例：**
  扮演一位经验丰富的旅游博主。写一段简短且引人入胜的段落，介绍罗马最好的隐藏宝石。

## Using Delimiters 
## 使用分隔符

Effective prompting involves clear distinction of instructions, context, examples, and input for language models. Delimiters, such as triple backticks (\`\`\`), XML tags (\<instruction\>, \<context\>), or markers (---), can be utilized to visually and programmatically separate these sections. This practice, widely used in prompt engineering, minimizes misinterpretation by the model, ensuring clarity regarding the role of each part of the prompt.
有效的提示涉及为语言模型清晰区分指令、上下文、示例和输入。分隔符，如三重反引号（\`\`\`）、XML标签（\<instruction\>，\<context\>）或标记（---），可用于直观和程序化地分隔这些部分。这种在提示工程中广泛使用的做法最大限度地减少了模型的误解，确保提示每个部分的角色清晰。

* **Example:**  
  \<instruction\>Summarize the following article, focusing on the main arguments presented by the author.\</instruction\>  
  \<article\>  
  \[Insert the full text of the article here\]  
  \</article\>
* **示例：**
  \<instruction\>总结以下文章，重点关注作者提出的主要论点。\</instruction\>
  \<article\>
  \[在此处插入文章全文\]
  \</article\>

# Contextual Engineering
# 上下文工程

Context engineering, unlike static system prompts, dynamically provides background information crucial for tasks and conversations. This ever-changing information helps models grasp nuances, recall past interactions, and integrate relevant details, leading to grounded responses and smoother exchanges. Examples include previous dialogue, relevant documents (as in Retrieval Augmented Generation), or specific operational parameters. For instance, when discussing a trip to Japan, one might ask for three family-friendly activities in Tokyo, leveraging the existing conversational context. In agentic systems, context engineering is fundamental to core agent behaviors like memory persistence, decision-making, and coordination across sub-tasks. Agents with dynamic contextual pipelines can sustain goals over time, adapt strategies, and collaborate seamlessly with other agents or tools—qualities essential for long-term autonomy. This methodology posits that the quality of a model's output depends more on the richness of the provided context than on the model's architecture. It signifies a significant evolution from traditional prompt engineering, which primarily focused on optimizing the phrasing of immediate user queries. Context engineering expands its scope to include multiple layers of information.
上下文工程与静态系统提示不同，动态地提供对任务和对话至关重要的背景信息。这种不断变化的信息帮助模型把握细微差别，回忆过去的交互，并整合相关细节，从而产生接地气的响应和更流畅的交流。示例包括先前的对话、相关文档（如检索增强生成中），或特定的操作参数。例如，在讨论日本之旅时，可以利用现有的对话上下文询问东京的三个适合家庭的活动。在代理系统中，上下文工程对记忆持久性、决策和跨子任务协调等核心代理行为至关重要。具有动态上下文管道的代理可以随时间维持目标、调整策略，并与其他代理或工具无缝协作——这些品质对长期自主性至关重要。这种方法论认为，模型输出的质量更多地取决于所提供上下文的丰富性，而非模型的架构。它标志着从传统提示工程（主要关注优化即时用户查询的措辞）的显著演变。上下文工程将其范围扩展到包括多层信息。

These layers include:
这些层包括：

* **System prompts:** Foundational instructions that define the AI's operational parameters (e.g., "You are a technical writer; your tone must be formal and precise").  
* **系统提示：** 定义人工智能操作参数的基础性指令（例如，"你是一个技术写作者；你的语气必须正式且精确"）。

* **External data:**  
  * **Retrieved documents:** Information actively fetched from a knowledge base to inform responses (e.g., pulling technical specifications).  
  * **Tool outputs:** Results from the AI using an external API for real-time data (e.g., querying a calendar for availability).  
* **外部数据：**
  * **检索文档：** 从知识库主动获取的信息，用于指导响应（例如，提取技术规格）。
  * **工具输出：** 人工智能使用外部 API 获取实时数据的结果（例如，查询日历的可用性）。

* **Implicit data:** Critical information such as user identity, interaction history, and environmental state. Incorporating implicit context presents challenges related to privacy and ethical data management. Therefore, robust governance is essential for context engineering, especially in sectors like enterprise, healthcare, and finance.
* **隐式数据：** 用户身份、交互历史和环境状态等关键信息。整合隐式上下文带来与隐私和伦理数据管理相关的挑战。因此，对于企业、医疗和金融等行业，上下文工程需要强大的治理。

The core principle is that even advanced models underperform with a limited or poorly constructed view of their operational environment. This practice reframes the task from merely answering a question to building a comprehensive operational picture for the agent. For example, a context-engineered agent would integrate a user's calendar availability (tool output), the professional relationship with an email recipient (implicit data), and notes from previous meetings (retrieved documents) before responding to a query. This enables the model to generate highly relevant, personalized, and pragmatically useful outputs. The "engineering" aspect involves creating robust pipelines to fetch and transform this data at runtime and establishing feedback loops to continually improve context quality.
核心原则是，即使是先进的模型，在对其运行环境的视角有限或构建不佳的情况下也会表现不佳。这种做法将任务从仅仅回答问题重新定义为为代理构建全面的运行图景。例如，一个经过上下文工程的代理在响应查询之前，会整合用户的日历可用性（工具输出）、与电子邮件收件人的专业关系（隐式数据）以及先前会议的笔记（检索文档）。这使模型能够生成高度相关、个性化和实用的输出。"工程"方面涉及创建强大的管道，在运行时获取和转换这些数据，并建立反馈循环以持续改进上下文质量。

To implement this, specialized tuning systems, such as Google's Vertex AI prompt optimizer, can automate the improvement process at scale. By systematically evaluating responses against sample inputs and predefined metrics, these tools can enhance model performance and adapt prompts and system instructions across different models without extensive manual rewriting. Providing an optimizer with sample prompts, system instructions, and a template allows it to programmatically refine contextual inputs, offering a structured method for implementing the necessary feedback loops for sophisticated Context Engineering.  
为了实现这一点，像 Google 的 Vertex AI 提示优化器这样的专门调优系统可以大规模自动化改进过程。通过系统地根据样本输入和预定义指标评估响应，这些工具可以增强模型性能，并在不需要大量手动重写的情况下调整不同模型的提示和系统指令。向优化器提供样本提示、系统指令和模板，使其能够以编程方式优化上下文输入，为实施复杂上下文工程所需的反馈循环提供一种结构化的方法。

This structured approach differentiates a rudimentary AI tool from a more sophisticated, contextually-aware system. It treats context as a primary component, emphasizing what the agent knows, when it knows it, and how it uses that information. This practice ensures the model has a well-rounded understanding of the user's intent, history, and current environment. Ultimately, Context Engineering is a crucial methodology for transforming stateless chatbots into highly capable, situationally-aware systems.
这种结构化的方法将一个基本的人工智能工具与更复杂、具有上下文感知能力的系统区分开来。它将上下文视为主要组成部分，强调代理知道什么、何时知道，以及如何使用这些信息。这种做法确保模型对用户的意图、历史和当前环境有全面的理解。最终，上下文工程是将无状态聊天机器人转变为高度能力、具有情境感知能力的系统的关键方法。

# Structured Output
# 结构化输出

Often, the goal of prompting is not just to get a free-form text response, but to extract or generate information in a specific, machine-readable format. Requesting structured output, such as JSON, XML, CSV, or Markdown tables, is a crucial structuring technique. By explicitly asking for the output in a particular format and potentially providing a schema or example of the desired structure, you guide the model to organize its response in a way that can be easily parsed and used by other parts of your agentic system or application. Returning JSON objects for data extraction is beneficial as it forces the model to create a structure and can limit hallucinations. Experimenting with output formats is recommended, especially for non-creative tasks like extracting or categorizing data.
通常，提示的目标不仅仅是获得自由格式的文本响应，还要以特定的、机器可读的格式提取或生成信息。请求结构化输出，如 JSON、XML、CSV 或 Markdown 表格，是一种关键的结构化技术。通过明确要求以特定格式输出，并可能提供所需结构的模式或示例，你引导模型以可以被代理系统或应用程序的其他部分轻松解析和使用的方式组织其响应。对于数据提取返回 JSON 对象是有益的，因为它迫使模型创建一个结构，并可以限制幻觉。建议尝试不同的输出格式，尤其是对于提取或分类数据等非创造性任务。

* **Example:**  
  Extract the following information from the text below and return it as a JSON object with keys "name", "address", and "phone_number".

  Text: "Contact John Smith at 123 Main St, Anytown, CA or call (555) 123-4567."
* **示例：**
  从下面的文本中提取信息，并将其作为具有 "name"、"address" 和 "phone_number" 键的 JSON 对象返回。

  文本："联系 John Smith，地址：123 Main St, Anytown, CA，电话：(555) 123-4567。"

Effectively utilizing system prompts, role assignments, contextual information, delimiters, and structured output significantly enhances the clarity, control, and utility of interactions with language models, providing a strong foundation for developing reliable agentic systems. Requesting structured output is crucial for creating pipelines where the language model's output serves as the input for subsequent system or processing steps.
有效利用系统提示、角色分配、上下文信息、分隔符和结构化输出，显著提高了与语言模型交互的清晰度、控制力和实用性，为开发可靠的代理系统提供了坚实的基础。请求结构化输出对于创建管道至关重要，在这些管道中，语言模型的输出作为后续系统或处理步骤的输入。

**Leveraging Pydantic for an Object-Oriented Facade:** A powerful technique for enforcing structured output and enhancing interoperability is to use the LLM's generated data to populate instances of Pydantic objects. Pydantic is a Python library for data validation and settings management using Python type annotations. By defining a Pydantic model, you create a clear and enforceable schema for your desired data structure. This approach effectively provides an object-oriented facade to the prompt's output, transforming raw text or semi-structured data into validated, type-hinted Python objects.
**利用 Pydantic 创建面向对象的外观：** 一种强大的技术是使用大语言模型生成的数据填充 Pydantic 对象实例，以强制执行结构化输出并增强互操作性。Pydantic 是一个使用 Python 类型注解进行数据验证和设置管理的 Python 库。通过定义 Pydantic 模型，你为所需的数据结构创建一个清晰且可执行的模式。这种方法有效地为提示的输出提供了一个面向对象的外观，将原始文本或半结构化数据转换为经过验证的、带类型提示的 Python 对象。

You can directly parse a JSON string from an LLM into a Pydantic object using the model_validate_json method. This is particularly useful as it combines parsing and validation in a single step.
你可以使用 model_validate_json 方法直接将大语言模型生成的 JSON 字符串解析为 Pydantic 对象。这特别有用，因为它将解析和验证结合在一个步骤中。

```python
from pydantic import BaseModel, EmailStr, Field, ValidationError
from typing import List, Optional
from datetime import date

# --- Pydantic Model Definition (from above) ---
class User(BaseModel):
    name: str = Field(..., description="The full name of the user.")
    email: EmailStr = Field(..., description="The user's email address.")
    date_of_birth: Optional[date] = Field(None, description="The user's date of birth.")
    interests: List[str] = Field(default_factory=list, description="A list of the user's interests.")

# --- Hypothetical LLM Output ---
llm_output_json = """
{
    "name": "Alice Wonderland",
    "email": "alice.w@example.com",
    "date_of_birth": "1995-07-21",
    "interests": [
        "Natural Language Processing",
        "Python Programming",
        "Gardening"
    ]
}
"""

# --- Parsing and Validation ---
try:
    # Use the model_validate_json class method to parse the JSON string.
    # This single step parses the JSON and validates the data against the User model.
    user_object = User.model_validate_json(llm_output_json)
    
    # Now you can work with a clean, type-safe Python object.
    print("Successfully created User object!")
    print(f"Name: {user_object.name}")
    print(f"Email: {user_object.email}")
    print(f"Date of Birth: {user_object.date_of_birth}")
    print(f"First Interest: {user_object.interests[0]}")
    
    # You can access the data like any other Python object attribute.
    # Pydantic has already converted the 'date_of_birth' string to a datetime.date object.
    print(f"Type of date_of_birth: {type(user_object.date_of_birth)}")
except ValidationError as e:
    # If the JSON is malformed or the data doesn't match the model's types,
    # Pydantic will raise a ValidationError.
    print("Failed to validate JSON from LLM.")
    print(e)
```

For XML data, the xmltodict library can be used to convert the XML into a dictionary, which can then be passed to a Pydantic model for parsing. By using Field aliases in your Pydantic model, you can seamlessly map the often verbose or attribute-heavy structure of XML to your object's fields.
对于 XML 数据，可以使用 xmltodict 库将 XML 转换为字典，然后将其传递给 Pydantic 模型进行解析。通过在 Pydantic 模型中使用字段别名，你可以将通常冗长或属性繁重的 XML 结构无缝映射到对象的字段。

This methodology is invaluable for ensuring the interoperability of LLM-based components with other parts of a larger system. When an LLM's output is encapsulated within a Pydantic object, it can be reliably passed to other functions, APIs, or data processing pipelines with the assurance that the data conforms to the expected structure and types. This practice of "parse, don't validate" at the boundaries of your system components leads to more robust and maintainable applications.
这种方法对于确保基于大语言模型的组件与更大系统的其他部分的互操作性是无价的。当大语言模型的输出封装在 Pydantic 对象中时，它可以可靠地传递给其他函数、API 或数据处理管道，并有保证数据符合预期结构和类型。在系统组件边界处采用"解析，而非验证"的做法，可以带来更健壮和可维护的应用程序。

Effectively utilizing system prompts, role assignments, contextual information, delimiters, and structured output significantly enhances the clarity, control, and utility of interactions with language models, providing a strong foundation for developing reliable agentic systems. Requesting structured output is crucial for creating pipelines where the language model's output serves as the input for subsequent system or processing steps.
有效利用系统提示、角色分配、上下文信息、分隔符和结构化输出，显著提高了与语言模型交互的清晰度、控制力和实用性，为开发可靠的代理系统提供了坚实的基础。请求结构化输出对于创建管道至关重要，在这些管道中，语言模型的输出作为后续系统或处理步骤的输入。

# Reasoning and Thought Process Techniques
# 推理和思考过程技术

Large language models excel at pattern recognition and text generation but often face challenges with tasks requiring complex, multi-step reasoning. This appendix focuses on techniques designed to enhance these reasoning capabilities by encouraging models to reveal their internal thought processes. Specifically, it addresses methods to improve logical deduction, mathematical computation, and planning.
大型语言模型在模式识别和文本生成方面表现出色，但在需要复杂、多步骤推理的任务中常常面临挑战。本附录重点介绍旨在通过鼓励模型揭示其内部思考过程来增强这些推理能力的技术。具体而言，它讨论了改进逻辑推理、数学计算和规划的方法。

## Chain of Thought (CoT)
## 思维链（Chain of Thought，CoT）

The Chain of Thought (CoT) prompting technique is a powerful method for improving the reasoning abilities of language models by explicitly prompting the model to generate intermediate reasoning steps before arriving at a final answer. Instead of just asking for the result, you instruct the model to "think step by step." This process mirrors how a human might break down a problem into smaller, more manageable parts and work through them sequentially.
思维链（Chain of Thought，CoT）提示技术是一种强大的方法，通过明确提示模型在得出最终答案之前生成中间推理步骤来提高语言模型的推理能力。不是仅仅要求结果，而是指示模型"逐步思考"。这个过程类似于人类如何将问题分解为更小、更易管理的部分并依次解决它们。

CoT helps the LLM generate more accurate answers, particularly for tasks that require some form of calculation or logical deduction, where models might otherwise struggle and produce incorrect results. By generating these intermediate steps, the model is more likely to stay on track and perform the necessary operations correctly.
CoT 帮助大语言模型生成更准确的答案，特别是对于需要某种形式的计算或逻辑推理的任务，在这些任务中，模型可能会遇到困难并产生不正确的结果。通过生成这些中间步骤，模型更有可能保持正确轨道并正确执行必要的操作。

There are two main variations of CoT:
CoT 有两种主要变体：

* **Zero-Shot CoT:** This involves simply adding the phrase "Let's think step by step" (or similar phrasing) to your prompt without providing any examples of the reasoning process. Surprisingly, for many tasks, this simple addition can significantly improve the model's performance by triggering its ability to expose its internal reasoning trace.  
  * **Example (Zero-Shot CoT):**  
    If a train travels at 60 miles per hour and covers a distance of 240 miles, how long did the journey take? Let's think step by step.
* **零样本 CoT：** 这涉及简单地在提示中添加短语"让我们一步步思考"（或类似措辞），而不提供推理过程的任何示例。令人惊讶的是，对于许多任务，这个简单的添加可以通过触发模型暴露其内部推理轨迹的能力，显著提高模型的性能。
  * **示例（零样本 CoT）：**
    如果一辆火车以每小时 60 英里的速度行驶，并覆盖了 240 英里的距离，这段旅程花费了多长时间？让我们一步步思考。

* **Few-Shot CoT:** This combines CoT with few-shot prompting. You provide the model with several examples where both the input, the step-by-step reasoning process, and the final output are shown. This gives the model a clearer template for how to perform the reasoning and structure its response, often leading to even better results on more complex tasks compared to zero-shot CoT.  
  * **Example (Few-Shot CoT):**  
    Q: The sum of three consecutive integers is 36\. What are the integers?  
    A: Let the first integer be x. The next consecutive integer is x+1, and the third is x+2. The sum is x \+ (x+1) \+ (x+2) \= 3x \+ 3\. We know the sum is 36, so 3x \+ 3 \= 36\. Subtract 3 from both sides: 3x \= 33\. Divide by 3: x \= 11\. The integers are 11, 11+1=12, and 11+2=13\. The integers are 11, 12, and 13\.

    Q: Sarah has 5 apples, and she buys 8 more. She eats 3 apples. How many apples does she have left? Let's think step by step.  
    A: Let's think step by step. Sarah starts with 5 apples. She buys 8 more, so she adds 8 to her initial amount: 5 \+ 8 \= 13 apples. Then, she eats 3 apples, so we subtract 3 from the total: 13 \- 3 \= 10\. Sarah has 10 apples left. The answer is 10\.
* **少样本 CoT：** 这将 CoT 与少样本提示相结合。你为模型提供几个示例，其中显示了输入、逐步推理过程和最终输出。这为模型提供了如何执行推理和构建响应的更清晰模板，通常在更复杂的任务上比零样本 CoT 产生更好的结果。
  * **示例（少样本 CoT）：**
    问：三个连续整数的和是 36。这些整数是什么？
    答：设第一个整数为 x。下一个连续整数是 x+1，第三个是 x+2。和是 x \+ (x+1) \+ (x+2) \= 3x \+ 3\。我们知道和是 36，所以 3x \+ 3 \= 36\。从两边减去 3：3x \= 33\。除以 3：x \= 11\。整数是 11、11+1=12 和 11+2=13\。整数是 11、12 和 13\。

    问：Sarah 有 5 个苹果，她又买了 8 个。她吃了 3 个苹果。她还剩下多少苹果？让我们一步步思考。
    答：让我们一步步思考。Sarah 最初有 5 个苹果。她买了 8 个，所以她将 8 加到初始数量上：5 \+ 8 \= 13 个苹果。然后，她吃了 3 个苹果，所以我们从总数中减去 3：13 \- 3 \= 10\。Sarah 还剩下 10 个苹果。答案是 10\。

CoT offers several advantages. It is relatively low-effort to implement and can be highly effective with off-the-shelf LLMs without requiring fine-tuning. A significant benefit is the increased interpretability of the model's output; you can see the reasoning steps it followed, which helps in understanding why it arrived at a particular answer and in debugging if something went wrong. Additionally, CoT appears to improve the robustness of prompts across different versions of language models, meaning the performance is less likely to degrade when a model is updated. The main disadvantage is that generating the reasoning steps increases the length of the output, leading to higher token usage, which can increase costs and response time.
CoT 提供了几个优势。它相对容易实现，并且可以在不需要微调的情况下对现成的大语言模型高度有效。一个显著的好处是模型输出的可解释性增强；你可以看到它遵循的推理步骤，这有助于理解它为什么得出特定答案，并在出现问题时进行调试。此外，CoT 似乎提高了跨不同版本语言模型的提示的鲁棒性，这意味着当模型更新时，性能不太可能下降。主要缺点是生成推理步骤会增加输出长度，导致更高的标记使用量，这可能增加成本和响应时间。

Best practices for CoT include ensuring the final answer is presented *after* the reasoning steps, as the generation of the reasoning influences the subsequent token predictions for the answer. Also, for tasks with a single correct answer (like mathematical problems), setting the model's temperature to 0 (greedy decoding) is recommended when using CoT to ensure deterministic selection of the most probable next token at each step.
CoT 的最佳实践包括确保最终答案在推理步骤*之后*呈现，因为推理的生成会影响答案的后续标记预测。另外，对于具有单一正确答案的任务（如数学问题），建议在使用 CoT 时将模型的温度设置为 0（贪婪解码），以确保在每一步中确定性地选择最可能的下一个标记。

## Self-Consistency
## 自我一致性

Building on the idea of Chain of Thought, the Self-Consistency technique aims to improve the reliability of reasoning by leveraging the probabilistic nature of language models. Instead of relying on a single greedy reasoning path (as in basic CoT), Self-Consistency generates multiple diverse reasoning paths for the same problem and then selects the most consistent answer among them.
基于思维链的思想，自我一致性技术旨在通过利用语言模型的概率性质来提高推理的可靠性。与基本 CoT 中依赖单一贪婪推理路径不同，自我一致性为同一问题生成多个不同的推理路径，然后选择其中最一致的答案。

Self-Consistency involves three main steps:
自我一致性涉及三个主要步骤：

1. **Generating Diverse Reasoning Paths:** The same prompt (often a CoT prompt) is sent to the LLM multiple times. By using a higher temperature setting, the model is encouraged to explore different reasoning approaches and generate varied step-by-step explanations.  
2. **Extract the Answer:** The final answer is extracted from each of the generated reasoning paths.  
3. **Choose the Most Common Answer:** A majority vote is performed on the extracted answers. The answer that appears most frequently across the diverse reasoning paths is selected as the final, most consistent answer.
1. **生成多样的推理路径：** 同一提示（通常是 CoT 提示）被多次发送给大语言模型。通过使用较高的温度设置，模型被鼓励探索不同的推理方法并生成多样的逐步解释。
2. **提取答案：** 从每个生成的推理路径中提取最终答案。
3. **选择最常见的答案：** 对提取的答案进行多数投票。在多样的推理路径中出现最频繁的答案被选为最终的、最一致的答案。

This approach improves the accuracy and coherence of responses, particularly for tasks where multiple valid reasoning paths might exist or where the model might be prone to errors in a single attempt. The benefit is a pseudo-probability likelihood of the answer being correct, increasing overall accuracy. However, the significant cost is the need to run the model multiple times for the same query, leading to much higher computation and expense.
这种方法提高了响应的准确性和连贯性，特别是对于可能存在多个有效推理路径的任务，或者模型在单次尝试中可能容易出错的任务。其好处是对答案正确性的伪概率似然性，从而提高整体准确性。然而，显著的成本是需要为同一查询多次运行模型，导致计算和开支大大增加。

* **Example (Conceptual):**  
  * *Prompt:* "Is the statement 'All birds can fly' true or false? Explain your reasoning."  
  * *Model Run 1 (High Temp):* Reasons about most birds flying, concludes True.  
  * *Model Run 2 (High Temp):* Reasons about penguins and ostriches, concludes False.  
  * *Model Run 3 (High Temp):* Reasons about birds *in general*, mentions exceptions briefly, concludes True.  
  * *Self-Consistency Result:* Based on majority vote (True appears twice), the final answer is "True". (Note: A more sophisticated approach would weigh the reasoning quality).
* **示例（概念性）：**
  * *提示：* "陈述'所有鸟类都会飞'是真是假？解释你的推理。"
  * *模型运行 1（高温）：* 推理大多数鸟类会飞，得出真。
  * *模型运行 2（高温）：* 推理企鹅和鸵鸟，得出假。
  * *模型运行 3（高温）：* 推理*总体上的*鸟类，简要提及例外，得出真。
  * *自我一致性结果：* 基于多数投票（真出现两次），最终答案是"真"。（注意：更复杂的方法会权衡推理质量）。

## Step-Back Prompting
## 回溯提示

Step-back prompting enhances reasoning by first asking the language model to consider a general principle or concept related to the task before addressing specific details. The response to this broader question is then used as context for solving the original problem.
回溯提示通过首先要求语言模型在处理具体细节之前考虑与任务相关的一般原则或概念来增强推理。对这个更广泛问题的响应随后被用作解决原始问题的上下文。

This process allows the language model to activate relevant background knowledge and wider reasoning strategies. By focusing on underlying principles or higher-level abstractions, the model can generate more accurate and insightful answers, less influenced by superficial elements. Initially considering general factors can provide a stronger basis for generating specific creative outputs. Step-back prompting encourages critical thinking and the application of knowledge, potentially mitigating biases by emphasizing general principles.
这个过程使语言模型能够激活相关的背景知识和更广泛的推理策略。通过关注底层原则或更高层次的抽象，模型可以生成更准确和富有洞察力的答案，不太受表面元素的影响。最初考虑一般因素可以为生成特定的创造性输出提供更强的基础。回溯提示鼓励批判性思考和知识应用，通过强调一般原则，可能缓解偏见。

* **Example:**  
  * *Prompt 1 (Step-Back):* "What are the key factors that make a good detective story?"  
  * *Model Response 1:* (Lists elements like red herrings, compelling motive, flawed protagonist, logical clues, satisfying resolution).  
  * *Prompt 2 (Original Task \+ Step-Back Context):* "Using the key factors of a good detective story \[insert Model Response 1 here\], write a short plot summary for a new mystery novel set in a small town."
* **示例：**
  * *提示 1（回溯）：* "构成一个好的侦探小说的关键因素是什么？"
  * *模型响应 1：*（列出诸如红鲱鱼、引人入胜的动机、有缺陷的主角、逻辑线索、令人满意的结局等元素）。
  * *提示 2（原始任务 \+ 回溯上下文）：* "使用好的侦探小说的关键因素 \[插入模型响应 1\]，为一个设置在小镇的新悬疑小说写一个简短的情节摘要。"

## Tree of Thoughts (ToT)
## 思想树（Tree of Thoughts，ToT）

Tree of Thoughts (ToT) is an advanced reasoning technique that extends the Chain of Thought method. It enables a language model to explore multiple reasoning paths concurrently, instead of following a single linear progression. This technique utilizes a tree structure, where each node represents a "thought"—a coherent language sequence acting as an intermediate step. From each node, the model can branch out, exploring alternative reasoning routes.
思想树（Tree of Thoughts，ToT）是一种高级推理技术，扩展了思维链方法。它使语言模型能够同时探索多个推理路径，而不是遵循单一的线性进展。这种技术利用树结构，其中每个节点代表一个"思想"——作为中间步骤的连贯语言序列。从每个节点，模型可以分支出去，探索替代的推理路线。

ToT is particularly suited for complex problems that require exploration, backtracking, or the evaluation of multiple possibilities before arriving at a solution. While more computationally demanding and intricate to implement than the linear Chain of Thought method, ToT can achieve superior results on tasks necessitating deliberate and exploratory problem-solving. It allows an agent to consider diverse perspectives and potentially recover from initial errors by investigating alternative branches within the "thought tree."
ToT 特别适合需要在得出解决方案之前进行探索、回溯或评估多种可能性的复杂问题。虽然比线性思维链方法在计算上更加昂贵且实现更加复杂，但 ToT 在需要深思熟虑和探索性问题解决的任务上可以取得卓越的结果。它允许代理考虑多样的视角，并通过调查"思想树"中的替代分支，可能从初始错误中恢复。

* **Example (Conceptual):** For a complex creative writing task like "Develop three different possible endings for a story based on these plot points," ToT would allow the model to explore distinct narrative branches from a key turning point, rather than just generating one linear continuation.
* **示例（概念性）：** 对于像"基于这些情节点开发故事的三种不同可能结局"这样复杂的创意写作任务，ToT 将允许模型从关键转折点探索不同的叙事分支，而不仅仅是生成一个线性延续。

These reasoning and thought process techniques are crucial for building agents capable of handling tasks that go beyond simple information retrieval or text generation. By prompting models to expose their reasoning, consider multiple perspectives, or step back to general principles, we can significantly enhance their ability to perform complex cognitive tasks within agentic systems.
这些推理和思考过程技术对于构建能够处理超越简单信息检索或文本生成的任务的代理至关重要。通过提示模型暴露其推理过程、考虑多个视角或回溯到一般原则，我们可以显著增强它们在代理系统中执行复杂认知任务的能力。