import requests
extension = ".jpg"
images = {"fenugreek" : "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/2017_0102_fenugreek_seeds.jpg/220px-2017_0102_fenugreek_seeds.jpg", 
          "mango" : "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Mangoes_pic.jpg/220px-Mangoes_pic.jpg", 
          "aubergine" : "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Solanum_melongena_24_08_2012_%281%29.JPG/220px-Solanum_melongena_24_08_2012_%281%29.JPG",
          "lantana" : "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/LantanaFlowerLeaves.jpg/220px-LantanaFlowerLeaves.jpg"
         }

n = len(images.keys())
i = 1
for image_name in images:
    print("image {} of {}".format(i, n))
    with open(image_name + extension, 'wb') as handle:
        print("", "trying to download", image_name, "image...........")
        image_url = images[image_name]
        response = requests.get(image_url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
        print("downloaded successfully\n\n")
        i += 1
