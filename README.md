# 🧹 Automated Data Cleaner

### 📊 A lightweight, intelligent Python tool that automatically identifies and cleans dirty data from raw CSV files — built to simplify and streamline the data preprocessing stage for Machine Learning and Analytics.

---
<p align="center">
  <a href="https://www.linkedin.com/in/suyash-kulkarni-yes777/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn Badge"/>
  </a>
  <a href="https://huggingface.co/HugFace4Suyash" target="_blank">
    <img src="https://img.shields.io/badge/HuggingFace-Profile-yellow?style=for-the-badge&logo=huggingface" alt="Hugging Face Badge"/>
  </a>
</p>

## 🔍 Overview

Data preprocessing is a critical step in the data science pipeline. Raw datasets often contain inconsistencies like missing values, incorrect data types, and unexpected characters — all of which can lead to flawed analytics or model failures.

This project, **Automated Data Cleaner**, was created to address such issues with a generalized Python-based automation script. It reads any CSV file, intelligently detects common dirty data patterns, and cleans the dataset using practical, explainable rules. This tool is ideal for data scientists, analysts, and ML engineers who want to quickly prepare datasets for downstream tasks.

---

## 🧠 What the Tool Does

Given a dataset (CSV), the cleaner:

- Detects missing or null values (`NaN`, `?`, `None`, empty strings).
- Detects invalid entries like `?`, unexpected symbols, or empty values.
- Identifies inconsistent datatypes and tries to convert them appropriately.
- Automatically replaces or removes invalid entries using sensible rules.
- Outputs a cleaned dataset for immediate use in ML or visualization.

---

## ⚙️ How the Data is Cleaned (with Justification)

### ✅ Step-by-step cleaning pipeline:

1. **Detect Missing Values**
   - Entries like `NaN`, `?`, empty strings, or string literals like `'null'` are treated as missing values.
   - These are replaced with `np.nan` using Pandas.

2. **Infer and Fix Datatypes**
   - The script attempts to infer data types (`int`, `float`, `str`, `datetime`) and corrects invalid parsing.
   - For example, a string `'29'` in a numeric column is cast to integer.

3. **Replacement Rules**
   | Column Type | Cleaning Rule |
   |-------------|----------------|
   | Numeric     | Replace missing values with **mean** of the column |
   | Categorical | Replace missing/invalid values with **mode** (most frequent value) |
   | Textual     | Replace missing values with `'Unknown'` or a placeholder |

   Example:
   - `age = ?` → `age = mean(age)`
   - `gender = ?` → `gender = mode(gender)`

4. **Log Transformations**
   - All replacements and transformations are logged internally for transparency and debugging.

5. **Export Cleaned CSV**
   - Cleaned dataset is exported to a new CSV named: `cleaned_<original_filename>.csv`

---

## 📁 Input Example

**Before Cleaning:**

```csv
name,age,gender,salary
John,29,Male,60000
nan,35,Female,72000
Alice,?,Male,80000
Mark,27,Male,55000
David,30,Male,?
```
**After Cleaning**
```
name,age,gender,salary
John,29.0,Male,60000.0
Unknown,35.0,Female,72000.0
Alice,30.2,Male,80000.0
Mark,27.0,Male,55000.0
David,30.0,Male,66750.0
```
## 🤔 Why These Replacements?
  Mean/Mode Imputation is a commonly used, effective, and computationally cheap technique for missing value handling when the dataset size is small or moderately large.
  
  Placeholder Texts like 'Unknown' are used when no statistically valid imputation is possible (e.g., names).
  
  It avoids removing rows to preserve data quantity (unless the data is >50% missing, which is optionally handled).
  
## ✅ Outcomes
  Quick preprocessing of messy datasets.
  
  Model-ready datasets for ML/AI pipelines.
  
  Avoids human error in manual imputation.
  
  Ideal for EDA, visualization, prototyping, or automated ML pipelines.

## 🚀 Future Scope
  We plan to expand this tool with the following features:
  
  📈 EDA Module: Auto-generate profile reports using Pandas Profiling.
  
  🧠 ML-Based Imputation: Use KNN or regression-based imputation.
  
  ⚠️ Outlier Detection: Flag and optionally remove outliers.
  
  🕵️ Anomaly Detection: Use statistical/machine learning techniques to identify anomalies.
  
  📊 UI Dashboard: Web-based interface for upload, preview, and download (using Streamlit or Gradio).
  
  🗃️ Multi-format Support: Excel, JSON, Parquet support for future data pipelines.
  
  🧪 Unit Testing: Add PyTest-based robust test cases to ensure cleaning integrity.
## 📦 Installation & Usage
  🔧 Requirements
  Python 3.7+
  
  pandas
  
  numpy
## 📥 Install dependencies
```
  pip install -r requirements.txt
```
## 🧼 Run the cleaner
```
  python cleaner.py input.csv
```
## Cleaned file will be saved as:
  cleaned_input.csv
## 👤 Author
Suyash Kulkarni (aka SUYASHH)
Aspiring AI | ML | DS Engineer



