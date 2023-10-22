#!/bin/sh

case "$1" in 
  "install")
    # for metal mac
    CMAKE_ARGS="-DLLAMA_METAL=on" pip install -r requirements.txt
  ;;
  "download")
    wget -P ./models https://huggingface.co/TheBloke/CodeLlama-7B-Python-GGUF/resolve/main/codellama-7b-python.Q6_K.gguf
    wget -P ./models https://huggingface.co/TheBloke/CodeLlama-7B-Python-GGUF/resolve/main/codellama-7b-python.Q4_K_M.gguf
  ;;
  "start")
    python ./private-prilot/app.py 
  ;;
esac