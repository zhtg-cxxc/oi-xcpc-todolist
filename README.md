# todolist
Argon Design 的 Todo List 工具，刷题的得力伙伴。

### Feature

1. 简洁清爽的 UI ，使用现代感十足的 Argon Design 框架；
2. ~~在浏览器中打开并编辑 Todo List ，而不是像 memset0 之前那个项目一样需要手改配置文件。~~ 由于该项目需要考虑部署在公网服务器的情况，所以正在调整该项功能，预期将会把展示界面与修改界面分离；
3. 支持常见的各大 OJ ，现在已有 ~~UOJ / LOJ / BZOJ~~ （UOJ/LOJ未经测试，想用需要暂时手动解除注释）/ 洛谷 ，将会马上添加 CF / Vjudge；
4. 支持获取其他网友的做题记录并进行比较，也可以用于机房的题目交流；
5. OJ爬虫做对象化处理，便于快速创建自定义OJ对象，快速应用到其他基于已有开源OJ类的自建的项目。

### Usage

安装 [Python3](https://www.baidu.com/s?wd=安装python3教程) 和 [git](https://www.baidu.com/s?wd=安装git教程) 环境，然后运行命令

```shell
git clone https://github.com/zhtg-cxxc/oi-xcpc-todolist
cd oi-xcpc-todolist
pip3 install -r requirements.txt
cp -r config.sample config
```

配置 `config/user.yml`, `config/config.yml`, `config/problem.yml` 后，在项目目录运行：

```shell
python3 server.py
```

项目将可通过 [localhost:25252](http://localhost:25252) 访问。

### Todo

按计划完成的顺序排序

* [x] ~~BZOJ 的权限题爬取~~ （BZOJ早爆炸了，现在可以通过创建自定义UOJ对象爬取[黑暗爆炸OJ](https://darkbzoj.cc/)的记录，不过UOJ暂未经过测试）
* [x] 洛谷的题目名称和做题记录爬取
* [ ] CodeForces 的题目名称和做题记录爬取
* [ ] VJudge 的题目名称和做题记录爬取