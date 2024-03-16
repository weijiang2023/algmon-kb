from openai import OpenAI

client = OpenAI()

# Read file name from a file called image_list
image_list_file = './image_list'
with open(image_list_file, 'r') as file:
    image_list = file.readlines()
    # Remove any extra whitespace or newline characters
    image_list = [line.strip() for line in image_list]
print(len(image_list))

for image_url in image_list:
    # {"type": "text", "text": "Assume you are a junior fashion buyer, what's in the image"},
    print("Process", image_url)
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "假设你是一个初级买手，从图中看到什么？"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    print(response.choices[0])
