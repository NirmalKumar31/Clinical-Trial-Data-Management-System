import mysql.connector
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt

# Connection details
USERNAME = "root"
PASSWORD = "Nk@31122002"  # Replace with your credentials
HOST = "localhost"
DATABASE = "clinicaltrailnirmal"

# Connect to MySQL
conn = mysql.connector.connect(
    host=HOST,
    user=USERNAME,
    password=PASSWORD,
    database=DATABASE
)
cursor = conn.cursor()

# Define Queries
queries = {
    "QUERY 1: Treatments After March 1, 2024": """
        SELECT T.Treatment_ID, T.Start_Date, T.End_Date, CT.Trial_Name
        FROM TREATMENT T
        JOIN CLINICAL_TRIAL CT ON T.Trial_ID = CT.Trial_ID
        WHERE T.Start_Date > '2024-03-01'
        ORDER BY T.Start_Date ASC;
    """,
    "QUERY 2: Total Quantity by Product Type": """
        SELECT PR.Type, SUM(PR.Quantity) AS Total_Quantity
        FROM PRODUCT PR
        JOIN USES U ON PR.Product_ID = U.Product_ID
        GROUP BY PR.Type;
    """,
    "QUERY 3: Researchers Monitoring Outcomes for Dosages Greater than Phase 3 Treatments": """
        SELECT DISTINCT P.Name AS Researcher_Name, T.Dosage
        FROM RESEARCHER R
        JOIN PERSON P ON R.Researcher_ID = P.Person_ID
        JOIN MONITORS M ON R.Researcher_ID = M.Researcher_ID
        JOIN OUTCOME O ON M.Outcome_ID = O.Outcome_ID
        JOIN TREATMENT T ON O.Treatment_ID = T.Treatment_ID
        WHERE CAST(SUBSTRING_INDEX(T.Dosage, 'mg', 1) AS UNSIGNED) > ANY (
            SELECT CAST(SUBSTRING_INDEX(T2.Dosage, 'mg', 1) AS UNSIGNED)
            FROM TREATMENT T2
            JOIN CLINICAL_TRIAL CT ON T2.Trial_ID = CT.Trial_ID
            WHERE CT.Phase = 3
        );
    """,
    "QUERY 4: Details of Treatments and Researchers": """
        SELECT T.Treatment_ID, T.Patient_ID, CT.Trial_Name, P.Name AS Researcher_Name
        FROM TREATMENT T
        JOIN CLINICAL_TRIAL CT ON T.Trial_ID = CT.Trial_ID
        JOIN OUTCOME O ON T.Treatment_ID = O.Treatment_ID
        JOIN MONITORS M ON O.Outcome_ID = M.Outcome_ID
        JOIN RESEARCHER R ON M.Researcher_ID = R.Researcher_ID
        JOIN PERSON P ON R.Researcher_ID = P.Person_ID;
    """,
    "QUERY 5: Patients with Hypertension in Trials": """
        SELECT DISTINCT CT.Trial_Name, CT.Phase, PT.Medical_History, P.Name AS Patient_Name
        FROM CLINICAL_TRIAL CT
        JOIN PARTICIPATES_IN PI ON CT.Trial_ID = PI.Trial_ID
        JOIN PATIENT PT ON PI.Patient_ID = PT.Patient_ID
        JOIN PERSON P ON PT.Patient_ID = P.Person_ID
        WHERE PT.Medical_History = 'Hypertension';
    """,
    "QUERY 6: Age Distribution of Patients": """
        SELECT
            CASE
                WHEN Age < 20 THEN '0-19'
                WHEN Age BETWEEN 20 AND 29 THEN '20-29'
                WHEN Age BETWEEN 30 AND 39 THEN '30-39'
                WHEN Age BETWEEN 40 AND 49 THEN '40-49'
                WHEN Age BETWEEN 50 AND 59 THEN '50-59'
                WHEN Age BETWEEN 60 AND 69 THEN '60-69'
                WHEN Age >= 70 THEN '70+'
                ELSE 'Unknown'
            END AS Age_Range,
            COUNT(*) AS Patient_Count
        FROM PATIENT
        GROUP BY Age_Range
        ORDER BY Age_Range;
    """,
    "QUERY 7: Number of Treatments Over Time": """
        SELECT DATE_FORMAT(T.Start_Date, '%Y-%m') AS Month, COUNT(*) AS Treatment_Count
        FROM TREATMENT T
        GROUP BY Month
        ORDER BY Month ASC;
    """,
    "QUERY 8: Number of Patients by Gender": """
    SELECT Gender, COUNT(*) AS Patient_Count
    FROM PATIENT
    GROUP BY Gender
    ORDER BY Patient_Count DESC;
""",
    "QUERY 9: Age Distribution Across Genders": """
    SELECT Gender, Age
    FROM PATIENT
    WHERE Gender IS NOT NULL AND Age IS NOT NULL
    ORDER BY Gender, Age;
""",
    
    "QUERY 10: Most Common Side Effects and Their Frequency": """
        SELECT O.Side_Effect, COUNT(*) AS Frequency
        FROM OUTCOME O
        WHERE O.Side_Effect IS NOT NULL
        GROUP BY O.Side_Effect
        ORDER BY Frequency DESC
        LIMIT 10;
""",
    "QUERY 11: Top 5 Drugs Used in Treatments": """
        SELECT PR.Name AS Drug_Name, COUNT(*) AS Usage_Count
        FROM PRODUCT PR
        JOIN USES U ON PR.Product_ID = U.Product_ID
        GROUP BY PR.Name
        ORDER BY Usage_Count DESC
        LIMIT 5;
    """
}

