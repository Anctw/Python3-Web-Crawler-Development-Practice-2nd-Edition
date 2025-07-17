## 一、下载

在以下地址下载zip文件解压缩，放到合适的目录

Download Elasticsearch | Elastic：https://www.elastic.co/cn/downloads/elasticsearch

此时下载的版本为8.17.4

## 二、启动

windows可直接点击bin目录下 elasticsearch.bat 文件，此时出现了第一个bug。

![image](.\250402191452.png)

```shell
warning: ignoring JAVA_HOME=D:\Environment\Java\jdk17; using bundled JDK

# 本地的jdk（jdk17.0.12）不可用，使用es中自带的jdk，也启动失败了
```

## 三、解决方案

#### 第一步

在es文件中添加记录日志的文件

```
\logs\elasticsearch.log
```

##### 尝试第一种方法

在网上搜了好多类似的情况，尝试通过修改elasticsearch-env.bat文件（失败）

##### 尝试第二种方法

升级jdk17.0.12——>jdk17.0.13（失败）

#### 第二步

通过查看日志分析

```shell
# 命令行显示
hjava.nio.file.NoSuchFileException: D:\WEAVER\Resin\lib\resin.jar
# 日志中 
java.nio.file.NoSuchFileException: D:\WEAVER\Resin\lib\resin.jar

# 启动Elasticsearch 命令
/bin/elasticsearch.bat 

# 发现自己目录里面没有这个文件
# 这个东西在环境变量 CLASSPATH中，因为CLASSPATH中就这一个变量值，我直接把把CLASSPATH删了
#  删掉之后命令行输出一大堆东西像是启动了
```



![image](.\250402193349.png)

#### 第三步

访问localhost:9200显示

<img src=".\250402194752.png" alt="image" style="zoom: 25%;" />

命令行输出 ：是因为ES8默认开启了 SSL 认证。

![image](.\250402195305.png)

因为 SSL 需要使用https方式请求，所以有以下两种解决办法：

**第一、使用 https 发送请求，即：把 http 请求改成 https 即可。**

1.需要登录用户名和密码

2.正常情况第一次的启动的时候会初始化一个密码 用户名默认**elastic**，但是由于日志文件中找不到，所以进行重置

3.进入es安装目录的**bin文件**中执行一下命令会返回最新的密码

命令 : elasticsearch-reset-password -u elastic

```
New value: vu3gHUi-52jDoHrtLbs-
```

![image](.\250402201453.png)

**第二、修改配置文件，需要修改配置文件则继续往下看。**

```shell
elasticsearch\elasticsearch-8.17.4\config\elasticsearch.yml
# 将
xpack.security.enabled: true
# 改为
xpack.security.enabled: true
```

![image](.\250402195719.png)

#### 第四步

下图显示正常访问

![image](.\250402200056.png)