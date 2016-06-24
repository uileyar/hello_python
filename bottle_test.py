#!/usr/bin/env python
# coding:utf-8

# pip install bottle-redis
# pip install bottle-mongo

import bottle
from bottle import Bottle, run, abort, request, response, template, static_file, redirect, route

from bottle_redis import RedisPlugin
from bottle_mongo import MongoPlugin

app = Bottle()

app.install(RedisPlugin(host='localhost', port='6379', keyword='rdbt'))
app.install(MongoPlugin(uri="mongodb://127.0.0.1", db="mydb", json_mongo=True))


@app.route('/redis/<id:int>')
def hello(id, rdbt):
    v = rdbt.get(id)
    if v:
        return 'get ' + str(id) + ' = ' + str(v)
    else:
        v = id*10
        rdbt.set(id, v)
        return  'set ' + str(id) + ' = ' + str(v)


@app.route('/mongo/<id>')
def hello(id, mongodb):
    item = mongodb.test.find_one({'id': id})
    if item:
        return 'get mongo=' + str(item)
    else:
        info = {'id': id, 'v': id * 10}
        mongodb.test.insert(info)
        return 'set mongo=' + str(info)


# main 在实际部署时不会执行
def main():
    port = 8888
    host = '0.0.0.0'
    run(host=host, port=port, app=app, debug=True, reloader=True)


if __name__ == "__main__":
    main()
