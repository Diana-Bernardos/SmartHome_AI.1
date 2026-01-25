from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from parser import interpretar_comando
from acciones import ejecutar_accion
import main  # To access helper functions like es_saludo, etc.

app = FastAPI(title="Asistente Domótico API", description="API para el asistente virtual con IA")

# Configure CORS to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development convenience
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CommandRequest(BaseModel):
    command: str

class CommandResponse(BaseModel):
    response: str
    action_type: str = None
    details: dict = None

@app.post("/api/chat", response_model=CommandResponse)
async def chat_endpoint(request: CommandRequest):
    comando = request.command.strip()
    
    if not comando:
        raise HTTPException(status_code=400, detail="Command cannot be empty")
        
    # 1. Check for conversation (Greetings, Goodbyes, Help, etc.)
    # We need to reuse logic from main.py. 
    # Since main.py code is inside functions, we can import them or duplicate logic if necessary.
    # Ideally, we should refactor main.py to make it more importable, but importing main works if functions are clean.
    
    conversation_response = main.responder_conversacion(comando)
    if conversation_response:
        return CommandResponse(response=conversation_response, action_type="conversation")
        
    # 2. Process Smart Home Command
    try:
        accion_parseada = interpretar_comando(comando)
        
        if accion_parseada:
            resultado = ejecutar_accion(accion_parseada)
            return CommandResponse(
                response=resultado, 
                action_type="command", 
                details=accion_parseada
            )
        else:
            return CommandResponse(
                response="No entendí ese comando. Intenta ser más específico o escribe 'ayuda'.", 
                action_type="unknown"
            )
            
    except Exception as e:
        print(f"Error processing command: {e}")
        return CommandResponse(response=f"Ocurrió un error interno: {str(e)}", action_type="error")

@app.get("/")
def read_root():
    return {"status": "online", "message": "Asistente Domótico API is running"}
