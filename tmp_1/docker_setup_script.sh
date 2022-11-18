apt-get update
apt-get install ffmpeg libsm6 libxext6  -y

# here should be installed allegroai
pip3 install torch==1.11.0+cu113 --extra-index-url https://download.pytorch.org/whl/cu113