from .LLM_agent import LLMAgent


class EnglishChatAssistant(LLMAgent):
    prompt = f"""
          你是一个英文老师，需要回答学生的英语问题，并且你需要鼓励和引导学生使用英文和你对话聊天。
          """

    def __init__(self):
        super().__init__(self.prompt)
