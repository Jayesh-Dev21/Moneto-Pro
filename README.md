# Moneto-Pro

Moneto-Pro is the upgraded version of **Moneto (FinanceWise)**, designed with an entirely new look and feel, as well as enhanced functionalities. It is a web-based financial chatbot that leverages advanced AI technologies to provide secure, seamless, and real-time financial assistance. Built on FastAPI with modern AI frameworks, Moneto-Pro emphasizes user privacy by implementing **temporary chat storage** to maintain financial data security.

---

## 🚀 Features

- **AI-Powered Financial Chatbot**: Built using advanced AI frameworks such as Groq API, DeepSeaK R1, and Llama to provide financial insights and assistance.
- **Temporary Chat Storage**: Ensures user privacy by only keeping chat data temporarily during active sessions and clearing it after the session ends.
- **FastAPI Backend**: A lightweight and high-performance API for real-time chatbot interactions.
- **No SQL Databases**: Eliminates the need for traditional database systems, focusing on speed and security.
- **Modern Web Interface**: A responsive, sleek, and user-friendly interface built with CSS, JavaScript, and HTML.
- **Real-Time Communication**: Provides instant responses to financial queries via WebSocket support with Uvicorn.

---

## 🛠️ Technology Stack

### **Frameworks and Libraries**
- **FastAPI**: For building a robust and high-performance API.
- **Uvicorn**: ASGI server for running FastAPI applications.
- **Groq API**: Powers the AI-driven chatbot for financial queries.
- **DeepSeaK R1**: Delivers advanced AI capabilities for deep financial analysis.
- **Llama**: Enhances natural language processing and conversational AI.

### **Security Features**
- **Temporary Chat Storage**: Chat logs are only retained during the session and are automatically purged afterward.
- **HTTPS Support**: Ensures secure communication between the client and the server.
- **No Persistent Storage**: The system avoids storing sensitive user data permanently, reducing the risk of breaches.

### **Frontend**
- **HTML, CSS, JavaScript**: Core technologies for building and styling the user interface.

---

## 📂 Repository Structure

```
Moneto-Pro/
│
├── api/                   # FastAPI endpoints and related logic
├── models/                # AI models and inference logic
├── static/                # Static files (CSS, JavaScript, Images)
├── templates/             # HTML templates for rendering pages
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🎯 How to Use

### Prerequisites
- **Python 3.9+**
- **Pip** (Python package manager)

### Steps to Run Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Jayesh-Dev21/Moneto-Pro.git
   cd Moneto-Pro
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Start the Uvicorn server:
   ```bash
   uvicorn api.main:app --reload
   ```

4. **Access the Application**:
   Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

---

## 🤖 AI Functionality

Moneto-Pro integrates advanced AI technologies to offer real-time financial support:
- **Groq API**: Powers the chatbot to answer user queries with financial insights.
- **DeepSeaK R1**: Enables complex data analysis for personalized recommendations.
- **Llama**: Enhances conversational capabilities with natural language processing.

The chatbot is designed to handle a wide range of financial queries securely and efficiently while prioritizing user privacy.

---

## 📦 Deployment

Moneto-Pro is ready for cloud-based deployment. Follow these steps to deploy:

1. **Prepare the Environment**:
   Ensure the server meets the prerequisites (e.g., Python, FastAPI, Uvicorn).

2. **Deploy on a Cloud Platform**:
   Platforms like AWS, Azure, or Google Cloud can be used for deployment. For a quick deployment, consider using Docker.

3. **Run the Application in Production**:
   Use Uvicorn with production settings:
   ```bash
   uvicorn api.main:app --host 0.0.0.0 --port 8000
   ```

---

## 💡 Future Enhancements

- Integration with third-party financial APIs for real-time market data.
- Multi-language support to cater to a global audience.
- Voice interaction capabilities to make the chatbot more accessible.

---

## 📧 Contact

For questions, feedback, or support, feel free to reach out:
- **Author**: [Jayesh-Dev21](https://github.com/Jayesh-Dev21)

---

## ⚠️ Disclaimer

This project does not include a license file. Use and distribution of this code should adhere to the principles of fair use or seek explicit permission from the repository owner.

---

With Moneto-Pro, enjoy secure, intelligent, and real-time financial management assistance while ensuring your data remains private and protected.

--- 
