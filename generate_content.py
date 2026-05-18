import os
import time
from datetime import datetime
from openai import OpenAI

# Initialize the AI client using the secure repository secret
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_autonomous_post():
    print("Waking up engine... Querying AI for new asset...")
    
    # Context-rich prompt tailored for a highly engaging survival/preparedness niche asset
    prompt = (
        "Write a comprehensive, deeply detailed, and practical survival guide or checklist article. "
        "Focus on high-utility topics like off-grid power, emergency water filtration, urban preparedness, "
        "or gear master-lists. Format the output directly in clean Markdown. "
        "Include an engaging 'Title:', followed by a brief introduction, structured '###' subheadings, "
        "bullet points for actionable steps, and a final conclusion highlighting essential gear."
    )
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", # Cost-effective, fast, and highly reliable for text generation
            messages=[
                {"role": "system", "content": "You are an expert operational automation assistant and survivalist strategist. You write highly analytical, actionable, and engaging content without fluff or generic AI phrasing."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        content = response.choices[0].message.content
        
        # Create the content directory if it doesn't exist yet
        os.makedirs("content", exist_ok=True)
        
        # Generate a unique filename using the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"content/post_{timestamp}.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"Success! Asset successfully written to {filename}")
        
    except Exception as e:
        print(f"Error during execution loop: {e}")

if __name__ == "__main__":
    generate_autonomous_post()
