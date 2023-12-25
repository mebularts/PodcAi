import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextBrowser, QFileDialog
from PyQt5.QtCore import Qt, QTimer
import openai
import speech_recognition as sr
import pyttsx3

# OpenAI API anahtarınızı buraya ekleyin
openai.api_key = 'YOUR_API_KEY'

class AIAssistantApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Assistant")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: #F5F5F5; color: #333333; font-size: 14px;")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.get_ai_response)

        # Konuşma algılayıcı
        self.recognizer = sr.Recognizer()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Kullanıcı girişi ve AI çıkış metin alanları
        self.chat_display = QTextBrowser(self)
        self.chat_display.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.chat_display)

        # Başlat/Duraklat düğmesi
        self.start_pause_button = QPushButton("▶", self)
        self.start_pause_button.clicked.connect(self.start_pause_timer)
        self.start_pause_button.setStyleSheet("background-color: #3498DB; color: #ECF0F1; border: none; padding: 10px 20px; font-size: 16px; border-radius: 8px; margin-top: 10px;")
        layout.addWidget(self.start_pause_button, alignment=Qt.AlignBottom | Qt.AlignRight)

        # Dışa Aktar düğmesi
        export_button = QPushButton("⤵", self)
        export_button.clicked.connect(self.export_conversation)
        export_button.setStyleSheet("background-color: #2ECC71; color: #ECF0F1; border: none; padding: 10px 20px; font-size: 16px; border-radius: 8px; margin-left: 800px; margin-top: 5px;")
        layout.addWidget(export_button, alignment=Qt.AlignBottom | Qt.AlignLeft)

        self.setLayout(layout)

        # Konuşmaları tutacak bir liste
        self.conversation = []

    def recognize_speech(self):
        with sr.Microphone() as source:
            print("Sorunuzu söyleyin:")
            try:
                audio = self.recognizer.listen(source, timeout=5)  # 5 saniye içinde konuşma algılanmazsa durdur
                return self.recognizer.recognize_google(audio, language="tr-TR")  # Türkçe dilinde algıla
            except sr.UnknownValueError:
                print("Konuşma algılanamadı.")
                return None

    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def generate_response(self, question):
        response = openai.Completion.create(
            engine="text-davinci-002",  # GPT-3 modeli
            prompt=question,
            max_tokens=150,  # Cevap uzunluğunu sınırla
            temperature=0.7,  # Yaratıcılığı kontrol et
        )
        return response['choices'][0]['text'].strip()

    def get_user_question(self):
        question = self.recognize_speech()
        return question

    def start_pause_timer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.start_pause_button.setText("▶")
        else:
            self.timer.start(1000)  # 1 saniye içinde yeni soru sorulmazsa mikrofonu kapat
            self.start_pause_button.setText("▐▐ ")

    def get_ai_response(self):
        question = self.get_user_question()
        if question:
            user_message = f"<div style='text-align: left; color: #333333; background-color: #E5E5EA; border-radius: 45px; padding: 10px; margin-bottom: 5px; width: 60%; margin-left: 20%;'>{question}</div>"
            self.chat_display.append(user_message)

            response = self.generate_response(question)
            ai_message = f"<div style='text-align: left; color: #FFFFFF; background-color: #007AFF; border-radius: 45px; padding: 10px; margin-bottom: 5px; width: 60%; margin-right: 20%;'>{response}</div>"
            self.chat_display.append(ai_message)
            self.conversation.append((question, response))  # Konuşmayı listeye ekle
            self.speak(response)

    def export_conversation(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Dışa Aktar", "", "Text Files (*.txt);;All Files (*)", options=options)
        
        if file_name:
            with open(file_name, 'w') as file:
                for user_msg, ai_msg in self.conversation:
                    file.write(f"Sen: {user_msg}\nPodcAi: {ai_msg}\n\n")
            print("Konuşma başarıyla dışa aktarıldı.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AIAssistantApp()
    window.show()
    sys.exit(app.exec_())
