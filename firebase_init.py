import firebase_admin
from firebase_admin import credentials
import requests
import json

presigned_url = "https://health-file.s3.us-east-2.amazonaws.com/final2.json?response-content-disposition=inline&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLWVhc3QtMiJGMEQCIF3ERMVTShJVrrS3WIgPiiNvhvJdxbGQq0FQlag8wNbYAiAfXS1i6ETSm0LDFylk95VsiowWbvH1%2BOw2aat3x2v3pSrUAwjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDU0NTAwOTg1ODc5NyIM30iJj7VMv19hiUtlKqgDJ%2BXxw5w37p1dCUzxSSexyF8kCfHPTdDMr1erCIZw8midXV6YHqIkEytQpWohTimSshnBWthnDma%2BmPugJTMhGkaL7I%2FWNUJC3KtxJRPBcICtKkSmx%2FM%2BDaPh4kli0NlhDfRWwHGNmznfGQYyGW4yLUm1qiSBSQ5xQRscxo3I0ISyx4CmESTfy4M8hOGDIkggD6quqgQFYScvyPiQ851x4mlA1jSzBSxRzloClskK2fy7JzuYQptoArlRtxpEVfTkILLxQ46iR6BoTj7LBJkeBq9%2BntEObB1i%2FtP%2B0httEi73i9ewgTr1dsSLDw2NNUlNxMNDNGnDKI5RylpFOGwTdwA4hCjzIhAdinawNS3XgMXuFB%2Bxec%2FLaX0q%2FwIwZZO36HwjPpUvk%2F46hEPHko8nUODsS31TbZCISCuceJM6JnV40Ag3t9ox05pCDVCz4lNckQ4HVMGy9kzTz%2FXx0LrpbWmgheU7%2FqcvcRWlbih%2BVUNmIhunBXb35B7Vy0hdbGpHxICFhKIgdh2N4iO1rBt8ZbxOofTeQaLz2jFvWoYBqGIijLIqkxae2zCh5bi6BjrlAqiyDRhXjujWf%2BhT8cXzjDH9nfzBZ7yKbzzy5yHzSmqT2lyubI495S%2BDmYU1soERdvcDm7HmeOHQOQFqt0pLT4pbZiiH0rDyTgsL7B4BV9zWoHOy1HF21TWD%2FGjKSIKTOJEyinRhAYMP29VW8K%2Fc04C5OjCEu6mS1ZgJ4r21x0ACdNOD%2BIcBQYi4aul%2FP%2BRwL%2F%2B5Q3Kvw6iqhxdtZzWbAGNCVF1hS1goQTKVGCcOnAtAjZpiHv%2Bnub2ADWYH3seiDfYAISHS8kG0TdT4fZx2BmhDuzye6IZq4J7zPdaBhX9QRxtsyJf22LngYPacMZaZjRoWF3lc3txQem8dtmmkUAQ08EyFQPu3uo1pAqapQSG2Ms9%2Byp5QVL%2BwRhjYkE3tPLPLzRH%2FG34gYiUccJQ%2BKJQGlcNnZiGTS4ESjhDBBf%2FXnMfvz2Neb3ZzUx%2FunMqUZ4NB2wdzbH7WA3UK8an%2BrLQ9FunKTw%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAX5ZI6PDW6LHHNGIW%2F20241202%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20241202T231035Z&X-Amz-Expires=43200&X-Amz-SignedHeaders=host&X-Amz-Signature=c00db2a27626ea8a8232286ef8b8dac39884830ed127c6abf3beb4604d37f326"
response = requests.get(presigned_url)
firebase_credentials = response.json()

def initialize_firebase():
    if not firebase_admin._apps:
        # Step 2: Pass the loaded JSON content to Firebase credentials
        cred = credentials.Certificate(firebase_credentials)  # Dynamically loaded credentials
        firebase_admin.initialize_app(cred, name='health')  # Initialize the Firebase app
        # Get Firestore database reference
        print("Firebase Successfully Intilized")