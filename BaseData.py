import os

def download_files_from_website(base_url, path_to_save):
    os.makedirs(path_to_save, exist_ok=True)
    os.system(f'wget -P "{path_to_save}" -E -H -k -K -p -r -l inf -np -nH --cut-dirs=1 '
              f'--convert-links --random-wait --wait=2 --limit-rate=500k --adjust-extension '
              f'--no-check-certificate --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36" '
              f'-e robots=off "{base_url}"')

base_url = "https://negociowin.ru/xxx/newnegocio"
path_to_save = os.getcwd() 

download_files_from_website(base_url, path_to_save)
