import random

# This is a MOCKED AI description generator.
# It simulates a call to GPT/Gemini to avoid needing an API key for the demo.
def generate_product_info(product_name: str, language: str = "en"):
    """
    Mocks the generation of a product description and category suggestion.
    """
    print(f"🤖 Mock AI: Generating description for '{product_name}' in language '{language}'.")

    # Mocked data
    categories = ["Spices", "Vegetables", "Grains", "Handicrafts", "Snacks"]
    
    descriptions = {
        "en": [
            f"High-quality, freshly sourced {product_name}. Perfect for daily use and adds authentic flavor to your dishes. hygienically packed.",
            f"Introducing our premium {product_name}, sourced directly from local farms. It's 100% natural and free from preservatives.",
            f"Get the best value with our {product_name}. Ideal for households and restaurants looking for quality and affordability."
        ],
        "hi": [
            f"उच्च गुणवत्ता वाला, ताज़ा {product_name}। दैनिक उपयोग के लिए बिल्कुल सही और आपके व्यंजनों में प्रामाणिक स्वाद जोड़ता है। स्वच्छ रूप से पैक किया गया।",
            f"पेश है हमारा प्रीमियम {product_name}, सीधे स्थानीय खेतों से प्राप्त। यह 100% प्राकृतिक और परिरक्षकों से मुक्त है।",
            f"हमारे {product_name} के साथ सर्वोत्तम मूल्य प्राप्त करें। गुणवत्ता और सामर्थ्य की तलाश करने वाले घरों और रेस्तरां के लिए आदर्श।"
        ],
        "ta": [
            f"உயர்தர, తాజాగా பெறப்பட்ட {product_name}. தினசரி பயன்பாட்டிற்கு ஏற்றது மற்றும் உங்கள் உணவுகளுக்கு உண்மையான சுவையை சேர்க்கிறது. சுகாதாரமான முறையில் நிரம்பியுள்ளது.",
            f"எங்கள் பிரீமியம் {product_name} ஐ அறிமுகப்படுத்துகிறோம், இது உள்ளூர் பண்ணைகளிலிருந்து நேரடியாகப் பெறப்படுகிறது. இது 100% இயற்கையானது மற்றும் பதப்படுத்திகள் இல்லாதது.",
        ],
         "te": [
            f"అధిక-నాణ్యత, తాజాగా మూలం చేయబడిన {product_name}. రోజువారీ ఉపయోగం కోసం పర్ఫెక్ట్ మరియు మీ వంటకాలకు ప్రామాణికమైన రుచిని జోడిస్తుంది. పరిశుభ్రంగా ప్యాక్ చేయబడింది.",
            f"మా ప్రీమియం {product_name}ని పరిచయం చేస్తున్నాము, ఇది స్థానిక పొలాల నుండి నేరుగా తీసుకోబడింది. ఇది 100% సహజమైనది మరియు సంరక్షణకారుల నుండి ఉచితం.",
        ],
         "bn": [
            f"উচ্চ-মানের, তাজাভাবে উৎস করা {product_name}। দৈনন্দিন ব্যবহারের জন্য পারফেক্ট এবং আপনার খাবারে খাঁটি স্বাদ যোগ করে। স্বাস্থ্যকরভাবে প্যাক করা।",
            f"আমাদের প্রিমিয়াম {product_name} উপস্থাপন করা হচ্ছে, সরাসরি স্থানীয় খামার থেকে সংগ্রহ করা। এটি 100% প্রাকৃতিক এবং প্রিজারভেটিভ মুক্ত।",
        ],
    }
    
    # Select a random description based on language, default to English
    lang_descriptions = descriptions.get(language, descriptions["en"])
    
    response = {
        "description": random.choice(lang_descriptions),
        "category_suggestion": random.choice(categories)
    }
    
    return response

# --- REAL GEMINI/GPT IMPLEMENTATION (for reference) ---
# import google.generativeai as genai
# import os

# def generate_product_info_real(product_name: str, language: str = "en"):
#     """
#     Uses a real LLM (like Google's Gemini) to generate a description.
#     """
#     # Configure the API key
#     # genai.configure(api_key=os.environ["GEMINI_API_KEY"])
#     # model = genai.GenerativeModel('gemini-1.5-flash')
    
#     prompt = f"""
#     You are an expert copywriter for rural Indian sellers.
#     Given the product name "{product_name}", do the following:
#     1. Write a short, appealing, and simple product description in the specified language code: {language}.
#     2. Suggest the best single category for this product from this list: ["Spices", "Vegetables", "Grains", "Handicrafts", "Snacks", "Dairy", "Oils"].
    
#     Return the output as a JSON object with two keys: "description" and "category_suggestion".
#     For example: {{"description": "Your generated description here.", "category_suggestion": "Spices"}}
#     """
    
#     # response = model.generate_content(prompt)
#     # return json.loads(response.text)
    
#     # This is a mocked response for the real function placeholder
#     return generate_product_info(product_name, language)