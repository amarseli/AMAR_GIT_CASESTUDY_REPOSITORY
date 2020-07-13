## budget and cuisine vizag with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "budgetmax": "500"}
    - slot{"budgetmax": "500"}
    - slot{"cuisine": "south indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"validate_cuisine": "valid"}
    - action_validate_budget
    - slot{"budget": 0}
    - slot{"budgetmin": 301}
    - slot{"budgetmax": 700}
    - slot{"validate_budget": "valid"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location": "Delhi"}
    - slot{"validate_location": "valid"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"emailid": "prajwalakonda@gmail.com"}
    - slot{"emailid": "prajwalakonda@gmail.com"}
    - action_trigger_email
    - utter_goodbye

## budgetmax 10000 Bangalore
* restaurant_search{"cuisine": "chinese", "budgetmax": "10000"}
    - slot{"budgetmax": "10000"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"validate_cuisine": "valid"}
    - action_validate_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 10000}
    - slot{"validate_budget": "valid"}
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_location
    - slot{"location": "Bangalore"}
    - slot{"validate_location": "valid"}
    - action_search_restaurants
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## Story of all in one guntur
* greet
    - utter_greet
* restaurant_search{"location": "guntur", "budgetmax": "700", "cuisine": "South Indian"}
    - slot{"budgetmax": "700"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "guntur"}
    - action_validate_location
    - slot{"location": "guntur"}
    - slot{"validate_location": "valid"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - slot{"validate_cuisine": "valid"}
    - action_validate_budget
    - slot{"budget": 0}
    - slot{"budgetmin": 301}
    - slot{"budgetmax": 700}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "guntur"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"emailid": "amarsrinivas.eli@sap.com"}
    - slot{"emailid": "amarsrinivas.eli@sap.com"}
    - action_trigger_email
    - utter_goodbye

## Giving only location and fastfood chinese query and budget
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "pune", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "pune"}
    - action_validate_location
    - slot{"location": "pune"}
    - slot{"validate_location": "valid"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"validate_cuisine": "valid"}
    - action_validate_budget
    - slot{"budget": 0}
    - slot{"budgetmin": 301}
    - slot{"budgetmax": 700}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"emailid": "amarsrinivas.eli@sap.com;DL_5B65150D5F99B7CE45000004@global.corp.sap"}
    - slot{"emailid": "amarsrinivas.eli@sap.com;DL_5B65150D5F99B7CE45000004@global.corp.sap"}
    - action_trigger_email
    - utter_goodbye

## Mumbai Italian in budget
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "italian", "budgetmax": "800"}
    - slot{"budgetmax": "800"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"location": "Mumbai"}
    - slot{"validate_location": "valid"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - slot{"validate_cuisine": "valid"}
    - action_validate_budget
    - slot{"budget": 0}
    - slot{"budgetmin": 701}
    - slot{"budgetmax": 10000}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"emailid": "amarsrinivas.eli@sap.com"}
    - slot{"emailid": "amarsrinivas.eli@sap.com"}
    - action_trigger_email
    - utter_goodbye

## budget and cuisine vizag with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "budgetmax": "900"}
    - slot{"budgetmax": "900"}
    - slot{"cuisine": "north indian"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"validate_cuisine": "valid"}
    - action_validate_budget
    - slot{"budget": 0}
    - slot{"budgetmin": 701}
    - slot{"budgetmax": 10000}
    - slot{"validate_budget": "valid"}
    - utter_ask_location
* restaurant_search{"location": "visakhapatnam"}
    - slot{"location": "visakhapatnam"}
    - action_validate_location
    - slot{"location": "visakhapatnam"}
    - slot{"validate_location": "valid"}
    - action_search_restaurants
    - slot{"location": "visakhapatnam"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"emailid": "amarsrinivas.eli@sap.com"}
    - slot{"emailid": "amarsrinivas.eli@sap.com"}
    - action_trigger_email
    - utter_goodbye

