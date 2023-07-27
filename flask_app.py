import openai
from flask import Flask, request, render_template,jsonify
from llama_index import load_index_from_storage,StorageContext
openai.api_key = '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'
app = Flask(__name__)

storage_context = StorageContext.from_defaults(persist_dir="vectorstoreindex")
loaded_index = load_index_from_storage(storage_context=storage_context)
query_engine = loaded_index.as_query_engine()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    prompt = request.form.get('user_input')

    prediction = query_engine.query(prompt)

    return jsonify({'prediction': str(prediction)})


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
