import docker

def download_websites_docker():
    client = docker.from_env()

    print(client.containers.list())

    return None