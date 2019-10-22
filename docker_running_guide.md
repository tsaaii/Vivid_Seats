### Please follow the following instructions to run the docker container and replicate this app on your local machine.
![Our Container structure.(modeled after a stock image)](https://github.com/tsaaii/Vivid_Seats/blob/prod/Img/fsql.png)

1. Steps to build the Docker image from the Dockerfile we specified in the current directory and then tag the image as latest.
    * Open the folder in a terminal and run the following command    

    >docker build -t submit:latest .

2. You can check all the images using the following command.

    >docker image ls

3. Run the container from the Alpine latest image.

    >docker run -it submit

4. If you want to run it on a specific port and expose it for external use, try following command.

    >docker run -it -d -p 5000:5000 submit

5. Now go to postman or any API testing client and test our API. Here is a sample.
![Sample Get request on 0.0.0.0:5000](https://github.com/tsaaii/Vivid_Seats/blob/prod/Img/ds.png)

