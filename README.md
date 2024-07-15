# FastAPI Udemy course project

## How to run the app

1. Install required package

```
pip install -r requirements.txt
```

2. Start a server

There are different commands for starting a server

```
uvicorn books:app --reload
```

Newer way of starting server, only supported in newer version of FastAPI

```
fastapi run books.py
```

Running dev server.

```
fastapi dev books.py
```

The fastapi command uses uvicorn under the hood. 
