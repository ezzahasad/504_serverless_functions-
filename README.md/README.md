**Google Cloud (GCP) Function Deployment- Potassium Classifier**
The severless function was deployed on Google Cloud Run (2nd generation) in the us-central1 region using the Flask framework and Python 3.12. The function runs on Google's fully managed severeless infrastructure, which automatically scales with demand. This function acceps JSON input contain a potassium value and classified the levels as normal or abnormal based on clinical reference ranges. Authentiction was configured as unauthenticated to enable open HTTP requests for demonstration purposes. 

**Deployment Instructions:**
All steps were performed in the Google Cloud Shell using the gcloud command-line interface. The function was deployed to Cloud Run under the project ezzahahi2025. The necessary files including (main.py) and (requirements.txt) were organized inside the gcp/ folder of the repo. Then, the command gcloud functions deploy potassium-classifier --gen2 --region=us-central1 --runtime=python312 --source=. --entry-point=potassium_classifier --trigger-http --allow-unauthenticated was used to deploy the function, package the source files, upload them to Cloud Run, and create a public HTTP endpoint. Google cloud managed the environment setup, installed all necessary dependencies, and generated the container image. After deployment, there was confirmation of the creation of the function and also a generated public URL for testing annd confirming that the function's entry point (potassium_classifier) was accurately recognized. Thus, the deployment logs verified all dependencies are installed without errors.

**Lab Rule and Citation**
Lab test: Serum Potassium (K+)
Normal Range: 3.5-5.0 mmol/L
Rule Implemented:
If potassium < 3.5 -> Abnormal (low)
If potassium > 5.0 -> Abnormal (high)
Otherwise -> Normal
Citation: Sur M, Mohiuddin SS. Potassium. [Updated 2024 Oct 5]. In: StatPearls [Internet]. Treasure Island (FL): StatPearls Publishing; 2025 Jan-. Available from: https://www.ncbi.nlm.nih.gov/books/NBK539791/?utm_source=chatgpt.com
 

**Demonstration of Deployment and Output**

![cloud_shell_deployment](screenshots/gcp_cloud_shell.png)
This screenshot captures the results of running the sucesss deployment of the potassum-classifier function using the gcloud command-line interface (CLI) within the Google Cloud Shell. The function is being deployed to the Cloud Run (2nd generation), confirming it ran in Python 3.12 in the us-central region. It also displays the public endpoint URL generated, further confriming the function was created successfully and is accessible. 

![GCP_service_list](screenshots/gcp_service_list.png)
This screenshot shows that under Cloud Run services, the function potassium-classifier was deployed. This confirmed the deploymnet type (Function), the region (us-central1), and authentication access (public). 

![GCP_service_details](screenshots/gcp_service_details.png)
This screenshot shows the configurations (runtime, scarling, Functions Framework) and confirms that the internal settings are accurate and correct. 

![gcp_trigger](screenshots/gcp_trigger_url.png)
This screenshot displays the public endpoint URL as well as the trigger type, confriming the accessibility and the authentication settings. 

![gcp_test_output](screenshots/gcp_test_output.png)
This screenshot shows the request for a real test and the correct JSON response. This demonstrated and confrimed that the function was working. 

![gcp_logs](screenshots/gcp_logs_success.png)
This screenshot captures all of the logs confirming all of the successful requests (POST 200) and is the final validation that proves its runtime activity and success. 

**Public Endpoint and Authentication**
The deployed function's public endpoint:
https://us-central1-ezzahahi2025.cloudfunctions.net/potassium-classifier
As mentioned previously, authentication was set to unauthenticated, which allows anyone to send POST requests without an API key. By doing so, this will make the function publicly accessible for demonstration purposes. 

**Example Request and Response**
A POST request was used to test the function with JSON input containing a potassium value using the command  curl -X POST https://us-central1-ezzahahi2025.cloudfunctions.net/potassium-classifier -H "Content-Type: application/json" -d '{"potassium": 4.2}'. The response output was  { "potassium": 4.2, "status": "normal", "category": "Normal (3.5–5.0 mmol/L)" } Values outside this range, such as 5.4, return "status": "abnormal" as expected, confirming the implemented rules were reflected. 

**Validation of Results**
The function's classification results aligned with the reference range defined by StatPerals (NCBI Bookshelf,2024) since it states that normal serum potassium levels fall between 3.5 and 5.0 mmol/L, When tested with the potassium value of 4.2 mmol/L, the function correctly responded with "Normal", which supported our rule and clinical standards. 