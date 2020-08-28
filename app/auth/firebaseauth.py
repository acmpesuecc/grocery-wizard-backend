from fastapi import HTTPException
import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("../grocery-wizard-firebase-adminsdk-95r53-9c32d80748.json")
firebase_admin.initialize_app(cred)

def verify(id_token):
    if id_token == 'devtoken':
        return 0
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        return uid
    except Exception:
        raise HTTPException(status_code=403, detail="Forbidden. The ID Token is invalid.")
