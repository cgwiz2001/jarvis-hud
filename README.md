# Jarvis HUD
Standalone two-way voice HUD. PIN-gated (set with `JARVIS_HUD_PIN=… tools/set-pin.py`); private connection settings live only in browser localStorage. Static page; your xAI API key lives only in your browser's localStorage (Settings → Forget key to remove). Set a spending cap at console.x.ai.
Routes: realtime speech-to-speech (`wss://api.x.ai/v1/realtime`, ephemeral token via `/v1/realtime/client_secrets`, voice `leo`), or classic (browser SpeechRecognition → chat completions → `/v1/tts`).
Hold the mic button or Space to talk. Esc stops speech.
