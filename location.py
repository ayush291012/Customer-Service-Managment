# importing googlemaps module

conerror="HTTPSConnectionPool(host='maps.googleapis.com', port=443): Max retries exceeded with url: /maps/api/distancematrix/json?destinations=Madhu+Resort%2Csikandra%2Cagra&origins=d-34+rangoli+colony%2Csikandra%2Cagra&key=AIzaSyArZlQRMt808tPj-A-5-38_2NVPs4euc2I (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x0000024D09C5DE20>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))"
import googlemaps
  
try:
    # Requires API key
    gmaps = googlemaps.Client(key='AIzaSyArZlQRMt808tPj-A-5-38_2NVPs4euc2I')
      
    # Requires cities name
    
    d1 = gmaps.distance_matrix('d-34 rangoli colony,sikandra,agra','Madhu Resort,sikandra,agra')#['rows'][0]['elements'][0]
      
    print(d1);
    # Printing the result
    #print(my_dist['distance'])
    
    
    #d1={'distance':{'text': '15.0 km', 'value': 15028},'duration':{'text': '38 mins', 'value': 2270},'status': 'OK'}
    
    
    #d2={'destination_addresses': ['NH-2, near Mathura Road, Sikandra, Agra, Uttar Pradesh 282007, India'], 'origin_addresses': ['D/34, Traveni Rangoli Colony, Sikandra, Agra, Uttar Pradesh 282007, India'], 'rows': [{'elements': [{'distance': {'text': '0.6 km', 'value': 582}, 'duration': {'text': '2 mins', 'value': 136}, 'status': 'OK'}]}], 'status': 'OK'}
#except Exception:
#    print("Check Your Internet Connection");

except Exception as E1:
    print(E1)
 


#print(d1)