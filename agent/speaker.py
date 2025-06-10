import pygame
import tempfile
import edge_tts
import asyncio
from PySide6.QtCore import QThread, Signal


class Speaker(QThread):
    finished = Signal()

    def __init__(self, loop):
        super().__init__()
        self.loop = loop
        self.text = ""
        self._stop_flag = False
        self.temp_file = None

    def set_text(self, text):
        self.text = text

    def stop(self):
        self._stop_flag = True
        pygame.mixer.music.stop()
        if self.temp_file:
            try:
                self.temp_file.close()
            except Exception:
                pass

    async def _create_audio(self):
        # 创建临时文件
        self.temp_file = tempfile.NamedTemporaryFile(suffix='.mp3', delete=False)
        self.temp_file.close()  # 关闭文件以便其他进程可以访问它

        # 使用edge_tts生成音频
        communicate = edge_tts.Communicate(text=self.text, voice="en-US-AriaNeural")
        await communicate.save(self.temp_file.name)
        return self.temp_file.name

    async def _play_audio(self, audio_file):

        # 初始化pygame混音器
        pygame.mixer.init()

        # 加载并播放音频
        pygame.mixer.music.load(audio_file)

        while not self._stop_flag:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()
            await asyncio.sleep(0.1)
        self._stop_flag = False

    def run(self):
        try:
            # 创建音频文件
            audio_file = self.loop.run_until_complete(self._create_audio())

            # 播放音频
            self.loop.run_until_complete(self._play_audio(audio_file))
        except Exception as e:
            print(f"Error in speaker thread: {e}")
        finally:
            self.finished.emit()
