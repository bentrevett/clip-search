from flask import Flask, request, jsonify
import open_clip

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    data = request.get_json()
    text = data["text"]
    tokenizer = open_clip.tokenizer.HFTokenizer("model")
    tokens = tokenizer(text, context_length=64)
    tokens_str = tokenizer.tokenizer.tokenize(text)
    model_name = "ViT-B-16-SigLIP-512"
    model, _, preprocess = open_clip.create_model_and_transforms(
        model_name,
        pretrained="model/open_clip_pytorch_model.bin",
    )
    value = model.encode_text(tokens).mean().item()
    return jsonify(tokens=tokens_str, value=value)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
