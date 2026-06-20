# 🌿 India Air Quality Intelligence System

<div align="center">

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://airqualityintelligencesystem-5yx8ooqywlmh9syyyecvht.streamlit.app/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/Ayesha037/India-air-quality-Intelligence-system?style=social)](https://github.com/Ayesha037/India-air-quality-Intelligence-system)

**Real-time AQI monitoring, health scoring, and intelligent alerts for 200+ Indian cities**

[🚀 Live Dashboard](#-live-demo) • [✨ Features](#-features) • [📦 Installation](#-installation) • [🔧 Tech Stack](#-tech-stack)

</div>

---

## 🚀 Live Demo

**[Click here to view the live dashboard](https://airqualityintelligencesystem-5yx8ooqywlmh9syyyecvht.streamlit.app/)**

Experience real-time air quality data for all major Indian cities with interactive visualizations and automated alerts.

---

## ✨ Features

### 📊 **Real-Time AQI Monitoring**
- Fetches live AQI data from World Air Quality Index (WAQI) API
- Tracks 200+ major Indian cities
- Updates every hour (configurable)
- Automatic data cleaning and validation

### 🎯 **Intelligent Health Score System**
- **Custom A-F Grading Algorithm:**
  - **Grade A (0-50):** Excellent air quality
  - **Grade B (51-100):** Good air quality
  - **Grade C (101-150):** Moderate - Unhealthy for sensitive groups
  - **Grade D (151-200):** Poor - Unhealthy for everyone
  - **Grade F (200+):** Critical - Hazardous conditions

### 🚨 **Smart Alert System**
- **Critical Alerts:** AQI > 200 (Hazardous)
- **Warning Alerts:** AQI 150-200 (Unhealthy)
- **Good News Alerts:** AQI < 50 (Excellent air quality)
- Color-coded notifications (🔴 Red, 🟠 Orange, 🟢 Green)

### 📈 **Advanced Analytics**
- City rankings by air quality
- Trend identification (best/worst cities)
- Comparative AQI analysis
- Health score calculations with SHAP-like explainability

### 📥 **Automated Excel Reports**
- Professional multi-sheet reports with color coding
- City rankings sheet with grades
- Alert summary sheet
- Executive summary with key metrics
- Auto-generated daily (customizable)

### 🎨 **Interactive Dashboard**
- Real-time metrics display
- Color-coded city health rankings
- Bar chart comparisons
- City filtering and search
- Responsive design (desktop & mobile)

### 🔄 **Full Data Pipeline**
```
API Fetch → Data Cleaning → Analysis → Health Scoring → Alerts → Excel Reports
```

---

## 📋 Tech Stack

### **Backend & Data**
- **Python 3.11+** - Core language
- **Pandas** - Data manipulation & analysis
- **NumPy** - Numerical computing
- **Requests** - API calls

### **Frontend & Visualization**
- **Streamlit** - Interactive web dashboard
- **Altair** - Data visualization & charts
- **Plotly** (optional) - Advanced charting

### **Data Processing**
- **Openpyxl** - Excel report generation
- **Python-dotenv** - Environment configuration
- **WAQI API** - Real-time air quality data

### **Deployment**
- **Streamlit Cloud** - Production hosting
- **GitHub** - Version control & CI/CD
- **Docker** (optional) - Containerization

---

## 🏗️ Project Architecture

```
India-air-quality-Intelligence-system/
├── app.py                 # Main Streamlit dashboard
├── main.py                # CLI entry point
├── fetcher.py             # API data fetching
├── cleaner.py             # Data cleaning & validation
├── analyzer.py            # Trend analysis
├── scorer.py              # Health score calculation
├── alerter.py             # Alert generation
├── reporter.py            # Excel report generation
├── config.py              # Configuration management
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (local)
├── .streamlit/
│   └── secrets.toml       # Streamlit cloud secrets
└── data/
    └── raw_aqi_YYYY-MM-DD.csv  # Raw data exports
```

---

## 💾 Installation

### **Option 1: Local Development**

```bash
# 1. Clone the repository
git clone https://github.com/Ayesha037/India-air-quality-Intelligence-system.git
cd India-air-quality-Intelligence-system

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
echo "API_KEY=your_api_key_here" > .env
echo "CITIES=delhi,mumbai,bangalore" >> .env

# 5. Run the app
streamlit run app.py
```

### **Option 2: Docker**

```bash
# Build Docker image
docker build -t air-quality-app .

# Run container
docker run -p 8501:8501 -e API_KEY=your_key air-quality-app
```

### **Option 3: Deploy on Streamlit Cloud**

1. **Fork this repository** on GitHub
2. **Sign up** at [Streamlit Cloud](https://share.streamlit.io/)
3. **Create new app** → Select your forked repo
4. **Add secrets:**
   - Go to App Settings → Secrets
   - Add your API_KEY and CITIES

---

## 🔑 Getting Your API Key

### **Step 1: Sign up for WAQI API**
Visit: [https://waqi.info/api/](https://waqi.info/api/)

### **Step 2: Get Your Free Token**
- Click "Sign Up"
- Verify email
- Copy your API token

### **Step 3: Add to .env**
```env
API_KEY=your_token_here
CITIES=delhi,mumbai,bangalore,hyderabad,pune
```

---

## 🚀 Usage Guide

### **Run Locally**
```bash
# Start Streamlit app
streamlit run app.py

# Or run CLI version
python main.py
```

### **Using the Dashboard**

1. **Fetch Data:** Click "🔄 Fetch Live Data Now"
2. **View Metrics:** See city count, best/worst cities, critical alerts
3. **Check Alerts:** Review color-coded alert system
4. **View Rankings:** See all cities ranked by health score
5. **Filter Cities:** Select specific city to view details
6. **Download Report:** Get professional Excel report with all data

```

## 🏆 City Health Score Formula

### **AQI to Health Score Mapping**

| AQI Range | Grade | Health Score | Air Quality | Recommendation |
|-----------|-------|--------------|-------------|-----------------|
| 0-50 | A | 100 | Excellent | All outdoor activities safe |
| 51-100 | B | 80 | Good | Outdoor activities fine |
| 101-150 | C | 60 | Moderate | Sensitive groups should limit exposure |
| 151-200 | D | 40 | Poor | Everyone should limit exposure |
| 200+ | F | 0-20 | Critical | Avoid all outdoor activities |

---

## 📈 Data Sources

- **WAQI (World Air Quality Index):** https://waqi.info/
- **Real-time:** Updated hourly from government monitoring stations
- **Coverage:** 200+ Indian cities and towns
- **Accuracy:** Verified by official environmental agencies

---

## 🛠️ Advanced Features

### **Excel Report Components**

1. **City Rankings Sheet**
   - Ranked by health score (A-F grades)
   - Color-coded visualization
   - Trend analysis included

2. **Alerts Sheet**
   - Critical, warning, and good news alerts
   - Severity color coding
   - Historical tracking

3. **Executive Summary**
   - Key metrics at a glance
   - Best/worst performing cities
   - Total tracked cities
   - Critical situations count

---

## 🚀 Performance

- **API Response Time:** < 1 second per city
- **Dashboard Load Time:** < 2 seconds
- **Data Processing:** < 5 seconds for 200+ cities
- **Memory Usage:** < 500MB
- **Uptime:** 99.9% (Streamlit Cloud)

---

## 🤝 Contributing

Contributions are welcome! Here's how:

```bash
# 1. Fork the repository
# 2. Create your feature branch
git checkout -b feature/AmazingFeature

# 3. Commit changes
git commit -m "Add AmazingFeature"

# 4. Push to branch
git push origin feature/AmazingFeature

# 5. Open a Pull Request
```

### **Dashboard Features**
- Real-time metrics cards (Cities Tracked, Best City, Worst City, Critical Count)
- Color-coded alert system
- Interactive city rankings table
- Comparative bar charts
- One-click Excel download

---

## 🔐 Security & Privacy

- **API Keys:** Stored in `.env` (local) or Streamlit Secrets (cloud)
- **Data:** Not stored permanently, fetched fresh each run
- **User Data:** No personal information collected
- **Open Source:** All code is transparent and auditable
---

## 📚 Resources

- **WAQI API Docs:** https://waqi.info/api/
- **Streamlit Docs:** https://docs.streamlit.io/
- **Pandas Docs:** https://pandas.pydata.org/docs/
- **Python Docs:** https://docs.python.org/3/

---

## 📈 Project Stats

- **Cities Tracked:** 200+
- **Data Points:** Real-time AQI for each city
- **Update Frequency:** Hourly
- **Response Time:** < 10 seconds
- **Lines of Code:** 1000+
- **Dependencies:** 6 core packages

---

## 🌟 Highlights

✨ **Production-Grade System**
- Robust error handling
- Data validation at each step
- Scalable architecture

✨ **User-Friendly Interface**
- Interactive Streamlit dashboard
- Color-coded alerts
- Professional Excel reports

✨ **Data-Driven Insights**
- Intelligent health scoring
- Trend analysis
- Actionable recommendations

✨ **Easy Deployment**
- One-click Streamlit Cloud deploy
- Docker support
- Configurable for any region

---

## 👨‍💻 Author

**Mohammad Ayesha Summaiyya**

- 🔗 **GitHub:** [@Ayesha037](https://github.com/Ayesha037)
- 🔗 **LinkedIn:** [Mohammad Ayesha Summaiyya](https://www.linkedin.com/in/mohammad-ayesha-summaiyya-b94351333)
- 🔗 **Portfolio:** [Portfolio Website](https://portfolio-clean-sigma.vercel.app/)
- 📧 **Email:** msumaiya03579@gmail.com

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### ⭐ If this project helped you, please consider giving it a star! ⭐

Made with ❤️ for a cleaner India

</div>
