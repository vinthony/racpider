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

## todo
- [x] 去掉url的hash
- [ ] 增强filter功能
- [ ] 将error信息放入error.log中
- [ ] 增加分布式功能
- [ ] 爬虫网页命名
- [ ] 层次爬虫or页面爬虫
- [ ] 优先级queue
- [ ] 重新组织项目
- [ ] 增加`racpider.json`来配置

