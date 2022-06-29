from googletrans import Translator

translator = Translator()
upload_response = "이 문장은 한글로 쓰여졌습니다"
trans_text=translator.translate(upload_response)
print(trans_text.text)
