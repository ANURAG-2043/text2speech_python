from gtts import gTTS
abc = open('/Users/dailyAnurag/Desktop/py prjs/python2/sample.txt')
text = abc.read()
language = 'en'
obj = gTTS(text = text,lang=language,slow=False)
obj.save("sample.mp3")
