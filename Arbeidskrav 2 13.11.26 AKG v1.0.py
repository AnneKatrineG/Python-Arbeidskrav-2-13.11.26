# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 17:26:27 2026

@author: Anne Katrine Gangstad

Arbeidskrav 2 - innleveringsfrist 13.11.26 - 6 oppgaver variabler, datatyper, array, plotting, funksjoner
"""

#%% Oppgave 1: Regn ut hvor gammel en person blir nå i løpet av år 2024

alder = int(input("Hvilket år er du født? "))

valgt_år = int(input("Hvilket år er du i nå? "))   #litt avvik fra oppgaven, gjorde "dagens" årstall fleksibelt, slik at man kan legge inn 2026 f eks

Antall_år_i_valgt_år = valgt_år - alder
print("Du er" , Antall_år_i_valgt_år , "år")

#%% Oppgave 2: Pizza på klassefest. Hver elev spiser 1/4 pizza. Hvor mange hele pizzaer må kjøpes inn

antall_elever = int(input('Skriv inn antall elever:' ))

import numpy as np                                          #må bruke numpy for å få funksjonalitet for å runde opp

antall_pizzaer = int(np.ceil(antall_elever * 0.25))         #bruker int for å få skrevet ut et heltall og np.ceil for å runde opp
print("Antall pizzaer som må handles inn er" , antall_pizzaer)

#%% Oppgave 3: Program som regner om fra grader til radianer

import numpy as np

v_grad = float(input('Skriv inn gradtallet:' ))
v_rad = v_grad*np.pi/180
print("Radiantallet til vinkelen =" ,round(v_rad, 2))       #bruker round for å runde av, har brukt 2 desimaler her

#%% Oppgave 4a og b: Opprett en dictionary og lag et program som skriver ut div. info om et land

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

land = input("legg inn (skriv) et av følgende land:  Norge, England, Frankrike eller Italia: ")     #må velge ett av disse landene

hovedstad = data[land][0]      #plukker det første ordet fra dictionaryen for landet som er lagt inn - altså hovedstaden
innbyggere = data[land][1]     #plukker det andre ordet fra dictionaryen for landet som er lagt inn - altså innbyggertallet
print(hovedstad, "er hovedstaden i", land, "og det er" , innbyggere, "mill. innbyggere i", hovedstad)  

# Oppgave 4c: La brukeren skrive inn info om et nytt land som ikke finnes i dictionaryen

print("Vi trenger hjelp til å utvide dictionaryen! Foreløpig inneholder den kun Norge, England, Frankrike og Italia")
land = input("Legg til et nytt land: " )                                                         #legger til det nye landet
hovedstad = input("Legg til hovedstaden i landet du la inn: " )                                  #legger til hovedstaden i det nye landet
innbyggere = float(input("Legg til antall innbyggere i hovedstaden (i millioner innbyggere): ")) #legger til innbyggere i hovedstaden    
data[land] = [hovedstad, innbyggere]                      #oppdaterer dictionaryen med nytt land, hovedstad og innbyggere 
print(data)

#%% Oppgave 5: Lag en funksjon som regner ut areal og ytre omkrets til en figur 

import numpy as np

a=2                                                       #la inn tenkte verdier for a og b selv om oppgaven egentlig ikke ber om det?
b=5                                                       #la inn tenkte verdier for a og b selv om oppgaven egentlig ikke ber om det?

def figur(a,b):
    areal_figur = a*b/2 + np.pi*((a/2)**2)/2              #arealet av trekanten pluss arealet av den halve sirkelen
    omkrets_figur = np.pi*a/2 + b + np.sqrt(a**2 + b**2)  #omkretsen av den halve sirkelen pluss omkretsen av b + hypotenusen i trekanten
    return areal_figur, omkrets_figur

areal_figur, omkrets_figur = figur(a,b)
print("Arealet på figuren =", round(areal_figur, 2), "og omkretsen =", round(omkrets_figur, 2))

#%% Oppgave 6: Skriv en kode som plotter funksjonen f(x) = -x**2 - 5, for x på intervallet [-10,10] 

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10, 200)                              #hint fra oppgaven
y = -x**2 - 5

plt.plot(x,y)                                             #selve plotkommandoen. trenger egentlig ikke mer enn denne
plt.xlabel("x")                                           #navngir x-aksen
plt.ylabel("f(x)")                                        #navngir y-aksen
plt.title("Funksjonen f(x) = -x^2 - 5")                   #legger inn tittel
plt.grid()                                                #viser rutenettet
plt.gca().set_facecolor("lightyellow")                    #legger inn lys gul farge bak plottet                      
plt.show()                                                #trenger vel strengt tatt ikke denne - plottet kommer når man kjører programmet



