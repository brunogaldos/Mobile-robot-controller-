xhost +

cd ../..
docker run \
    -it \
    --rm \
    --net=host \
    --privileged \
    --env="DISPLAY" \
    -v "$HOME/.Xauthority:/root/.Xauthority:rw" \
    --name test \
    controller_docker-ros:main \
    bash
