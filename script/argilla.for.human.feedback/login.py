import os
import argilla as rg

#print("step 0")
#set your variable here
#os.environ["ARGILLA_API_URL"] = "http://localhost:6900/"
#os.environ["ARGILLA_API_KEY"] = "admin.apikey"

print("step 1")
rg.init(
    api_url="http://localhost:6900/",
    api_key="admin.apikey",
    workspace="admin"
)