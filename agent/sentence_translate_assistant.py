from .LLM_agent import LLMAgent
import re
from PySide6.QtCore import Signal


class SentenceTranslateAssistant(LLMAgent):
    prompt = f"""
      你是一个英文句子翻译大师，我给你输入英文句子，你需要帮我翻译成中文，翻译的尽量信达雅
      请严格按照以下格式返回（不要添加额外内容）：
      含义：[内容]
      """
    return_result_signal = Signal(dict)

    def __init__(self):
        super().__init__(self.prompt)
        self.sentence = None
        self.finished.connect(self.parse_result)

    def translate_sentence(self, sentence):
        self.sentence = sentence
        if len(self.messages) == 2:
            self.messages.pop()
        self.messages.append({"role": "user", "content": sentence})
        self.start()

    def run(self):
        if self.sentence is None:
            pass
        super().run()

    def parse_result(self, response):
        try:
            pattern = r"含义：(.*)"
            match = re.search(pattern, response, re.DOTALL)
            if not match:
                raise ValueError("API返回格式异常，解析失败")

            result = {
                "sentence": self.sentence,
                "meaning": match.group(1).strip(),
            }
            self.return_result_signal.emit(result)
        except Exception as e:
            self.return_result_signal.emit({"error": f"获取单词信息失败: {str(e)}"})
