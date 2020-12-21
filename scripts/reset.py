import os
from distutils.dir_util import remove_tree

os.system("pipenv --rm")
try:
    remove_tree(os.getenv("FRONTEND_DIR", "frontend"))
    remove_tree(os.getenv("BACKEND_DIR", "backend"))
except FileNotFoundError:
    pass
