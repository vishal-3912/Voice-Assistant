import google.generativeai as genai

# Configure the Gemini API with your key
genai.configure(api_key="AIzaSyCd_uMYd3fY_GgDcfUlWYUepiKMy5dytuA")  # Replace with your actual key

def ask_gemini(prompt):
    """Send a prompt to Gemini AI and return the response."""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Correct model name
        response = model.generate_content(prompt)
        return response.text if response else "Sorry, I couldn't generate a response."
    
    except Exception as e:
        return f"Error: {str(e)}"








