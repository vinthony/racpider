# racpider
a spider framework base on python

## getting start

```shell
./run.sh
```


## feature

* `Racpider.json` to config the project
* easy to use
* using python decorator and regexp to fetch the selected url
* you can only config one file to fetch the website
* spider commond line
* you can use build-in html parse or beautiful soup or something else.
* you can config the database if you have to
* an interactor init process using `racpider init`
* a command base on one file or base on the whole project
* using `orm` to deal with the database (NoSQL or related-SQL) you don't need to 
care about the low level of database engine.
* using decorator `@api` to make return value a json
* add some arguments to fetch data to a json file or xml file
* have beautiful web client ,dragging to build returning api
* using `racpider install` to update the necessary libraries which is defined in config  

## hence
- [ ] `cil`程序

## todo
- [x] 去掉url的hash
- [x] 增强filter功能，修复match为search
- [x] 将error信息放入error.log中
- [ ] 增加分布式功能
- [ ] 爬虫网页命名
- [ ] 层次爬虫or页面爬虫
- [ ] 优先级queue
- [ ] 重新组织项目
- [x] 增加`racpider.json`来配置
- [ ] 增加默认racpider
- [ ] 数据库配置
- [ ] 获取超时
- [ ] 配置顶层目录
- [ ] `[bug]`racpider.json 无法输入正则
- [ ] `[bug]`filename too long 
- [ ] 多重结束条件，时间/层次/抓取的总任务数/指定任务页
- [ ] 多线程
