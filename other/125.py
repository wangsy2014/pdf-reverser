import requests

# 设置 API 密钥和 API 基础 URL
API_KEY = "Bearer sk-3MMLOnKYZ8AmLbBi58A06f159e9a4c44BaF718Ac480bC70d"
API_URL = "https://chat.aidirectlink.icu/v1/chat/completions"

# 定义请求函数
def generate_sonnet(prompt):

    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json",
    }
    
    data = {
        "model": "claude-3-5-sonnet-20241022",  # 或者根据版本选择 Claude 模型
        "prompt": prompt,
        "max_tokens_to_sample": 300,  # 设置生成的最大 token 数
        "temperature": 0.7,  # 控制生成随机性
        "stop_sequences": ["\n\n"],  # 可选，用于终止生成
    }

    response = requests.post(API_URL, headers=headers, json=data)

    # 解析并返回结果
    if response.status_code == 200:
        return response.json()["completion"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

# 测试生成十四行诗
prompt = (
    "\n\nHuman: Please write a Shakespearean sonnet about the beauty of nature.\n\nAssistant:"
)
try:
    sonnet = generate_sonnet(prompt)
    print("Generated Sonnet:\n", sonnet)
except Exception as e:
    print("Error:", e)