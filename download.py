#模型下载（这一步需要记录下载的位置）
from modelscope import snapshot_download
model_dir = snapshot_download('Qwen/Qwen2.5-VL-7B-Instruct')
