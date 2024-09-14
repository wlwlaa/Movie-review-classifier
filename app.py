import gradio as gr
import torch
from transformers import AutoTokenizer

from model import DistilBertClass


model = DistilBertClass()
model.load_state_dict(torch.load('models/model_7000_Loss_0.09370.pth', weights_only=True, map_location=torch.device('cpu')))
tokenizer = AutoTokenizer.from_pretrained('distilbert/distilbert-base-uncased-finetuned-sst-2-english', do_lower_case=True)


def get_score(pred):
    pred += 1
    if pred >= 5:
        pred += 2
    return pred


def predict(review):
    review_tokenized = tokenizer(review, truncation=True, padding=True, return_tensors='pt')
    review_tokenized['token_type_ids'] = None

    model.eval()
    with torch.inference_mode():
        output = model(**review_tokenized)
    
    output = output.softmax(dim=1).squeeze()
    pred = output.argmax(dim=0).item()
    score = get_score(pred)

    if score == 4 or score == 7 and output[pred] < 0.6:
        return 'This review is most likely neutral'
    else:
        return f'This review is negative. Possible review rating: {score}/10' if score <= 4 else f'This review is positive. Possible review rating: {score}/10'

    
gr.Interface(
    fn=predict,
    inputs=['text'],
    outputs='text'
).launch()