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

***Run a PostgreSQL Docker container and Create a database in PostgreSQL***
```bash
docker run --name users-postgres -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres
docker exec -ti users-postgres createdb -U postgres users_db
```

```bash
source venv/bin/activate
cd user_service/
uvicorn user_service.main:app --port 8001 --reload
```

**Terminal 2:**

***Run a PostgreSQL Docker container and Create a database in PostgreSQL***
```bash
docker run --name orders-postgres -p 5433:5432 -e POSTGRES_PASSWORD=password -d postgres
docker exec -ti orders-postgres createdb -U postgres orders_db
```

```bash
source venv/bin/activate
cd order_service/
uvicorn order_service.main:app --port 8002 --reload
```

**Terminal 3:**

***Run a PostgreSQL Docker container and Create a database in PostgreSQL***
```bash
docker run --name payments-postgres -p 5434:5432 -e POSTGRES_PASSWORD=password -d postgres
docker exec -ti payments-postgres createdb -U postgres payments_db
```

```bash
source venv/bin/activate
cd payment_service/
uvicorn payment_service.main:app --port 8003 --reload
```
