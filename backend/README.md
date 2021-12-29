# Useful resources
- API Documentation: [here](https://documenter.getpostman.com/view/18831621/UVRGF4Pi)
- Backend Plan Doc: [here](https://docs.google.com/document/d/1xH0LKhaQSp-aiNjJPbK_I6Zl_LmEJh32MQlc6zEkXpk/edit)
# How to run the backend locally?

## For MacOS

1. Install MongoDB using [this](https://docs.mongodb.com/manual/installation/) link
Note: You can also install MongoDB Compass to get a graphical interface to interact with the DB
2. Activate the backend virtual environment by running the following command from `backend/`
```
source env/bin/activate
```
3. Install all python libraries required by using the following command from `backend/`
```
python3 -m pip install -r requirements.txt
```
4. Run `python3 run.py` from `backend/` to start the backend server. This will generally run the backend server on `localhost:5000` so you can start testing the API by sending requests here. In case, the server is not hosted on this port, please check the terminal output from the command to see the appropriate port.

Feel free to reach out to Aman in case you find it hard to get the local backend up and running. 

Please refer to [this](https://docs.google.com/document/d/1xH0LKhaQSp-aiNjJPbK_I6Zl_LmEJh32MQlc6zEkXpk/edit?usp=sharing) google doc for the backend plan


