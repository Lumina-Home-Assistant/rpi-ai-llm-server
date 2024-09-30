if [ ! ollama ]; then
        echo "Ollama is not installed. Please install it."
else
#       ollama pull gemma:2b
        ollama serve &
#       ollama pull gemma:2b
fi

source ./.venv/bin/activate
if [ $? -ne 0]; then
        echo "Failed to activate virtual environment."
        exit 1
fi

python3 app.py
