# py-fastapi-facebook-webhook
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Basic template for starting facebook chatbot app service, using FastAPI.
FastAPI provides high performance and perfect tools for developing a small Async 
web server.


### Requirements
* Facebook App.
* Facebook Page.
* Google App Engine Service [Optional].

### Deployment [Google App Engine]
Google App Engine is not must, can be deployed on Amazon and Azure too. however
I attached an app.yaml file which make your life easier deploying the project 
on GAE.

#### Deploy The Service On GAE:
* [SetUp gcloud console](https://cloud.google.com/functions/docs/quickstart)
* Go to the app.yaml directory.
* run `gcloud app deploy`
#### Setup Facebook App:  
* Generate access token for your page.
* Set the **PAGE_ACCESS_TOKEN* value at the **app.yaml** file to be the access
token that was generated at the step above.
* Go to your Facebook App.
* Sidebar -> Webhooks -> Edit Page Subscription.
    * At the callback URL field add your service url.  
    * At the Verify Token field add the value that you set for **VERIFY_TOKEN** 
    at the **app.yaml** file.


### API DOC 
Also Available on {service_uri}/docs. 
<table>
    <thead>
        <tr>
            <th>Endpoint</th>
            <th>Method</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=4>/api/webhook</td>
            <td>GET</td>
            <td>Verifies the endpoint and returns the "hub.challenge" query parameter back as an echo on success.</td>
        </tr>
        <tr>
            <td rowspan=2>POST</td>
            <td>Handling messages</td>
        </tr>
    </tbody>
</table>


### Debug
* Install [ngrok](https://ngrok.com/).
* Expose your local service running `ngrok http 8000`
* Use the protected uri as a callback URL at your app configuration.
