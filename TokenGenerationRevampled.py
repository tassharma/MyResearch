from datetime import datetime, timedelta
import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBearer
from pydantic import BaseModel
import json


# Will need to do pip install pyjwt for token generation
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
clientid = "Tasneem"

token_auth_scheme = HTTPBearer()

class Token(BaseModel):
    access_token: str
    token_type: str

app = FastAPI()

@app.post("/oauth/RefreshToken", response_model=Token)
def create_access_token():
    # Fetch the client id from the Authorization Header
    #For now Hard Coding it here
    data={"clientId":clientid}
    to_encode = data.copy()
    print(to_encode)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + access_token_expires
    print("Original Expiry")
    print(expire)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    #Store the encoded_jwt and expire in the database table access_token where service ='FROM-MYTONOMY'
    return {"access_token": encoded_jwt, "expiry" :expire}

#@app.post("/token", response_model=Token)
def publish():
    # Fetch the token from Authorization Bearer
    # Check the if the token matches from the database table access_token where service ='FROM-MYTONOMY'
    # If it does not match then throw HTTP Exception with status_code = 401 with Message Invalid Token
    # If token is null then throw HTTP Exception with status_code = 400 with Message Missing Token Information

    # If token matches then need to check if the token has expired, for that will need to fetch the
    # 'exp' key from the token

    # right now generating the token here
    generatedToken = create_access_token()
    print("Generated Token")
    print(generatedToken)
    print("-----------------------")
    
    #fetch the token value from the generated token
    encryptedToken  = generatedToken["access_token"]
    #decode this encrypted token to get the Expiry
    expiry = decode_access_token(encryptedToken)
    print("Decoded Expiry")
    print(expiry)

    #Check if the the expiry is less than current date if yes then throw HTTPException with status code = 401
    # And message that Token is expired
    #If not expired then carry the further process


def decode_access_token(encodedToken):
    payload = jwt.decode(encodedToken, SECRET_KEY, algorithms=[ALGORITHM])
    fetchedExpiry = payload.get("exp")
    return fetchedExpiry

# generatedToken =login_for_access_token()   
# print("Generated Token")
# print(generatedToken)
# print("-----------------------")

# encryptedClientId  = generatedToken["access_token"]
# print("Encrypted Client Id fetched using access token")
# print(encryptedClientId)
# print('DECODED TOKEN')

# decodedToken = decode_access_token(encryptedClientId)

# print(decodedToken)
publish()
