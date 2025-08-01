from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Powered By 𓆩ཫ--FʀᴏɴᴛMᴀɴ--ཀ𓆪</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            margin: 0;
            background: linear-gradient(135deg, #212529, #3e1c47);
            font-family: 'Segoe UI', Arial, sans-serif;
            color: #fff;
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 80vh;
        }
        .logo {
            width: 130px;
            height: 130px;
            border-radius: 50%;
            margin-bottom: 1.5em;
            object-fit: cover;
            border: 3px solid #c080ff;
            background: #fff;
            box-shadow: 0 4px 18px #00000055;
        }
        .main-title {
            font-size: 2.3em;
            background: linear-gradient(90deg, #d895ed 10%, #5e17eb 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.7em;
            font-weight: bold;
        }
        .powered-by {
            font-size: 1.2em;
            margin-bottom: 30px;
        }
        footer {
            background: #11101d;
            color: #d9d9d9;
            padding: 1.3em 0;
            position: fixed;
            width: 100%;
            bottom: 0;
            border-top: 2px solid #a56be7;
        }
        .footer__copyright-info {
            font-size: 1em;
            letter-spacing: 0.05em;
        }
        @media (max-width: 600px) {
            .main-title { font-size: 1.5em; }
            .logo { width: 80px; height: 80px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Apni image ka path niche vali line me dijiye -->
        <img src="https://envs.sh/BEx.jpg/IMG20250729462.jpg" alt=𓆩ཫ--FʀᴏɴᴛMᴀɴ--ཀ𓆪"" class="logo" />
        <div class="main-title">Powered By <span style="color:#b094fa">FrontMan Services</span></div>
        <div class="powered-by"><strong>FrontManProtects You 🛡️</strong></div>
        <a href="https://t.me/MrFrontMan001" target="_blank" style="color:#e5b8ff; text-decoration:none; font-size:1.15em; font-weight:bold;">
            Visit my GitHub →
        </a>
    </div>
    <footer>
        <div class="footer__copyright">
            <p class="footer__copyright-info">
                © 2025 Video Downloader. All rights reserved. | Designed with ❤️ by <span style="color:#b094fa">Saini Mata Bots</span>
            </p>
        </div>
    </footer>
</body>
</html>

"""


if __name__ == "__main__":
    app.run()
