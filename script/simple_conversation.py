from langchain.llms import OpenAI
# option 1:
# https://api.openai-365pro.com/v1
# sk-dLEQRqK3WcT9SHl2XiyJGbP4DZsfuAxr7BMjhn5vOY8z6aI
# status check:
# 
# option 2:
# https://api.link-ai.chat/v1/
# Link_uzmfmWsBHkUbrflrcK8O2TpyLFujSm8DMCV3gfGei7
# status check:
#
# option 3:
# the official openai site

api_base = "https://api.openai-365pro.com/v1"
api_key = "sk-dLEQRqK3WcT9SHl2XiyJGbP4DZsfuAxr7BMjhn5vOY8z6aI"

#api_base = "https://api.link-ai.chat/v1/"
#api_key = "Link_uzmfmWsBHkUbrflrcK8O2TpyLFujSm8DMCV3gfGei7"
llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.9, openai_api_base=api_base, openai_api_key=api_key)
text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text)) # SockSpectrum
