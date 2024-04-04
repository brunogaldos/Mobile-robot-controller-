#!/bin/bash
# IP addresses and names of hosts
ROS_DOMAIN_ID=30
RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

HOST_NAME=$USER
HOST_IP=localhost 

# Name of docker containers and docker images
IMAGE_OPTITRACK_DRIVER=controller_docker-ros:main

CONTAINER_NAME_OPTITRACK_DRIVER=controller_docker-ros




# Docker kill commands
DOCKER_KILL_COMMAND_OPTITRACK_DRIVER="docker ps -q --filter name=${CONTAINER_NAME_OPTITRACK_DRIVER} | grep -q . && docker rm -fv ${CONTAINER_NAME_OPTITRACK_DRIVER}"


# Tmux session
TMUX_SESSION='tmux-session_'
RANDOM_NUMBER=$RANDOM
TMUX_SESSION_NAME="$TMUX_SESSION$RANDOM_NUMBER"

# Function to test the connection
function ping_test() {
	if ping -c 1 $1 &>/dev/null; then
		echo "Connection to $1 successful!"
	else
		echo "Can't establish a connection to $1!"
	fi
}

# Function to kill all docker containers with q
function kill_all() {
	bash -c "${DOCKER_KILL_COMMAND_OPTITRACK_DRIVER}"

	# Kill tmux
	sleep 5
    TMUX_SESSION_NAME_ATTACHED=$(tmux display-message -p '#S')
    tmux kill-session -t ${TMUX_SESSION_NAME_ATTACHED}
    tmux kill-session -t ${TMUX_SESSION_NAME}
}

# Function that waits for user input and then kills all running docker containers and tmux session
function wait_for_user_and_kill() {
	echo "Press 'q' to kill every process"
	while :; do
		read -n 1 k <&1

		if [[ $k = q ]]; then
			printf "\nQuitting all processes\n"
			kill_all
		fi
	done
}
"$@"

# Allow clients to access the x-server
xhost +

# Create a new session named $TMUX_SESSION_NAME, split panes and change directory in each
tmux new-session -d -s $TMUX_SESSION_NAME

# Config tmux
tmux set -g mouse on

# Run optitrack driver
ping_test $HOST_IP
tmux send-keys -t $TMUX_SESSION_NAME "ssh -Y -t ${HOST_NAME}@${HOST_IP} \
	'${DOCKER_KILL_COMMAND_OPTITRACK_DRIVER}; \
	docker run \
		-it \
		--rm \
		--net=host \
		--pid=host \
		--ipc=host \
		--privileged \
		-v /dev:/dev \
        --env RMW_IMPLEMENTATION=${RMW_IMPLEMENTATION} \
        --env ROS_DOMAIN_ID=${ROS_DOMAIN_ID} \
        --name ${CONTAINER_NAME_OPTITRACK_DRIVER} \
        ${IMAGE_OPTITRACK_DRIVER} \
        /entrypoint_scripts/entrypoint_controller.sh'" Enter

sleep 2

# Kill process terminal
tmux split-window -t $TMUX_SESSION_NAME
tmux send-keys -t $TMUX_SESSION_NAME "bash $0 wait_for_user_and_kill" Enter

# Attach to session named $TMUX_SESSION_NAME
tmux attach -t $TMUX_SESSION_NAME
