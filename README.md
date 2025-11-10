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

***Run a PostgreSQL Docker container***
```bash
docker run --name users-postgres -p 5432:5432 -e POSTGRES_USER=user_1 -e POSTGRES_PASSWORD=password -d postgres
```
***Create a database in PostgreSQL***
```bash
docker exec -ti users-postgres createdb -U user_1 users_db
```
***Activate the virtal environment from the root project folder***
```bash
source venv/bin/activate
```
***Enter the users directory***
```bash
cd user_service/
```
***Run the users service***
```bash
uvicorn main:app --port 8001 --reload
```

**Terminal 2:**

***Run a PostgreSQL Docker container***
```bash
docker run --name orders-postgres -p 5433:5432 -e POSTGRES_USER=user_1 -e POSTGRES_PASSWORD=password -d postgres
```
***Create a database in PostgreSQL***
```bash
docker exec -ti orders-postgres createdb -U postgres orders_db
```

***Activate the virtal environment from the root project folder***
```bash
source venv/bin/activate
```
***Enter the orders directory***
```bash
cd order_service/
```
***Run the orders service***
```bash
uvicorn main:app --port 8002 --reload
```

**Terminal 3:**

***Run a PostgreSQL Docker container***
```bash
docker run --name payments-postgres -p 5434:5432 -e POSTGRES_USER=user_1 -e POSTGRES_PASSWORD=password -d postgres
```
***Create a database in PostgreSQL***
```bash
docker exec -ti payments-postgres createdb -U postgres payments_db
```

***Activate the virtal environment from the root project folder***
```bash
source venv/bin/activate
```
***Enter the payments directory***
```bash
cd payment_service/
```
***Run the payments service***
```bash
uvicorn main:app --port 8003 --reload
```
