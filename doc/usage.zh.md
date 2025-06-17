# 使用指南

## 脚本结构
脚本是JSON对象，每个键代表一个引擎:
```json
{
  "engine_name": engine_specific_configuration
}
```

## 环境变量
在字符串中使用`${VAR}`语法进行变量扩展:
```json
{
  "cmd": ["echo", "${MESSAGE}"],
  "env": {"MESSAGE": "你好"}
}
```

## 自定义引擎
初始化时注册额外引擎:
```python
from seqript import Seqript

def custom_engine(seqript, **kwargs):
    print(f"自定义引擎调用参数 {kwargs}")

seqript = Seqript(engines={
    "custom": custom_engine,
    **Seqript._DEFAULT_ENGINES
})
```