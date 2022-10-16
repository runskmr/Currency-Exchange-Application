from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
def CADConversion(request):
    
    response = requests.get("https://ca.statebank/home")
    soup = BeautifulSoup(response.text, 'html.parser')
    sp = soup.find_all("span", attrs = {"class":"value"})
    for span in sp:
    # print(span)
    # print(span.get("id"))
    # span = sp[0]
        sp1 = span.get_text().strip()
    # print(sp1)
        ss = sp1.split()
    # print(ss)
    #print(len(ss))
    #print(ss[0])
    #print("In for loop")
    # print(ss[0])
        if(ss[0] == '₹'):
        # print("Ïn if conditon")
            inr = ss[1]
        # print(inr)
        #print("INR " + ss[1])
        elif(ss[0] == '$'):
        # print("In elf condition")
            usd = ss[1]
        #print("USD " + ss[1])
        # print(usd)
    
        # print(inr)
        # print(usd)
    context = {
        'INR': inr,
        'USD': usd,
    }
    return render(request, 'hello_world.html', context)

def USDConversion(request):
    
    response = requests.get("https://ca.statebank/home")
    soup = BeautifulSoup(response.text, 'html.parser')
    sp = soup.find_all("span", attrs = {"class":"value"})
    for span in sp:
        sp1 = span.get_text().strip()
    # print(sp1)
        ss = sp1.split()
        if(ss[0] == '₹'):
            inr = ss[1]
        elif(ss[0] == '$'):
            usd = ss[1]

    context = {
        'INR': inr,
        'USD': usd,
    }
    return render(request, 'americandollar.html', context)
        
    