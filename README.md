1. What was the theme you chose?

The theme that I chose for this project is Indian food. I live in Nepal, located in South Asia and wanted everyone to know some cuisine.


2. How did you pick your searches to fit the theme?

I picked three API from Spoonacular to get the Indian cuisine and display the ingredients. One twitter search API to display indian cuisine tweets.

3. What are at least 3 issues you encountered with your project? How did you fix them?

First problem, getting the right values from json. 

solution: I was lost for a moment to get what I wanted from JSON, with trial and error, eventually I understood how to make it work.

Second problem was with requests_oauthlib ,and deploying Heroku as it didn't work.

solution: I had to use pip3 instead of pip and for Heroku, I had to remove os from requirements.txt.

Third problem was with displaying ingredients. It showed up as list.

solution: I had to create an empty string and change the list to string.

4. What are known problems, if any, with your project?

There are no known problems, I will update if any is seen in future. However there is a limit of how many time you can refresh the website due to Spoonacular daily limit.

5. What would you do to improve your project in the future?

I wished to have a (/) link that would ask user to enter a cuisine name and then based on the input, my website would display the cuisine to (/display) the user by their choice. But due to time constraint and I wasn't able to implement it. I look forward to doing that as a side project.
