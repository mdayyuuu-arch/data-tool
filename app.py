from flask import Flask, render_template_string, request
app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html>
<head>
<title>Data Analysis Tool</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
body{background:#0a0c0f;color:#00ff41;font-family:monospace;padding:16px}
h1{text-align:center;text-shadow:0 0 10px #00ff41}
.card{border:1px solid #1a2a1a;padding:12px;margin:10px 0;background:#0f1318}
textarea{background:#111;color:#00ff41;border:1px solid #00ff41;padding:8px;width:100%;margin:6px 0;font-family:monospace}
button{background:#00ff41;color:#000;padding:8px;border:none;width:100%;font-weight:bold;cursor:pointer}
.result{background:#060809;border:1px solid #00ff41;padding:12px;margin-top:12px;white-space:pre-wrap;font-size:0.78rem}
</style>
</head>
<body>
<h1>Data Analysis Tool</h1>
<p style="text-align:center;color:#4a7a55">by Mohammed Ayaan</p>
<div class="card">
<h3>Enter Numbers (one per line)</h3>
<form method="POST">
<textarea name="data" rows="5" placeholder="10&#10;20&#10;30&#10;40&#10;50"></textarea>
<button type="submit">Analyze</button>
</form>
</div>
{% if result %}
<div class="result">{{ result }}</div>
{% endif %}
</body></html>"""

@app.route("/", methods=["GET","POST"])
def home():
    result = ""
    if request.method == "POST":
        data = request.form.get("data","")
        try:
            nums = [float(x.strip()) for x in data.strip().splitlines() if x.strip()]
            total = sum(nums)
            avg = total/len(nums)
            result = f"Count: {len(nums)}\nSum: {total}\nAverage: {avg:.2f}\nMin: {min(nums)}\nMax: {max(nums)}"
        except:
            result = "Error: Enter valid numbers!"
    from flask import render_template_string
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    print("[*] Data Tool: http://127.0.0.1:5003")
    app.run(host="127.0.0.1", port=5003, debug=False)

