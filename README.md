# fullstack-microservices-architecture
Full-stack project using multiple fastapi microservices, a frontend, and docker for containerization.

### 🚀 How to Run

1. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the services (each in a separate terminal)**

   **Terminal 1:**
   ```bash
   uvicorn user_service.main:app --port 8001 --reload
   ```

   **Terminal 2:**
   ```bash
   uvicorn order_service.main:app --port 8002 --reload
   ```

   **Terminal 3:**
   ```bash
   uvicorn payment_service.main:app --port 8003 --reload
   ```
