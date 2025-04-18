from tqdm import tqdm
import requests
import os


class AirKoreaPy:
    def __init__(self):
        self.year = None
        self.file_id = '1657eebba9237'
        self.base_url = "https://www.airkorea.or.kr/jfile/readDownloadFile.do"
        self.headers = {
            'User-Agent': 'Mozilla/5.0'
        }
        self.folder_path = 'data/airkorea'
        self.file_path = None
        self.file_name = 'airkorea_{year}_data.xlsx'

    def set_env(self, year):
        self.filename = self.file_name.format(year=year)
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
        self.file_path = os.path.join(self.folder_path, self.filename)

    def download_fixed_data(self, year):
        self.set_env(year)
        self.year = year
        params = {
            'fileId': self.file_id,
            'fileSeq': str(year)[2:],
        }
        download_url = (
            f"{self.base_url}?fileId={params['fileId']}"
            f"&fileSeq={params['fileSeq']}"
        )

        with requests.get(
                download_url,
                headers=self.headers,
                stream=True) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            block_size = 1024  # 1KB
            t = tqdm(total=total_size, unit='iB', unit_scale=True)

            # with open(file_name, 'wb') as f:
            with open(self.file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=block_size):
                    if chunk:
                        f.write(chunk)
                        t.update(len(chunk))
            t.close()


if __name__ == "__main__":
    akc = AirKoreaPy()
    akc.download_fixed_data(year=2024)
