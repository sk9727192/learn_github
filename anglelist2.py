import urllib2
import json
import hashlib
import csv
from hashlib import md5
present=[]
loc=[]
Url=[]
angel_url=[]
j=0
f = open('Angle list-7.csv','r')
reader = csv.DictReader(f,dialect='excel')

for row in reader:
  email=row['email']
  m=hashlib.md5(email)
  md5_text=m.hexdigest()
  url1 = 'https://api.angel.co/1/users/search?md5='+md5_text+'&access_token=fb202096d631cbfb91c941d0667e1cbe349a3555074b9c50'
  url2 = 'https://api.angel.co/1/users/search?md5='+md5_text+'&access_token=b574f13eb5fb5958721234b0a993ceded8a25bd073afa4e4'
  locality = email.replace(' ', '%20')
  j=j+1
  print	j
  try:
    json_obj = urllib2.urlopen(url1) 
    data = json.load(json_obj) 
    present.append("Yes")
    if not data['locations']:
    	loc.append("None")
    if data['locations']:
	    if data['locations'][0] ==[]:
	        loc.append("None")
	    else:
	        loc.append(data['locations'][0]['name'])    
    if data['linkedin_url'] is None:
    	if data['twitter_url'] is None:
    		if data['facebook_url'] is None:
    			Url.append("None")
    		else:
    			Url.append(data['facebook_url'])
        else:
            Url.append(data['twitter_url'])
    else:
        Url.append(data['linkedin_url'])
    angel_url.append(data['angellist_url'])                
  except urllib2.HTTPError, err:
    if err.code == 404:
	   present.append("No")
	   loc.append("No")
	   Url.append("No")
	   angel_url.append("No")
  except urllib2.URLError, e:
  	try:
  		print "From ==== 2"
  		json_obj = urllib2.urlopen(url2)
  		data = json.load(json_obj)
  		present.append("Yes")
  		if not data['locations']:
  			loc.append("None")
  		if data['locations']:
  			if data['locations'][0] ==[]:
  				loc.append("None")
  			else:
  				loc.append(data['locations'][0]['name'])
  		if data['linkedin_url'] is None:
  			if data['twitter_url'] is None:
  				if data['facebook_url'] is None:
  					Url.append("None")
  				else:
  					Url.append(data['facebook_url'])
  			else:
  				Url.append(data['twitter_url'])
  		else:
  			Url.append(data['linkedin_url'])
  		angel_url.append(data['angellist_url'])
  	except urllib2.HTTPError, err:
  		if err.code == 404:
  			present.append("No")
  			loc.append("No")
  			Url.append("No")
  			angel_url.append("No")
  		else:
  			raise  			
for item in loc,present,Url,angel_url:
    print item  
f.close() 
print "======================================="
with open('main_angellist-7.csv', 'wb') as csvfile:
    fieldnames = ['on anglelist','city','angellist_url','Url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(loc)):
    	foo=Url[i].encode('ascii','ignore') 
       	writer.writerow({'on anglelist':present[i],'city':loc[i],'angellist_url':angel_url[i],'Url':foo})