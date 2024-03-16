import random
from gtts import gTTS
import time

# The words to be used in the dictation, in their original order
words = ["苹果", "雪梨", "香蕉"]

# Shuffling the words to randomize the order
random.shuffle(words)

# Creating the text with pauses for the audio
text_with_pauses = " ".join([word + ".........，" for word in words])
print(text_with_pauses)

# Generating the speech
tts = gTTS(text_with_pauses, lang='zh-cn')
tts.save("./dictation.mp3")


'''
from gtts import gTTS


def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")


# Example usage:
if __name__ == "__main__":
    text = "Hello, welcome to the world of Text to Speech."
    text_to_speech(text, 'en')
'''
