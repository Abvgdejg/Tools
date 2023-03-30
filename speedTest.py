import requests
from time import sleep
import os
from . import timeTools as TT
import sys
from threading import Thread 

TT = TT.TimeTools()

def Start(image_path, start_url = "0.0.0.0:8888", time=0):

    url = f"http://{start_url}/"

    new_file = [('image', open(image_path, 'rb'))]
    headers = {'Accept': 'application/json'}
    response_one = requests.post(url, files=new_file, headers=headers)

    send_time = TT.ChechTimer(time)

    link_one = response_one.json()["result_link"]
    estime = float(response_one.json()["estime"].split("s")[0]) + 0.5

    url = f"http://{start_url}{link_one}"


    headers = {'Accept': 'application/json'}
    sleep(estime)
    status = requests.get(url, headers=headers).json()["status"]
    while status == "new":
    
        response_two = requests.get(url, headers=headers)
        
        status = response_two.json()["status"]

    if status == "complete":
        number = requests.get(url, headers=headers).json()["number"]
        return (number, send_time, float(TT.ChechTimer(time))-0.5)
    else: return "ERROR"        
    
    
def CheckTime(image_path, start_url = "0.0.0.0:8888", count:int=1):
    
    addresses = []
    lifetimes = []

    for i in range(count):
        print(f"Start {i} checker")
        url = f"http://{start_url}/"

        new_file = [('image', open(image_path, 'rb'))]
        headers = {'Accept': 'application/json'}
        response_one = requests.post(url, files=new_file, headers=headers)

        link_one = response_one.json()["result_link"]
        

        url = f"http://{start_url}{link_one}"
        TT.StartTimer(f"await_{i}")
        lifetimes.append(10 + 1.4*(i+1))
        addresses.append(url)

    headers = {'Accept': 'application/json'}
    
    for i in range(count):
        
        while True:
            try:
                response_two = requests.get(addresses[i], headers=headers)
                
                status = response_two.json()["status"]

                sleep(1)
            except:
                print(f"{i} Checker: {TT.ChechTimer(f'await_{i}')}/{lifetimes[i]}")
                
                
                break
            



def SpeedTest(count):
    TT.StartTimer()
    for i in range(count):
            print(f"Iterration time: {float(TT.ChechTimer())-0.5*i}")
            TT.StartTimer(i)
            number,send, time = Start("./g.png", "192.168.21.63:8888", i)
            print(f"{i+1}) " + number + f" Time: {float(TT.ChechTimer(i))-0.5}, Send: {send}, Complete: {time}")
           
    t = float(TT.ChechTimer()) - (count * 0.5)
    print(f"Total time: {t}")
    print(f"Time to one file: {t / count}")

def Load():
    print("1) SpeedTest")
    print("2) CheckTime")
    choose = int(input("Choose option: "))
    if choose == 1:
        count = int(input("Choose count: "))
        SpeedTest(count)
    else: 
        count = int(input("Choose count: "))
        CheckTime("./g.png", count=count)
        # thread = []
        # for i in range(count): 
        #     thread.append(Thread(target=CheckTime, name=i, args=("./g.png", "0.0.0.0:8888", i)))
        #     thread[i].start()
        
    