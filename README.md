# ILTPWC - You are using visual studio code wrong

This repository contains the working example used wihtin the YouTube Video "You are using VSCode wrong".

The VSCode DevContainer extension lets you use a Docker container as a full-featured development environment to ensure that everyone in your Team has a consistent and reliable development environment - you will never say "It worked on my Machine" again. 


## Prerequisite

1. You need to install [VSCode](https://code.visualstudio.com)
2. As well as [Docker](https://www.docker.com)
3. Within your VSCode you need to install the [Dev Container Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)


## Get started with Dev Containers

1. Within your project create a folder called .devcontainer
2. Create a file called devcontainer.json that specified how you want to build the dev container
3. Create a docker-compse.yml file that specified the development environment outside of your container (eg. databases, message broker etc.)
4. Create a Dockerfile that specifies your DevContainer

## Execute the Demo

1. When opening the folder VSCode will ask you to open in a dev container => do that! 
2. If VSCode does not ask you click in the button left corner and select reopen in a container
3. Within the dev container terminal execute flask run --host=0.0.0.0 (important if you want to enable SSL via traefik otherwise only localhost is available) to start the demo app
4. You can access it without SSL certificates on 127.0.0.1:5000 or
5. You can modify my configuration for traefik with your domain and do the demo with SSL enabled

## Links

Dev Container metadata reference: [DevContainerSpecification](https://github.com/ILTPWC/E2023-VSCode-DevContainer.git)
ILTPWC YouTube Channel: [ILTPWC Channel](https://www.youtube.com/@ILTPWC)

## Information

As always this example works with letsencrypt and a digitalocean resolver because it's my nameserver provider you need to change that in order to make the example work with your provider. The devcontainer is reachable via localhost:5000 and via your application domain if you configure that within traefik.


Thanks for watching ILTPWC - and don't forget to play with computers!

If you like what I am doing please consider to like the Video and subscribe to my channel - it makes a whole lot of a difference!