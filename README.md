# PodcAi: AI Assistant

PodcAi, konuşma tanıma ve OpenAI GPT-3 modelini kullanarak doğal dil işleme yeteneklerine sahip bir yapay zeka asistanıdır. Kullanıcılar, sesli olarak sorularını sorabilir ve AI asistan, GPT-3 modeli aracılığıyla cevaplar verecektir.

## Özellikler

- Sesli soru sorma ve sesli cevap alma
- OpenAI GPT-3 modelini kullanarak doğal dil işleme
- Türkçe ve İngilizce dil seçeneği
- Farklı seslendirme motorları ve seslendirme dil seçenekleri

## Kullanım

1. Programı başlatın.
2. "Başlat" düğmesine tıklayarak konuşma tanıma özelliğini etkinleştirin.
3. Sesli olarak sorularınızı sorun.
4. AI asistan, GPT-3 modeli aracılığıyla cevap verecektir.

## Dil ve Seslendirme Seçenekleri

- Program, kullanıcıya Türkçe veya İngilizce dil seçeneği sunar.
- Seslendirme motorunu ve seslendirme dilini seçebilirsiniz.

## Dışa Aktarma

Konuşma geçmişinizi "Dışa Aktar" düğmesiyle metin dosyasına kaydedebilirsiniz.

## Bağımlılıklar

- PyQt5
- OpenAI Python
- SpeechRecognition
- pyttsx3

## Kurulum

1. Python'u yükleyin: [Python İndirme Sayfası](https://www.python.org/downloads/)
2. Gerekli kütüphaneleri yüklemek için terminal veya komut istemcisine şu komutu yazın:

    ```bash
    pip install PyQt5 openai speechrecognition pyttsx3
    ```

3. Programı çalıştırın:

    ```bash
    python podcai.py
    ```

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

------------------------------------------------------------------------------

||EN||

# PodcAi: AI Assistant

PodcAi is an artificial intelligence assistant with speech recognition and natural language processing capabilities using the OpenAI GPT-3 model. Users can ask questions verbally, and the AI assistant will respond using the GPT-3 model.

## Features

- Voice question asking and receiving voice answers
- Natural language processing using the OpenAI GPT-3 model
- Turkish and English language options
- Different speech engines and voice options

## Usage

1. Start the program.
2. Click the "Start" button to enable speech recognition.
3. Verbally ask your questions.
4. The AI assistant will respond using the GPT-3 model.

## Language and Voice Options

- The program provides users with the option to choose Turkish or English.
- You can choose the speech engine and voice language.

## Export

You can save your conversation history to a text file with the "Export" button.

## Dependencies

- PyQt5
- OpenAI Python
- SpeechRecognition
- pyttsx3

## Installation

1. Install Python: [Python Download Page](https://www.python.org/downloads/)
2. Run the following command in the terminal or command prompt to install the required libraries:

    ```bash
    pip install PyQt5 openai speechrecognition pyttsx3
    ```

3. Run the program:

    ```bash
    python podcai.py
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
