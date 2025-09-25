# Personal Finance Tracker

A web-based application that allows users to track and manage their personal finances. Users can log income and expenses, categorize them (e.g., Food, Rent, Salary), and view monthly summaries and savings. The app provides visual insights through charts and graphs, helping users understand their spending habits.

## Features :
- Add income/expenses with date, amount, category, and note.

- View all transactions and filter by date or category.

- Update existing transactions to correct details.

- Delete transactions when no longer needed.

- Categorize transactions for organized tracking.

- Show monthly income, expenses, and savings.

- Predict next month’s expenses using past data.

## Project Structure

Peronal Finance Tracker/
|
|---src/                #core application logic
|    |---logic.py       #Business logic and task 
operations              
|    |_db.py            #Database operations
|
|---api/                #Backend API
|    |_main.py          #FastAPI endpoints
|
|---frontend/           #Frontend applications
|    |_app.py           #Streamlit web interface
|
|___requirements.txt    #Python Dependencies
|
|___README.md           #Project Documentation
|
|___.env                #Python variables

## Quick start

### Prerequisites

- python 3.8 or higher
- A Supabase account
- Git(push,cloning)

### 1.Clone or Download the Project
# Option 1: Clone with Git
git clone <repository-url>

# Option 2: Download and extract the ZIP file

### 2.Install Dependencies

# Install all required Python packages
pip install -r requirements.txt

### 3. Set Up Supabase Database

1.Create a Supabase Project:

2.Create the Tasks Table:

- Go to the SQL Editor in your Supabase dashboard

- Run this SQL command:

---sql
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES finusers(user_id) ON DELETE CASCADE,
    date DATE NOT NULL,
    type VARCHAR(20) NOT NULL CHECK (type IN ('income', 'expense')),
    category VARCHAR(50) NOT NULL,
    amount NUMERIC(10,2) NOT NULL,
    note TEXT
);

3. **Get Your Credentials:

### 4. Configure Environment Variables

1. Create a '.env' file in the project root

2. Add your Supabase credentials to '.env' : 
SUPABASE_URL=your_project_url_here
SUPABASE_KEY=your_anon_key_here

**Example:**
SUPABASE_URL="https://wkhpmrprnxapbqvmalcr.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndraHBtcnBybnhhcGJxdm1hbGNyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODI0ODIsImV4cCI6MjA3MzY1ODQ4Mn0.whDjtf7FfIGNKFCkbvz1NEEVjRUXG4D2plJY4471Yog"

### 5. Run the Application

## Streamlit Frontend
streamlit run frontend/app.py

The app will open in your browser at 'http://localhost:8501'

## FastAPI Backend

cd api
python main.py

The API will be available at 'http://localhost:8500'

## How to use

## Technical Details

### Technologies Used

- **Frontend**: Streamlit (Python web framework)
- **Backend**: FastAPI (Python REST API framework)
- **Database**: Supabase (PostgreSQL-based backend-as-a-service)
- **Language**: Python 3.8+

### Key Componenets

1. **'src/db.py'**: Database operations 
    -Handles all CRUD operations with Supabase

3. **'src/logic.py'**: Business logic
    -Task validation and processing

## Troubleshooting

## Common Issues

1. **"Module not found" erros**
    - Make sure you've installed all dependencies: 'pip install -r requirements.txt'
    - Check that you're running commands from the correct directory

## Future Enhancements

Ideas for extending this project:

- **User Authentication**: Add user accounts and login
- **Task Categories**: Organize tasks by subject or category
- **Mobile App**: React Native or Flutter mobile version

## Support

If you encounter any issues or have questions:
7674876604
nandinipatelpadam@gmail.com
