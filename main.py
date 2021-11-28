from website import ssis_app
from dotenv import load_dotenv

load_dotenv('.env')

app = ssis_app()

if __name__ == '__main__':
    app.run(debug=True)
        