# TestCases Rule

## 1）有四个一级关键字；name,request,params,validate和可选account

## 2）在request关键字下包括二级关键字；method，headers,baseUrl,router和多个可选关键字

## 3）传参方式

### 1.如果是get请求，通过params或url传参

### 2.如果是post请求，传json通过data关键字传参，传表单通过data关键字

### 3.如果是文件格式，通过files关键字传参，如

        files ： 
                meida： "C:\founder.png"

## 4）如果做接口关联，必须使用一级关键字：config，框架支持json提取和正则提取

### 提取

    1.json提取 如：
        config：
            access_token: access_token
    2.正则表达式提取 如:
        config:
            access_token: '"access_token":"(.*?)"'

### 取值

    如： 
        ${get_config_data{access_token}}

## 5) 热加载 当yaml需要使用动态参数时，可以在readParams.py文件中调用

## 6) 两种断言方式：equals 和 contains

    如：
    validates：
        equals：
            code:1
        contains:
            - access_token