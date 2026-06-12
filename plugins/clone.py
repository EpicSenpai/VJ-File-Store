from pymongo import MongoClient
from config import DB_URI

# Database connection intact rakha hai taaki errors na aayein
mongo_client = MongoClient(DB_URI)
mongo_db = mongo_client["cloned_vjbotz"]

# Saari clone commands jadd se mita di hain.

async def restart_bots():
    # Is function ko khali chhod diya hai taaki main file boot ke waqt crash na ho
    pass
    
