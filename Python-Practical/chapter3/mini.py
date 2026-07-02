import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
import xgboost as xgb

@st.cache_data
def load_data(choice):
    if choice == "Heart Attack":
        df = pd.read_csv('Data/heart.csv')
        target = 'target'
    else:  # Breast Cancer
        df = pd.read_csv('Data/breast_cancer.csv')
        target = 'diagnosis'
    X = df.drop(target, axis=1)
    y = df[target]
    return X, y

st.sidebar.title("ML Healthcare Web App")
dataset_choice = st.sidebar.selectbox("Select Dataset", ["Heart Attack", "Breast Cancer"])
alg_choice = st.sidebar.selectbox("Select Algorithm", ["Logistic Regression", "KNN", "SVM", "Decision Tree",
                                                      "Random Forest", "Gradient Boosting", "XGBoost"])

X, y = load_data(dataset_choice)
test_size = st.sidebar.slider("Test Size (%)", 10, 50, 20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size/100, random_state=42)

model = None
if alg_choice == "Logistic Regression":
    model = LogisticRegression(max_iter=1000)
elif alg_choice == "KNN":
    model = KNeighborsClassifier()
elif alg_choice == "SVM":
    model = SVC()
elif alg_choice == "Decision Tree":
    model = DecisionTreeClassifier()
elif alg_choice == "Random Forest":
    model = RandomForestClassifier()
elif alg_choice == "Gradient Boosting":
    model = GradientBoostingClassifier()
elif alg_choice == "XGBoost":
    model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')

model.fit(X_train, y_train)
predictions = model.predict(X_test)

acc = accuracy_score(y_test, predictions)
prec = precision_score(y_test, predictions, average='binary', zero_division=0)
rec = recall_score(y_test, predictions, average='binary', zero_division=0)
f1 = f1_score(y_test, predictions, average='binary', zero_division=0)
cm = confusion_matrix(y_test, predictions)

st.write(f"**Accuracy**: {acc:.2%}")
st.write(f"**Precision**: {prec:.2%}")
st.write(f"**Recall**: {rec:.2%}")
st.write(f"**F1‑Score**: {f1:.2%}")
st.write("Confusion Matrix:")
st.write(cm)

# User Input for Custom Prediction
if st.button("Predict on Your Data"):
    user_input = [float(st.number_input(col, value=0.0)) for col in X.columns]
    user_pred = model.predict([user_input])[0]
    st.success("High Risk" if user_pred else "Low Risk")
