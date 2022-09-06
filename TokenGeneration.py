from datetime import datetime, timedelta
import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBearer
from pydantic import BaseModel
import json

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
clientid = "Tasneem"

token_auth_scheme = HTTPBearer()

class Token(BaseModel):
    access_token: str
    token_type: str

app = FastAPI()

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    print(to_encode)
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

#@app.post("/token", response_model=Token)
def login_for_access_token():
    # user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    # if not user:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Incorrect username or password",
    #         headers={"WWW-Authenticate": "Bearer"},
    #     )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"clientId":clientid}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}
    

def decode_access_token(encodedToken):
    #payloadBase64Decoded  = base64.b64decode(encodedToken)
   
    payload = jwt.decode(encodedToken, SECRET_KEY, algorithms=[ALGORITHM])
    fetchedClientId = payload.get("clientId")
    return fetchedClientId

generatedToken =login_for_access_token()   
print("Generated Token")
print(generatedToken)
print("-----------------------")

encryptedClientId  = generatedToken["access_token"]
print("Encrypted Client Id fetched using access token")
print(encryptedClientId)
print('DECODED TOKEN')

decodedToken = decode_access_token(encryptedClientId)

print(decodedToken)

