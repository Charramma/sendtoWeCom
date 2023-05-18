from flask import Flask, request
import json
import requests

app = Flask(__name__)


def get_config(config):
    """
    Read configuration information from a configuration file
    :param config: The path to the configuration file
    :return: configuration information
    """
    with open(config, 'r') as f:
        return json.load(f)


config = get_config('./config.json')


def msg_filter(req):
    content = json.loads(req)
    msg = {
        "Title": content['ruleName'],
        "Message": content['message'],
        "evalMatches": content["evalMatches"],
        "State": content['state']
    }
    return json.dumps(msg, indent=4, ensure_ascii=False)


@app.route(config["route"], methods=['POST'])
def get_grafana_request():
    req = request.get_data(as_text=True)
    send_to_WeCom(msg=msg_filter(req))
    return "Received the POST request."


def get_token(cropid, secret):
    """
    Get Token
    :param cropid:
    :param secret:
    :return:
    """
    GURL = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={cropid}&corpsecret={secret}"
    response = requests.get(GURL)
    return response.json().get('access_token')


def send_to_WeCom(msg):
    token = get_token(cropid=config['wecom']['cropid'], secret=config['wecom']['secret'])
    send_body = {
        "touser": config['wecom']['touser'],
        "toparty": config['wecom']['toparty'],
        "agentid": config['wecom']['agentid'],
        "msgtype": "text",
        "text": {
            "content": msg
        },
        "safe": 0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0
    }
    send_json = json.dumps(send_body, indent=4)
    send_url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token}"
    response = requests.post(send_url, data=send_json, headers={'Content-Type': 'application/json'})
    response.raise_for_status()


if __name__ == '__main__':
    app.run(host=config['bind'], port=config['port'])

