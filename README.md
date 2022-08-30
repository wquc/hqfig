# hqfig
High quality figure setup for matplotlib plotting

### Installation
```
pip install git+https://github.com/wquc/hqfig
```

### Usage
```python
import matplotlib.pyplot as plt
import numpy as np
import hqfig

hqfig.setup_aesthetics()
color_list = hqfig.get_color_list()

x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, color=color_list[1], label='Y1')
plt.plot(x, y2, color=color_list[2], label='Y2')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('test.png', dpi=300, bbox_inches='tight')
```
