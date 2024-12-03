import firebase_admin
from firebase_admin import credentials
import requests
import json



def initialize_firebase():
    presigned_url = "https://health-file.s3.us-east-2.amazonaws.com/final2.json?response-content-disposition=inline&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLWVhc3QtMiJGMEQCICYw8LzGnskvGOLOZ3stVBNqLeOa6OiMpbMMAhaRd06AAiB3TafoPDy0IWyNAVdTY%2Bx9L%2BhuHSXYA0jfNcsx%2B9YhlCrUAwjV%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDU0NTAwOTg1ODc5NyIM%2FNUJjtYZi93ncmquKqgD9MhAmBjCBQWblVWGGC4NvmzYS7UmbyH0hh81tSgxvvSUhsvZWaOcYPo%2FSgn44zNLlqRrxnq3KSsc70VX7zMB3UiZUrD5Aa3Yj2XHr%2BDCw5JpDsEwof25ZvcHXZBQqY%2FL6YNQY8WVKtSS5ILpglperMR7N8xpeV8abgHOQahTGE3vWBxKJsZu4CPtHT2EnB5stAdb3CUkUtuxTUJMhNMK0vwPIxrqILWSqvp6YI3RbhUnZRhS3MMQn70eOMaBsoUaV3PBSlkkTN%2Bmn%2BUwKRGdRrsGkNx1Z4Ay1B5ZhHgcqvuKzC0d36jOczWdo%2FhLhgAcrLa0UxSlG1NiKKkiay4Zw93Difm2Wdrl9CkAE2S9K7N5mMaFekS%2BKW6rRNELcPHlZtG8iki0MPVgIznHNDCSBKOXGlzqZX37Ry%2BiZXE68jmkZYfVgqc%2Bw1jeonFGpLeu4TCGEfe3IswFe48KEAxFnlT8ufeRQr7hxgc1EI9DgoshZu%2F%2FTbzBned3dNzCSVrcQDUZ6K3GmiSjuRhy2tmhY0dZZa6KeT8g9xTDlXaOR320qpizhKC0yjDa4bu6BjrlAhI1oE1xDnhPAux3X8UVVrUQHLRBD1tUqzApjHFYGh2uonmIH%2FyK7z2ygEYzZY7CxM1qc1RGlyVDEWfuL4JBVDq3OQ3u5ceDYZ61piZ2RafbDnumymVAv7MqPeUAXR9ki9zYo1pR%2BtXyhA2VykV7VGDPPGS2D7X4TAghZS%2BDeBWDOyj%2Fd70PtiSlQqoCD6UNE6Uzcmjw7NuMKDCEKGUU61q2sIAkmhPDTT906VzXgTykv1zyWoZORy%2BpnI3NgDkl7cGD%2FyzzpICCeSbA4GdR7Z7B9qFpRPY%2Bj7SqrNdzkvJ5QOzPAhLtKZhohgZjnDgSjOvvDmEudpNqb3Wgv7L2HmrE0RxsrPhmJ6P5d7UXCxPZmDSmevNx6p%2F49MnIom5CzKvcbaC7NdEP8OFm0w%2BJhsEaNFsF9Jt%2Bh30MunIMjWqSUK8T2vh%2F11cLk6DiO5u4KcpC0ygL5r9PVmB8yljDejqyrwM3XQ%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAX5ZI6PDWS7KM6GNZ%2F20241203%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20241203T115417Z&X-Amz-Expires=43200&X-Amz-SignedHeaders=host&X-Amz-Signature=9286d11fe346960b4c0705a5923ccd88bcac7d992794eee86c936ed7daf8b032"  
    response = requests.get(presigned_url)
    firebase_credentials = response.json()

    if not firebase_admin._apps:
        # Step 2: Pass the loaded JSON content to Firebase credentials
        cred = credentials.Certificate(firebase_credentials)  # Dynamically loaded credentials
        firebase_admin.initialize_app(cred)  # Initialize the Firebase app
        # Get Firestore database reference
        print("Firebase Successfully Intilized")
    else :
        print("Firebase not intialized")