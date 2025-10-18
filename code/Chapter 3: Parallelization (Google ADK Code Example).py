# Part of agent.py --> Follow https://google.github.io/adk-docs/get-started/quickstart/ to learn the setup
# agent.py 的一部分 --> 访问 https://google.github.io/adk-docs/get-started/quickstart/ 了解设置

# --- 1. Define Researcher Sub-Agents (to run in parallel) ---
# --- 1. 定义研究者子代理（并行运行） ---

# Researcher 1: Renewable Energy
# 研究者 1：可再生能源

researcher_agent_1 = LlmAgent(
    name="RenewableEnergyResearcher",
    model=GEMINI_MODEL,
    instruction="""You are an AI Research Assistant specializing in energy.
Research the latest advancements in 'renewable energy sources'.
Use the Google Search tool provided.
Summarize your key findings concisely (1-2 sentences).
Output *only* the summary.
""",
    instruction="""你是一个专门研究能源的人工智能研究助手。
研究'可再生能源'的最新进展。
使用提供的 Google 搜索工具。
简明扼要地总结你的关键发现（1-2 句）。
仅输出总结。
""",
    description="Researches renewable energy sources.",
    description="研究可再生能源来源。",
    tools=[google_search],
    # Store result in state for the merger agent
    # 为合并代理存储结果
    output_key="renewable_energy_result"
)

# Researcher 2: Electric Vehicles
# 研究者 2：电动汽车
researcher_agent_2 = LlmAgent(
    name="EVResearcher",
    model=GEMINI_MODEL,
    instruction="""You are an AI Research Assistant specializing in transportation.
Research the latest developments in 'electric vehicle technology'.
Use the Google Search tool provided.
Summarize your key findings concisely (1-2 sentences).
Output *only* the summary.
""",
    instruction="""你是一个专门研究交通运输的人工智能研究助手。
研究'电动汽车技术'的最新发展。
使用提供的 Google 搜索工具。
简明扼要地总结你的关键发现（1-2 句）。
仅输出总结。
""",
    description="Researches electric vehicle technology.",
    description="研究电动汽车技术。",
    tools=[google_search],
    # Store result in state for the merger agent
    # 为合并代理存储结果
    output_key="ev_technology_result"
)

# Researcher 3: Carbon Capture
# 研究者 3：碳捕获
researcher_agent_3 = LlmAgent(
    name="CarbonCaptureResearcher",
    model=GEMINI_MODEL,
    instruction="""You are an AI Research Assistant specializing in climate solutions.
Research the current state of 'carbon capture methods'.
Use the Google Search tool provided.
Summarize your key findings concisely (1-2 sentences).
Output *only* the summary.
""",
    instruction="""你是一个专门研究气候解决方案的人工智能研究助手。
研究'碳捕获方法'的当前状态。
使用提供的 Google 搜索工具。
简明扼要地总结你的关键发现（1-2 句）。
仅输出总结。
""",
    description="Researches carbon capture methods.",
    description="研究碳捕获方法。",
    tools=[google_search],
    # Store result in state for the merger agent
    # 为合并代理存储结果
    output_key="carbon_capture_result"
)

# --- 2. Create the ParallelAgent (Runs researchers concurrently) ---
# --- 2. 创建并行代理（并发运行研究者） ---
# This agent orchestrates the concurrent execution of the researchers.
# 这个代理协调研究者的并发执行。
# It finishes once all researchers have completed and stored their results in state.
# 一旦所有研究者完成并在状态中存储结果，它就会完成。
parallel_research_agent = ParallelAgent(
 name="ParallelWebResearchAgent",
 sub_agents=[researcher_agent_1, researcher_agent_2, researcher_agent_3],
 description="Runs multiple research agents in parallel to gather information."
 description="并行运行多个研究代理以收集信息。"
)

