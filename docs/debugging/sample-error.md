# Sample Error Supression

```py
try:
    micropython.schedule(self.call_handlers, Rotary.ROT_CW)
except RuntimeError:
    pass # ignore the error
```