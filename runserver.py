import uvicorn

def main():
    """
    Application entrypoint.
    Runs the FastAPI app defined in app/api.py.
    """
    uvicorn.run(
        "src.api:personAPI",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()
