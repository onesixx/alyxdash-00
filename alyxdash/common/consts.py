# JWT_SECRET = "ABCD1234!"
# JWT_ALGORITHM = "HS256"
# EXCEPT_PATH_LIST = ["/", "/openapi.json"]
# EXCEPT_PATH_REGEX = "^(/docs|/redoc|/api/auth)"
# MAX_API_KEY = 3
# MAX_API_WHITELIST = 10

# from app.common.consts import MENU_ITEMS
import os
# MENU_ITEMS = [
#     "home",
#     "basic_cards", "social_cards", "tab_cards",
#     "basic_boxes", "value_boxes",
#     "gallery_1", "gallery_2"
# ]


folder_path = '/home/oschung_skcc/my/git/alyxdash/pages/'
MENU_ITEMS = []
for entry in os.listdir(folder_path):
    # '__pycache__':
    if os.path.isdir(os.path.join(folder_path, entry)) and entry[0] != '_':
        MENU_ITEMS.append(entry)

print(MENU_ITEMS)
