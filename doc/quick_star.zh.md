# 快速开始

## 基本用法

1. 创建脚本文件 (`example.json`):
```json
{
  "seq": [
    {"comment": "我的第一个脚本"},
    {"sleep": 2},
    {"cmd": ["echo", "你好世界"]}
  ]
}
```

2. 执行脚本:
```python
from seqript import Seqript

seqript = Seqript(name="example")
with open("example.json") as f:
    seqript(**json.load(f))
```

## 可用引擎
- `seq`: 顺序执行
- `par`: 并行执行
- `cmd`: 命令执行
- `nop`: 空操作
- `sleep`: 延迟执行
- `comment`: 打印消息