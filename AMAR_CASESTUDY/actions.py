from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import smtplib
import requests
from email.message import EmailMessage

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
from zomatopy import budgetcount
import json
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
g_email_rest = []

class ActionValidateLocation(Action):
	def name(self):
		return 'action_validate_location'

	def run(self, dispatcher, tracker, domain):
	    config={ "user_key":"Kee your Zomato Key"}
	    zomato = zomatopy.initialize_app(config)
	    
	    loc = tracker.get_slot('location')
	    locuttermsg  = "None"
	    validate_location  = 'None'
	    try:
	        validate_location = zomato.validatelocation(loc)
	        #print('validate_location ::', validate_location)
	        d2 = json.loads(validate_location)
	        validate_location = d2['data']['validate_location']
	        #print('incoming location : ', loc)
	        #print('location validation flag : ', validate_location)
	        if validate_location == 'valid':
	            locuttermsg = 'Thanks for entering valid city'
	        else:
	            locuttermsg = "Sorry, we do not serve at the requested location. Please try for other city"
	    
	    except:
	        validate_location = 'invalid'
	        locuttermsg = "Sorry, we do not serve at the requested location. Please try for other city"
	    
	    dispatcher.utter_message("-----"+locuttermsg)
	    return [SlotSet("location", loc), SlotSet("validate_location", validate_location)]

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def get_location_suggestions(self, loc, zomato):
        
        # Get location details including latitude, longitude and City Id
        location_detail = zomato.get_location(loc, 1) # 1 is to filter only 1 city
        d1 = json.loads(location_detail)
        #print('location_detail :', d1)
        
        lat = 0
        lon = 0
        
        location_suggest = len(d1["location_suggestions"])
        
        if (location_suggest > 0):
            lat = d1["location_suggestions"][0]["latitude"]
            lon = d1["location_suggestions"][0]["longitude"]
            city_id = d1["location_suggestions"][0]["city_id"]
        
        return location_suggest, lat, lon, city_id
    
    def get_restaurants(self, lat, lon, budgetmin, budgetmax , cuisine, cityId):
        config={ "user_key":"Kee your Zomato Key"}
        zomato = zomatopy.initialize_app(config)
        
        # To get the restaurants from Zomato we need the cusine id.
        # Consideringeach city may have differnt ids for Cusine, we will get the cusine id dictionary from Zomato service 
        cuisines_dict = zomato.get_cuisines(cityId)
        #print('cusine dictionary :: ', cuisines_dict)
        rest_d = []
        #print('MYcuisine :', cuisine)
        #print('lat :', lat)
        #print('lon :', lon)
        #print('budgetmin :', budgetmin)
        #print('budgetmax :', budgetmax)
        #print('cityId eee : ', cityId)
        executor = ThreadPoolExecutor(max_workers=5)
        for res_key in range(0, 101, 20):
            executor.submit(retrieve_restaurant, lat, lon, cuisines_dict, cuisine, res_key, rest_d)
        executor.shutdown()
        
        return rest_d

    def run(self, dispatcher, tracker, domain):
        # Initialize Zomato
        try:
            config={ "user_key":"Kee your Zomato Key"}
            zomato = zomatopy.initialize_app(config)

            # Get location from slot
            loc = tracker.get_slot('location')

            # Get cuisine from slot
            cuisine = tracker.get_slot('cuisine')

            #Get the Budget min and max slots
            budgetmin = tracker.get_slot('budgetmin')
            budgetmax = tracker.get_slot('budgetmax')

            # Check the location suggestions from Zomato
            location_suggest, lat, lon, city_id = self.get_location_suggestions(loc,zomato)

            #print('location_suggest :', location_suggest)
            #print('location_lat :', lat)
            #print('location_lon :', lon)
            #print('location_cityid :', city_id)
            rest_d = ''

            if location_suggest == 0:

                # Zomato API could not find suggestions for this location.
                validate_restaurant = False
                dispatcher.utter_message("Sorry, no results found in this location:("+ "\n")
            else:
                rest_d = self.get_restaurants(lat, lon, budgetmin, budgetmax, cuisine, city_id)

                #print(' rest_d :: ', rest_d)

                # Filter the results based on budget
                budget_d = [rest_d_single for rest_d_single in rest_d if ((rest_d_single['restaurant']['average_cost_for_two'] > budgetmin) & (int(rest_d_single['restaurant']['average_cost_for_two']) < budgetmax))]
                #print('budget_d :: ',budget_d)
                # Sort the results according to the restaurant's rating
                budget_d_rating_sorted = sorted(
                    budget_d, key=lambda k: k['restaurant']['user_rating']['aggregate_rating'], reverse=True)
                #print('budget_d_rating_sorted  :: ',budget_d_rating_sorted)
                # Build the response
                response = ""
                validate_restaurant = False

                if len(budget_d_rating_sorted) == 0:
                    dispatcher.utter_message("Sorry, we could not able to found results with this budget criteria:("+ "\n")
                else:
                    # Pick the top 5
                    budget_d_rating_top5 = budget_d_rating_sorted[:5]
                    global g_email_rest
                    g_email_rest = budget_d_rating_sorted[:10]
                    if(g_email_rest and len(g_email_rest) > 0):
                        validate_restaurant = True
                    for ind, restaurant in enumerate(budget_d_rating_top5):
                        response = response + str(ind+1) +' :    ' + restaurant['restaurant']['name'] + " in " + str(restaurant['restaurant']['location']['address']) + \
                            " has been rated " + \
                            str(restaurant['restaurant']['user_rating']['aggregate_rating']) + "\n" + "\n"

                    #g_email_rest = response 
                    #print('validate_restaurant - *** ',validate_restaurant)
                    dispatcher.utter_message("Here are the top best restaurants for you!"+ "\n" + response)
        except:
                validate_restaurant = False
                dispatcher.utter_message("Sorry, no results found in this location:("+ "\n")
                return [SlotSet('location', loc),  SlotSet('validate_restaurant', validate_restaurant)]

        return [SlotSet('location', loc),  SlotSet('validate_restaurant', validate_restaurant)]


