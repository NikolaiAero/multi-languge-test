# Hello!

**This project was created for stepik users.**

1. Add your path to chromedriver in a variable. *path_to_driver*
```
import pytest


# путь до chromedriver
path_to_driver = 'path to chromedriver'

driver_service = Service(executable_path=path_to_driver)
```
2. Run the test with this command


```
pytest -s --language=es test_items.py
```
3. Run the test with this command


```
pytest -s --language=fr test_items.py
```

😊 Thanks for watching!
