# fullstack-microservices-architecture
Full-stack project using multiple FastAPI microservices, a frontend, and Docker for containerization.

### 🚀 How to Run

1. **Create and activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the services (each in a separate terminal)**  
*(Activate the virtual environment in each terminal before running the commands.)*

**Terminal 1:**
```bash
source venv/bin/activate
uvicorn user_service.main:app --port 8001 --reload
```

**Terminal 2:**
```bash
source venv/bin/activate
uvicorn order_service.main:app --port 8002 --reload
```

**Terminal 3:**
```bash
source venv/bin/activate
uvicorn payment_service.main:app --port 8003 --reload
```

***Create a PostgreSQL DB using Docker container***
```bash
docker run --name postgres-db -p 5432:5432 -e POSTGRESS_PASSWORD=password -d postgres
```
