# Phishing Application – Kubernetes Project

## 📌 Project Overview

This project is a **Kubernetes-based phishing simulation application** built for educational and training purposes. It demonstrates how containerized frontend and backend services can be deployed, exposed, and connected using Kubernetes resources such as Deployments, Services, Volumes, Init Containers, and Ingress.

The application consists of:

* A **frontend** login page served by **NGINX**
* A **backend** API built with **Flask**
* A **MySQL** database to store submitted credentials
* **Kubernetes Ingress** to expose the application externally

> ⚠️ This project is strictly for **learning and lab purposes only**.

---

## 🏗️ Architecture

```
User Browser
     │
     ▼
Ingress (phishing.local)
     │
     ├── /        → Frontend Service (NGINX)
     └── /login   → Backend Service (Flask)
                         │
                         ▼
                    MySQL Database
```

---

## 🧰 Technologies Used

* Docker
* Kubernetes (Minikube)
* NGINX
* Flask (Python)
* MySQL
* Git & GitHub

---

## 📁 Project Structure

```
phishing-directory/
├── frontend/
│   ├── index.html
│   └── Dockerfile
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── project-files/
│   ├── frontend-deployment.yaml
│   ├── backend-deployment.yaml
│   ├── mysql-deployment.yaml
│   ├── services.yaml
│   └── ingress.yaml
│
├── .gitignore
└── README.md
```

---

## 🚀 How to Run the Project

### 1️⃣ Prerequisites

* Docker installed
* Minikube installed and running
* kubectl configured

---

### 2️⃣ Build and Push Docker Images

```bash
# Frontend
cd frontend
docker build -t <dockerhub-username>/phishing-frontend .
docker push <dockerhub-username>/phishing-frontend

# Backend
cd ../backend
docker build -t <dockerhub-username>/phishing-backend .
docker push <dockerhub-username>/phishing-backend
```

---

### 3️⃣ Deploy to Kubernetes

```bash
kubectl apply -f project-files/
```

Verify:

```bash
kubectl get pods
kubectl get svc
kubectl get ingress
```

---

### 4️⃣ Configure Hosts File

Get Minikube IP:

```bash
minikube ip
```

Add to `/etc/hosts`:

```
<MINIKUBE-IP> phishing.local
```

---

### 5️⃣ Access the Application

Open browser:

```
http://phishing.local
```

Enter any username and password.

---

## 🗄️ Verify Data in MySQL

```bash
kubectl exec -it <mysql-pod-name> -- mysql -uroot -proot
```

```sql
USE phishing;
SELECT * FROM creds;
```

---

## ✅ Kubernetes Features Demonstrated

* Docker image creation and push
* Deployments for frontend, backend, and database
* ClusterIP services
* emptyDir volume
* Init Container for file sharing
* Ingress-based external access
* Inter-service communication

---

## 📸 Suggested Screenshots for Submission

<img width="1068" height="153" alt="My-Project4" src="https://github.com/user-attachments/assets/cc4ad3a0-03ac-4b55-b8c8-c3e567578827" />
<img width="1145" height="601" alt="My-Project1" src="https://github.com/user-attachments/assets/836de124-8b20-4fcc-85e9-8952e7baaf8b" />
<img width="654" height="141" alt="My-Project2" src="https://github.com/user-attachments/assets/97c76069-fed7-4e42-9e5b-904eba5b1b96" />
<img width="848" height="196" alt="My-Project3" src="https://github.com/user-attachments/assets/5ff48d93-5e1e-46c8-afe3-0870c48baf21" />


---
### CI/CD
- CI implemented using GitHub Actions to build and push Docker images.
- CD implemented using Argo CD following GitOps principles.

---


## 👤 Author

**Rawan Osama**

---

## 📜 License

This project is for **educational use only**.
# test
# test
