# Neccessary imports
import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv() 

# Client initialization
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Accessing data
data = supabase.table("profiles").select("*").execute()

# Assert we pulled real data.
assert len(data.data) > 0

# Data output
print(data.data)