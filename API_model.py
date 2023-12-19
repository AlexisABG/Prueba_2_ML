from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Cargar el modelo entrenado
model = joblib.load('rf_model.pkl')

# Definir la estructura del cuerpo de la solicitud (input)
class Item(BaseModel):
    feature1: float
    feature2: float

# Crear la instancia de FastAPI
app = FastAPI()

# Definir la ruta para realizar predicciones
@app.post("/predict")
async def predict(item: Item):
    # Convertir los datos de entrada a un arreglo de NumPy
    features = np.array([[item.feature1, item.feature2]])

    # Realizar la predicción
    prediction = model.predict(features)

    # Devolver el resultado
    return {"prediction": int(prediction[0])}

import uvicorn
if __name__ == "__main__":
    uvicorn.run("API_model:app", host="0.0.0.0", port=8000, reload=False, log_level="debug", debug=True,
                workers=1, limit_concurrency=1, limit_max_requests=1)

