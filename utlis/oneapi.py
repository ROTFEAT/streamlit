# -*-coding: utf-8 -*-
# @Time: 2024/2/23 10:30
# @Author: debug
# @Email:debug@hi.want.net
import  requests
class OneApi:
    def __init__(self, token='sk-zTPfa2jzWSgxr2Dz872fA7Aa24C1456d8a3607C7BbA91e24',model = "gpt-3.5-turbo-16k"):
        self.token = token
        self.model = model

    def complete_chat(self, content):
        res_lst = []
        while True:
            try:
                res = requests.post(url="https://api.clinetwant.net/v1/chat/completions",
                                        headers={
                                            "Authorization": self.token,
                                            "Content-Type": "application/json"},
                                        json={
                                            "model": self.model,
                                            # "model": "gpt-4",
                                            # "model": "gpt-4-1106-preview",
                                            # "temperature": 2,
                                            "presence_penalty": 2,
                                            "messages": [
                                                {
                                                    "role": "user",
                                                    "content": content
                                                }
                                            ]
                                        }
                                        , stream=False
                                        )

                data = res.json()
                res_val = data["choices"][0]["message"]["content"]
                res_lst.append(res_val)
                return res_lst
            except Exception as e:
                print(e,'请求出错oneapi')





if __name__ == '__main__':
    oneapi = OneApi() #ok了
    res = oneapi.complete_chat('hello')
    a = 1
