import requests
extension = ".jpg"
images = {"fenugreek" : "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Lantana-Violet.jpg/220px-Lantana-Violet.jpg", 
          "mango" : "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Lantana-Violet.jpg/220px-Lantana-Violet.jpg", 
          "aubergine" : "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Lantana-Violet.jpg/220px-Lantana-Violet.jpg",
          "lantana" : "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Lantana-Violet.jpg/220px-Lantana-Violet.jpg"
         }


for image_name in images:
    with open(image_name + extension, 'wb') as handle:
        image_url = images[image_name]
        response = requests.get(image_url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
