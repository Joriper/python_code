########### How to Setup project on local machine ########

1. Install Gitbash for windows/10/8
2. Get clone from github [git clone]
3. Go to the Directory of project
4. In .env file paste your mongo string in MONGO_CONNECTION
5. Run Command ["pip install -r requirements.txt"]
6. Then Run ["python3 run.py {YOUR LOCAL IP} {YOUR LOCAL PORT} -> python3 run.py 0.0.0.0 8888]
7. Open the browser and go to the [Example: http://0.0.0.0:8888/docs/]

############## API Routes from Items and clocks ###########

1. POST /items -> to Create a items
2. GET /items/filter -> to Filter the Items based on parameters
3. GET /items/{id} -> to Get the Item from id
4. DELETE /items/{id} -> to Delete the Item from id
5. PUT /items/{id} -> to update the items based on parameters

1. POST /clock-in -> to crate a clock based on parameters
2. GET /clock-in/filter -> to filter a clock based on parameters
3. GET /clock-in/{id} -> to get the clock
4. PUT /clock-in/{id} -> to update the clock
5. DELETE /delete-in/{id} -> to delete the clock


