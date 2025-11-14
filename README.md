# COE 379L Project 2
## Authors: Sanika Nandpure and Melissa Huang

Our docker image is published under the name: sanikanandpure/ml-damage-api. 
Available publicly on Docker Hub [here](https://hub.docker.com/repository/docker/sanikanandpure/ml-damage-api/general). 

An external user can access this by pulling the docker image: 
```python
docker pull sanikanandpure/ml-damage-api
```

We decided not to include a docker-compose since the image simply contains one container, and a docker-compose is typically more useful the image contains multiple containers or services. 
Therefore, they can start the container, mapping the port properly and setting a name: 
```python
docker run -d -p 5000:5000 --name inference_server sanikanandpure/ml-damage-api
```

When the container is running, a user can make a POST request to the API endpoint at “http://localhost:5000/inference”. First, they must upload the image file to the appropriate directory. In their request, they must include the proper path to that image as the value to the key “image,” contained within a “files” object to send within the request body.  

Here’s a code example using Python requests. A user would need to create a new Python file with the below code (suppose it’s named “test.py”). Then, in their terminal, they would simply execute the code via the command “python test.py”. 

```python
import requests
url = "http://localhost:5000/inference"

with open("<path_to_image_here>.jpg", "rb") as img:
    files = {"image": img}
    response = requests.post(url, files=files)
print(response.json())
```
