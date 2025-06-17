# Usage Guide

## Script Structure
Scripts are JSON objects where each key represents an engine:
```json
{
  "engine_name": engine_specific_configuration
}
```

## Environment Variables
Use `${VAR}` syntax in strings for variable expansion:
```json
{
  "cmd": ["echo", "${MESSAGE}"],
  "env": {"MESSAGE": "Hello"}
}
```

## Custom Engines
Register additional engines during initialization:
```python
from seqript import Seqript

def custom_engine(seqript, **kwargs):
    print(f"Custom engine called with {kwargs}")

seqript = Seqript(engines={
    "custom": custom_engine,
    **Seqript._DEFAULT_ENGINES
})
```