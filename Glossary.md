# Glossary
# 术语表

# Fundamental Concepts
# 基础概念

**Prompt:** A prompt is the input, typically in the form of a question, instruction, or statement, that a user provides to an AI model to elicit a response. The quality and structure of the prompt heavily influence the model's output, making prompt engineering a key skill for effectively using AI.
**提示词（Prompt）：** 提示词是用户提供给人工智能模型以引发响应的输入，通常以问题、指令或陈述的形式出现。提示词的质量和结构极大地影响模型的输出，使得提示词工程成为有效使用人工智能的关键技能。

**Context Window:** The context window is the maximum number of tokens an AI model can process at once, including both the input and its generated output. This fixed size is a critical limitation, as information outside the window is ignored, while larger windows enable more complex conversations and document analysis.
**上下文窗口（Context Window）：** 上下文窗口是人工智能模型一次可以处理的最大标记数，包括输入和生成的输出。这个固定大小是一个关键限制，因为窗口外的信息会被忽略，而更大的窗口则能实现更复杂的对话和文档分析。

**In-Context Learning:** In-context learning is an AI's ability to learn a new task from examples provided directly in the prompt, without requiring any retraining. This powerful feature allows a single, general-purpose model to be adapted to countless specific tasks on the fly.
**上下文学习（In-Context Learning）：** 上下文学习是人工智能直接从提示中提供的示例中学习新任务的能力，无需重新训练。这一强大特性使得单一的通用模型能够即时适应无数特定任务。

**Zero-Shot, One-Shot, & Few-Shot Prompting:** These are prompting techniques where a model is given zero, one, or a few examples of a task to guide its response. Providing more examples generally helps the model better understand the user's intent and improves its accuracy for the specific task.
**零样本、单样本和少样本提示（Zero-Shot, One-Shot, & Few-Shot Prompting）：** 这些是提示技术，模型被给予零个、一个或几个任务示例来引导其响应。提供更多示例通常有助于模型更好地理解用户意图，并提高特定任务的准确性。

**Multimodality:** Multimodality is an AI's ability to understand and process information across multiple data types like text, images, and audio. This allows for more versatile and human-like interactions, such as describing an image or answering a spoken question.
**多模态性（Multimodality）：** 多模态性是人工智能跨越文本、图像和音频等多种数据类型理解和处理信息的能力。这使得交互更加多样化和类人，如描述图像或回答口头问题。

**Grounding:** Grounding is the process of connecting a model's outputs to verifiable, real-world information sources to ensure factual accuracy and reduce hallucinations. This is often achieved with techniques like RAG to make AI systems more trustworthy.
**基础（Grounding）：** 基础是将模型输出连接到可验证的现实世界信息源的过程，以确保事实准确性并减少幻觉。这通常通过 RAG 等技术实现，使人工智能系统更值得信赖。

# Core AI Model Architectures
# 核心人工智能模型架构

**Transformers:** The Transformer is the foundational neural network architecture for most modern LLMs. Its key innovation is the self-attention mechanism, which efficiently processes long sequences of text and captures complex relationships between words.
**Transformer：** Transformer 是大多数现代大型语言模型的基础神经网络架构。其关键创新是自注意力机制，能高效处理长文本序列并捕捉单词之间的复杂关系。

**Recurrent Neural Network (RNN):** The Recurrent Neural Network is a foundational architecture that preceded the Transformer. RNNs process information sequentially, using loops to maintain a "memory" of previous inputs, which made them suitable for tasks like text and speech processing.
**循环神经网络（Recurrent Neural Network，RNN）：** 循环神经网络是 Transformer 之前的基础架构。RNN 按顺序处理信息，使用循环来维持先前输入的"记忆"，这使它们适合文本和语音处理等任务。

**Mixture of Experts (MoE):** Mixture of Experts is an efficient model architecture where a "router" network dynamically selects a small subset of "expert" networks to handle any given input. This allows models to have a massive number of parameters while keeping computational costs manageable.
**专家混合模型（Mixture of Experts，MoE）：** 专家混合模型是一种高效的模型架构，其中"路由器"网络动态选择少量"专家"网络来处理任何给定输入。这使模型能拥有大量参数，同时保持可管理的计算成本。

