# Multi-Doc Q&A Chatbot

Small Streamlit app that uses Google Gemini (via the `google-generativeai` SDK) to answer questions about uploaded images (for example, invoices). The main app entrypoint is `app.py`.

Features
- Upload an image (jpg / jpeg / png) and ask questions about it.
- Choose a Gemini model from the UI (e.g. `gemini-2.5-pro`, `gemini-2.5-flash`).
- Simple Streamlit UI for quick testing and iteration.

Files
- `app.py` — main Streamlit app and functions: `get_gemini_response`, `input_image_setup`.
- `requirements.txt` — Python dependencies used by the project.
- `.env` — environment variables (not checked in). Add `GOOGLE_API_KEY` here.

Quickstart

1. Create a virtual environment and activate it (recommended):
   ```sh
   python3 -m venv env
   source env/bin/activate   # macOS / Linux (zsh / bash)
   ```

2. Install dependencies (choose one):
   - From `requirements.txt`:
     ```sh
     pip install -r requirements.txt
     ```
   - Or install core packages individually:
     ```sh
     pip install --upgrade google-generativeai streamlit pillow python-dotenv
     ```

3. Create a `.env` file at the project root and add your Google API key:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```
   The app loads this via `load_dotenv()` in `app.py`.

4. Run the app with Streamlit:
   ```sh
   streamlit run app.py
   ```
   Open the URL shown in the terminal (usually http://localhost:8501).

Usage
- Select a Gemini model from the dropdown.
- Enter a question in the text input box.
- Upload an image (jpg / jpeg / png) containing the document you want to ask about.
- Click "Generate Response" to call the Gemini model and display the answer.

Implementation notes
- `input_image_setup` converts the uploaded file into the MIME+bytes structure expected by the Gemini SDK.
- `get_gemini_response` creates a `genai.GenerativeModel` and calls `generate_content` with the text and image parts.
- The code expects `GOOGLE_API_KEY` to be available in environment variables.

Troubleshooting
- "No file uploaded": make sure you uploaded an image before clicking "Generate Response".
- API key errors: check that `GOOGLE_API_KEY` is set in `.env` and the key is valid for the Google Generative AI / Gemini service.
- Streamlit not launching: ensure dependencies are installed in the active environment and `streamlit` is available (`which streamlit`).
- If you see errors from the `google-generativeai` package, upgrade to the latest version:
  ```sh
  pip install --upgrade google-generativeai
  ```

Security & privacy
- Do not commit your `.env` or API keys to source control.
- Uploaded images are sent to Google Gemini for processing. Ensure you are comfortable sharing the content with the API.

Extending the project
- Add OCR pre-processing to extract text from images before sending to Gemini.
- Add structured extraction to output JSON of invoice fields (date, total, vendor, line items).
- Add more robust error handling and logging.



