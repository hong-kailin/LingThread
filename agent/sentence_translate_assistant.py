from .LLM_agent import LLMAgent
import re
from PySide6.QtCore import Signal


class SentenceTranslateAssistant(LLMAgent):
    prompt = f"""
      你是一个英语单词解析大师，后面我每次给你输入一个单词你都需要为我输出以下内容
      1. 含义：注明词性（如n./v./adj.等）和中文释义
      2. 音标：先输出英式音标（DJ音标），再输出美式音标（KK音标）
      3. 单词助记：提供快速记忆方法（拆分/词根/联想等）
      4. 发音助记：提供包含该单词部分的简单单词（如查询"light"可提供"flight"）

      请严格按照以下格式返回（不要添加额外内容）：
      含义：[内容]
      音标：[内容]
      单词助记：[内容]
      发音助记：[内容]
      """
    return_result_signal = Signal(dict)

    def __init__(self):
        super().__init__(self.prompt)
        self.word = None
        # self.finished.connect(self.parse_result)

    def translate_sentence(self, sentence):
        print("hello")
        # self.word = word
        # if len(self.messages) == 2:
        #     self.messages.pop()
        # self.messages.append({"role": "user", "content": word})
        # self.start()

    def run(self):
        if self.word is None:
            pass
        super().run()
