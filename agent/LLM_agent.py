from openai import OpenAI
from PySide6.QtCore import QThread, Signal


class LLMAgent(QThread):
    finished = Signal(str, bool)

    def __init__(self, messages):
        super().__init__()
        self.client = OpenAI(api_key="sk-c8860ff4cb9246c28b3de26f0e00aff9",
                             base_url="https://api.deepseek.com")
        self.messages = messages

    def run(self):
        try:
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=self.messages,
                stream=False
            )

            ai_response = response.choices[0].message.content
            self.finished.emit(ai_response, True)
        except Exception as e:
            error_message = f"API调用错误: {str(e)}"
            self.finished.emit(error_message, False)
