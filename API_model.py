from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# Definir la estructura del cuerpo de la solicitud (input)
class InputData(BaseModel):
    data: list

# Crear la instancia de FastAPI
app = FastAPI()

# Cargar el modelo previamente guardado
model_path = "rf_model.pkl"
loaded_model = joblib.load(model_path)

# Definir la ruta para realizar la predicción con una lista de datos
@app.post("/predict_list")
async def predict_list(input_data: InputData):
    # Obtener la lista de datos de la solicitud
    input_list = input_data.data
    scaler = StandardScaler()
    scaled = scaler.fit_transform([[x] for x in input_list[:8]])
    scaled = scaled.flatten().tolist()
    input_list = scaled + input_list[8:] 
    print(input_list)

    # Convertir la lista a un arreglo de NumPy
    input_array = np.array(input_list).reshape(1, -1)

    # Utilizar el modelo cargado para realizar la predicción
    prediction = loaded_model.predict(input_array)

    # Devolver la predicción como un número (aquí es solo un ejemplo)
    return {"prediction": float(prediction[0])}

# Si ejecutas este archivo directamente, arranca el servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
