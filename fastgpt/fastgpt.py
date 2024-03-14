# -*-coding: utf-8 -*-
# @Time: 2024/2/18 16:09
# @Author: debug
# @Email:debug@hi.want.net

from config import *
import requests
class Fastgpt:
    def create_text_set(self,content,name="test"):
        # authorization = FASTGPT_TOKEN
        headers = {
            'Authorization': 'Bearer authorization'.replace('authorization',FASTGPT_TOKEN),
            'Content-Type': 'application/json',
        }
        json_data = {
            'text': content,
            'datasetId': '65d1bf7c6182151f0cc132b2',
            'parentId': None,
            'name': name,
            'trainingType': 'qa',
            'chunkSize': 8000,
            'chunkSplitter': '',
            'qaPrompt': '11',
            'metadata': {},
        }

        # url = 'https://localhost:3000/api/core/dataset/collection/create/text'.replace("https://localhost:3000",FASTGPT_URL)
        url = "http://8.222.137.190:3000/api/core/dataset/collection/create/text"
        response = requests.post(url, headers=headers, json=json_data,verify=False).json()
        print(response)

    def complete_chat(self,prompt):
        #使用默认的fastgpt
        headers = {
            'Authorization': 'Bearer authorization'.replace('authorization', FASTGPT_APP),
            'Content-Type': 'application/json',
        }
        json_data = {
            'chatId': 'sdasdasdasd',
            'stream': False,
            'detail': False,
            'messages': [
                {
                    'content': prompt,
                    'role': 'user',
                },
            ],
        }

        response = requests.post('http://8.222.137.190:3000/api/v1/chat/completions', headers=headers, json=json_data,verify=False)
        data = response.json()
        res_lst = []
        res_val = data["choices"][0]["message"]["content"]
        res_lst.append(res_val)
        return res_lst

        # return response

if __name__ == '__main__':
    # prompt = "hello "
    prompt = """
    finish this sub-section use html format output
    <Comparison with Other Molding Processes>
    Differences between compression molding and injection molding
    Material flow, tooling, production capacity, and precision
    Comparison with transfer molding
    Process similarities and differences in material pressurization
    """
    fastgpt = Fastgpt()
    res = fastgpt.complete_chat(prompt)
    # res = fastgpt_chat(prompt)
    a = 1
    # create_text_set('sssssss')
