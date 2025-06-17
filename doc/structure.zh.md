# 项目结构

## 核心组件
- `Seqript`: 解析和执行脚本的主类
- 引擎: 模块化操作 (`cmd`, `seq`, `par` 等)
- 变量扩展: `${var}` 替换系统

## 文件组织
```
seqript/
├── init.py
├── seqript.py # 主类
├── util/
│    └── expand_variable.py
└── engine/
    ├── init.py
    ├── cmd.py # 命令执行
    ├── nop.py # 空操作
    ├── par.py # 并行执行
    ├── seq.py # 顺序执行
    └── contrib/ # 额外引擎
        ├── sleep.py
        └── comment.py
```

## 扩展点
1. 添加引擎到 `engine/contrib/`
2. 初始化时覆盖默认引擎
3. 扩展变量匹配模式