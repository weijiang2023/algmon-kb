from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="Here is the story image of the young wizard Lila casting her grand spell, with words turning into magical light to protect the land of Lexiconia. The ancient library can be seen in the background, and a beautiful protective dome of words is being created above them.",
  #prompt="Create an illustration for a children's story titled 'The Curious Little Robot'. In the center of the image, there should be a cute, small robot with a friendly appearance named Toby. He is exploring a vibrant city filled with colorful buildings and futuristic technology. Toby should look curious and determined, with gears and tools attached to him, indicating his ability to learn and adapt. The backdrop of the scene should be a lively urban environment with larger robots in the background, busy with their tasks, but looking down at Toby with a sense of pride and encouragement. Please ensure the image has a warm, inviting atmosphere and is appropriate for a children's book. The aspect ratio should be 16:9.",
  n=1,
)

image_url = response.data[0].url
print(image_url)