class ActionValidateBudget(Action):

    def name(self):
        return "action_validate_budget"

    def run(self, dispatcher, tracker, domain):
        try:
            budgetmin = 0
            budgetmax = 0
            budget = 0
            loc = tracker.get_slot('location')
            validate_location = tracker.get_slot('validate_location')
            cuisine = tracker.get_slot('cuisine')
            people = tracker.get_slot('people')
            email = tracker.get_slot('email')
            budget = tracker.get_slot('budget')
            budgetmin = tracker.get_slot('budgetmin')
            budgetmax = tracker.get_slot('budgetmax')

            buttonflag = False

            if budget == '1 - 300':
                buttonflag = True
                budgetmin = 1
                budgetmax = 300
            elif budget == '301 - 700':
                buttonflag = True
                budgetmin = 301
                budgetmax = 700
            elif budget == '701 - 10000':
                buttonflag = True
                budgetmin = 701
                budgetmax = 10000

            error_msg = "Sorry!! no restaurants found for given search criteria. try once again"
            validate_budget = 'invalid'

            if buttonflag == True:
                dispatcher.utter_message('You have selected valid budget.')
                return [SlotSet('budget', budget), SlotSet('budgetmin', budgetmin), SlotSet('budgetmax', budgetmax), SlotSet('validate_budget', 'valid')]
            else:
                try:
                    budget = int(budget)
                except:
                    budget = 0

                try:
                    budgetmin = int(budgetmin)
                except:
                    budgetmin = 0

                try:
                    budgetmax =  int(budgetmax)
                except:
                    budgetmax = 0

                #print('budgetmin ', budgetmin)
                #print('budgetmax ', budgetmax)
                #print('budget    ', budget)
                
                #master_dict = [ [0,300], [301, 700], [701, 10000]] 
                #master_budget = [ [budget], [budgetmin], [budgetmax] ]
                if budget > 0 and budgetmin == 0 and budgetmax == 0:
                    if budget > 1 and budget < 301:
                        budgetmin = 1
                        budgetmax = 300
                    elif budget > 300 and budget < 701:
                        budgetmin = 301
                        budgetmax = 700
                    elif budget > 700:
                        budgetmin = 701
                        budgetmax = 10000
                elif budgetmin == 0 and budgetmax == 0:
                    budgetmin = 1
                    budgetmax = 100
                elif budgetmin == 0 and budgetmax <= 300:
                    budgetmin = 1
                    budgetmax = 300
                elif budgetmin <= 301 and budgetmax == 0:
                    budgetmin = 1
                    budgetmax = 300
                elif budgetmin > 300 and budgetmax == 0:
                    budgetmin = 301
                    budgetmax = 700
                elif budgetmin == 0 and budgetmax <= 700:
                    budgetmin = 301
                    budgetmax = 700
                elif budgetmin <= 700 and budgetmax == 0:
                    budgetmin = 300
                    budgetmax = 701
                elif budgetmin == 0 and budgetmax > 700:
                    budgetmin = 701
                    budgetmax = 10000
                elif budgetmin > 700 and budgetmax == 0:
                    budgetmin = 701
                    budgetmax = 10000

                dispatcher.utter_message('You have selected valid budget.')
                return [SlotSet('budget', budget), SlotSet('budgetmin', budgetmin), SlotSet('budgetmax', budgetmax), SlotSet('validate_budget', 'valid')]
            
        except:
            dispatcher.utter_message(error_msg)
            return [SlotSet('budget', budget), SlotSet('budgetmin', budgetmin), SlotSet('budgetmax', budgetmax), SlotSet('validate_budget', 'invalid')]


