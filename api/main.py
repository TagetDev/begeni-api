import json
from fastapi import FastAPI, UploadFile, File, HTTPException, Query
from pydantic import BaseModel

app = FastAPI()

# Endpoint to save the Instagram post link
@app.post("/open_post/")
async def save_post_link(link: str = Query(..., description="Instagram post URL")):
    with open('post_link.txt', 'w') as file:
        file.write(link)
    return {"message": "Post processing started"}

# Endpoint to retrieve the Instagram post link and clear the file
@app.get("/open_post/")
async def get_instagram_post():
    try:
        with open('post_link.txt', 'r') as file:
            post_link = file.read()
        # Clear the file after reading
        open('post_link.txt', 'w').close()
        return {"post_link": post_link}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")

# Endpoint to upload file
@app.post("/usernames/")
async def upload_file(file: UploadFile = File(...)):
    try:
        content = await file.read()
        with open('output.txt', 'wb') as f:
            f.write(content)
        return {"message": "File uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")

# Endpoint to retrieve usernames
@app.get("/usernames/")
async def get_usernames():
    try:
        with open('output.txt', 'r', encoding='utf-8') as file:
            text = file.read()
        data = json.loads(text)
        usernames = [user['username'] for user in data["users"]]
        return {"usernames": usernames}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
