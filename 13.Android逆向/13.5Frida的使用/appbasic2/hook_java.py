import frida
import sys

CODE = open('hook_java.js', encoding='utf-8').read()
# PROCESS_NAME = 'com.germey.appbasic1'
PROCESS_NAME = 'Appbasic2'


def on_message(message, data):
    print(message)

print('open1')

process = frida.get_usb_device().attach(PROCESS_NAME)

print('open2')
print(process)
script = process.create_script(CODE)
script.on('message', on_message)
script.load()
sys.stdin.read()
