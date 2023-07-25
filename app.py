from flask import Flask, render_template

summaries = ["Always refer to the latest Azure documentation for the most accurate information.",
 "Always refer to the latest Azure documentation for the most accurate information.",
 "Always refer to the latest Azure documentation for the most accurate information."]

links = ["https://github.com/arpit57/TextSummarizer", "https://github.com/arpit57/TextSummarizer", "https://github.com/arpit57/TextSummarizer"]

img_urls = ["https://tse4.mm.bing.net/th?id=OIP.o01pM7cb-KEA7GT-cC7nEgHaE8&pid=Api&P=0&h=180",
"https://tse4.mm.bing.net/th?id=OIP.o01pM7cb-KEA7GT-cC7nEgHaE8&pid=Api&P=0&h=180",
"https://tse4.mm.bing.net/th?id=OIP.o01pM7cb-KEA7GT-cC7nEgHaE8&pid=Api&P=0&h=180"]

time_stamps = ["2PM", "2PM", "2PM"]

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html", summariesLinksImagesStamps=zip(summaries, links, img_urls, time_stamps))

if __name__ == "__main__":
    app.run(debug=True)
