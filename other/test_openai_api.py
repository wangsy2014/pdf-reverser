import os

from openai import OpenAI

client = OpenAI(
    api_key = "sk-MOnW2ZNGTQuVTJU8A545BaBaFc994409883204567fB24cA7",
    base_url = "https://up.aicol2025.mom/v1"
)


def generate_text(prompt):
    try:
        # 创建一个 OpenAI 客户端
        # client = openai.Client()
        
        # 发送聊天完成请求

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # 选择合适的模型
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        
        # 获取生成的文本
        generated_text = response.choices[0].message.content
        return generated_text
    
    except openai.APIError as e:
        print(f"API Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    prompt = "Translate the following sentence: 'Hello, world!' to French."
    generated_text = generate_text(prompt)
    print(generated_text)

