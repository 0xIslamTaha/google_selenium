# google_selenium
This is a test suite cover some basic features of google search engine and it follows the Page-Object design pattern.

## TravisCI integration:
As part of a project, It is integrated with TravisCI and here is the last [result](https://travis-ci.org/0xIslamTaha/google_selenium/builds/561453262) of executing the test suite.

## Test Suite Structure:
```bash
.
├── config.ini
├── elements.py
├── framework
│   ├── base_selenium.py
│   └── __init__.py
├── __init__.py
├── pages
│   ├── base_page.py
│   ├── __init__.py
│   ├── results_page.py
│   └── search_page.py
├── README.md
├── requirements.txt
└── testcases
    ├── base_tests.py
    ├── __init__.py
    └── test01_text_search.py
```

## Manual Execution:
If you don't like TravisCI and wanna execute it in your local machine here are the steps:

### Pre-requests:
- Chrome driver compatible with your google chrome browser

### Installation steps:
```bash
sudo apt-get install -y python3-dev python3-pip git xvfb
git clone https://github.com/0xIslamTaha/google_selenium.git
cd google_selenium
sudo pip3 install -r requirements.txt
export PYTHONPATH='./'
nosetests-3.4 -vs --logging-level=WARNING testcases --tc-file=config.ini
```