## budget and cuisine vizag without email
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "budgetmax": "900"}
    - slot{"budgetmax": "900"}
    - slot{"cuisine": "north indian"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"validate_cuisine": "valid"}
    - action_validate_budget
    - slot{"budget": 0}
    - slot{"budgetmin": 701}
    - slot{"budgetmax": 10000}
    - slot{"validate_budget": "valid"}
    - utter_ask_location
* restaurant_search{"location": "visakhapatnam"}
    - slot{"location": "visakhapatnam"}
    - action_validate_location
    - slot{"location": "visakhapatnam"}
    - slot{"validate_location": "valid"}
    - action_search_restaurants
    - slot{"location": "visakhapatnam"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* deny
    - utter_goodbye

## Bangalore full story
* greet	
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - slot{"validate_location": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "North Indian"}
    - slot{"validate_cuisine": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "301 - 700"}
    - slot{"budget": "301 - 700"}
    - action_validate_budget
    - slot{"budget": "301 - 700"}
    - slot{"budgetmin": 301}
    - slot{"budgetmax": 700}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* restaurant_search{"location": "chirag.vardia@sap.com"}
    - slot{"location": "chirag.vardia@sap.com"}

## pune full story
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - slot{"location": "pune"}
    - slot{"validate_location": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "North Indian"}
    - slot{"validate_cuisine": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "1 - 300"}
    - slot{"budget": "1 - 300"}
    - action_validate_budget
    - slot{"budget": "1 - 300"}
    - slot{"budgetmin": 1}
    - slot{"budgetmax": 300}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* restaurant_search{"emailid": "chirag.vardia@sap.com"}
    - slot{"emailid": "chirag.vardia@sap.com"}
    - action_trigger_email
    - utter_goodbye



## single line story-1
* restaurant_search{"location": "mumbai", "cuisine": "chinese", "budgetmax": "600"}
    - slot{"budgetmax": "600"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - action_validate_location
    - slot{"location": "mumbai"}
    - slot{"validate_location": "valid"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"validate_cuisine": "valid"}
    - action_validate_budget
    - slot{"budgetmin": 301}
    - slot{"budgetmax": 700}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"emailid": "amarseli.aimlmasters@gmail.com"}
    - slot{"emailid": "amarseli.aimlmasters@gmail.com"}
    - action_trigger_email
    - utter_goodbye
	

## Rajahmundry
* greet
    - utter_greet
* restaurant_search{"location": "Rajahmundry"}
    - slot{"location": "Rajahmundry"}
    - action_validate_location
    - slot{"location": "Rajahmundry"}
    - slot{"validate_location": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - slot{"validate_cuisine": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "300 - 700"}
    - slot{"budget": "300 - 700"}
    - action_validate_budget
    - slot{"budget": "300 - 700"}
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "Rajahmundry"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* restaurant_search{"emailid": "prajwalakonda@gmail.com"}
    - slot{"emailid": "prajwalakonda@sap.com"}
    - action_trigger_email
    - utter_goodbye

## delhi
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - slot{"validate_location": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "Italian"}
    - slot{"validate_cuisine": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "300 - 700"}
    - slot{"budget": "300 - 700"}
    - action_validate_budget
    - slot{"budget": "300 - 700"}
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* restaurant_search{"emailid": "prajwalakonda@gmail.com"}
    - slot{"emailid": "prajwalakonda@sap.com"}
    - action_trigger_email
    - utter_goodbye

## Story {"cuisine": "chinese", "location": "Bangalore"}
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bangalore"}
    - action_validate_location
    - slot{"location": "Bangalore"}
    - slot{"validate_location": "valid"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"validate_cuisine": "valid"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
    - slot{"budgetmax": "10000"}
    - slot{"budgetmin": "700"}
    - action_validate_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"emailid": "amar.sappo@gmail.com"}
    - slot{"emailid": "amar.sappo@gmail.com"}
    - action_trigger_email
    - utter_goodbye

## Story {"cuisine": "South Indian", "location": "Hyderabad"}
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "Hyderabad"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Hyderabad"}
    - action_validate_location
    - slot{"location": "Hyderabad"}
    - slot{"validate_location": "valid"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - slot{"validate_cuisine": "valid"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
    - slot{"budgetmax": "10000"}
    - slot{"budgetmin": "700"}
    - action_validate_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"emailid": "amar.sappo@gmail.com"}
    - slot{"emailid": "amar.sappo@gmail.com"}
    - action_trigger_email
    - utter_goodbye

## jaipur
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_validate_location
    - slot{"location": "jaipur"}
    - slot{"validate_location": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - slot{"validate_cuisine": "valid"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
    - slot{"budgetmax": "10000"}
    - slot{"budgetmin": "700"}
    - action_validate_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "jaipur"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* send_email
    - utter_ask_emailid
* send_email{"emailid": "amar.sappi@gmail.com"}
    - slot{"emailid": "amar.sappi@gmail.com"}
    - action_trigger_email
    - utter_goodbye
    - action_restart

## kakinada
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kakinada"}
    - slot{"location": "kakinada"}
    - action_validate_location
    - slot{"location": "kakinada"}
    - slot{"validate_location": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - slot{"validate_cuisine": "valid"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - slot{"budgetmin": "0"}
    - action_validate_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "kakinada"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* send_email
    - utter_ask_emailid
* send_email{"emailid": "amar.sappi@gmail.com"}
    - slot{"emailid": "amar.sappi@gmail.com"}
    - action_trigger_email
    - utter_goodbye
    - action_restart

## visakhapatnam {"cuisine": "chinese", "location": "visakhapatnam"}
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "visakhapatnam"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "visakhapatnam"}
    - action_validate_location
    - slot{"location": "visakhapatnam"}
    - slot{"validate_location": "valid"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"validate_cuisine": "valid"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "700", "budgetmax": "10000"}
    - slot{"budgetmax": "10000"}
    - slot{"budgetmin": "700"}
    - action_validate_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "visakhapatnam"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"emailid": "amar.sappi@gmail.com"}
    - slot{"emailid": "amar.sappi@gmail.com"}
    - action_trigger_email
    - utter_goodbye

## warangal budgetmax
* restaurant_search{"budgetmax": "1000"}
    - slot{"budgetmax": "1000"}
    - utter_ask_location
* restaurant_search{"location": "warangal"}
    - slot{"location": "warangal"}
    - action_validate_location
    - slot{"location": "warangal"}
    - slot{"validate_location": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - slot{"validate_cuisine": "valid"}
    - action_validate_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 1000}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"emailid": "amar.sappi@gmail.com"}
    - slot{"emailid": "amar.sappi@gmail.com"}
    - action_trigger_email
    - utter_goodbye
    - action_restart

## interactive_story_3
* restaurant_search{"budgetmin": "700", "location": "goa"}
    - slot{"budgetmin": "701"}
    - slot{"location": "goa"}
    - action_validate_location
    - slot{"location": "goa"}
    - slot{"validate_location": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"validate_cuisine": "valid"}
    - action_validate_budget
    - slot{"budget": 0}
    - slot{"budgetmin": 701}
    - slot{"budgetmax": 1000}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "goa"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"emailid": "prajwalakonda@gmail.com"}
    - slot{"emailid": "prajwalakonda@gmail.com"}
    - action_trigger_email
    - utter_goodbye
	
## blr invalid location
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "blr"}
    - slot{"location": "blr"}
    - action_validate_location
    - slot{"location": null}
    - slot{"validate_location": "invalid"}
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_location
    - slot{"location": "Bangalore"}
    - slot{"validate_location": "valid"}
    - utter_ask_cuisine
* deny
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"validate_cuisine": "valid"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "0", "budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - slot{"budgetmin": "0"}
    - action_validate_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## Bangalore Mexican
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_location
    - slot{"location": "Bangalore"}
    - slot{"validate_location": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"validate_cuisine": "valid"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_validate_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"emailid": "prajwalakonda@gmail.com"}
    - slot{"emailid": "prajwalakonda@gmail.com"}
    - action_trigger_email
    - utter_goodbye
    - action_restart

## bangaaaaaaaaaaaaaaaaloruuuu
    - utter_ask_howcanhelp
* restaurant_search{"budgetmax": "1000"}
    - slot{"budgetmax": "1000"}
    - utter_ask_location
* restaurant_search{"location": "bangaaaaaaaaaaaaaaaaloruuuu"}
    - slot{"location": "bangaaaaaaaaaaaaaaaaloruuuu"}
    - action_validate_location
    - slot{"location": null}
    - slot{"validate_location": "invalid"}
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_location
    - slot{"location": "Bangalore"}
    - slot{"validate_location": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - slot{"validate_cuisine": "valid"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_validate_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## search{"cuisine": "chinese", "location": "Bangalore"} 
* restaurant_search{"cuisine": "chinese", "location": "Bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bangalore"}
    - action_validate_location
    - slot{"location": "Bangalore"}
    - slot{"validate_location": "valid"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"validate_cuisine": "valid"}
    - utter_ask_budget
* restaurant_search{"budgetmin": "300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_validate_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* deny
    - utter_goodbye

## mexican in mumbai
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "mumbai"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "mumbai"}
    - action_validate_location
    - slot{"location": "mumbai"}
    - slot{"validate_location": "valid"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"validate_cuisine": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "701 - 10000"}
    - slot{"budget": "701 - 10000"}
    - action_validate_budget
    - slot{"budget": "701 - 10000"}
    - slot{"budgetmin": 701}
    - slot{"budgetmax": 10000}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"emailid": "kodalia267@gmail.com"}
    - slot{"emailid": "kodalia267@gmail.com"}
    - action_trigger_email
    - utter_goodbye

## goa mexican budget
* restaurant_search{"location": "goa", "cuisine": "mexican", "budgetmax": "1000"}
    - slot{"budgetmax": "1000"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "goa"}
    - action_validate_location
    - slot{"location": "goa"}
    - slot{"validate_location": "valid"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"validate_cuisine": "valid"}
    - action_validate_budget
    - slot{"budget": 0}
    - slot{"budgetmin": 701}
    - slot{"budgetmax": 10000}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "goa"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"emailid": "amar.sappo@gmail.com"}
    - slot{"emailid": "amar.sappo@gmail.com"}
    - action_trigger_email
    - utter_goodbye

## mexican cuisine.
    - slot{"cuisine":"mexican"}
* restaurant_search{"cuisine":"mexican"}
    - slot{"cuisine":"mexican"}
    - action_validate_cuisine
    - slot{"cuisine":"mexican"}
    - utter_ask_location
    - slot{"location":"washington"}
* restaurant_search{"location":"washington"}
    - slot{"location":"washington"}
    - action_validate_location
    - slot{"location":"washington"}
    - utter_ask_location
    - slot{"location":"hyderabad"}
* restaurant_search{"location":"hyderabad"}
    - action_validate_location
    - slot{"location":"hyderabad"}
    - utter_ask_cuisine
    - slot{"cuisine":"South Indian"}
* restaurant_search{"cuisine":"South Indian"}
    - action_validate_cuisine
    - slot{"cuisine":"South Indian"}
    - utter_ask_budget
    - slot{"budget":"701 - 10000"}
* restaurant_search{"budget":"701 - 10000"}
    - action_validate_budget
    - slot{"budget":"701 - 10000"}
    - action_search_restaurants
    - slot{"location":"hyderabad"}
    - utter_ask_email
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - slot{"validate_cuisine": "valid"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - slot{"validate_location": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "301 - 700"}
    - slot{"budget": "301 - 700"}
    - action_validate_budget
    - slot{"budget": "301 - 700"}
    - slot{"budgetmin": 301}
    - slot{"budgetmax": 700}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"emailid": "jayasankar.jagili@itelligencegroup.com"}
    - slot{"emailid": "jayasankar.jagili@itelligencegroup.com"}
    - action_trigger_email
    - utter_goodbye

## directly giving email without any other key details.
* send_email{"emailid": "amar.sappo@gmail.com"}
    - slot{"emailid": "amar.sappo@gmail.com"}
    - utter_ask_location
* restaurant_search{"location": "guntur"}
    - slot{"location": "guntur"}
    - action_validate_location
    - slot{"location": "guntur"}
    - slot{"validate_location": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "American"}
    - slot{"validate_cuisine": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "701 - 10000"}
    - slot{"budget": "701 - 10000"}
    - action_validate_budget
    - slot{"budget": "701 - 10000"}
    - slot{"budgetmin": 701}
    - slot{"budgetmax": 10000}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "guntur"}
    - slot{"validate_restaurant": true}
    - action_trigger_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"budgetmax": "300", "cuisine": "south indian", "location": "hyderabad"}
    - slot{"budgetmax": "300"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "hyderabad"}
    - action_validate_location
    - slot{"location": "hyderabad"}
    - slot{"validate_location": "valid"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"validate_cuisine": "valid"}
    - action_validate_budget
    - slot{"budget": 0}
    - slot{"budgetmin": 1}
    - slot{"budgetmax": 300}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "hyderabad"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"emailid": "amarsrinivas.eli@sap.com"}
    - slot{"emailid": "amarsrinivas.eli@sap.com"}
    - action_trigger_email
    - utter_goodbye

