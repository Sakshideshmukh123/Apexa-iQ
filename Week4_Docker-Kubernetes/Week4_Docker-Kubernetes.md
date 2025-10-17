# Week4_Docker-Kubernetes

## **1. Monolithic vs Microservices Architecture**

[https://www.geeksforgeeks.org/system-design/monolithic-architecture-system-design/](https://www.geeksforgeeks.org/system-design/monolithic-architecture-system-design/)

---

### **1.1 What is Monolithic Architecture**

Monolithic architecture means building an **entire application as one single unit**.

All parts of the app — like the **User Interface (UI)**, **Business Logic (functionality)**, and **Data Handling (database operations)** — are combined together in **one big codebase**.

It is the **traditional way** of designing software because it is **simple and easy to start**.

However, as the application grows, it becomes **difficult to manage, update, or scale** because every component is tightly connected.

Changing a small part may require rebuilding and redeploying the entire application.

In modern systems, developers prefer **Microservices Architecture**, where the app is divided into **smaller, independent modules** that can be developed and deployed separately.

---

### **1.2 Importance of Monolithic Systems**

Even with the popularity of microservices, monolithic systems are still important in many situations due to the following reasons:

1. **Simplicity**
    - Easy to build and deploy since all components are in one place.
    - Developers can understand the entire system easily.
2. **Cost-Effective**
    - Cheaper to develop and maintain, especially for small projects or startups.
    - Requires less infrastructure and setup compared to distributed systems.
3. **Good Performance**
    - All components run within the same process, resulting in **faster communication** and **better efficiency**.
4. **Better Security (in some cases)**
    - Fewer communication points mean **fewer chances for security attacks**.
5. **Legacy System Support**
    - Many old systems still use this architecture, so understanding it helps maintain and upgrade them easily.

---

### **1.3 Characteristics of Monolithic Architecture**

1. **Single Codebase**
    - The entire application code is stored in one single project or repository.
    - Easier to manage and deploy initially.
2. **Tight Coupling**
    - All modules depend on each other.
    - Changing one module can affect others.
3. **Shared Memory**
    - All components share the same memory and runtime space, allowing faster communication.
4. **Centralized Database**
    - One main database is used for the entire system, making data management simple but scaling harder.
5. **Layered Structure**
    - Usually divided into layers:
        - **Presentation Layer** – Handles user interface.
        - **Business Logic Layer** – Contains the main operations and rules.
        - **Data Access Layer** – Manages database connections.
6. **Limited Scalability**
    - To scale one feature, the whole application must be scaled, leading to higher resource usage.

---

### **1.4 Key Components of Monolithic Architecture**

1. **User Interface (UI):** Manages user interaction using screens, buttons, and forms.
2. **Application Logic:** Contains business rules and main functionality.
3. **Data Access Layer:** Handles database operations like insert, update, and delete.
4. **Database:** Centralized storage for all application data.
5. **External Dependencies:** Interacts with external APIs or third-party services.
6. **Middleware:** Handles logging, security, and performance monitoring.

---

### **1.5 Design Principles of Monolithic Systems**

- **Modularity:** Organize code into logical sections for better maintenance.
- **Separation of Concerns:** Separate UI, logic, and database handling.
- **Encapsulation:** Hide internal details and expose only required interfaces.
- **Consistency:** Follow uniform coding standards and architecture.
- **Scalability:** Use caching and performance optimization where needed.

---

### **1.6 Challenges in Monolithic Architecture**

- **Long Deployment Cycles:** Entire application must be rebuilt and redeployed.
- **Downtime Risk:** Updates may require temporary shutdown.
- **Limited Scalability:** Cannot scale specific parts independently.
- **High Resource Usage:** Becomes heavy as it grows.
- **Limited Flexibility:** Changes in one area can affect multiple modules.

---

### **1.7 Scaling Strategies for Monolithic Systems**

1. **Vertical Scaling:** Increase CPU, RAM, or storage on the existing server.
2. **Caching:** Store frequently used data for faster access.
3. **Load Balancing:** Distribute incoming traffic across multiple servers.
4. **Database Sharding:** Split data into smaller parts for better performance.
5. **Performance Optimization:** Improve queries, code, and resource handling.

---

### **1.8 Migration from Monolithic to Microservices**

When a monolithic application becomes too large, it can be converted into microservices gradually using these strategies:

1. **Strangler Fig Pattern:** Replace parts of the monolith step by step with microservices.
2. **Decomposition by Business Capability:** Divide the app by business areas (e.g., users, payments).
3. **Database Decoupling:** Assign separate databases for each service.

# 

# **Microservices Architecture**

---

## **What are Microservices?**

Microservices architecture breaks an application into **small, independent services**, each performing a **specific business function**. Unlike monolithic systems, each service can be **developed, deployed, and scaled independently**.

- Can use **different programming languages** and frameworks per service.
- Services communicate via **APIs** for standardized interaction.
- Reduces risk of system failure because **services are loosely coupled**.

---

## **Importance of Microservices**

1. **Independent Development**
    - Teams can work on different services simultaneously.
2. **Better Scalability**
    - Each service can scale according to demand without scaling the whole system.
3. **Resilience**
    - Failures in one service do not affect the entire application.
4. **Flexibility**
    - Use the best technology for each service.
5. **Faster Deployment**
    - Services can be deployed individually, reducing downtime.

---

# Characteristics of Monolithic Architecture

[https://www.geeksforgeeks.org/system-design/microservices/](https://www.geeksforgeeks.org/system-design/microservices/)

Monolithic architecture exhibits several defining characteristics:

- **Single Codebase:** The program is simpler to manage and implement since all of its components are created and maintained in a single codebase.
- **Tight Coupling:** The architecture's components are closely linked, rely on one another, and frequently exchange resources and data directly.
- **Shared Memory:** Monolithic applications typically share the same memory space, allowing components to communicate efficiently without the need for network overhead.
- **Centralized Database:** Data storage is centralized within the application, typically using a single database instance for all data storage needs.
- **Layered Structure:** The structure of monolithic systems is frequently layered, with separate layers for data access, business logic, and presentation. This might result in dependencies across layers even while it separates issues.
- **Limited [Scalability](https://www.geeksforgeeks.org/system-design/what-is-scalability/):** Because the entire application must be scaled at once, scaling a monolithic application can be difficult and frequently leads to inefficiencies and higher resource usage.

---

## **Key Components**

1. **Microservices:** Small, autonomous services for business functions.
2. **API Gateway:** Manages requests, authentication, and routes traffic.
3. **Service Registry & Discovery:** Keeps track of service locations.
4. **Load Balancer:** Distributes traffic across service instances.
5. **Containerization:** Docker containers with orchestration via Kubernetes.
6. **Event Bus / Message Broker:** Enables asynchronous communication.
7. **Database per Service:** Promotes data independence and easier scaling.
8. **Caching & Fault Tolerance:** Enhances performance and resilience.

---

## **Design Patterns**

- **API Gateway Pattern:** Central interface for clients.
- **Service Registry Pattern:** Dynamic discovery of services.
- **Circuit Breaker Pattern:** Prevents repeated failures from affecting system.
- **Saga Pattern:** Handles complex transactions across services.
- **Event Sourcing Pattern:** Stores state changes as events.
- **Strangler Pattern:** Gradual replacement of monolithic parts.
- **Bulkhead Pattern:** Isolates failures to one service.
- **API Composition Pattern:** Combines multiple service responses.
- **CQRS Pattern:** Separates commands (writes) and queries (reads).

---

## **Real-World Example – Amazon E-Commerce**

- **User Service:** Manages user accounts and preferences.
- **Search Service:** Indexes products for quick searching.
- **Catalog Service:** Handles product listings.
- **Cart & Wishlist Services:** Manage shopping carts and saved items.
- **Order & Payment Services:** Process orders and payments.
- **Logistics & Warehouse Services:** Manage delivery and stock.
- **Notification & Recommendation Services:** Notify users and suggest products.

---

## **Migration from Monolithic to Microservices**

1. Analyze current monolith and identify components.
2. Break down by **business functionality**.
3. Apply **Strangler Pattern** to gradually replace monolithic parts.
4. Define clear **APIs** and service contracts.
5. Use **CI/CD pipelines** for automation.
6. Implement **service discovery, logging, and monitoring**.
7. Manage **cross-cutting concerns** like security consistently.
8. Iteratively refine and expand services based on feedback.

---

## **Applications**

- E-commerce platforms
- Banking & FinTech
- Streaming services (Netflix, Spotify)
- Travel & booking systems
- Healthcare systems
- Social media platforms

---

## **Benefits**

- Independent team development
- Failures isolated to specific services
- Efficient resource utilization
- Faster deployments
- Flexible technology choices

---

## **Challenges**

- Complex communication and data consistency
- Distributed transactions and error handling
- Increased operational overhead
- Requires monitoring and orchestration tools

---

## **Microservices vs Monolithic Architecture**

| Aspect | Microservices | Monolithic |
| --- | --- | --- |
| Architecture | Independent services | Single unit |
| Scalability | Individual services | Entire app |
| Deployment | Service-level | Whole app |
| Resource Usage | Efficient | Full app dependent |
| Flexibility | High | Limited |
| Maintenance | Easier | Complex |

### **Blue-Green Deployment Environment**

**Definition:**

Blue-Green deployment is a **software release technique** that aims to **minimize downtime and reduce risk** when releasing new application versions. It achieves this by running **two identical production environments** and switching user traffic between them.

---

### **How It Works:**

1. **Two Identical Environments:**
    - **Blue Environment:** The current live production system serving all users.
    - **Green Environment:** A copy of the production environment where the new version of the application is deployed and tested.
2. **Deployment Process:**
    - Deploy the new application version to the green environment.
    - Perform **testing and validation** in the green environment to ensure the application works as expected.
    - When ready, **switch user traffic** from blue to green, making green the new live environment.
    - Blue remains intact as a **rollback option** in case issues are detected in green.
3. **Traffic Switching:**
    - Can be done using a **load balancer** or **DNS switch**.
    - The switch is usually **instantaneous**, resulting in **zero downtime** for users.

---

### **Advantages:**

- **Zero Downtime:** Users continue working without noticing deployment.
- **Quick Rollback:** If the new version fails, traffic can be redirected back to the previous (blue) environment immediately.
- **Safe Testing:** New code is tested in a production-like environment without affecting live users.
- **Reduced Deployment Risk:** Problems in the new release do not impact the live environment immediately.
- **Continuous Delivery Friendly:** Works well with CI/CD pipelines.

---

### **Considerations & Challenges:**

- **Resource Requirements:** Requires maintaining two identical environments, which may increase infrastructure costs.
- **Data Consistency:** If the application uses a database, schema changes must be carefully handled to keep both environments in sync.
- **Monitoring:** Requires proper monitoring to ensure traffic switches smoothly and issues are detected quickly.
- **Configuration Management:** Both environments must remain identical except for the application version to avoid unexpected behavior.

# What is Docker

[https://www.geeksforgeeks.org/devops/introduction-to-docker/](https://www.geeksforgeeks.org/devops/introduction-to-docker/)

[https://docs.docker.com/get-started/docker-overview/](https://docs.docker.com/get-started/docker-overview/)

**Docker** is a tool that simplifies the process of developing, packaging, and deploying applications. By using containers, Docker allows you to create lightweight, self-contained environments that run consistently on any system, minimising the time between writing code and deploying it into production.

Docker is an OS‑level virtualization (or containerization) platform, which allows applications to share the host OS kernel instead of running a separate guest OS like in traditional virtualization. This design makes Docker containers lightweight, fast, and portable, while keeping them ****isolated from one another.

- Written in the **Go** programming language.
- Supports Windows, macOS, and Linux installations (Docker Engine runs natively on Linux).
- Solves the *“works on my machine”* problem by ensuring code runs identically across environments.
- Unlike VMware (hardware‑level virtualization), Docker operates at the OS level.

### **Docker’s Solution:**

Standardizes the runtime environment by bundling everything (app + dependencies) into containers.

- **Portability**: Runs anywhere in local machine, cloud, on‑prem servers.
- **Consistency**: Same behavior in development, testing, and production.
- **Lightweight**: No full OS per app; containers share the host kernel.
- **Scalability**: Ideal for microservices and orchestrators like Kubernetes and Docker Swarm.
- **Efficiency**: Starts in seconds, uses fewer system resources.

# Components of Docker

The following are the some of the key components of Docker:

- **Docker Engine: [Docker Engine](https://www.geeksforgeeks.org/devops/what-is-docker-engine/)** has a core part docker daemon , that handles the creation and management of containers.
- **Docker Image: [Docker Image](https://www.geeksforgeeks.org/devops/what-is-docker-image/)** is a read-only template that is used for creating containers, containing the application code and dependencies.
- **Docker Hub:** It is a cloud based repository that is used for finding and sharing the container images.
- **Dockerfile:** It is a file that describes the steps to create an image quickly.
- **Docker Registry** : It is a storage distribution system for docker images, where you can store the images in both public and private modes.

### Docker CLI

- Command-line interface to interact with Docker
- Common commands: docker run, docker build, docker pull

### Docker Rest API

- HTTP API used by the CLI and other tools
- Facilitates communication with the Docker daemon

### Docker Daemon

- Handles images, containers, networks, and volume
- Core service that manages Docker objects

### **High-Level Runtime**

- Manages container lifecycle operations
- Tasks include create, start, stop, and delete containers

# Docker Image

A [**Docker Image**](https://www.geeksforgeeks.org/devops/what-is-docker-image/) is a file made up of multiple layers that contains the instructions to build and run a Docker container. t acts as an executable package that includes everything needed to run an application — code, runtime, libraries, environment variables, and configurations.

**How it Works**:

- The image defines how a container should be created.
- Specifies which software components will run and how they are configured.
- Once an image is run, it becomes a Docker Container.

**Relation to Containers**:

- **Docker Image** → Blueprint (static, read-only).
- **Docker Container** → Running instance of that image (dynamic, executable)

# Docker Container

A [**Docker Container**](https://www.geeksforgeeks.org/devops/docker-containers-shells/) is a lightweight, runnable instance of a Docker Image. It packages the application code together with all its dependencies and runs it in an isolated environment. Containers allow applications to run quickly and consistently across different environments — whether on a developer’s laptop, test servers, or production.

- A container is created when a **Docker Image is executed**.
- It runs as an isolated process on the host machine but shares the host’s operating system kernel.
- Multiple containers can run on the same system without interfering with each other.

# What is Docker Hub?

[**Docker Hub**](https://www.geeksforgeeks.org/devops/what-is-docker-hub/) is a repository service and it is a cloud-based service where people push their Docker Container Images and also pull the Docker Container Images from the Docker Hub anytime or anywhere via the internet.

          Generally it makes it easy to find and reuse images. It provides features such as you can push your images as private or public registry where you can store and share Docker images.

Mainly DevOps team uses the Docker Hub. It is an open-source tool and freely available for all operating systems. It is like storage where we store the images and pull the images when it is required. When a person wants to push/pull images from the Docker Hub they must have a basic knowledge of Docker. Let us discuss the requirements of the Docker tool.

# Docker Engine

The software that hosts the containers is named [**Docker Engine**](https://www.geeksforgeeks.org/devops/what-is-docker-engine/). Docker Engine is a client-server based application. The docker engine has 3 main components:

1. **Server:** It is responsible for creating and managing Docker images, containers, networks, and volumes on the Docker. It is referred to as a daemon process.
2. [**REST API](https://www.geeksforgeeks.org/node-js/rest-api-introduction/) :** It specifies how the applications can interact with the Server and instructs it what to do.
3. **Client:** The Client is a docker command-line interface (CLI), that allows us to interact with Docker using the docker commands.

# **Docker Commands**

Docker is a powerful tool for **containerization**, helping developers streamline development, deployment, and application management. The following are some commonly used Docker commands:

---

## **1. docker run**

- **Purpose:** Launches a container from a Docker image and allows specifying runtime options.
- **Syntax:**
    
    ```bash
    docker run [options] <image_name> [command]
    
    ```
    
- **Example:**
    
    ```bash
    docker run -it ubuntu bash
    
    ```
    
    This command runs an **Ubuntu container interactively** with a bash shell.
    

---

## **2. docker pull**

- **Purpose:** Downloads a Docker image from a container registry (like Docker Hub) to the local machine.
- **Syntax:**
    
    ```bash
    docker pull <image_name>:<tag>
    
    ```
    
- **Example:**
    
    ```bash
    docker pull nginx:latest
    
    ```
    
    This pulls the **latest Nginx image** from Docker Hub.
    

---

## **3. docker ps**

- **Purpose:** Lists **all running containers** along with details such as container ID, image, status, and ports.
- **Syntax:**
    
    ```bash
    docker ps [options]
    
    ```
    
- **Example:**
    
    ```bash
    docker ps
    
    ```
    
    Use `docker ps -a` to see **all containers**, including stopped ones.
    

---

## **4. docker stop**

- **Purpose:** Gracefully stops a running container, shutting down processes inside it.
- **Syntax:**
    
    ```bash
    docker stop <container_id|container_name>
    
    ```
    
- **Example:**
    
    ```bash
    docker stop my_container
    
    ```
    
    Stops the container named `my_container`.
    

---

## **5. docker start**

- **Purpose:** Restarts a stopped container, resuming its previous state.
- **Syntax:**
    
    ```bash
    docker start <container_id|container_name>
    
    ```
    
- **Example:**
    
    ```bash
    docker start my_container
    
    ```
    
    Starts the container named `my_container`.
    

---

## **6. docker login**

- **Purpose:** Logs in to a Docker registry to access **private repositories**.
- **Syntax:**
    
    ```bash
    docker login [registry_url]
    
    ```
    
- **Example:**
    
    ```bash
    docker login
    
    ```
    
    Prompts for **username and password** to log in to Docker Hub.
    

---

## **7. docker images**

- **Purpose:** Lists all images available locally on your machine.
- **Syntax:**
    
    ```bash
    docker images
    
    ```
    

---

## **8. docker rm**

- **Purpose:** Removes a stopped container.
- **Syntax:**
    
    ```bash
    docker rm <container_id|container_name>
    
    ```
    
- **Example:**
    
    ```bash
    docker rm my_container
    
    ```
    

---

## **9. docker rmi**

- **Purpose:** Removes a Docker image from the local system.
- **Syntax:**
    
    ```bash
    docker rmi <image_name>:<tag>
    
    ```
    
- **Example:**
    
    ```bash
    docker rmi nginx:latest
    
    ```
    

---

## **10. docker exec**

- **Purpose:** Executes commands inside a running container.
- **Syntax:**
    
    ```bash
    docker exec -it <container_id|container_name> <command>
    
    ```
    
- **Example:**
    
    ```bash
    docker exec -it my_container bash
    
    ```
    
    Opens a bash shell **inside the running container**.
    

# Kubernetes overview

Kubernetes is an open-source container management platform.

- Automates the deployment, management, and scaling of container-based applications.
- Developed at Google in 2014, Kubernetes draws on Google’s production experience and is now maintained by the Cloud Native Computing Foundation.
- It orchestrates containers grouping them into logical units called *pods* and managing their lifecycle across a cluster of machines.
- It automatically restarts failed containers, replaces them when necessary, and reschedules workloads onto healthy nodes to maintain the desired state.

Think of Kubernetes as an ****orchestra conductor. Each container is a musician. While you can manage a few musicians yourself, you need a conductor to coordinate an entire orchestra to play a complex symphony. You simply give the conductor the sheet music (your desired configuration), and they ensure every musician plays their part correctly, replacing someone who falls ill and bringing in more players.

### Monolithic Vs Microservices

In the past, applications were built using a monolithic architecture, where everything was interconnected and bundled into one big codebase. This made updates risky for example, if you wanted to change just the payment module in an e-commerce app, you had to redeploy the entire application. A small bug could crash the whole system.

To overcome this, the industry moved toward microservices**,** where each feature (like payments, search, or notifications) is built and deployed independently. This made applications more flexible and scalable.

But with **microservices** came a new challenge:instead of running one big app, companies now had to manage hundreds or thousands of small containerized services. Containers solved the packaging problem, but without a way to orchestrate them, things got messy. That’s where Kubernetes came in acting like a smart manager that automates deployment, scaling, and coordination of all those microservices.

# Terminologies in K8s

Think of Kubernetes as a well-organized company where different teams and systems work together to run applications efficiently. Here’s how the key terms fit into this system:

### **1. Pod**

A [**Pod**](https://www.geeksforgeeks.org/devops/kubernetes-pods/) is the smallest unit you can deploy in Kubernetes. It wraps one or more containers that need to run together, sharing the same network and storage. Containers inside a Pod can easily communicate and work as a single unit.

### **2. Node**

A [**Node**](https://www.geeksforgeeks.org/devops/kubernetes-node/) is a machine (physical or virtual) in a Kubernetes cluster that runs your applications. Each Node contains the tools needed to run Pods, including the container runtime (like Docker), the Kubelet (agent), and the Kube proxy (networking).

### **3. Cluster**

A Kubernetes [**cluster**](https://www.geeksforgeeks.org/devops/kubernetes-cluster/) is a group of computers (called nodes) that work together to run your containerized applications. These nodes can be real machines or virtual ones.

There are two types of nodes in a Kubernetes cluster:

1. **Master node (Control Plane):**
    - Think of it as the brain of the cluster.
    - It makes decisions, like where to run applications, handles scheduling, and keeps track of everything.
2. **Worker nodes:**
    - These are the machines that actually run your apps inside containers.
    - Each worker node has a Kubelet (agent), a container runtime (like Docker or containerd), and tools for networking and monitoring.

### **4. Deployment**

A [**Deployment**](https://www.geeksforgeeks.org/devops/kubernetes-deployment/) is a Kubernetes object used to manage a set of Pods running your containerized applications. It provides declarative updates, meaning you tell Kubernetes what you want, and it figures out how to get there.

### **5. ReplicaSet**

A [**ReplicaSet**](https://www.geeksforgeeks.org/devops/kubernetes-creating-a-replicaset/) ensures that the right number of identical Pods are running.

### **6. Service**

A [**Service**](https://www.geeksforgeeks.org/devops/kubernetes-service/) in Kubernetes is a way to connect applications running inside your cluster. It gives your Pods a stable way to communicate, even if the Pods themselves keep changing.

### **7. Ingress**

[**Ingress**](https://www.geeksforgeeks.org/devops/what-is-kubernetes-ingress/) is a way to manage external access to your services in a Kubernetes cluster. It provides HTTP and HTTPS routing to your services, acting as a reverse proxy.

### **8. ConfigMap**

A [**ConfigMap**](https://www.geeksforgeeks.org/devops/kubernetes-configmap/) stores configuration settings separately from the application, so changes can be made without modifying the actual code.

Imagine you have an application that needs some settings, like a database password or an API key. Instead of hardcoding these settings into your app, you store them in a ConfigMap. Your application can then read these settings from the ConfigMap at runtime, which makes it easy to update the settings without changing the app code.

### **9. Secret**

A [**Secret**](https://www.geeksforgeeks.org/devops/kubernetes-secrets/) is a way to store sensitive information (like passwords, API keys, or tokens) securely in a Kubernetes cluster.

### **10. Persistent Volume (PV)**

A Persistent [**Volume**](https://www.geeksforgeeks.org/devops/kubernetes-volumes/) (PV) in Kubernetes is a piece of storage in the cluster that you can use to store data and it doesn’t get deleted when a Pod is removed or restarted.

### **11. Kubelet**

A [**Kubelet**](https://www.geeksforgeeks.org/devops/what-is-kubelet-in-kubernetes/) runs on each Worker Node and ensures Pods are running as expected.

### **12. Kube-proxy**

[**Kube-proxy**](https://www.geeksforgeeks.org/devops/understanding-kubernetes-kube-proxy-and-its-role-in-service-networking/) manages networking inside the cluster, ensuring different Pods can communicate.

5. Docker implementation

# Kubernetes Vs Docker

**Kubernetes** and **Docker** are two of the most widely used technologies in modern application deployment and DevOps. Docker allows you to package applications into containers, making them easy to run anywhere. Kubernetes helps you manage, scale, and automate the deployment of these containers across multiple servers. In this article, we’ll explore how Kubernetes and Docker work together and why they are essential in today’s cloud-native environments

# Quick summary of the problems I faced

- `docker` CLI works but **Server (Engine)** returns `500 Internal Server Error` (e.g. `dockerDesktopLinuxEngine/v1.51/info`).
- `docker run` and other commands are **very slow** or hang.
- Docker Desktop **takes long to open** or doesn’t fully start.
- Confusion between **Windows containers** and **Linux containers** (`nanoserver` vs `ubuntu`).