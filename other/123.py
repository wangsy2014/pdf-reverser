import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用警告信息
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def chat_with_gpt(prompt, api_key):
    """
    与 GPT 模型对话的函数
    """
    url = "https://up.aicol2025.mom/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        # "Authorization": f"Bearer sk-bmRhWR6FQCwqu1qnA8C814582aF5405b9799AdFe383b37Af"
        "Authorization": f"Bearer sk-MOnW2ZNGTQuVTJU8A545BaBaFc994409883204567fB24cA7"
    }
    
    data = {
        "model": "gpt-4-1106-preview",  # 或者使用 "gpt-3.5-turbo"
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 150
    }
    
    try:
        response = requests.post(
            url,
            headers=headers,
            json=data,
           
        )
        
        # 检查响应状态
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            return f"Error: {response.status_code}, {response.text}"
            
    except Exception as e:
        return f"Error occurred: {str(e)}"

def main():
    # 你的 OpenAI API key
    api_key = "YOUR_API_KEY"
    
    # 测试对话
    while True:
        user_input = input("\n请输入你的问题 (输入 'quit' 退出): ")
        
        if user_input.lower() == 'quit':
            break
            
        print("\n正在等待 GPT 回复...\n")
        response = chat_with_gpt(user_input, api_key)
        print("GPT:", response)

if __name__ == "__main__":
    main()