# Execute queries and display results
dataframes = {}
for title, query in queries.items():
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns=columns)
    dataframes[title] = df
    print(f"\n{title}\n")
    print(tabulate(df, headers="keys", tablefmt="pretty"))

# Close connection
cursor.close()
conn.close()

# Visualization for QUERY 2: Total Quantity by Product Type
product_data = dataframes["QUERY 2: Total Quantity by Product Type"]

# Ensure the Total_Quantity column is numeric
product_data["Total_Quantity"] = pd.to_numeric(product_data["Total_Quantity"], errors="coerce")

# Check for any NaN values after conversion
if product_data["Total_Quantity"].isnull().any():
    print("Warning: There are non-numeric values in the Total_Quantity column.")
    print(product_data)

# Plot the pie chart
product_data.set_index("Type")["Total_Quantity"].plot.pie(
    autopct="%1.1f%%", startangle=90, figsize=(8, 8), colors=["lightblue", "orange", "lightgreen", "red"]
)
plt.title("Total Quantity by Product Type")
plt.ylabel("")  # Remove y-axis label
plt.show()

# Visualization for QUERY 6: Age Distribution of Patients
age_data = dataframes["QUERY 9: Age Distribution Across Genders"]["Age"]
age_data = pd.to_numeric(age_data, errors="coerce")
plt.figure(figsize=(10, 6))
plt.hist(age_data, bins=10, color="green", alpha=0.8, edgecolor="black")
plt.title("Age Distribution of Patients")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(axis="y", alpha=0.75)
plt.tight_layout()
plt.show()

#Visualization for QUERY 7: Number of Treatments Over Time
treatments_over_time = dataframes["QUERY 7: Number of Treatments Over Time"]

# Ensure the Treatment_Count column is numeric
treatments_over_time["Treatment_Count"] = pd.to_numeric(treatments_over_time["Treatment_Count"], errors="coerce")

# Convert Month column to datetime
treatments_over_time["Month"] = pd.to_datetime(treatments_over_time["Month"])

# Plot the line chart
plt.figure(figsize=(10, 6))
plt.plot(treatments_over_time["Month"], treatments_over_time["Treatment_Count"], marker="o", color="purple")
plt.title("Number of Treatments Over Time")
plt.xlabel("Month")
plt.ylabel("Number of Treatments")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization for QUERY 8: Number of Patients by Gender
gender_data = dataframes["QUERY 8: Number of Patients by Gender"]

# Ensure the Patient_Count column is numeric
gender_data["Patient_Count"] = pd.to_numeric(gender_data["Patient_Count"], errors="coerce")

# Plot the bar chart
plt.figure(figsize=(10, 6))
plt.bar(gender_data["Gender"], gender_data["Patient_Count"], color=["skyblue", "orange"])
plt.title("Number of Patients by Gender")
plt.xlabel("Gender")
plt.ylabel("Count of Patients")
plt.xticks(rotation=0)  # Keep labels horizontal
plt.tight_layout()
plt.show()

# Visualization for QUERY 9: Age Distribution Across Genders
age_gender_data = dataframes["QUERY 9: Age Distribution Across Genders"]

# Ensure the Age column is numeric
age_gender_data["Age"] = pd.to_numeric(age_gender_data["Age"], errors="coerce")

# Create a violin plot using Seaborn
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.violinplot(data=age_gender_data, x="Gender", y="Age", palette="muted")
plt.title("Age Distribution Across Genders")
plt.xlabel("Gender")
plt.ylabel("Age")
plt.tight_layout()
plt.show()


# Analytical queries Visualization

# Visualization for QUERY 10: Most Common Side Effects
if "QUERY 10: Most Common Side Effects and Their Frequency" in dataframes:
    side_effects_data = dataframes["QUERY 10: Most Common Side Effects and Their Frequency"]
    side_effects_data["Frequency"] = pd.to_numeric(side_effects_data["Frequency"], errors="coerce")
    plt.figure(figsize=(10, 6))
    plt.barh(side_effects_data["Side_Effect"], side_effects_data["Frequency"], color="orange")
    plt.title("Most Common Side Effects")
    plt.xlabel("Frequency")
    plt.ylabel("Side Effect")
    plt.tight_layout()
    plt.show()

# Visualization for QUERY 11: Top 5 Drugs Used in Treatments
if "QUERY 11: Top 5 Drugs Used in Treatments" in dataframes:
    drugs_data = dataframes["QUERY 11: Top 5 Drugs Used in Treatments"]
    drugs_data["Usage_Count"] = pd.to_numeric(drugs_data["Usage_Count"], errors="coerce")
    plt.figure(figsize=(10, 6))
    plt.bar(drugs_data["Drug_Name"], drugs_data["Usage_Count"], color="green")
    plt.title("Top 5 Drugs Used in Treatments")
    plt.xlabel("Drug Name")
    plt.ylabel("Usage Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


