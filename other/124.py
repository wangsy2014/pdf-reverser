import requests
import json

def call_claude_api():
    url = "https://chat.aidirectlink.icu/v1/chat/completions"
    headers = {
        "Accept": "text/event-stream",
        "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8",
        "Authorization": "Bearer sk-A5UC1hqNRmjEmpeeCf07539dAa9f419d9bBa20F497092a4c",
        "Content-Type": "application/json",
       
    }
    data = {
        "max_tokens": 1024,
        "model": "claude-3-5-sonnet-20241022",
        "temperature": 0.5,
        "top_p": 1,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "messages": [
            {"role": "system", "content": "You are Claude, a large language model trained by Anthropic.\nKnowledge cutoff: 2024-04\nCurrent model: claude-3-5-sonnet-20241022\nCurrent time: 2024/12/1 15:03:59\nLatex inline: $x^2$\nLatex block: $$e=mc^2$$"},
            {"content": "你好", "role": "user"},
            {"content": "你好!我是 Claude。很高兴见到你。有什么我可以帮你的吗?", "role": "assistant"},
            {"role": "user", "content": "你好今天天气怎么用"}
        ],
        "stream": True
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # 检查响应状态

        # 处理流式响应
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                print(decoded_line)
    except requests.exceptions.RequestException as e:
        print(f"Error calling Claude API: {e}")

# 调用函数
call_claude_api()

