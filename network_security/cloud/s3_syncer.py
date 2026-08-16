import subprocess
import os

class S3Sync:
    def sync_folder_to_s3(self, folder, aws_bucket_url):
        if not os.path.exists(folder):
            raise ValueError(f"Folder does not exist: {folder}")
        
        try:
            result = subprocess.run(
                ["aws", "s3", "sync", folder, aws_bucket_url],
                check=True,
                capture_output=True,
                text=True
            )
            return result.returncode == 0
        except subprocess.CalledProcessError as e:
            raise Exception(f"S3 sync failed: {e.stderr}")

    def sync_folder_from_s3(self, folder, aws_bucket_url):
        os.makedirs(folder, exist_ok=True)
        
        try:
            result = subprocess.run(
                ["aws", "s3", "sync", aws_bucket_url, folder],
                check=True,
                capture_output=True,
                text=True
            )
            return result.returncode == 0
        except subprocess.CalledProcessError as e:
            raise Exception(f"S3 sync failed: {e.stderr}")