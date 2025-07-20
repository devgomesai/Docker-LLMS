import requests

url = "http://localhost:12434/engines/llama.cpp/v1/chat/completions"


data = {
    "model":"ai/smollm2",
    "messages":[
        {
            "role":"system",
            "content":"You are a helpful assistant"
            
        },
        {
            "role":"user",
            "content":"Create a travel itinerary to Bangalore."
            
        }
    ]
}

response = requests.post(url, json=data)

response.raise_for_status()

print(response.json()["choices"][0]["message"]["content"])

""" 
    -- Response -- :
    
    Here's a suggested travel itinerary to Bangalore:

    **Day 1: Arrival and Exploring the City**

    1. Arrive in Bangalore and check-in at the Bangalore International Airport.
    2. Spend the evening exploring the city's popular attractions such as the National Gallery of Modern Art, the Science City, and the Goa Palace.
    3. Visit the beautiful Ranganathaswamy Temple on the southern side of the city.
    4. Take a ride on the Goa Palace Express to the Goa Palace.
    5. Explore the old part of the city, including the Victoria Memorial, the T. S. C. B. Building, and the old railway station.

    **Day 2: Exploring Bangalore's Downtown and Outside the City**

    1. Visit the famous B. L. Brodie Centre for the Arts, located on the southern side of the city, which houses the B. L. Brodie Centre for the Arts and Art Gallery.
    2. Take a stroll along the Bangalore City Walk, a beautiful public promenade that runs along the southern and eastern sides of the city.
    3. Visit the Science City and the Goa Palace on the way.
    4. Explore the popular food and nightlife areas of Bangalore, such as the Science City, the Goa Palace, and the Bangalore City Market.

    **Day 3: Visiting Other Attractions and Exploring Bangalore's Backwaters**

    1. Visit the Goa Palace for a picnic or take a photo with the statue of the goddess.
    2. Visit the nearby Vrindavan district, which is known for its serene lakes, waterfalls, and picturesque villages.
    3. Explore the nearby Chittor Fort, a 600-year-old fort that is famous for its intricate carvings and the surrounding gardens.
    4. Visit the Vrindavan Hills, a nature reserve with beautiful hills, lakes, and waterfalls.

    **Day 4: Day Trip to Mysore**

    1. Take a day trip to the nearby Mysore Palace and the Chitti Hills.
    2. Take a ride on the Mysore Palace Express and enjoy the views of the palace from the top.
    3. Visit the nearby Fort William and the Chitti Hills, and enjoy the scenery.

    **Day 5: Visiting the National Museum and Other Off-Tracks**

    1. Visit the National Museum, which is known for its excellent art and artifacts.
    2. Take a ride on the Goa Palace Express and visit the nearby Goa Palace.
    3. Visit the nearby Goa Palace, which is known for its intricate carvings and the surrounding gardens.        
    4. Take a stroll in the nearby Goa Palace, and enjoy the views of the palace from the top.

    **Day 6: Return to the Airport**

    1. Depart from the Bangalore International Airport.

    This is a suggested itinerary, and you can adjust it based on your personal preferences and the time of year you visit.

"""
