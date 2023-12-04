from PySide6.QtWidgets import QApplication, QLineEdit, QTextEdit, QVBoxLayout, QWidget, QPushButton, QComboBox, QCheckBox
from PySide6.QtCore import Slot, QSize
from PySide6.QtGui import QPalette, QColor
import sys, asyncio, g4f
from typing import List
from googletrans import Translator

class GptChat(QWidget):
    def __init__(self, prv: List[g4f.Provider.BaseProvider] = None):
        super().__init__()

        self.translate_to_persian = False
        self.translator = Translator()
        self.messages_input_field, self.conversation_box, self.send_button, self.provider_selection, self.translate_button = QLineEdit(), QTextEdit(), QPushButton('Send Message'), QComboBox(), QCheckBox('Answer Persian')
        self.conversation_box.ensureCursorVisible()
        self.provider_selection.setFixedSize(400, 25)

        self.messages_input_field.setPlaceholderText('Type your message here...')
        prv = prv or ['GPTalk', 'Hashnode', 'GeekGpt', 'ChatBase', 'OnlineGpt', 'Llama2', 'Bing', 'AiChatOnline', 'Koala', 'Poe', 'PerplexityAi', 'GptGo', 'Bard', 'OpenaiChat', 'FakeGpt', 'DeepInfra', 'Phind', 'GptForLove']

        self.provider_selection.addItems(prv)
        self._prv = [getattr(g4f.Provider, prv[0])]

        self.conversation_box.setReadOnly(True)
        self.conversation_box.setPlaceholderText('Your conversation will appear here ...')

        self.messages_input_field.returnPressed.connect(self.on_send)
        self.send_button.clicked.connect(self.on_send)
        self.translate_button.toggled.connect(self.set_translate_to_persian)
        self.provider_selection.currentIndexChanged.connect(self.on_provider_changed)

        self.layout = QVBoxLayout(self)
        [self.layout.addWidget(x) for x in [self.provider_selection, self.conversation_box, self.messages_input_field, self.send_button, self.translate_button]]

        self.apply_black_theme()
        self.set_interface_size()

    @Slot()
    def on_provider_changed(self):
        self._prv = [getattr(g4f.Provider, self.provider_selection.currentText())]

    @Slot(bool)
    def set_translate_to_persian(self, state):
        self.translate_to_persian = state

    def apply_black_theme(self):
        pal, colors = QPalette(), [(QPalette.Window, QColor(53, 53, 53)), (QPalette.WindowText, QColor(255, 255, 255)), (QPalette.Base, QColor(25, 25, 25)), (QPalette.AlternateBase, QColor(53, 53, 53)), (QPalette.ToolTipBase, QColor(255, 255, 255)), (QPalette.ToolTipText, QColor(255, 255, 255)), (QPalette.Text, QColor(255, 255, 255)), (QPalette.Button, QColor(53, 53, 53)), (QPalette.ButtonText, QColor(255, 255, 255)), (QPalette.BrightText, QColor(255, 0, 0)), (QPalette.Link, QColor(42, 130, 218)), (QPalette.Highlight, QColor(42, 130, 218)), (QPalette.HighlightedText, QColor(255, 255, 255))]
        [pal.setColor(x[0], x[1]) for x in colors]
        self.setPalette(pal)

    def set_interface_size(self):
        self.resize(QSize(450, 600))

    @Slot()
    def on_send(self):
        if (msg := self.messages_input_field.text().lower()):
            self.conversation_box.append("▶ You: " + msg)
            self.messages_input_field.clear()
            self.conversation_box.append("⏳ Generating response, please wait ..." )
            asyncio.get_event_loop().run_in_executor(None, asyncio.run, self._start_conversation(msg))

    async def chat_with_prv(self, prv: g4f.Provider.BaseProvider, prm: str) -> None:
        chat_msg = {"role": "system", "content": f"User: {prm}"}
        rsp = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[chat_msg],
            provider=prv,
            jailbreak='gpt-evil-1.0',
            internet_access=True,
            auth=True,
        )
        if self.translate_to_persian:
            rsp = self.translator.translate(rsp, dest='fa').text
        self.conversation_box.append(f"🤖 ChatBot: \n {rsp}")

    async def _start_conversation(self, prm: str) -> None:
        tasks = [self.chat_with_prv(prv, prm) for prv in self._prv]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    chatgui = GptChat()
    chatgui.setWindowTitle('Friendly Chat Interface')
    chatgui.show()

    sys.exit(app.exec())