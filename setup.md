```sh
/home/shardul.junagade/miniconda3/bin/conda create --name striprcnn python=3.8 -y
source /home/shardul.junagade/miniconda3/bin/activate striprcnn
conda install pytorch==1.8.0 torchvision==0.9.0 cudatoolkit=10.2 -c pytorch
pip install -U openmim
mim install mmcv-full
mim install mmdet
git clone https://github.com/YXB-NKU/Strip-R-CNN.git
cd Strip-R-CNN
# pip install -r requirements.txt       # worked for me
pip install -v -e .
```