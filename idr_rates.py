import requests

json_data=requests.get('http://www.floatrates.com/daily/idr.json')
json_dict=json.da
for data in json_data.text:
    print( data['code'] )
    print ( data [ 'name' ] )
    print ( data [ 'date' ] )
    print ( data [ 'inverseRate' ] )
