# ============================================
# FLIGHT DELAY PREDICTION PROJECT
# COMPLETE CLEAN PROGRAM
# ============================================

# =========================
# IMPORT LIBRARIES
# =========================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("cleaned_flights.csv")

print("================================")
print("DATA LOADED")
print("================================")

print(df.head())

# =========================
# CREATE TARGET COLUMN
# =========================

# Flight delayed if arrival delay > 15 mins

df["IsDelayed"] = (df["arr_delay"] > 15).astype(int)

print("\nTARGET COLUMN CREATED")

# =========================
# REMOVE DATA LEAKAGE
# =========================

leakage_cols = [
    "arr_delay",
    "dep_delay",
    "weather_delay",
    "nas_delay",
    "security_delay",
    "late_aircraft_delay",
    "carrier_delay"
]

for col in leakage_cols:

    if col in df.columns:
        df.drop(col, axis=1, inplace=True)

print("\nDATA LEAKAGE COLUMNS REMOVED")

# =========================
# HANDLE MISSING VALUES
# =========================

# Fill numeric columns with 0

numeric_cols = df.select_dtypes(include=['number']).columns

df[numeric_cols] = df[numeric_cols].fillna(0)

# Fill string columns with "Unknown"

string_cols = df.select_dtypes(include=['object', 'string']).columns

df[string_cols] = df[string_cols].fillna("Unknown")

print("\nMISSING VALUES FILLED")

# =========================
# SELECT SAFE FEATURES
# =========================

safe_features = [
    "year",
    "month",
    "day_of_month",
    "day_of_week"
]

X = df[safe_features]

y = df["IsDelayed"]

print("\nFEATURES USED:")

print(X.columns)

# =========================
# ENCODE CATEGORICAL DATA
# =========================

cat_cols = X.select_dtypes(include=['object', 'string']).columns

for col in cat_cols:

    le = LabelEncoder()

    X[col] = le.fit_transform(X[col].astype(str))

print("\nCATEGORICAL DATA ENCODED")

# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTRAIN TEST SPLIT COMPLETED")

# =========================
# TRAIN MODEL
# =========================

model = RandomForestClassifier(
    n_estimators=100,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

print("\nMODEL TRAINING COMPLETED")

# =========================
# MODEL PREDICTION
# =========================

y_pred = model.predict(X_test)

# =========================
# MODEL EVALUATION
# =========================

accuracy = accuracy_score(y_test, y_pred)

print("\n================================")
print("MODEL ACCURACY")
print("================================")

print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nCLASSIFICATION REPORT:\n")

print(classification_report(
    y_test,
    y_pred,
    zero_division=1
))

# =========================
# SAVE MODEL
# =========================

joblib.dump(model, "flight_delay_model.pkl")

print("\nMODEL SAVED SUCCESSFULLY ✅")

# ============================================
# USER INPUT PREDICTION
# ============================================

print("\n================================")
print("FLIGHT DELAY PREDICTION")
print("================================")

# User Inputs

year = int(input("Enter Year: "))
month = int(input("Enter Month: "))
day_of_month = int(input("Enter Day of Month: "))
day_of_week = int(input("Enter Day of Week (1-7): "))

if day_of_week < 1 or day_of_week > 7:
    print("Invalid Day Of Week")
    exit()

# Create Input DataFrame

input_df = pd.DataFrame([{
    "year": year,
    "month": month,
    "day_of_month": day_of_month,
    "day_of_week": day_of_week
}])

# Predict

result = model.predict(input_df)[0]

# Display Result

print("\n================================")

if result == 1:
    print("✈️ RESULT: FLIGHT WILL BE DELAYED")
else:
    print("✈️ RESULT: FLIGHT WILL NOT BE DELAYED")

print("================================")