# --- 3. Define the Merger Agent (Runs *after* the parallel agents) ---
# --- 3. 定义合并代理（在并行代理*之后*运行） ---
# This agent takes the results stored in the session state by the parallel agents
# 这个代理获取并行代理存储在会话状态中的结果
# and synthesizes them into a single, structured response with attributions.
# 并将它们综合成一个带有归属的结构化响应。
merger_agent = LlmAgent(
 name="SynthesisAgent",
 model=GEMINI_MODEL,  # Or potentially a more powerful model if needed for synthesis
 # 或者在需要综合时使用更强大的模型
 instruction="""You are an AI Assistant responsible for combining research findings into a structured report.

Your primary task is to synthesize the following research summaries, clearly attributing findings to their source areas. Structure your response using headings for each topic. Ensure the report is coherent and integrates the key points smoothly.

**Crucially: Your entire response MUST be grounded *exclusively* on the information provided in the 'Input Summaries' below. Do NOT add any external knowledge, facts, or details not present in these specific summaries.**

**Input Summaries:**

*   **Renewable Energy:**
 {renewable_energy_result}

*   **Electric Vehicles:**
 {ev_technology_result}

*   **Carbon Capture:**
 {carbon_capture_result}

**Output Format:**

## Summary of Recent Sustainable Technology Advancements

### Renewable Energy Findings
(Based on RenewableEnergyResearcher's findings)
[Synthesize and elaborate *only* on the renewable energy input summary provided above.]

### Electric Vehicle Findings
(Based on EVResearcher's findings)
[Synthesize and elaborate *only* on the EV input summary provided above.]

### Carbon Capture Findings
(Based on CarbonCaptureResearcher's findings)
[Synthesize and elaborate *only* on the carbon capture input summary provided above.]

### Overall Conclusion
[Provide a brief (1-2 sentence) concluding statement that connects *only* the findings presented above.]

Output *only* the structured report following this format. Do not include introductory or concluding phrases outside this structure, and strictly adhere to using only the provided input summary content.
""",
 instruction="""你是一个负责将研究发现整合成结构化报告的人工智能助手。

你的主要任务是综合以下研究总结，清晰地将发现归因于其来源领域。使用每个主题的标题构建你的响应。确保报告连贯，并顺利整合关键点。

**关键：你的整个响应必须*仅*基于下面'输入总结'中提供的信息。不要添加这些特定总结中未出现的任何外部知识、事实或细节。**

**输入总结：**

*   **可再生能源：**
 {renewable_energy_result}

*   **电动汽车：**
 {ev_technology_result}

*   **碳捕获：**
 {carbon_capture_result}

**输出格式：**

## 最近可持续技术进展总结

### 可再生能源发现
（基于可再生能源研究者的发现）
[仅综合和阐述上面提供的可再生能源输入总结。]

### 电动汽车发现
（基于电动汽车研究者的发现）
[仅综合和阐述上面提供的电动汽车输入总结。]

### 碳捕获发现
（基于碳捕获研究者的发现）
[仅综合和阐述上面提供的碳捕获输入总结。]

### 总体结论
[提供一个简短的（1-2句）结论陈述，仅连接上面呈现的发现。]

仅按照此格式输出结构化报告。不要在此结构之外包含引言或结论性短语，并严格遵守仅使用提供的输入总结内容。
""",
 description="Combines research findings from parallel agents into a structured, cited report, strictly grounded on provided inputs.",
 description="将并行代理的研究发现组合成一个结构化的、有引用的报告，严格基于提供的输入。",
 # No tools needed for merging
 # 合并不需要工具
 # No output_key needed here, as its direct response is the final output of the sequence
 # 这里不需要输出键，因为它的直接响应是序列的最终输出
)

# --- 4. Create the SequentialAgent (Orchestrates the overall flow) ---
# --- 4. 创建顺序代理（协调整体流程） ---
# This is the main agent that will be run. It first executes the ParallelAgent
# 这是将要运行的主代理。它首先执行并行代理
# to populate the state, and then executes the MergerAgent to produce the final output.
# 以填充状态，然后执行合并代理以生成最终输出。
sequential_pipeline_agent = SequentialAgent(
 name="ResearchAndSynthesisPipeline",
 # Run parallel research first, then merge
 # 先运行并行研究，然后合并
 sub_agents=[parallel_research_agent, merger_agent],
 description="Coordinates parallel research and synthesizes the results."
 description="协调并行研究并综合结果。"
)

root_agent = sequential_pipeline_agent