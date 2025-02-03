# 🏥 Clinical Trial Database Management System   

### 📌 **IE 6700 - Data Management for Analytics**  
👥 **Author:** Nirmalkumar Thirupallikrishnan Kesavan

📅 **Date:** September 2024 - November 2024  

---

## 🌟 Project Overview  
This project presents a **Clinical Trial Database Management System** designed to efficiently manage **patient data, treatments, clinical trials, researchers, suppliers, and outcomes**.  

🔗 The system integrates **MySQL (Relational DB)** & **MongoDB (NoSQL)** for structured and unstructured data, enabling:  
✅ **Real-time Data Analytics**  
✅ **Advanced Data Modeling**  
✅ **Optimized Decision-Making for Clinical Trials**  

🖥️ **Project Report:**  
📄 [**Clinical Trial Management System Report**](https://github.com/NirmalKumar31/Clinical-Trial-Data-Management-System/blob/3b7302cf414f0f8f776bf15b424471ec5569030c/Clinical%20Trail%20Database%20Management%20System/Clinical%20Trial%20Database%20Management%20System-Report.pdf)  

---

## 📂 System Architecture  

### 🏗️ **Conceptual Data Modeling**  
Designed **EER and UML diagrams** to map relationships:  
🔹 **Patients** – Linked to medical history, treatments, and trial participation  
🔹 **Clinical Trials** – Monitored by researchers with tracked results  
🔹 **Treatments & Outcomes** – Evaluating drug effectiveness  
🔹 **Products & Suppliers** – Managing medical supplies for trials  

📄 [**Conceptual Models Report**](YOUR_GITHUB_REPO_LINK/blob/main/Conceptual%20Models%20.pdf)  

---

🔑 **Key Entities & Their Attributes:**  
- **Patient**: `Patient_ID, Name, Age, Gender, Medical_History`  
- **Researcher**: `Researcher_ID, Name, Age, Gender, Speciality`  
- **Clinical Trial**: `Trial_ID, Trial_Name, Phase, Start_Date, End_Date`  
- **Treatment**: `Treatment_ID, Patient_ID, Trial_ID, Product_ID (Drug Used), Dosage, Start_Date, End_Date`  
- **Outcome**: `Outcome_ID, Treatment_ID, Result, Side_Effects, Date`  
- **Product (Drug)**: `Product_ID, Name, Type, Quantity`  
- **Supplier**: `Supplier_ID, Name, Address, City, Product_ID (Product Supplied)`   

🖼️ **EER Diagram:**  
![EER Diagram](https://github.com/NirmalKumar31/Clinical-Trial-Data-Management-System/blob/daba2e10b2083bf654d6522fc06fdcc0727ee081/Clinical%20Trail%20Database%20Management%20System/EER%20MODEL%20-%20drawio.png)

---

🖼️ **UML Diagram:**  
![UML Diagram](https://github.com/NirmalKumar31/Clinical-Trial-Data-Management-System/blob/daba2e10b2083bf654d6522fc06fdcc0727ee081/Clinical%20Trail%20Database%20Management%20System/UML%20DIAGRAM%20-%20drawio.png)

---

## 🛠️ Database Implementation  

### 🗄️ **Relational Model (MySQL)**  
Structured relational model with **primary & foreign key constraints** ensuring data integrity.  

📄 [**SQL Implementation**](https://github.com/NirmalKumar31/Clinical-Trial-Data-Management-System/blob/daba2e10b2083bf654d6522fc06fdcc0727ee081/Clinical%20Trail%20Database%20Management%20System/SQL%20Implementation%20.pdf)  

---

### 📊 **NoSQL Database (MongoDB)**  
📄 [**NoSQL Implementation**](https://github.com/NirmalKumar31/Clinical-Trial-Data-Management-System/blob/3b7302cf414f0f8f776bf15b424471ec5569030c/Clinical%20Trail%20Database%20Management%20System/NoSQL%20Implementation.pdf)  

🌍 **MongoDB Atlas for Unstructured Data**  
✅ Stores patient records, unstructured trial data  
✅ Enables flexible querying & schema-less storage  

---

## 📈 Data Analytics & Visualization  

### 📊 **Insights from Clinical Trials**  
To analyze **key trends, patient demographics, and trial outcomes**, the system leverages **Python-based visualizations**:

✅ **Age Distribution of Patients**  
![Age Distribution](https://github.com/NirmalKumar31/Clinical-Trial-Data-Management-System/blob/ffaf0f2f239e064a2bc7b43698262bb87d5fb731/Clinical%20Trail%20Database%20Management%20System/Data%20Visualization/Age%20distribution%20of%20patients.png)  

✅ **Age Distribution Across Genders**  
![Age vs Gender](https://github.com/NirmalKumar31/Clinical-Trial-Data-Management-System/blob/ffaf0f2f239e064a2bc7b43698262bb87d5fb731/Clinical%20Trail%20Database%20Management%20System/Data%20Visualization/Age%20distribution%20across%20genders.png)  

✅ **Most Common Side Effects**  
![Side Effects Analysis](https://github.com/NirmalKumar31/Clinical-Trial-Data-Management-System/blob/ffaf0f2f239e064a2bc7b43698262bb87d5fb731/Clinical%20Trail%20Database%20Management%20System/Data%20Visualization/Most%20common%20side%20effects.png)  

✅ **Number of Patients by Gender**  
![Patients by Gender](https://github.com/NirmalKumar31/Clinical-Trial-Data-Management-System/blob/ffaf0f2f239e064a2bc7b43698262bb87d5fb731/Clinical%20Trail%20Database%20Management%20System/Data%20Visualization/Number%20of%20patients%20by%20gender.png)  

✅ **Number of Treatments Over Time**  
![Treatments Over Time](https://github.com/NirmalKumar31/Clinical-Trial-Data-Management-System/blob/ffaf0f2f239e064a2bc7b43698262bb87d5fb731/Clinical%20Trail%20Database%20Management%20System/Data%20Visualization/Number%20of%20treatments%20over%20time.png)  

✅ **Top 5 Drugs Used in Treatments**  
![Top Drugs](https://github.com/NirmalKumar31/Clinical-Trial-Data-Management-System/blob/ffaf0f2f239e064a2bc7b43698262bb87d5fb731/Clinical%20Trail%20Database%20Management%20System/Data%20Visualization/Top%205%20drugs%20used%20in%20treatments.png)  

✅ **Total Quantity by Product Type**  
![Product Quantity](https://github.com/NirmalKumar31/Clinical-Trial-Data-Management-System/blob/ffaf0f2f239e064a2bc7b43698262bb87d5fb731/Clinical%20Trail%20Database%20Management%20System/Data%20Visualization/Total%20quantity%20by%20product%20type.png)  

---

## 🔮 Future Enhancements 🚀  

🚀 **Real-time Data Integration** for continuous monitoring  
📊 **Predictive Analytics** to forecast treatment success  
⚡ **Scalability for Multi-Center Clinical Trials**  
🔒 **Enhanced Data Security & Compliance**  

---

## 🏆 Conclusion  

The **Clinical Trial Database Management System** is a **scalable, efficient, and data-driven solution** for managing **clinical trials, patient data, and research insights**.  

✅ **Integrated MySQL & MongoDB for optimized performance**  
✅ **Faster clinical trial decisions & improved healthcare outcomes**  

📄 [**Full Project Report**](https://github.com/NirmalKumar31/Clinical-Trial-Data-Management-System/blob/3b7302cf414f0f8f776bf15b424471ec5569030c/Clinical%20Trail%20Database%20Management%20System/Clinical%20Trial%20Database%20Management%20System-Report.pdf)  

---

## ⭐ Contribute & Connect
💡 If you find this useful, star ⭐ this repo!  

🔗 LinkedIn: [Nirmalkumar Thirupallikrishnan Kesavan](https://www.linkedin.com/in/nirmalkumartk/)  
🔗 GitHub: [NirmalKumar31](https://github.com/NirmalKumar31)  


📩 **For questions, feel free to reach out!** 🚀  
