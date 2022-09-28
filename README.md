# ai_detection_backend

1.2 项目目录
```shell
ai_detection_backend/
|—ai_detection_backend/		#后端项目目录
	|—logs/				#项目运行时/开发时的日志目录
	|—manage.py			
	|—luffyapi/			#项目主应用，开发时的代码保存
	|	|—apps/			#开发者的代码保存目录，以模块[子应用]为目录保存
	|	|—libs/			#第三方内裤的保存目录[第三方组件、模块]
	|	|—settings/			
	|		|—dev.py		#项目开发时的本地配置
	|		|—prod.py		#项目上线时的运行配置
	|	|—urls.py	#总路由
	|	|—utils		#多个模块[子应用]的公共函数类库[自己开发的组件]
	|_scripts/		#保存项目运行时的脚本文件
```
### 测试环境中需要注意的配置项

#### 数据库配置： 

mysql: 5.7.25版本

数据库名: luffy

用户名和密码在/settings/dev.py 文件中的DATABASES下设置。

#### pycharm中的配置环境（manage)

Parameters: runserver api.luffycity.cn:8000      # 其中 api.luffycity,cn是自己在C盘host文件中设置的   api代表后端域名，www代表前端域名

```
127.0.0.1  api.luffycity.cn
127.0.0.1  www.luffycity.cn
```


