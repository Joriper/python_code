import os,sys,uvicorn


uvicorn.run("app:apps", host=str(sys.argv[1]), port=int(sys.argv[2]))
print(f"server is litening at: {sys.argv[1]} and port {sys.argv[2]}")