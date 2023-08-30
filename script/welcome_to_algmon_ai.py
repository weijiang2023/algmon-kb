import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")

req = "请简单介绍算法妈妈这家公司"
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": req}
  ]
)

#print(completion.choices[0].message.encode('utf-8').decode('unicode_escape'))
res = completion.choices[0].message
print("请求：", req)
print("回答：", res["content"])

'''
请求： 请简单介绍棉花糖王国和他的校长
回答： 算法妈妈是一家公司，专注于算法和数据科学领域。他们致力于为企业提供高质量的数据分析和机器学习解决方案。算法妈妈的团队由一群热爱数据和算法的专家组成，他们拥有丰富的行业经验和技术知识。无论是帮助企业构建预测模型、优化业务流程还是提供数据可视化工具，算法妈妈都能够提供定制化的解决方案，帮助企业实现更好的业务结果。所以，算法妈妈不仅仅是一个具体的产品或服务，而是一个专业团队，为企业提供数据科学和算法方面的支持和咨询。
'''