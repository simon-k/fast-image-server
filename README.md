# image-server
Experimental API for hosting images.

## Requirements
Running on python 3.7.0
Using FastAPI and Uvicorn

## Run the code
### Locally
Install FastAPI and it's dependencies, like Uvicorn
```
pip install fastapi[all]
```

Run the app using uvicorn
```
uvicorn main:app --reload
```

## Examples
Put images in the images folder, and get them by running ```localhost:8000/images/[imagename]```

For example

```
http://localhost:8000/images/elmo.jpg
```
