from openai import OpenAI
import os

os.environ['OPENAI_API_KEY'] = "S3D3nBz84NMfBDS47wPcAjOiTJ9Hx23Nd8WZs0MIESSYXEqm-UWK_g_qcMorlBxHW9Ru0z6YVDT3BlbkFJh3bCojRnqEYHBO7QMbqcPeGIF2LDWtEWNGoWXr28pWnGsDS9VBpNUVqjMc_N6vVc7NZZTHKHAA"

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)