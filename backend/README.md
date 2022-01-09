# Useful resources
- API Documentation: [here](https://documenter.getpostman.com/view/18831621/UVRGF4Pi)
- Backend Plan Doc: [here](https://docs.google.com/document/d/1xH0LKhaQSp-aiNjJPbK_I6Zl_LmEJh32MQlc6zEkXpk/edit)
- Postman collection: [here](./ImageTransformation.postman_collection.json)
# How to run the backend locally?
### Setup environment and install all dependencies
1. Change into the backend/ directory
2. Create a virtual environment: `python3 -m venv env`
3. Activate the new environment: `source env/bin/activate`
4. Install all the third party python libs: `python3 -m pip install -r requirements.txt`
### Run the server
- Run the command: `make run-backend`

# How to run the backend locally using a local DB?
1. Install MongoDB using [this](https://docs.mongodb.com/manual/installation/) link
2. Get a local mongoDB instance running
3. Change the `MONGO_URI` in `imageTransformer/config.py` to the local URI
4. Run: `make run-backend` (or follow setup steps if server isn't setup)

# Developmental instructions
1. Everytime you use a new library, update the `requirements.txt`
Note - Can use `python3 -m pip freeze > requirements.txt` if you want to reset `requirements.txt` to all libraries currently in your environment.
2. MongoDB Compass can be used to look at your DB live
3. (HACK to be removed) If you see an error like:
```
http.py", line 851, in quote_etag
    if '"' in etag:
TypeError: argument of type 'NoneType' is not iterable
```
Please modify the quote_etag function in `*/lib/python3.9/site-packages/werkzeug/http.py", line 851, in quote_etag` to:
```

def quote_etag(etag: str, weak: bool = False) -> str:
    """Quote an etag.

    :param etag: the etag to quote.
    :param weak: set to `True` to tag it "weak".
    """
    if not etag:
        return etag
    if '"' in etag:
        raise ValueError("invalid etag")
    etag = f'"{etag}"'
    if weak:
        etag = f"W/{etag}"
    return etag

```

Please refer to [this](https://docs.google.com/document/d/1xH0LKhaQSp-aiNjJPbK_I6Zl_LmEJh32MQlc6zEkXpk/edit?usp=sharing) google doc for the backend plan