## 1500 mexican
* restaurant_search{"cuisine": "mexican", "budgetmax": "1500"}
    - slot{"budgetmax": "1500"}
    - slot{"cuisine": "mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"validate_cuisine": "valid"}
    - action_validate_budget
    - slot{"budget": 0}
    - slot{"budgetmin": 701}
    - slot{"budgetmax": 10000}
    - slot{"validate_budget": "valid"}
    - utter_ask_location
* restaurant_search{"location": "gurgaon"}
    - slot{"location": "gurgaon"}
    - action_validate_location
    - slot{"location": "gurgaon"}
    - slot{"validate_location": "valid"}
    - action_search_restaurants
    - slot{"location": "gurgaon"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
    - utter_goodbye


## 1500 delhi
* restaurant_search{"budget": "1500", "location": "delhi"}
    - slot{"budget": "1500"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - slot{"validate_location": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - slot{"validate_cuisine": "valid"}
    - action_validate_budget
    - slot{"budget": 1500}
    - slot{"budgetmin": 701}
    - slot{"budgetmax": 10000}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"emailid": "amar.a"}
    - slot{"emailid": "amar.a"}
    - action_trigger_email
    - utter_ask_emailid
* send_email{"emailid": "amar.sappi@gmail.com"}
    - slot{"emailid": "amar.sappi@gmail.com"}
    - action_trigger_email
    - utter_goodbye
    - action_restart

## mid range
* restaurant_search{"budgetmax": "700", "cuisine": "chinese"}
    - slot{"budgetmax": "700"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"validate_cuisine": "valid"}
    - action_validate_budget
    - slot{"budget": 0}
    - slot{"budgetmin": 301}
    - slot{"budgetmax": 700}
    - slot{"validate_budget": "valid"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - slot{"validate_location": "valid"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
    - utter_goodbye

## invalid city
* restaurant_search{"budgetmax": "300"}
    - slot{"budgetmax": "300"}
    - utter_ask_location
* restaurant_search{"location": "eluru"}
    - slot{"location": "eluru"}
    - action_validate_location
    - slot{"location": "eluru"}
    - slot{"validate_location": "invalid"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_location
    - slot{"location": "mumbai"}
    - slot{"validate_location": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "andhra"}
    - slot{"cuisine": "andhra"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - slot{"validate_cuisine": "invalid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"validate_cuisine": "valid"}
    - utter_ask_budget
* restaurant_search{"budget": "1 - 300"}
    - slot{"budget": "1 - 300"}
    - action_validate_budget
    - slot{"budget": "1 - 300"}
    - slot{"budgetmin": 1}
    - slot{"budgetmax": 300}
    - slot{"validate_budget": "valid"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"validate_restaurant": true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_email{"emailid": "prajwalakonda@gmail.com"}
    - slot{"emailid": "prajwalakonda@gmail.com"}
    - action_trigger_email
    - utter_goodbye
