# 使用 requests 库发送 HTTP 请求到 OpenRouter AI 服务
import requests
import json

# 发送 POST 请求到 OpenRouter AI 的聊天完成 API
response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer <OPENROUTER_API_KEY>",  # 替换为你的 OpenRouter API 密钥
    "HTTP-Referer": "<YOUR_SITE_URL>", # 可选。用于在 openrouter.ai 上的排名的站点 URL
    "X-Title": "<YOUR_SITE_NAME>", # 可选。用于在 openrouter.ai 上的排名的站点标题
  },
  data=json.dumps({
    "model": "openai/gpt-4o", # 可选，指定使用的模型
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?"  # 发送给 AI 的用户消息
      }
    ]
  })
)