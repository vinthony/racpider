# racpider

一个使用web服务器来进行分布式的爬虫框架

核心思想如下：

![racpider](http://vinthony.u.qiniudn.com/racpider.png)

使用Redis来进行缓存队列，当有slaver发送pull请求时，redis出队列，分配一个url到slaver

slaver进行爬虫工作，将数据采用mongodb存储在本地硬盘上，并且返回新的一轮url（此处使用requests包进行http发送请求）

新的url将会push到服务器端，此时服务器端使用bloomfilter来进行重复url过滤，将不重复的url加入到redis队列中，重复此过程直至redis队列为空。

后续分析时，从slaver中逐个读取mongodb中相应数据库的collection进行分析汇总。

重写`src/analy/script.py`中的`filter`方法，将url符合提取要求的函数筛选出来

重写`src/analy/script.py`中的`parse`方法，parse方法的函数参数为`body`,使用`bs4`等进行解析或者存储

## getting start

```shell
#服务器端
./src/monitor.py

#client端
./src/slaver.py
```

## enhance

- [ ] `cil`程序

## delay

- [ ] 带cookies的爬虫(增加auth)
- [ ] 友好的web界面监控各个服务器信息
- [ ] 更加稳定的爬虫过程

## todo

- [x] 去掉url的hash
- [x] 增强filter功能，修复match为search
- [x] 将error信息放入error.log中
- [x] 增加`racpider.json`来配置
- [x] 增加默认racpider
- [x] 爬虫网页命名
- [x] 多重结束条件，时间/层次
- [x] 增加分布式功能
- [x] 数据库Queue配置(redis)
- [x] mongodb 来存储内容


## bugs
- [x] filename too long 

## questions
- [x] 如何高效的存储抓下来的网页的名称? 【使用mongodb存储】
- [x] 分布式生成的html是存在当个集群的db下？如果不这样，返回整个html和正常的过程一致

## Server
- [x] 配置redis 分配seed url 到slave
- [x] bloom filter 用来过滤已经fetch过得url
- [ ] 增加robot.txt过滤信息
- [ ] 分配url策略(一致性hash)
- [x] 采用json来传输数据

## slave
- [x] 从url接收job
- [x] 存储网页内容
- [x] url使用
- [x] `GET server/pull` 向服务器请求一个job
- [x] `GET server/push` 向服务器push一个结果


## changelog

#### 5月9日

- 增加cli入口
- fixed download为unicode类型导致无法getlink的问题
- 增加mongodb支持存入数据

#### 5月14日

- 增加服务器端数据收集功能

#### client dependence

* beautifulsoup4
* pymongo
* mongo

## server dependence

* request
* redis
* pymongo

#### 5月24日

* 使用JSON来进行传输
* 客户端增加优先级队列


## 配置文件在`Racpider.json`中
```js
{
	"seeds":["http://news.qq.com/"], //为要抓取的种子
	"regexp":"qq.com", //抓取域名的匹配正则
	"name":"qq_news", // 爬虫名称
	"redis":{  //redis配置
		"host":"127.0.0.1",
		"port":"6379",
		"db":"0"
	},
	"mongodb":{ //客户端mongodb配置
		"host":"127.0.0.1",
		"port":"20132",
		"name":"racpider"
		},
	"server":{ // web服务器配置，用来实现分布式
		"host":"192.168.31.110",
		"port":"5237",
		"debug":"False"
	},
	"auth":{ //【todo】认证
		"username":"username",
		"password":"password"
	},
	"timeout":"2",//超时时间
	"sleep":"1", //每次抓取空当时间
	"clients":[ //供master来进行分析
		{
			"host":"10.211.55.5",
			"port":"20132"
		},
		{
			"host":"10.211.55.7",
			"port":"20132"
		}
	]
}

```



## LISCENSE

The MIT License (MIT)

Copyright (c) 2015 Xiaodong Cun

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

