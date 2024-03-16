'''
# from huggingface
from gradio_client import Client

client = Client("https://humanaigc-outfitanyone.hf.space/--replicas/o90fr/")
result = client.predict(0, api_name="/load_example")
# print(result)
'''

# from modelscope
from gradio_client import Client
client = Client(
    "https://modelscope.cn/api/v1/studio/DAMOXR/OutfitAnyone/gradio/")
result = client.predict(0, api_name="/load_example")
'''
result = client.predict(
    "null",  # str (filepath to JSON file) in 'AI Model' Label component
    # str (filepath on your computer (or URL) of image) in 'top garment' Image component
    "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",
    # str (filepath on your computer (or URL) of image) in 'lower garment' Image component
    "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",
    fn_index=3
)
'''
print(result)
