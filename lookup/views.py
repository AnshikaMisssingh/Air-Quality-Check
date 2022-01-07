from django.shortcuts import render

# Create your views here.

def home(request):
    import json
    import requests
    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=6FFD3F78-7697-4485-BD0B-0C73B912DE2E")
        try:
            api = json.loads(api_request.content)
        except:
            api = "No Data Available"

        if api[0]['Category']['Name']:
            category_description = "The AQI value for your community is between 0 and 50. Air quality is satisfactory and poses little or no health risk."
            category_color = "good"
        elif api[0]['Category']['Name']:
            category_description = "The AQI is between 51 and 100. Air quality is acceptable; however, pollution in this range may pose a moderate health concern for a very small number of individuals. People who are unusually sensitive to ozone or particle pollution may experience respiratory symptoms."
            category_color = "moderate"
        elif api[0]['Category']['Name']:
            category_description = "When AQI values are between 101 and 150, members of sensitive groups may experience health effects, but the general public is unlikely to be affected."
            category_color = "usg"
        elif api[0]['Category']['Name']:
            category_description = " Everyone may begin to experience health effects when AQI values are between 151 and 200. Members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name']:
            category_description = "AQI values between 201 and 300 trigger a health alert, meaning everyone may experience more serious health effects."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name']:
            category_description = "AQI values over 300 trigger health warnings of emergency conditions. The entire population is even more likely to be affected by serious health effects."
            category_color = "hazardous"
        elif api[0]['Category']['Name']:
            category_description = "Range 500+ The air quality is beyond the AQI scale in your area. Use an oxygen mask, maybe..."
            category_color = "beyond"
        
        
        return render(request, 'home.html', {
            'api': api,
            'category_description':category_description,
            'category_color': category_color
        })
        
    else:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=02115&distance=25&API_KEY=6FFD3F78-7697-4485-BD0B-0C73B912DE2E")
        try:
            api = json.loads(api_request.content)
        except:
            api = "No Data Available"

        if api[0]['Category']['Name']:
            category_description = "The AQI value for your community is between 0 and 50. Air quality is satisfactory and poses little or no health risk."
            category_color = "good"
        elif api[0]['Category']['Name']:
            category_description = "The AQI is between 51 and 100. Air quality is acceptable; however, pollution in this range may pose a moderate health concern for a very small number of individuals. People who are unusually sensitive to ozone or particle pollution may experience respiratory symptoms."
            category_color = "moderate"
        elif api[0]['Category']['Name']:
            category_description = "When AQI values are between 101 and 150, members of sensitive groups may experience health effects, but the general public is unlikely to be affected."
            category_color = "usg"
        elif api[0]['Category']['Name']:
            category_description = " Everyone may begin to experience health effects when AQI values are between 151 and 200. Members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name']:
            category_description = "AQI values between 201 and 300 trigger a health alert, meaning everyone may experience more serious health effects."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name']:
            category_description = "AQI values over 300 trigger health warnings of emergency conditions. The entire population is even more likely to be affected by serious health effects."
            category_color = "hazardous"
        elif api[0]['Category']['Name']:
            category_description = "Range 500+ The air quality is beyond the AQI scale in your area. Use an oxygen mask, maybe..."
            category_color = "beyond"
        
        
        return render(request, 'home.html', {
            'api': api,
            'category_description':category_description,
            'category_color': category_color
        })
        

    