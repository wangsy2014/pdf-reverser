import os
import anthropic
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

# 从环境变量获取API密钥和基础URL
api_key = "sk-A5UC1hqNRmjEmpeeCf07539dAa9f419d9bBa20F497092a4c"
api_url = "https://chat.aidirectlink.icu/v1/chat/completions"

# 检查是否成功获取了环境变量
if not api_key or not api_url:
    raise ValueError("请确保设置了环境变量 ANTHROPIC_API_KEY 和 ANTHROPIC_API_URL")

# 打印环境变量以进行调试
print(f"ANTHROPIC_API_KEY: {api_key}")
print(f"ANTHROPIC_API_URL: {api_url}")

# 自定义Anthropic类以使用自定义API URL
class CustomAnthropic(Anthropic):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api_url = api_url

    def _make_request(self, method, url, **kwargs):
        # 使用自定义API URL
        full_url = f"{self.api_url}{url}"
        return super()._make_request(method, full_url, **kwargs)

# 初始化自定义的Anthropic客户端
client = CustomAnthropic(api_key=api_key)

# 创建消息
message = client.completions.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens_to_sample=1024,
    prompt=f"{HUMAN_PROMPT}Hello, Claude{AI_PROMPT}",
)

# 打印生成的文本
print(message.completion)

