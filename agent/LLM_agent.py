import os.path

from openai import OpenAI
from PySide6.QtCore import QThread, Signal
import toml


class LLMAgent(QThread):
    finished = Signal(str, bool)

    def __init__(self, base_prompt):
        super().__init__()
        self.load_config()
        self.client = OpenAI(api_key=self.default_settings["api_key"],
                             base_url=self.default_settings["base_url"])
        self.messages = [{"role": "system", "content": base_prompt}]

    def load_config(self):
        config_path = "./config.toml"
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as file:
                data = toml.load(file)

            base_llm = data.get("llm", {})
            self.default_settings = {
                "model": base_llm.get("model"),
                "base_url": base_llm.get("base_url"),
                "api_key": base_llm.get("api_key"),
                "max_tokens": base_llm.get("max_tokens", 4096),
                "temperature": base_llm.get("temperature", 1.0),
                "api_type": base_llm.get("api_type", ""),
                "api_version": base_llm.get("api_version", ""),
            }
        else:
            self.default_settings = None

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
