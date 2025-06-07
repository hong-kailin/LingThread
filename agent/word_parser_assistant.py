from .LLM_agent import LLMAgent
import re
from PySide6.QtCore import Signal


class WordParserAssistant(LLMAgent):
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
        self.finished.connect(self.parse_result)

    def parser_word(self, word):
        self.word = word
        self.messages.append({"role": "user", "content": word})
        self.run()

    def run(self):
        if self.word is None:
            pass
        super().run()

    def parse_result(self, response):
        try:
            pattern = r"含义：(.*?)\n音标：(.*?)\n单词助记：(.*?)\n发音助记：(.*)"
            match = re.search(pattern, response, re.DOTALL)
            if not match:
                raise ValueError("API返回格式异常，解析失败")

            result = {
                "word": self.word,
                "meaning": match.group(1).strip(),
                "phonetic": match.group(2).strip(),
                "mnemonic": match.group(3).strip(),
                "pronunciation_tip": match.group(4).strip()
            }
            self.return_result_signal.emit(result)
        except Exception as e:
            self.return_result_signal.emit({"error": f"获取单词信息失败: {str(e)}"})
