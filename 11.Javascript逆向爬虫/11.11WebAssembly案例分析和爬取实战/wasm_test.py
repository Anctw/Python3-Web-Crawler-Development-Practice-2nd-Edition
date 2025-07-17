# pywasm 2.0.1
# python 3.11
import pywasm
import time
import requests


"""1.pywasm库"""
# Test01
# runtime = pywasm.core.Runtime()
# m = runtime.instance_from_file('./Wasm.wasm')
# result = runtime.invocate(m, 'encrypt', [1, 2])
# print(result)


# Test02
# BASE_URL = 'https://spa14.scrape.center'
# TOTAL_PAGE = 10
#
# runtime = pywasm.core.Runtime()
# m = runtime.instance_from_file('./Wasm.wasm')
# for i in range(TOTAL_PAGE):
#     offset = i * 10
#     sign = runtime.invocate(m, 'encrypt', [offset, int(time.time())])[0]
#     url = f'{BASE_URL}/api/movie/?limit=10&offset={offset}&sign={sign}'
#     # print(url)
#     response = requests.get(url)
#
#     print(response.json())


"""2.wasmer库 不支持python3.11"""
# Test01
# from wasmer import engine, Store, Module, Instance
# from wasmer_compiler_cranelift import Compiler
# store = Store(engine.JIT(Compiler))
# module = Module(store, open('Wasm.wasm', 'rb').read())
# instance = Instance(module)
# result = instance.exports.encrypt(1, 2)
# print(result)




