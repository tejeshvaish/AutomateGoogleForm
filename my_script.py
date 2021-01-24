import requests
url='https://docs.google.com/forms/d/e/1FAIpQLSeGEpmM1Xqh2P4qMqaGt2F-5M_eQAusAXOx6OHsYTJ6vaFjKQ/formResponse'

values = {
"entry.1392870018":"Tejesh",
"entry.2026807687":"Tejesh",
"entry.569460078":"Tejesh",


"entry.946016447":"Piyush",
"entry.413127116":"Vineet",
"entry.38844410":"Vats",


"entry.656562348":"Tejesh",
"entry.390568429":"Shubham",
"entry.822623602":"Nippon",


"entry.97414856":"Nishant",
"entry.1826528568":"Rajit",
"entry.292168865":"Vivek",


"entry.812270944":"Piyush",
"entry.401503891":"Vineet",
"entry.687305271":"Rajit",


"entry.46104463":"Tejesh",
"entry.911065770":"Tejesh",
"entry.1587402005":"Tejesh",
}

"""user_agent = {'Referer':'https://docs.google.com/forms/d/e/1FAIpQLSeGEpmM1Xqh2P4qMqaGt2F-5M_eQAusAXOx6OHsYTJ6vaFjKQ/viewform'
','User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"}"""

for i in range(100000):
     r = requests.post(url, data=values)
