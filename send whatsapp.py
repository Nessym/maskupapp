from twilio.rest import Client
account_sid = 's_id here' 
auth_token = 'auth_token here'


# In[32]:


client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='whatsapp:twilio sandbox number here', 
                              //Whatsapp alert message containing picture of students improperly wearing masks and not weaaring masks
                              body='Mask Up App Alert!!! \n Student is entering without a face mask. \n See in camera to recognize student. \n Please advise to Mask Up!!',
                              media_url = 'http://6f470b37db77.ngrok.io/.jpeg',
                         
                              to='whatsapp:put your phone number here'
                              )
                              





