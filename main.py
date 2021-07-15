import requests


class ChatRebot(object):
    def __init__(self, content):
        self.content = content

    def chat(self):
        url_api = "http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + self.content
        r = requests.get(url_api)
        print(eval(r.text)['content'])


if __name__ == "__main__":
    print("=====欢迎来到聊天机器人=====")
    while True:
        myContent = input(">>>")
        chatRebot = ChatRebot(myContent)
        chatRebot.chat()
