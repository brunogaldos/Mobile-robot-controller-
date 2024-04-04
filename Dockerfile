ARG ROS_DISTRO=humble
FROM osrf/ros:${ROS_DISTRO}-desktop AS base

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Install dependencies with apt

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
        ament-cmake \
        python3-pip \
        ros-${ROS_DISTRO}-rmw-cyclonedds-cpp \
    && apt-get update --fix-missing


# Copy colcon_ws to docker image
COPY colcon_ws/src/ /colcon_ws/src/

# Install module dependencies of colcon_ws
WORKDIR /colcon_ws/
RUN rosdep update \
    && rosdep install --from-paths src --ignore-src -r -y

# Source and build colcon_ws
RUN source /opt/ros/${ROS_DISTRO}/setup.bash && colcon build --symlink-install

# Copy entrypoint scripts and make executable
COPY entrypoint_scripts/ /entrypoint_scripts
RUN chmod +x /entrypoint_scripts/*.sh

