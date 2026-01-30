# AMRITANETRA – Amrita Network Threat Recognition & Analysis 

## 🎯 Objective

Phishing is a prevalent cyber threat that manipulates users into trusting malicious URLs and websites. The objective of **AMRITANETRA** is to train machine learning models and deep neural networks on a curated dataset to detect phishing websites accurately. The system gathers both phishing and legitimate URLs, extracts URL and content-based features, and evaluates model performance to identify the most effective detection approach.

## 🔒 Cyber Threat Coverage

| Threat Type | Status | | Threat Type | Status |
|-------------|--------|-|-------------|--------|
| 🔍 **Phishing** | ✅ | | 🔄 **Credential Stuffing** | ✅ |
| 📱 **Smishing** | ✅ | | 📊 **SQL Injection** | ❌ |
| 📞 **Vishing** | ❌ | | 🌐 **Cross-Site Scripting** | ✅ |
| 🔗 **URL Spoofing** | ✅ | | 🕵️ **Man-in-the-Middle Attack** | ✅ |
| 💧 **Watering Hole Attack** | ❌ | | 🔤 **DNS Spoofing** | ✅ |
| 🦠 **Malware** | ✅ | | 🖱️ **Clickjacking** | ✅ |
| 👥 **Social Engineering** | ✅ | | 💾 **Drive-By Download** | ✅ |
| 💥 **Zero-Day Attack** | ✅ | | | |

## ⚙️ Installation

To install the required packages and libraries, run this command in the project directory after forking and cloning this repository:

```bash
pip install -r requirements.txt
```

## 🧰 Technologies Used

* **NumPy**
* **Pandas**
* **Matplotlib**
* **Scikit-Learn**
* **Flask**

## 🤖 AI Bot Integration (Our Novelty)

AMRITANETRA integrates a **Smart AI Bot** to further enhance phishing detection and user interaction. The AI bot functions as a virtual assistant that interacts with users on the platform. It assists users in identifying suspicious URLs by providing real-time suggestions based on the URL analysis. By integrating Natural Language Processing (NLP) techniques, the AI bot is capable of answering user queries about potential phishing risks and guiding them in real-time about how to protect themselves from phishing attacks. This integration not only provides a user-friendly interface but also helps enhance the overall phishing detection process by incorporating user feedback.

## 🔍 Feature Extraction

The system begins by retrieving URLs to be analyzed. These are submitted through a web interface and processed to extract relevant features from the URLs and web content. Features are derived based on the domain, HTML structure, and address bar contents to train and test the machine learning models effectively.

## 🤖 Machine Learning Models

Several models were trained and compared to identify phishing websites. The best-performing model classifies URLs as either phishing or legitimate based on a learned decision boundary. Predictions are displayed on the front-end interface.

📄 **Refer `amritanetra.ipynb` for detailed implementation and training.**

## 📊 Results

| # | ML Model               | Accuracy | F1 Score | Recall | Precision |
| - | ---------------------- | -------- | -------- | ------ | --------- |
| 0 | Gradient Boosting      | 0.974    | 0.977    | 0.994  | 0.986     |
| 1 | CatBoost Classifier    | 0.972    | 0.975    | 0.994  | 0.989     |
| 2 | Multi-layer Perceptron | 0.969    | 0.973    | 0.995  | 0.981     |
| 3 | Random Forest          | 0.967    | 0.971    | 0.993  | 0.990     |
| 4 | Support Vector Machine | 0.964    | 0.968    | 0.980  | 0.965     |
| 5 | Decision Tree          | 0.960    | 0.964    | 0.991  | 0.993     |
| 6 | K-Nearest Neighbors    | 0.956    | 0.961    | 0.991  | 0.989     |
| 7 | Logistic Regression    | 0.934    | 0.941    | 0.943  | 0.927     |
| 8 | Naive Bayes Classifier | 0.605    | 0.454    | 0.292  | 0.997     |

## 🧠 Conclusion

* **AMRITANETRA** effectively applies multiple machine learning models for phishing URL detection.
* It performs Exploratory Data Analysis (EDA) to understand key distinguishing features.
* Features like `HTTPS`, `AnchorURL`, and `WebsiteTraffic` significantly influence phishing classification.
* **Gradient Boosting Classifier** emerged as the top performer with **97.4% accuracy**, minimizing the risk of phishing attacks by accurately distinguishing malicious URLs.
* The project enhances understanding of model performance tuning and feature impact on prediction accuracy.
* The **AI Bot Integration** adds a novel layer of user interaction, enhancing real-time phishing risk assessment and making the platform more intuitive.

---

📌 *For suggestions, contributions, or questions, feel free to open an issue or pull request!*
