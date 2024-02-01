# input: a vertical domain query like what are the words from nce1 lesson 73
# datafiles: ./data/nce1.lession73.md ./data/nce1.lesson74.md
# computation: your time
# output: the words are the following ...

# iteration 1
#def read_md(lesson_file):
#    with open (lesson_file, "r") as file:
#        return file.read()

##main
#print("Hello Assistant")
#print("What are the words from nce1 lesson 73")
#lesson_file = 'script/data/nce1.lesson74.md'
#lesson73_words = read_md(lesson_file)
#print(lesson73_words)


# iteration 2, ask for file name, automatically select correct file, try to understand input users intention, error message upon invalid request
#def read_lesson():
    #move input ask inside function
    #instead of asking for exact input, append number given into file name
#    lesson_number = input("please give the lesson number you are looking for ")
#    lesson_file = "script/data/nce1.lesson" + lesson_number + ".md"
    #try except method to handle invalid inputs
#    try:
#        with open (lesson_file, "r") as file:
#            return file.read()
#    except FileNotFoundError:
#        print("The lesson you are looking for cannot be found")

##main
#print("Hello Assistant")
#print("What are the words from nce1 lesson 73")
#lesson73_words = read_lesson()
#print(lesson73_words)

# iteration 3, word defintions, chinese translations, sentence examples
#need subprocess library to install nltk for defintions
import subprocess

def read_lesson():
    lesson_number = input("please give the lesson number you are looking for ")
    lesson_file = "script/data/nce1.lesson" + lesson_number + ".md"

    #try except method to handle invalid inputs
    try:
        with open (lesson_file, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("The lesson you are looking for cannot be found\n")

def any_questions():
    #loop to ask for more word defintions
    more_information_ask = "yes"
    while more_information_ask == "yes":
        ask_question = input("type a word you would like more information on \n" )
        try:
            word_definitions_examples_translations(ask_question)
            more_information_ask = input("would you like to know more about another word?\n")
        except FileNotFoundError:
            print("cannot find word")

#create function that can pull definitions and sentence examples
def word_definitions_examples_translations(word):
    import nltk
    from nltk.corpus import wordnet
    nltk.download('wordnet')
    import jieba
    from translate import Translator

    word_synsets = wordnet.synsets(word)
    if not word_synsets:
        print("word info not found")
        return
    translated_language = Translator(to_lang = "zh")
    translation = translated_language.translate(word)
    #the printed outputs of the function
    print("\n")
    print(translation)
    print("\n")
    print(word_synsets[0].definition())
    print("\n")
    print(word_synsets[0].examples())
    print("\n")
    return

##main
#to create these defintions and translations, import external libraries
subprocess.run(['pip', 'install', 'nltk', 'translate'], check=True)
print("Hello Assistant")
print("What are the words from nce1 lesson 73")
lesson73_words = read_lesson()
print(lesson73_words)
any_questions()

#iteration 4 , https://www.algmon.com/docs/rag/intro incorporate RAG,
#patent innovation point, integrate knowledge in real time, precise information retrieval technique
