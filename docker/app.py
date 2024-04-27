from flask import Flask, request, jsonify
from flask_cors import CORS
import open_clip
import torch
import torch.nn.functional as F
import faiss
import json

app = Flask(__name__)
CORS(app)


@app.route("/lookup", methods=["POST"])
def lookup():
    data = request.get_json()
    text = data["text"]
    tokenizer = open_clip.tokenizer.HFTokenizer("model")
    tokens = tokenizer(text, context_length=64)
    model_name = "ViT-B-16-SigLIP-512"
    model, _, preprocess = open_clip.create_model_and_transforms(
        model_name,
        pretrained="model/open_clip_pytorch_model.bin",
    )
    with torch.no_grad():
        text_embedding = model.encode_text(tokens)
        text_embedding = F.normalize(text_embedding, p=2, dim=-1)
    index = faiss.read_index("index.faiss")
    similarity, items = index.search(text_embedding, index.ntotal)
    similarity = similarity[0].tolist()
    items = items[0].tolist()
    with open("mapping.json") as f:
        mapping = json.load(f)
    image_paths = [mapping[item] for item in items]
    return jsonify(
        similarity=similarity,
        imagePaths=image_paths,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
