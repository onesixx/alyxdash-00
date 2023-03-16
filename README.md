# AlyxDash
AlyxDash is a Python package that does something really useful.

## Installation
You can install AlyxDash using pip:
pip install -e .


## Usage
Here's an example of how to use AlyxDash:
```python
import alyxdash

# Do something with AlyxDash

This README file includes a brief description of the package, instructions for installing and using the package, a section on contributing to the package, and a statement on the package's license. 

Feel free to modify the contents of the README file to suit your needs and to accurately describe your package's functionality.

pip install -r requirements.txt



# dash-fasta
based rusnyder / fastapi-plotly-dash

# How to add a dash page 
> example> add menu stock plot
## 1. Make a new folder(stock) and files 
- dashPages/stock
- dashPages/stock/view.py
- dashPages/stock/model.py
- dashPages/stock/callbacks.py

==================
## 2 Insert a view path to /ui/main.py    alyxdash/templates.py
자동화 되어 skip가능.
```
import dashPages.stock.view
body = dac.Body(
    dac.TabItems([
        #dashPages.home.view.content,
        dashPages.stock.view.content,
    ])
)
```
# 3. 사이드바 
사이드바는 필요시 수동으로 추가.
## 3-1. Make sidebar to /ui/sidebar.py   alyxdash/templates.py
```
sideMenu = 	dac.SidebarMenu(
    [ ...   
        dac.SidebarHeader(children="etc."),
        dac.SidebarMenuItem(id='menu_stock', label='Stock plot',  icon='desktop'),
    ]
)
```

## 3-1. modify input, output callback /ui/sidebar_callbacks.py
자동화됨.
```
...
MENU_ITEMS = ( "basic_cards", "social_cards", "tab_cards", 
               "basic_boxes", "value_boxes",
               "gallery_1", "gallery_2",
               "Stock")
def update_breadcrumbs( nClick1, nClick2, nClick3, nClick4, nClick5, nClick6, nClick7, nClick8,
    basic_cards, social_cards, tab_cards, basic_boxes, value_boxes, gallery_1, gallery_2, stock ): 
....

```




## 4. add callbacks path to /routes.py 
????
```
from dashPages.stock.callbacks import update_graph
```