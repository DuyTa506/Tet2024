import requests


def download_image(url, save_path):
    """
    Save an image to path from a URL
    :param url: the URL of the image
    :param save_path: the path to save the image
    :return: None
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"Image {save_path} downloaded successfully!\n")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")