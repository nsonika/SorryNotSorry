# SorryNotSorry - AI-Powered Excuse Generator

SorryNotSorry is a playful web application that generates witty, humorous, and creative excuses for life's awkward moments using AI.

## Features
- **Category Selection**: Choose from categories like Work, Social, Relationships, or Custom.
- **Humor Levels**: Pick your humor style - Mild, Witty, or Absurd.
- **Custom Context**: Add specific details to make excuses relatable and fun.
- **Dynamic Excuse Generation**: Powered by AI for tailored and unique excuses.

---

## Installation and Setup

### Prerequisites
- Python 3.10 or higher
- Docker and Docker Compose
- Node.js and npm (for frontend)
- An SAMBANOVA API key for AI-powered functionality

---

## Backend Setup

### 1. Clone the Repository
```bash
git clone https://github.com/nsonika/SorryNotSorry
git cd SorryNotSorry
```

### 2. Setup Environment Variables
Create a `.env` file in the `backend` directory with the following variables:
```env
SAMBANOVA_API_KEY=your_openai_api_key
SAMBANOVA_BASE_URL=your_openai_base_url
```

### 3. Install Dependencies
#### Using Virtual Environment:
```bash
cd backend
python -m venv excusegen-env
source excusegen-env/bin/activate   # For Linux/MacOS
# OR
excusegen-env\Scripts\activate    # For Windows
pip install -r requirements.txt
```

### 4. Run Locally
#### Using Python:
```bash
uvicorn main:app --host 0.0.0.0 --port 7000 --reload
```
Access the backend at: `http://localhost:7000`

---

## Docker Setup in Backend

### 1. Build and Run with Docker Compose
Ensure Docker is installed and running, then execute:
```bash
docker compose up --build
```
The app will be available at `http://localhost:7000`.


---

## Frontend Setup

### 1. Navigate to the Frontend Directory
```bash
cd frontend
```

### 2. Install Dependencies
Run the following command to install the required packages:
```bash
npm install
```

### 3. Add Environment Variables
Create a `.env` file in the `frontend` directory with the following:
```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:7000
```

### 4. Start the Development Server
Run the following command:
```bash
npm run dev
```
The frontend will be available at `http://localhost:3000` by default.

---

## Usage
1. Open the frontend app in your browser at `http://localhost:3000`.
2. Select a category and humor level.
3. Optionally, provide custom context.
4. Click "Generate" to receive a unique excuse!

