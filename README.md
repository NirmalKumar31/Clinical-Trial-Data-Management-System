# 🏥 Clinical Trial Database Management System   

### 📌 **IE 6700 - Data Management for Analytics**  
👥 **Author:** Nirmalkumar Thirupallikrishnan Kesavan

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

📄 [**SQL Implementation Report**](https://github.com/NirmalKumar31/Clinical-Trial-Data-Management-System/blob/daba2e10b2083bf654d6522fc06fdcc0727ee081/Clinical%20Trail%20Database%20Management%20System/SQL%20Implementation%20.pdf)  

---

### 📊 **NoSQL Database (MongoDB)**  
📄 [**NoSQL Implementation Report**](https://github.com/NirmalKumar31/Clinical-Trial-Data-Management-System/blob/3b7302cf414f0f8f776bf15b424471ec5569030c/Clinical%20Trail%20Database%20Management%20System/NoSQL%20Implementation.pdf)  

🌍 **MongoDB Atlas for Unstructured Data**  
✅ Stores patient records, unstructured trial data  
✅ Enables flexible querying & schema-less storage  

---

## 📈 Data Analytics & Visualization  

### 📊 **Insights from Clinical Trials**  
To analyze **key trends, patient demographics, and trial outcomes**, the system leverages **Python-based visualizations**:  
✅ **Age Distribution of Patients**  
✅ **Number of Treatments Over Time**  
✅ **Common Side Effects Analysis**  
✅ **Top 5 Drugs Used in Trials**  

🖼️ **Sample Visualization:**  
![Data Visualization](https://github.com/NirmalKumar31/Clinical-Trial-Data-Management-System/tree/0bd4750cc3a26c798ce30a72b7e7d7ad64d4eb02/Clinical%20Trail%20Database%20Management%20System/Data%20Visualization)

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
✅ **Automated data entry & real-time analytics**  
✅ **Faster clinical trial decisions & improved healthcare outcomes**  

📄 [**Full Project Report**](https://github.com/NirmalKumar31/Clinical-Trial-Data-Management-System/blob/3b7302cf414f0f8f776bf15b424471ec5569030c/Clinical%20Trail%20Database%20Management%20System/Clinical%20Trial%20Database%20Management%20System-Report.pdf)  

---

## 🤝 Contributors 🎓  
- **Nirmalkumar Thirupallikrishnan Kesavan**  

📩 **For questions, feel free to reach out!** 🚀  
