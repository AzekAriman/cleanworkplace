import requests
from requests.auth import HTTPDigestAuth
from PIL import Image
import io

# url = "http://45.138.163.92:7502/cameras"
# username = "test"
# password = "Rtest3"
# response = requests.get(url, auth=HTTPDigestAuth(username, password))
# if response.status_code == 200:
#     # Access the response content or save it to a file
#     content = response.content
#     print(content)
#
# else:
#     print("Failed to access the URL:", response.status_code)


params = {
    "keep_aspect_ratio": 1,
    "resolution": "640x480"
}

headers = {
    "Accept": "image/*"
}
# 0 1 2 3 9 11 12 13 14 15
url = "http://45.138.163.92:7502/cameras/0/image"
username = "test"
password = "Rtest3"

response = requests.get(url, auth=HTTPDigestAuth(username, password), params=params, headers=headers)

if response.status_code == 200:
    # Access the image content or save it to a file
    image_content = response.content

    # Create an image object from the binary data
    image = Image.open(io.BytesIO(image_content))

    # Display the image
    image.show()

    # Save the image to a file
    image.save("image.jpg")
    # Do whatever you want with the image content
else:
    print("Failed to access the image:", response.status_code)
