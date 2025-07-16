import json

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def update_translation(en_data, ja_data, todo_suffix=" [TODO 翻訳]"):
    updated_ja = ja_data.copy()

    for key, en_value in en_data.items():
        if key in ja_data:
            updated_ja[key] = ja_data[key]
        else:
            updated_ja[key] = f"{en_value}{todo_suffix}"

    return updated_ja

if __name__ == "__main__":
    en = load_json("en.json")
    ja = load_json("ja.json")
    updated_ja = update_translation(en, ja)
    save_json("ja.updated.json", updated_ja)
    print("✅ ja.updated.json を生成しました。翻訳抜けは [TODO 翻訳] でマーク済みです。")

