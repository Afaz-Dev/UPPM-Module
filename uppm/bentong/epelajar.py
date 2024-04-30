from bs4 import BeautifulSoup
from curl_cffi import requests

baseurl = "https://uppmmrsmbentong.com/epelajar/"

#Check credientials
def checkCred(id : str, ic : str) :
  returndat = {"error" : "unknown"}
  
  url = baseurl + "MenuUtama.asp"
  
  payload = {
    "txtNoMak": id,
    "txtPwd": ic
  }
  
  #send request
  response = requests.post(url, data=payload, impersonate="chrome110")
  
  if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    if response.url != "https://uppmmrsmlangkawi.com/epelajar/LoginGagal.asp" :
      returndat = True
    else :
      returndat = False
  else:
    fail = "Failed to retrieve. Status code: " + str(response.status_code)
    returndat = {"error" : fail}
  
  return returndat

#Get profile
def getProfile(id : str, ic : str, year : str) :
  returndat = {"error" : "unknown"}
  
  url = baseurl + "DataPeribadi.asp"
  
  payload = {
    "txtNoMak": id,
    "txtPwd": ic,
    "cboTahun": year
  }
  
  #send request
  response = requests.post(url, data=payload, impersonate="chrome110")
  
  if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    p_elements = soup.find_all("span")
    num = 0
    profile = {}
  
    while num <= 22 :
      if (num % 2) == 0:
        profile[p_elements[num].text.strip()] = p_elements[num+1].text.strip()
  
      num += 1
    profile['ALAMAT SURAT MENYURAT'] = [p_elements[25].text.strip(), p_elements[26].text.strip(), p_elements[27].text.strip(), p_elements[28].text.strip()]
    profile[p_elements[29].text.strip()] = p_elements[30].text.strip()
    returndat = profile
  else:
    fail = "Failed to retrieve. Status code: " + str(response.status_code)
    returndat = {"error" : fail}
  
  return returndat

#Get PAJSK info
def getpajsk(id : str, ic : str, year : str, form : str) :
  returndat = {"error" : "unknown"}

  url = baseurl + "KokuPajsk.asp"

  payload = {
    "txtNoMak": id,
    "txtPwd": ic,
    "cboTahun": year,
    "cboTingkatan": form
  }

  #send request
  response = requests.post(url, data=payload, impersonate="chrome110")

  if response.status_code == 200:
    returndat = response.text
  else:
    fail = "Failed to retrieve. Status code: " + str(response.status_code)
    returndat = {"error" : fail}

  return returndat
  


  
