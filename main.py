import requests
import PyPDF2
import playsound as ps
from environs import Env

env=Env()
env.read_env()

API_KEY = env.str("API_KEY")
END_POINT = "https://api.voicerss.org/"

# opening up the .pdf file and read its content
with open('just_text.pdf', "rb") as file_name:
    pdf_reader = PyPDF2.PdfReader(file_name)
    pages = pdf_reader.pages[:]
    read_text = ""
    for page in pages:
        read_text += page.extract_text().replace("\n", "")

# parameters for request
parameters = {
    "key": API_KEY,
    "src":read_text[1000:2000],
    "hl": "en-us",
}

# sending get request to the endpoint
response = requests.get(END_POINT, params=parameters)
print(response.status_code)
with open("sound.wav", "wb") as file_name:
    file_name.write(response.content)

# playing the sound
ps.playsound("sound.wav")