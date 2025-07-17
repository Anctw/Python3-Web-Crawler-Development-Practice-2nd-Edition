
"""3.实例引入"""
"""4.splash Lua脚本"""
# 入口及返回值 (Lua语言)
# function main(splash, args)
# 		splash:go("http://www.baidu.com")
#   	splash:wait(0.5)
#   	local title = splash:evaljs("document.title")
#   	return {title=title}
# end

# 异步处理 (Lua语言)
# function main(splash, args)
#     local example_urls = {"www.baidu.com", "www.taobao.com", "www.zhihu.com"}
#     local urls = args.urls or example_urls
#     local results = {}
#     for index, url in ipairs(urls) do
#         local ok, reason = splash:go("http://" .. url)
#         if ok then
#             splash:wait(2)
#             results[url] = splash:png()
#         end
#     end
#     return results
# end

"""5.splash对象的属性"""
# args属性 (Lua语言)
# function main(splash, args)
#     local url = args.url
# end
#
# function main(splash)
#     local url = splash.args.url
# end

# js_enabled (Lua语言)
# function main(splash, args)
#    splash:go("https://www.baidu.com")
#    splash.js_enabled = false
#    local title = splash:evaljs("document.title")
#     return {title=title}
# end

# resource timeout属性 (Lua语言)
# function main(splash, args)
#     splash.resource_time = 0.1
#     assert(splash:go('https://www.taobao.com'))
#     return splash:png()
# end

# images_enabled属性 (Lua语言)
# function main(splash, args)
#     splash.images_enabled = false
#     assert(splash:go("https://www.jd.com"))
#     return {png=splash:png()}
# end

# plugins_enabled属性 (Lua语言)
# splash.plugins_enabled = true/false

# scroll_position属性 (Lua语言)
# function main(splash, args)
#     assert(splash:go("https://www.taobao.com"))
#     splash.scroll_position = {y=400}
#     return {png=splash:png()}
# end

"""6.splash对象的方法"""
# go方法 (Lua语言)
# function main(splash, args)
#     local ok, reason = splash:go{"https://www.httpbin.org/post", http_method="POST", body="name=Germey"}
#     if ok then
#         return splash:html()
#     end
# end

# wait方法
# function main(splash, args)
#     splash:go("https://www.taobao.com")
#     splash:wait(2)
#     return {html=splash:html()}
# end

# jsfunc方法 (Lua语言)
# function main(splash, args)
#     local get_div_count = splash:jsfunc([[function () {
#         var body = document.body;
#         var divs = body.getElementsByTagName('div');
#         return divs.length;}
#     ]])
#     splash:go("https://www.baidu.com")
#     return ("There are % s DIVs"):format(get_div_count())
# end

# evaljs方法 (Lua语言)
# 例句：result = splash:evaljs(js)
# function main(splash, args)
#     local title = splash:evaljs("document.title")
# end

# runjs方法 (Lua语言)
# function main(splash, args)
#     splash:go("https://www.baidu.com")
#     splash:runjs("foo = function() {return 'bar'}")
#     local result = splash:evaljs("foo()")
#     return result
# end

# html方法 (Lua语言)
# function main(splash, args)
#     splash:go("https://www.httpbin.org/get")
#     return splash:html()
# end

# png方法 (Lua语言)
# function main(splash, args)
#     splash:go("https://www.taobao.com")
#     return splash:png()
# end

# jpeg方法 (Lua语言)
# function main(splash, args)
#     splash:go("https://www.taobao.com")
#     return splash:jpeg()
# end

# har方法 (Lua语言)
# function main(splash, args)
#     splash:go("https://www.baidu.com")
#     return splash:har()
# end

# url方法 (Lua语言)
# function main(splash, args)
#     splash:go("https://www.baidu.com")
#     return splash:url()
# end

# set_user_agent方法 (Lua语言)
# function main(splash, args)
#     splash:set_user_agent('Splash')
#     splash:go("https://www.httpbin.org/get")
#     return splash:html()
# end

# select方法 (Lua语言)
# function main(splash, args)
#     splash:go("https://www.baidu.com/")
#     input = splash:select("#kw")
#     input:send_text('Splash')
#     splash:wait(3)
#     return splash:png()
# end

# select_all方法 (Lua语言)
# function main(splash, args)
#     local treat = require('treat')
#     assert(splash:go("http://quotes.toscrape.com/"))
#     assert(splash:wait(0.5))
#     local texts = splash:select_all('.quote .text')
#     local results = {}
#     for index, text in ipairs(texts) do
#         results[index] = text.node.innerHTML
#     end
#     return treat.as_array(results)
# end

# mouse_click方法 (Lua语言)
# function main(splash, args)
#     splash:go("https://www.baidu.com/")
#     input = splash:select("#kw")
#     input:send_text('Splash')
#     splash:wait(3)
#     submit = splash:select('#su')
#     submit:mouse_click()
#     splash:wait(5)
#     return splash:png()
# end

"""7.调用Splash提供的API"""
# render.html(Python)
# url = 'http://192.168.81.130:8050/render.html?url=https://www.baidu.com'
# response = requests.get(url)
# print(response.text)

# url = 'http://192.168.81.130:8050/render.html?url=https://www.taobao.com&amp;wait=5'
# response = requests.get(url)
# print(response.text)

# render.png(Python)
# url = 'http://192.168.81.130:8050/render.png?url=https://www.jd.com&wait=10&width=1000&height=700'
# response = requests.get(url)
# with open('jd.png', 'wb') as f:
#     f.write(response.content)

# render.jpeg(Python)


# render.har(Python)
# url = 'http://192.168.81.130:8050/render.har?url=https://www.taobao.com&wait=5'
# response = requests.get(url)
# print(response.text)

# render.json(Python)
# url = 'http://192.168.81.130:8050/render.json?url=https://www.taobao.com&har=1'
# response = requests.get(url)
# print(response.text)

# execute(Python)
import requests
from urllib.parse import quote

lua = """
function main(splash, args)
    local treat = require("treat")
    local response = splash:http_get("http://www.httpbin.org/get")
    return {html=treat.as_string(response.body),
        url=response.url,
        status=response.status
    }
end
"""
url = 'http://192.168.81.130:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)

"""8.负载均衡配置"""
