# Import necessary libraries
import requests
from bs4 import BeautifulSoup 
from flask import Flask, request, render_template

app = Flask(__name__)

# Function to fetch and analyze SEO details
def seo_checker(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract Title
        title = soup.title.string if soup.title else "No title found"

        # Extract Meta Description
        meta_desc = soup.find("meta", attrs={"name": "description"})
        meta_desc_content = meta_desc['content'] if meta_desc else "No meta description found"

        # Extract H1 Tag
        h1_tag = soup.find("h1")
        h1_text = h1_tag.text.strip() if h1_tag else "No H1 tag found"

        # Extract H2 Tags
        h2_tags = [h2.text.strip() for h2 in soup.find_all("h2")]
        h2_list = h2_tags if h2_tags else ["No H2 tags found"]

        # Extract Images and Alt Attributes
        images = [{"src": img["src"], "alt": img.get("alt", "No alt text")} for img in soup.find_all("img")]

        # Word Count
        text_content = soup.get_text()
        word_count = len(text_content.split())

        return {
            "Title": title,
            "Meta Description": meta_desc_content,
            "H1 Tag": h1_text,
            "H2 Tags": h2_list,
            "Images": images,
            "Word Count": word_count
        }
    except Exception as e:
        return {"Error": str(e)}

# Flask Route to render the web page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            result = seo_checker(url)
            return render_template("index.html", result=result, url=url)
    
    return render_template("index.html", result=None)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
