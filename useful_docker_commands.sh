# docker container prune --> to remove all containers that are not running.
# docker rm $(docker ps -aq) --> to remove all containers that are not running.
# docker rm -f $(docker ps -aq) --> to remove all containers.
# docker build -t <image_name:image_version> . --> to create a new image.
# docker volume prune --> to remove all volumes that are not associated with any containers.
# docker network prune --> to remove all networks that are not associated with any containers.
# docker rmi <image_id> --> to remove an image.
