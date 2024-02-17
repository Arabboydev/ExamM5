import os
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
import threading

def save_page_as_pdf(url, page_num):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for p in soup.find_all('p'):
        pdf.cell(200, 10, p.get_text(), ln=True)
    pdf.output(f"homonyms/page_{page_num}.pdf")

def save_all_pages(start_page, end_page):
    for page_num in range(start_page, end_page+1):
        url = f"https://tilshunos.com/omonims/?page={page_num}"
        save_page_as_pdf(url, page_num)

os.makedirs("homonyms", exist_ok=True)

num_threads = 5

pages_per_thread = (1320 // num_threads) + 1
threads = []

for i in range(num_threads):
    start_page = i * pages_per_thread + 1
    end_page = min((i + 1) * pages_per_thread, 1320)
    thread = threading.Thread(target=save_all_pages, args=(start_page, end_page))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("Hamma fayllar homonyms faylga saqlanadi")
