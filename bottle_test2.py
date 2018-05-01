#!/usr/bin/env python
# coding:utf-8

# pip install bottle-redis
# pip install bottle-mongo

import bottle
from bottle import Bottle, run, request, response

boy = Bottle()


@boy.hook('before_request')
def before_request():
    request.user = {'name': 'boy'}
    print('boy request={}'.format(request.user))


@boy.get("/hello")
def hello():
    return "boy hello = {}".format(request.user.get('name'))

girl = Bottle()


@girl.hook('before_request')
def before_request():
    request.user = {'name': 'girl'}
    print('girl request={}'.format(request.user))


@girl.get("/hello")
def hello():
    return "girl hello = {}".format(request.user)


app = Bottle()
app.mount("v1/boy", boy)
app.mount("girl", girl)


@app.hook('before_request')
def before_request():
    request.user = {'name': 'app'}
    print('app request={}'.format(request.user))


@app.get("/hello")
def hello():
    return "app hello = {}".format(request.user)


# main 在实际部署时不会执行
def main():
    port = 8888
    host = '127.0.0.1'
    run(host=host, port=port, app=app, debug=True, reloader=True)


if __name__ == "__main__":
    main()
