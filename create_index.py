import faiss
from pathlib import Path
import open_clip
from PIL import Image
import torch
import torch.nn.functional as F
import json

model_name = "ViT-B-16-SigLIP-512"
model, _, preprocess = open_clip.create_model_and_transforms(
    model_name,
    pretrained="model/open_clip_pytorch_model.bin",
)

output_dim = model.text.output_dim
index = faiss.IndexFlatIP(output_dim)

image_paths = list(Path("images").rglob("*.jpg"))
images = [Image.open(image_path) for image_path in image_paths]
images = [preprocess(image) for image in images]
images = torch.stack(images)

with torch.no_grad():
    image_embeddings = model.encode_image(images)
    image_embeddings = F.normalize(image_embeddings, p=2, dim=-1)

index.add(image_embeddings)
faiss.write_index(index, "docker/index.faiss")
with Path("docker/mapping.json").open("w") as f:
    json.dump([str(image_path) for image_path in image_paths], f)
