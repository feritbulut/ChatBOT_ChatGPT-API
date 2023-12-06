import os

import openai
import gradio as gradio

openai.api_key = 'YOUR_CHATGPT_APIKEY'
#chatgpt_API

def clean_textbox(*args):
    n = len(args)
    return [""] * n


class ChatGPT:
    def _init_(self):
        self.messages = [{'role': 'system', 'content': "You are now a very useful maid assistant! If you have a question you can't answer, please reply with I can't answer this question"}]

    def reset(self, *args):
        self.messages = [{'role': 'system', 'content': "You are now a very useful maid assistant! If you have a question you can't answer, please reply with I can't answer this question"}]
        return clean_textbox(*args)

    def chat(self, prompt):
        self.messages.append({"role": "user", "content": prompt})
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            temperature=0.7
        )
        res_msg = completion.choices[0].message["content"].strip()
        self.messages.append({"role": "assistant", "content": res_msg})
        return res_msg


if _name_ == '_main_':
    my_chatgpt = ChatGPT()
    with gr.Blocks(title="BIGBRAINS") as demo:
        gr.Markdown('''
        # ChatBot EXPORT LAW ASSISTANT (ELÂ) 
                ''')

        with gr.Row():
            with gr.Column(scale=9):
                prompt = gr.Text(label='ChatGPT_Prompt', show_label=False, lines=3,
                                 placeholder='Giriş...')
                res = gr.Text(label='ChatGPT_result', show_label=False, lines=3,
                              placeholder='Sonuc...')

            with gr.Column(scale=1):
                btn_gen = gr.Button(value="Gönder", variant='primary')
                btn_clear = gr.Button(value="Konuşmayı temizle")

        gr.Examples([
            ["ready prompt1"],
            ["ready prompt2"],
            ["ready prompt3"],
            ["ready prompt4"]],
            inputs=[prompt],
            outputs=[res],
            fn=my_chatgpt.chat,
            cache_examples=False)

        gr.Markdown('''
                        # ChatBot by Ferit BULUT
                                ''')

        btn_gen.click(fn=my_chatgpt.chat, inputs=prompt,
                      outputs=res)
        btn_clear.click(fn=my_chatgpt.reset,
                        inputs=[prompt, res],
                        outputs=[prompt, res])

    demo.queue()
    demo.launch()