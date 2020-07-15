from jinja2 import Template
from showdata import showdata

def html():
    # time_tag = str(time.strftime("%Y-%m-%d %H:%M-%S"))
    userinfo_data = showdata()

    with open('template/08 jinja2版动态版.html', 'r', encoding='utf-8') as f1:
        data = f1.read()
    tem = Template(data)
    data = tem.render({'userinfo':userinfo_data})
    # data = data.replace('$time$', userinfo_data['name'])
    return data.encode('utf-8')

def css():
    with open('static/css/t1.css', 'rb') as f1:
        data = f1.read()
    return data

def js():
    with open('static/js/j1.js', 'rb') as f1:
        data = f1.read()
    return data

def jpg():
    with open('static/img/timg.jpg', 'rb') as f1:
        data = f1.read()
    return data

def ico():
    with open('static/img/wode.ico', 'rb') as f1:
        data = f1.read()
    return data

