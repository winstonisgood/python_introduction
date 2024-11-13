import docker

def run_docker_container(image_name):
    client = docker.from_env()
    
    # Run a container from the image
    container = client.containers.run(image_name, detach=True)
    
    print(f"Container {container.id} is running")
    
    # Inspect the container
    logs = container.logs()
    print(f"Logs: {logs.decode('utf-8')}")
    
    return container

# Example usage
container = run_docker_container("nginx:latest")