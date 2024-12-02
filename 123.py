import openai

def call_openai_api():
    # 设置API密钥
    openai.api_key = "your_openai_api_key"  # 请替换为你的API密钥

    try:
        # 调用OpenAI API
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt="Hello, world!",
            max_tokens=5
        )

        # 返回结果
        return response
    except openai.error.OpenAIError as e:
        print("Error calling OpenAI API:", e)
        return None

# 调用函数并打印结果
response = call_openai_api()
if response:
    print(response) 