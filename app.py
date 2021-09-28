from flask import Flask,jsonify,request


app= Flask(__name__)

stores = [
    {
        'quiz': 'kahoot 2',
        'items': [
            {
                'question': 'Which car company uses the tagline "The ultimate driving machine"?',
                'answer': 'BMW'
            }
        ]
    },
    {
        'quiz': 'kahoot 2',
        'items': [
            {
                'question': 'What is Toyatas luxury division called?',
                'answer': 'Lexus'
            }
        ]
    },
    {
        'quiz': 'kahoot 2',
        'items': [
            {
                'question': 'What does BMW stand for?',
                'answer': 'Bavarian Motor Works'
            }
        ]
    },
    {
        'quiz': 'kahoot 2',
        'items': [
            {
                'question': 'Which race car is known as the widow maker?',
                'answer': 'Porsche 917'
            }
        ]
    },
     {
        'quiz': 'kahoot 2',
        'items': [
            {
                'question': 'Which iconic car manufacturer also made airplane engines?',
                'answer':' Rolls Royce'
            }
        ]
    }
    
    

    

]
@app.route('/')
def home():
    return "Hello to Api"


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'quiz': request_data['quiz'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store_name(quiz):
    for store in stores:
        if(store['quiz'] == quiz):
            return jsonify(store)
    return jsonify({'message': 'store not found'})


@app.route('/store')
def get_all_store_name():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(quiz):
    request_data = request.get_json()
    for store in stores:
        if(store['quiz'] == quiz):
            new_item = {
                'quiz': request_data['quiz'],
                'answer': request_data['answer']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})


@app.route('/store/<string:name>/item')
def get_store_item(quiz):
    for store in stores:
        if(store['quiz'] == quiz):
            return jsonify(store['items'])
    return jsonify({'message': 'store not found'})


app.run()