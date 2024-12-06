import google.generativeai as genai
from app.core.config import settings
from markdownify import markdownify

genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel(model_name=settings.GEMINI_MODEL)

def clean_markdown(text):
    return markdownify(text)

def enforce_token_limit(text, max_tokens=1000):
    tokens = text.split()
    if len(tokens) > max_tokens:
        return " ".join(tokens[:max_tokens])
    return text

def paginate_output(text, max_length=500):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

def gemini_response(text):
    text = enforce_token_limit(text)
    try:
        response = model.generate_content(text)
        clean_text = clean_markdown(response.text)
        paginated_response = paginate_output(clean_text)
        return paginated_response
    except Exception as e:
        print(f"Error generating content: {e}")
        return None