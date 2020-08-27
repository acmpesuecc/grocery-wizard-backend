import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("../grocery-wizard-firebase-adminsdk-95r53-9c32d80748.json")
firebase_admin.initialize_app(cred)

def verify(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        return uid
    except Exception:
        return -1
