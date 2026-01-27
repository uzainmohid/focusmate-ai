# 🚀 Quick Start Guide

Get FocusMate AI running in 5 minutes!

## Prerequisites Check

Before starting, ensure you have:
- ✅ Python 3.8+ installed
- ✅ Node.js 16+ installed
- ✅ A terminal/command prompt

---

## Option 1: Automated Setup (Recommended)

### For Mac/Linux:
```bash
chmod +x setup.sh
./setup.sh
```

### For Windows:
```cmd
setup.bat
```

---

## Option 2: Manual Setup

### Step 1: Backend Setup (Terminal 1)

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate it
# Mac/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

✅ Backend should now be running on `http://localhost:5000`

### Step 2: Frontend Setup (Terminal 2)

**Open a NEW terminal window**

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

✅ Frontend should now be running on `http://localhost:3000`

---

## Step 3: Open the App

Open your browser and go to:
```
http://localhost:3000
```

🎉 **You should see the FocusMate AI dashboard!**

---

## First Time Usage

1. **Add your first task**
   - Click "+ Add Task"
   - Fill in title, urgency, effort
   - Watch AI calculate the priority score

2. **Start a focus session**
   - Go to "Focus" tab
   - Select duration (try 25 minutes)
   - Start session and see AI's focus prediction

3. **Check your dashboard**
   - View productivity score
   - See AI recommendations
   - Track your progress

---

## Troubleshooting

### Backend won't start?
- Check if Python 3.8+ is installed: `python --version`
- Make sure you activated the virtual environment
- Check if port 5000 is already in use

### Frontend won't start?
- Check if Node.js is installed: `node --version`
- Delete `node_modules` and run `npm install` again
- Check if port 3000 is already in use

### Database issues?
- Delete `focusmate.db` in the backend folder
- Restart the backend - it will create a fresh database

---

## What to Try First

### 🎯 Complete Workflow Test

1. **Add 3 tasks** with different urgencies
2. **Start a 25-minute focus session**
3. **Complete a task** during the session
4. **Check insights** to see your productivity score
5. **View AI recommendations** on the dashboard

This will generate data and show you all the AI features in action!

---

## Next Steps

- Read the full README.md for detailed documentation
- Explore the AI algorithms in `backend/app.py`
- Customize the UI in `frontend/src/`
- Add more tasks and complete focus sessions to see better AI predictions

---

## Need Help?

1. Check the full README.md
2. Verify both servers are running
3. Check browser console for errors (F12)
4. Make sure you're using http://localhost:3000 (not 5000)

---

**Enjoy using FocusMate AI! 🧠✨**
