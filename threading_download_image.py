from concurrent.futures import ThreadPoolExecutor ,as_completed 
import requests
from threading import Thread 
images = [
    "https://plus.unsplash.com/premium_photo-1668241683684-c65571f89df2",
    "https://images.unsplash.com/photo-1490730141103-6cac27aaab94",
    "https://images.unsplash.com/photo-1501183007986-d0d080b147f9"
]

def download_image(url:str):
    *file, name = url.split("/")
    image_bytes = requests.get(url=url).content 
    with open(f"{name}.jpg","wb") as file:
        file.write(image_bytes)
    return f"downloaded : {url}"


# with  ThreadPoolExecutor(max_workers=10) as executor:
#     # results = executor.map(download_image,images)
#     # for res in results :
#     #     print(res)
    
#     results = [executor.submit(download_image,image)  for image in images]
#     for res in as_completed(results) :
#         print(res.result())

for image in images :
    t = Thread(target=download_image,args=[image])
    t.start()

print("code ends ................")