**Diffusion Models:** Diffusion models are generative models that excel at creating high-quality images. They work by adding random noise to data and then training a model to meticulously reverse the process, allowing them to generate novel data from a random starting point.
**扩散模型（Diffusion Models）：** 扩散模型是擅长创建高质量图像的生成模型。它们通过向数据添加随机噪声，然后训练模型精确地反转这个过程，从而能从随机起点生成新数据。

**Mamba:** Mamba is a recent AI architecture using a Selective State Space Model (SSM) to process sequences with high efficiency, especially for very long contexts. Its selective mechanism allows it to focus on relevant information while filtering out noise, making it a potential alternative to the Transformer.
**Mamba：** Mamba 是一种最新的人工智能架构，使用选择性状态空间模型（Selective State Space Model，SSM）以高效处理序列，特别是对于非常长的上下文。其选择性机制使其能够专注于相关信息，同时过滤掉噪声，使其成为 Transformer 的潜在替代方案。

# The LLM Development Lifecycle
# 大型语言模型开发生命周期

The development of a powerful language model follows a distinct sequence. It begins with Pre-training, where a massive base model is built by training it on a vast dataset of general internet text to learn language, reasoning, and world knowledge. Next is Fine-tuning, a specialization phase where the general model is further trained on smaller, task-specific datasets to adapt its capabilities for a particular purpose. The final stage is Alignment, where the specialized model's behavior is adjusted to ensure its outputs are helpful, harmless, and aligned with human values.
大型语言模型的开发遵循一个独特的序列。它从预训练开始，在这个阶段通过在海量通用互联网文本数据集上训练，构建一个庞大的基础模型，学习语言、推理和世界知识。接下来是微调，这是一个专业化阶段，通用模型在更小的特定任务数据集上进一步训练，以适应特定目的。最后阶段是对齐，调整专业化模型的行为，确保其输出有帮助、无害，并与人类价值观一致。

**Pre-training Techniques:** Pre-training is the initial phase where a model learns general knowledge from vast amounts of data. The top techniques for this involve different objectives for the model to learn from. The most common is Causal Language Modeling (CLM), where the model predicts the next word in a sentence. Another is Masked Language Modeling (MLM), where the model fills in intentionally hidden words in a text. Other important methods include Denoising Objectives, where the model learns to restore a corrupted input to its original state, Contrastive Learning, where it learns to distinguish between similar and dissimilar pieces of data, and Next Sentence Prediction (NSP), where it determines if two sentences logically follow each other.
**预训练技术：** 预训练是模型从海量数据中学习一般知识的初始阶段。顶级技术涉及模型学习的不同目标。最常见的是因果语言建模（Causal Language Modeling，CLM），模型预测句子中的下一个词。另一种是掩码语言建模（Masked Language Modeling，MLM），模型填充文本中故意隐藏的词。其他重要方法包括去噪目标，模型学习将损坏的输入恢复到原始状态；对比学习，学习区分相似和不相似的数据片段；以及下一句预测（Next Sentence Prediction，NSP），确定两个句子是否逻辑上相连。

**Fine-tuning Techniques:** Fine-tuning is the process of adapting a general pre-trained model to a specific task using a smaller, specialized dataset. The most common approach is Supervised Fine-Tuning (SFT), where the model is trained on labeled examples of correct input-output pairs. A popular variant is Instruction Tuning, which focuses on training the model to better follow user commands. To make this process more efficient, Parameter-Efficient Fine-Tuning (PEFT) methods are used, with top techniques including LoRA (Low-Rank Adaptation), which only updates a small number of parameters, and its memory-optimized version, QLoRA. Another technique, Retrieval-Augmented Generation (RAG), enhances the model by connecting it to an external knowledge source during the fine-tuning or inference stage.
**微调技术：** 微调是使用更小的专业数据集将通用预训练模型调整到特定任务的过程。最常见的方法是监督微调（Supervised Fine-Tuning，SFT），模型在正确的输入-输出对标签示例上训练。一个流行的变体是指令调优，专注于训练模型更好地遵循用户命令。为提高这一过程的效率，使用参数高效微调（Parameter-Efficient Fine-Tuning，PEFT）方法，顶级技术包括 LoRA（低秩适应），仅更新少量参数，以及其内存优化版本 QLoRA。另一种技术，检索增强生成（Retrieval-Augmented Generation，RAG），通过在微调或推理阶段将模型连接到外部知识源来增强模型。

