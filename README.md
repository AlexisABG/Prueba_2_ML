# Prueba_2_ML
Este repositorio tiene como objetivo almacenar los resultados del ejercico propuesto como segunda prueba para aspirar al cargo de ML Engineer.

Todo el desarrollo y prueba de los diferentes modelos utilizados se encuentran detallados dentro del jupyer notebook [Prueba_ML.ipynb](https://github.com/AlexisABG/Prueba_2_ML/blob/d269674b0de6cdabc51cbeb419a15f31f06ae787/Prueba_ML.ipynb)

En compresión tipo rar se adjunta el [modelo seleccionado](https://github.com/AlexisABG/Prueba_2_ML/blob/a8d84ccb111fe1776f127d2584a45ec61a39de9f/rf_model.rar) para que se cargado en su entorno mediante la libreria joblib.
El archivo .py llamado API_modelo debe ser descargado en el mismo directorio raiz en donde tenga instalado Fast API y Uvicorn así como el modelo seleccionado con el objetivo de hacer uso de la API. Ejecute el comando bash uvicorn API_modelo:app --reload para abilitar el servidor local, postaeriormente abra en su navegador la siguinete dirección http://127.0.0.1:8000/docs.

En el archico datos prueba API.txt podra encontrar 4 listas que contienen los valores de columnas para probar la API


[![API.png](https://i.postimg.cc/7hvLpWB4/API.png)](https://postimg.cc/k6c9Sf3Y)
