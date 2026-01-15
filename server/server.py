import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from google.genai import types
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

# 1. Setup Client (New Library Syntax)
# Make sure your API key is correct here!
os.environ["GOOGLE_API_KEY"] = "AIzaSyCN5558zpd0UDi2nTJOhsoDZakRT_xKmwU"
client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

@app.route('/translate', methods=['POST'])
def translate_audio():
    try:
        if 'audio' not in request.files:
            return jsonify({"error": "No audio file"}), 400
        
        audio_file = request.files['audio']
        filename = secure_filename(audio_file.filename)
        temp_path = os.path.join("/tmp", filename)
        audio_file.save(temp_path)

        print(f"🎤 Processing audio...")

        # 2. Upload file to Gemini
        # The new SDK lets us upload and generate in one go easily
        with open(temp_path, "rb") as f:
            audio_bytes = f.read()

        prompt = """
        Listen to this audio. 
        1. Transcribe the original speech exactly.
        2. Translate the meaning into **casual, conversational Hinglish** (a natural mix of Hindi and English used by Gen Z Indians).
        3. Use words like 'yaar', 'bas', 'scene', 'mast', 'tension' where they fit naturally.
        4. Do NOT simply translate word-for-word. Capture the *emotion*.
        
        Return ONLY a JSON object like this: 
        { "original": "text here", "translated": "text here" }
        """

        # 3. Generate Content (New Syntax)
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=[
                types.Part.from_bytes(data=audio_bytes, mime_type="audio/wav"),
                prompt
            ]
        )
        
        # Cleanup
        os.remove(temp_path)
        
        print(f"🤖 AI Response: {response.text}")
        return jsonify(response.text)

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # WE CHANGED THE PORT TO 5001 TO FIX THE CRASH
    app.run(host='0.0.0.0', port=5001, debug=True)