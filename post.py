import requests
import  json

def get_translate_data(word=None):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    Form_data = {'i': word,
  'from': 'AUTO',
  'to': 'AUTO',
  'smartresult': 'dict',
  'client': 'fanyideskweb',
  'salt': '15629866146500',
  'sign': '3980757ebe914c2d22649888361da473',
  'ts': '1562986614650',
  'doctype': 'json',
  'version': '2.1',
  'keyfrom': 'fanyi.web',
  'action': 'FY_BY_REALTlME'}
    #请求表单数据
    response = requests.post(url, data = Form_data)
    #讲JSON格式字符串转自字典
    content = json.loads(response.text)
    #打印翻译后的数据
    print(content['translateResult'][0][0]['tgt'])


if __name__ == '__main__':
    get_translate_data('傻子')
