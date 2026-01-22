# taxi-prediction-fullstack-haza
Machine Learning

Detta projekt är en fullstack-applikation som förutspår taxipriser baserat på flera olika faktorer såsom distans, tid på dygnet, väder och trafik. 

**Applikationen består av:**
- Backend (FastAPI) - som servrar data och gör prediktioner 
- Machine Learning-modell - trännad taxidata 
- Frontend (Streamlit) - där användaren kan se datasetet och testa prediktioner 

**EDA & Data cleaning**
I Jupyter genomfördes: 
- Analys av dataset 
- Hantering av nullvärden 
- Borttagning av outliers
- Val av relevanta features 

Den rensade datan exporterades till final_data.csv 

**Machine Learning-modell**
Flera modeller testades (Linear Regression, KNN, Random Forest)
Random Forest valdes då den gav bäst resultat.  
Den färdigtränade modellen sparades som final_model.joblib


**Backend - FastAPI**
Backend laddar ML-modellen och erbjuder två endpoints:
- **GET /taxi/data** – returnerar rensad taxidata.
- **POST /taxi/predict** – tar emot användarens input och returnerar ett beräknat taxipris

Används av frontend för att hämta data och göra prediktioner.


**Frontend – Streamlit**
Applikationen består av tre sidor:

- **Home** – visar en kort introduktion och instruktioner för hur appen används.
- **View data** – visar den rensade taxidatan i tabellform direkt från backend.
- **Predict Taxi Price** – ett formulär där användaren fyller i resans detaljer och får ett beräknat taxipris. En "Show details"-ruta visar vilka värden som skickades till modellen.

Frontend kommunicerar med backend via httpx.

# Home
![home](images/home.png)

# View data
![data](images/data.png)

# Predict Taxi Price
![predict](images/predict.png)

# Prediction result
![result](images/result.png)

