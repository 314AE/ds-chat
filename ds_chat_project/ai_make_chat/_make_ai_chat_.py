from openai import OpenAI
class MakeAIChat(object):
    def __init__(self,chatContent=None):
        self.__chatContent = chatContent
    def createAIChat(self):
        if self.__chatContent is not None:
            # for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
            # 填写自己的deepseek创建的api_key
            client = OpenAI(api_key="XXXXXXXXXXX", base_url="https://api.deepseek.com")

            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant"},
                    {"role": "user", "content": f"{self.__chatContent}"},
                ],
                max_tokens=1024,
                temperature=0.7,
                stream=False
            )
            resContent = response.choices[0].message.content
            print(resContent)
            return resContent
        else:
            return None
