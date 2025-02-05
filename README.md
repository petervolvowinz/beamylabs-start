# Ongoing

Go [here](https://github.com/beamylabs/beamylabs-start/discussions) to check what's ongoing and try the latest featues.

# Get started with Beamy Broker

## Prerequisite

To be able to get going; that is docker pull, you need custom credentials. Contact us at www.beamylabs.com.

## Start

Clone this repository and make sure you have `docker` and `docker-compose` installed, then run:

```bash
NODE_NAME=$(scripts/resolve-ip.sh eth0) SIGNALBROKER_IP=$(scripts/resolve-ip.sh eth0) docker-compose -f docker-compose-full-system.yml up -d
```
> On a generic setup `NODE_NAME` and `SIGNALBROKER_IP` will likely be set to the same value.

> `$(scripts/resolve-ip.sh eth0)` assumes that the interface for your main
> ethernet connection is called `eth0`. If that's not the case, you need to
> change `eth0` to the correct name. (Hint you can can find your interface name using `ifconfig` or
> `ipconfig`).

> Some dated docker compose versions might show <br /> `ERROR: Invalid interpolation format for "command" option... `. <br /> 
>> If you can't upgrade your docker-compose you can fix this by manually adding the ip address in the  [docker-compose-full-system.yml](docker-compose-full-system.yml) like so: <br /> [`command: ./grpcwebproxy --backend_addr=${SIGNALBROKER_IP:?Add SIGNALBROKER_IP to the .env file}:50051 ...`](https://github.com/beamylabs/beamylabs-start/blob/master/docker-compose-full-system.yml#L34) <br /> with your ip resulting in: <br /> `command: ./grpcwebproxy --backend_addr=192.x.x.x:50051 ...` <br /> manually.

> Running the above `docker-compose` command only needs to be done once. It is
> persistant over system reboot, and will restart the containers upon reboot,
> over and over again.

Point your web browser at the machine running Beamybroker, an address like
`http://192.0.2.42:8080/`. If you are connected to a hosted WLAN Access Point
like `beamylabs`, the address should be `http://192.168.4.1:8080/`.

> BEWARE: if you change your your interface settings you must restart by do doing [STOP](#stop)/[START](#start)

## Stop

```bash
NODE_NAME=$(scripts/resolve-ip.sh eth0) SIGNALBROKER_IP=$(scripts/resolve-ip.sh eth0) docker-compose -f docker-compose-full-system.yml down
```

## Upgrade
>When you upgrade; remember to upgrade **THIS** repository as well `git pull`, as examples are continuously updated and improved. You will also find the latest pre-generated grpc files in this repository.

```bash
NODE_NAME=$(scripts/resolve-ip.sh eth0) SIGNALBROKER_IP=$(scripts/resolve-ip.sh eth0) ./upgrade.sh
git pull
```
> Alternatively just pull the latest container manually: 
`
NODE_NAME=$(scripts/resolve-ip.sh eth0) SIGNALBROKER_IP=$(scripts/resolve-ip.sh eth0) docker-compose -f docker-compose-full-system.yml pull
`

## Use a specific version (advanced feature)
To pull a specific version you can specify custom tag for `BEAMYBROKER_TAG` alternatively `BEAMYWEBCLIENT_TAG` as in:

```bash
BEAMYBROKER_TAG=v0.0.7-4-g12 NODE_NAME=$(scripts/resolve-ip.sh eth0) SIGNALBROKER_IP=$(scripts/resolve-ip.sh eth0) docker-compose -f docker-compose-full-system.yml pull
```
## API - gRPC
The server is accesible using [gRPC](https://github.com/grpc/grpc#grpc---an-rpc-library-and-framework), which effectively means that you can access it with your language of choice. Stubs to access the server are generated by providing [proto files](proto_files/) which contains the api specification. 

Pre generated files and samples are avaliable for a selection of [languages](examples/grpc). 
If you need another language you can get inspiration by how it's done for python [here](examples/grpc/python/README.md#re-generate-stubs).

## Inspiration - get started

- [python](examples/grpc/python/README.md)
- [go](examples/grpc/go/README.md)
- [elixir](examples/grpc/elixir/car5g/README.md)
- [grpc-web](examples/grpc/grpc-web/README.md)

## Statistics and usage 

In order to understand usage of the product and it's enviroment it will try and send system information based on your interfaces.json and it's execution enviroment on start. The data is obfuscated and it is not distributed to any other party. Its sole purpose is the make the software better.

This is not mandatoy and can be disabled, however to keep us motivated we would please urge you not to disable this feature.
