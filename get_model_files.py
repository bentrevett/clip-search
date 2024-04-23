from huggingface_hub import hf_hub_download
import open_clip
import shutil
import os

repo_id = "timm/ViT-B-16-SigLIP-512"
open_clip_repo_id = f"hf-hub:{repo_id}"

model, preprocess = open_clip.create_model_from_pretrained(open_clip_repo_id)
tokenizer = open_clip.get_tokenizer(open_clip_repo_id)

file_names = [
    "open_clip_config.json",
    "open_clip_pytorch_model.bin",
    "special_tokens_map.json",
    "tokenizer.json",
    "tokenizer_config.json",
]

model_dir = "model"
for file_name in file_names:
    src_path = hf_hub_download(repo_id, file_name)
    dst_path = os.path.join(model_dir, file_name)
    dst_dir = os.path.dirname(dst_path)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    shutil.copy(src_path, dst_path)
