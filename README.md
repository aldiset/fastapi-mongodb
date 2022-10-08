# fastapi-mongodb
How to connect fastAPI to MongoDB

## MongoDB 
- https://hub.docker.com/_/mongo
- ```docker pull mongo```
- ```docker run -d -it -p 27017:27017 mongo:tag```

## Install dependencie
- Move to directori project (/fastapi-mongodb)
- run 
``` pipenv install ```
- is done, you can type
``` pipenv shell ```

## Run FastAPI
- ``` uvicorn mani:app --reload --port 80 (or your port wont) ```
