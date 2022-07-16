# Simple HTML5 boilerplate console utility
*By barbiewir3 ❤️*

## Quick review:
- **It's a console script ( See all available commands simply typing *-h* )**
- ***Script is written fully in Python***
- ***Script Don't demands any side packages***
- ***Could be scaled by adding additional files -very easy***

## Structure You'll get by default:
![](../../Desktop/boiler.png)

You can see a nice, pretty simple boilerplate for your project \
\
***Note: Don't forget it could be customized by adding a few new instances*** \
*util.py:*

```python
import contents
from managment import BaseFileCreator  # class ancestor


class HTMLFileCreator(BaseFileCreator):
    content = contents.HTML  # content that will be displayed in file 
    name = 'index.html'  # name of the file and extension
    represent_in_dir = False  # create an additional folder (see the screen above: css folder) 
                              

class JSFileCreator(BaseFileCreator):
    content = ''
    name = 'script.js'

    
class CSSMainFileCreator(BaseFileCreator):
    content = ''
    name = 'styles.css'
    represent_in_dir = True
```
Hopefully it was straight enough... 

# Happy coding 👾