class ActionValidateCuisine(Action):
    def name(self):
        return "action_validate_cuisine"
    
    def run(self, dispatcher, tracker, domain):
        validate_cuisine = 'None'
        cuisineslist = ['italian' ,
                    'Italian' , 
                    'italy' , 
                    'itallian' , 
                    'italia' , 
                    'Itallian' , 
                    'Chinese' , 
                    'chinese' , 
                    'Chines' , 
                    'chines' , 
                    'China' , 
                    'china' , 
                    'north' , 
                    'North Indian' , 
                    'North Ind' , 
                    'northindian' , 
                    'NorthIndia' , 
                    'North' , 
                    'north side' , 
                    'northern' , 
                    'north indian' , 
                    'South Indian' , 
                    'South Ind' , 
                    'southindian' , 
                    'SouthIndia' , 
                    'South' , 
                    'south side' , 
                    'southern' , 
                    'Southern spcice' , 
                    'south spicy' , 
                    'south indian' , 
                    'american' , 
                    'America' , 
                    'america' , 
                    'mexican' , 
                    'Mexican' , 
                    'Mexica' , 
                    'Mexicann' , 
                    'Mexi']
        cuisine = tracker.get_slot('cuisine')
        error_msg = "Sorry!! The cuisine is not supported. Please re-enter."
        cuisine = tracker.get_slot('cuisine')
        
        if cuisine in cuisineslist:
            dispatcher.utter_message('Thanks for entering valid cuisine. We are searching for restaurants')
            return [SlotSet('cuisine', cuisine), SlotSet('validate_cuisine', 'valid')]
        else:
            dispatcher.utter_message(error_msg)
            return [SlotSet('cuisine', None), SlotSet('validate_cuisine', 'invalid')]

def retrieve_restaurant(lat, lon, cuisines_dict, cuisine, res_key, d_rest):
    
    #print('retrieve_cuisine :', cuisine)
    #print('retrieve_lat :', lat)
    #print('retrieve_lon :', lon)
    #print('retrieve_cuisines_dict :', cuisines_dict)
    #print('retrieve_res_key :', res_key)
    #print('retrieve_d_rest eee : ', d_rest)
    base_url = "https://developers.zomato.com/api/v2.1/"
    headers = {'Accept': 'application/json',
                'user-key': 'Kee your Zomato Key'}
    try:
        results = (requests.get(base_url + "search?" + "&lat=" + str(lat) + "&lon=" + str(lon) + "&cuisines=" + str(
            cuisines_dict.get(cuisine)) + "&start=" + str(res_key)+"&count=20", headers=headers).content).decode("utf-8")
        
        #print('results inside retrieve rest :', results)
    except:
        return
    d = json.loads(results)
    d_rest.extend(d['restaurants'])

      

class ActionTrigerEmail(Action):
    
    def name(self):
        return 'action_trigger_email'
        
    def run(self, dispatcher, tracker, domain):
        try:
            to_email = tracker.get_slot('emailid')

            # Import the email modules we'll need
            # Open the plain text file whose name is in textfile for reading.
            msg = EmailMessage()
            
            print(' User Entered Email ID : ', to_email)

            # me == the sender's email address
            # you == the recipient's email address

            loc = tracker.get_slot('location')

            cuisine = tracker.get_slot('cuisine')

            global g_email_rest
            email_rest_count = len(g_email_rest)
            #print(' g_email_rest :: \n', g_email_rest)
            
            var1 = '<h2>WELCOME TO INDIAs BEST FOODIE APP </h2>'
            
            var2 = '<img src=\"FOODIE_APP.jpg\" alt=\"Trulli\" width=\"600\" height=\"200\">'

            d_email_subj = "Top " + str(email_rest_count) + " " + cuisine.capitalize() + " restaurants in " + str(loc).capitalize()

            msg['Subject'] = '' + d_email_subj

            msg['From'] = 'your from email id'

            msg['To'] = to_email

            g_email_msg = '<p><strong> Here are the ' + d_email_subj + '</strong></p><ol>' 
            

            for ind, restaurant in enumerate(g_email_rest):
                if ind < 5:
                    g_email_msg = g_email_msg + '<li>' + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + '</li>' +"\n"
                else:
                    break

            # Send the message via our own SMTP server.
            
            #g_email_msg + g_email_msg + '</ol>'+ '\n'+ '<p><strong>&nbsp;</strong><strong>Thank you for using our FOODIE APP. See you next time. Have a nice day</strong></p><p><strong>&nbsp;</strong></p>'
            
            
            s = smtplib.SMTP("smtp.gmail.com", 587)

            s.starttls()

            s.login("from email id", "from email id login password")

            #print('Email Content :: \n', g_email_msg)

            #msg.set_content(var1+var2)
            msg.set_content(var1+"""\
<html>
  <head></head>
  <body>"""+ g_email_msg + """\
<p><strong>&nbsp;</strong><strong>Thank you for using our FOODIE APP. See you next time. Have a nice day</strong></p>
<p><strong>&nbsp;</strong></p>
  </body>
</html>
""".format(), subtype='html')

            s.send_message(msg)

            #print('Email sent ')
            
            g_email_rest = ''

            s.quit()

            dispatcher.utter_message("**** EMAIL SENT! HAPPY DINING :) ****")
        except:
            dispatcher.utter_message("**** Sorry Please enter a valid email ID :) ****")
            
        return []
