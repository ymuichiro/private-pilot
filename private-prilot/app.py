import uvicorn
from fastapi import FastAPI, Request, Response, status
from fastapi.responses import JSONResponse
from models import OpenAIinput
from errors import HttpException
from generator import generate
from fastapi.exceptions import RequestValidationError
import traceback

app = FastAPI(title="Private Pilot", description="for vscode")


@app.exception_handler(HttpException)
async def any_handler(_: Request, exc: HttpException):
    return JSONResponse(status_code=400, content=exc.json())


@app.exception_handler(RequestValidationError)
async def request_validation_handler(_: Request, exc: RequestValidationError):
    print(exc)
    return JSONResponse(content={}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@app.post("/v1/engines/codegen/completions")
async def completions(data: OpenAIinput):
    try:
        data = data.model_dump()
        print("model-dump", data)
        content = generate(input=data["prompt"])
        return Response(
            status_code=status.HTTP_200_OK,
            content=content,
            media_type="application/json",
        )
    except Exception as e:
        traceback.print_exc()
        print("codegen", e)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000)