**Alignment & Safety Techniques:** Alignment is the process of ensuring an AI model's behavior aligns with human values and expectations, making it helpful and harmless. The most prominent technique is Reinforcement Learning from Human Feedback (RLHF), where a "reward model" trained on human preferences guides the AI's learning process, often using an algorithm like Proximal Policy Optimization (PPO) for stability. Simpler alternatives have emerged, such as Direct Preference Optimization (DPO), which bypasses the need for a separate reward model, and Kahneman-Tversky Optimization (KTO), which simplifies data collection further. To ensure safe deployment, Guardrails are implemented as a final safety layer to filter outputs and block harmful actions in real-time.
**对齐与安全技术：** 对齐是确保人工智能模型的行为与人类价值观和期望一致，使其有帮助且无害的过程。最突出的技术是来自人类反馈的强化学习（Reinforcement Learning from Human Feedback，RLHF），其中一个在人类偏好上训练的"奖励模型"指导人工智能的学习过程，通常使用近端策略优化（Proximal Policy Optimization，PPO）算法以保持稳定性。出现了更简单的替代方案，如直接偏好优化（Direct Preference Optimization，DPO），绕过了对单独奖励模型的需求，以及卡尼曼-特夫斯基优化（Kahneman-Tversky Optimization，KTO），进一步简化了数据收集。为确保安全部署，护栏被实施为最终的安全层，实时过滤输出并阻止有害行为。

# Enhancing AI Agent Capabilities
# 增强人工智能代理能力

AI agents are systems that can perceive their environment and take autonomous actions to achieve goals. Their effectiveness is enhanced by robust reasoning frameworks.
人工智能代理是能够感知其环境并自主采取行动以实现目标的系统。它们的有效性通过强大的推理框架得到增强。

**Chain of Thought (CoT):** This prompting technique encourages a model to explain its reasoning step-by-step before giving a final answer. This process of "thinking out loud" often leads to more accurate results on complex reasoning tasks.
**思维链（Chain of Thought，CoT）：** 这种提示技术鼓励模型在给出最终答案之前，逐步解释其推理过程。这种"自言自语"的过程通常在复杂推理任务上产生更准确的结果。

**Tree of Thoughts (ToT):** Tree of Thoughts is an advanced reasoning framework where an agent explores multiple reasoning paths simultaneously, like branches on a tree. It allows the agent to self-evaluate different lines of thought and choose the most promising one to pursue, making it more effective at complex problem-solving.
**树状思维（Tree of Thoughts，ToT）：** 树状思维是一种先进的推理框架，其中代理同时探索多个推理路径，就像树的分支一样。它允许代理自我评估不同的思维路线，并选择最有前途的一条来追求，使其在复杂问题解决上更加有效。

**ReAct (Reason and Act):** ReAct is an agent framework that combines reasoning and acting in a loop. The agent first "thinks" about what to do, then takes an "action" using a tool, and uses the resulting observation to inform its next thought, making it highly effective at solving complex tasks.
**ReAct（Reason and Act）：** ReAct 是一个结合推理和行动的循环框架。代理首先"思考"要做什么，然后使用工具采取"行动"，并使用结果观察来指导其下一个思考，使其在解决复杂任务上非常有效。

**Planning:** This is an agent's ability to break down a high-level goal into a sequence of smaller, manageable sub-tasks. The agent then creates a plan to execute these steps in order, allowing it to handle complex, multi-step assignments.
**规划（Planning）：** 这是代理将高层次目标分解为一系列更小、更易于管理的子任务的能力。代理然后创建一个计划来按顺序执行这些步骤，使其能够处理复杂的多步骤分配。

**Deep Research:** Deep research refers to an agent's capability to autonomously explore a topic in-depth by iteratively searching for information, synthesizing findings, and identifying new questions. This allows the agent to build a comprehensive understanding of a subject far beyond a single search query.
**深度研究（Deep Research）：** 深度研究是指代理自主深入研究主题的能力，通过迭代搜索信息、综合发现并识别新问题。这使代理能够建立对主题的全面理解，远远超出单次搜索查询。

**Critique Model:** A critique model is a specialized AI model trained to review, evaluate, and provide feedback on the output of another AI model. It acts as an automated critic, helping to identify errors, improve reasoning, and ensure the final output meets a desired quality standard.
**批评模型（Critique Model）：** 批评模型是专门训练来审查、评估和提供反馈的人工智能模型。它充当中控批评者，帮助识别错误、改进推理，并确保最终输出符合期望的质量标准。