from fastapi import FastAPI
from fastapi.responses import HTMLResponse


appp = FastAPI()

@appp.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Мое простое приложение</title>
        <meta charset="UTF-8">
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #333;
                text-align: center;
            }
            p {
                color: #666;
                line-height: 1.6;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Добро пожаловать!</h1>
            <p>Это простое FastAPI приложение, которое возвращает HTML страницу.</p>
            <p>Приложение работает на Ubuntu и готово к использованию!</p>
            <p><strong>Время:</strong> <span id="time"></span></p>
        </div>
        
        <script>
            function updateTime() {
                const now = new Date();
                document.getElementById('time').textContent = now.toLocaleString('ru-RU');
            }
            updateTime();
            setInterval(updateTime, 1000);
        </script>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(appp, host="0.0.0.0", port=8000)
