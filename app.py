import os
from fastapi import FastAPI, Body, HTTPException
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List
import motor.motor_asyncio
import pymongo
from uuid import uuid4 as uuid


app = FastAPI()



class Vehiculo(BaseModel):
    id:Optional[str]
    marca:str
    modelo:int
    tipo:str
    placa:str
    valor:int

vehiculos = []

@app.get("/")
def root():
    return "Hola: bienvenidos al api"


@app.get("/carros")
def get_vehiculos():
    return vehiculos


@app.post("/carros")
def save_vehiculos(vehiculos:Vehiculo):
    vehiculos.id = str(uuid)
    vehiculos.append(vehiculos.dict())

    return vehiculos[-1]


@app.get("/carros/{vehiculos_id}")
def get_vehiculos(vehiculos_id:str):
    for vehiculos in vehiculos:
        if vehiculos["id"]==vehiculos_id:
            return vehiculos
    
    raise HTTPException(status_code=404, detail="Pagina no encontrada")


@app.delete("/carros/{vehiculos_id}")
def delete_vehiculo(vehiculos_id:str):
    for index, post in enumerate(vehiculos):
        if post["id"]==vehiculos_id:
            vehiculos.pop(index)
            return {"el vehiculos a sido eliminado exitosamente"}


@app.put("/carros/{vehiculos_id}")
def update_vehiculo(vehiculos_id:str, updatePaquete:Vehiculo):
    for index, post in enumerate(vehiculos):
        if vehiculos["id"]== vehiculos_id:
            vehiculos[index]["marca"] = update_vehiculo.dict()["marca"]
            vehiculos[index]["modelo"] = update_vehiculo.dict()["modelo"]
            vehiculos[index]["tipo"] = update_vehiculo.dict()["tipo"]
            vehiculos[index]["placa"] = update_vehiculo.dict()["plata"]
            vehiculos[index]["valor"] = update_vehiculo.dict()["valor"]
