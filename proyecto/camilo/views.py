from django.http import HttpResponse

def index(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Camilo</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Segoe UI', sans-serif;
                background: #0a0a0a;
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
            }
            .container { text-align: center; }
            .dot {
                width: 60px;
                height: 60px;
                border-radius: 50%;
                background: #e94560;
                margin: 0 auto 30px;
            }
            h1 { font-size: 2rem; font-weight: 300; letter-spacing: 8px; text-transform: uppercase; }
            p { color: #555; margin-top: 10px; font-size: 0.85rem; letter-spacing: 3px; }
            .line { width: 40px; height: 1px; background: #e94560; margin: 25px auto; }
            .tags { display: flex; gap: 20px; justify-content: center; margin-top: 20px; }
            .tag { color: #555; font-size: 0.75rem; letter-spacing: 2px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="dot"></div>
            <h1>Camilo Toro</h1>
            <p>DESARROLLADOR WEB</p>
            <div class="line"></div>
            <div class="tags">
                <span class="tag">PYTHON</span>
                <span class="tag">DJANGO</span>
                <span class="tag">GIT FLOW</span>
            </div>
        </div>
    </body>
    </html>
    """)