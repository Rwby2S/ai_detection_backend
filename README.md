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
