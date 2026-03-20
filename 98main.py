import multiprocessing
import requests

def downloadFile(url, name):
    print(f"Started Downloading File_{name}.jpg")
    response = requests.get(url)
    
    with open(f"File_{name}.jpg", "wb") as f:
        f.write(response.content)

    print(f"Finished Downloading File_{name}.jpg")


if __name__ == "__main__":

    url = "https://picsum.photos/200/300"
    pros = []

    for i in range(5):
        p = multiprocessing.Process(target=downloadFile, args=(url, i))
        p.start()
        pros.append(p)

    # wait for all processes to finish
    for p in pros:
        p.join()

    print("All files downloaded successfully")