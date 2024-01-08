from transformers import GPT2LMHeadModel, GPT2Tokenizer

def load_gpt2_model():
    model_name = "gpt2"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    return model, tokenizer

def generate_response(model, tokenizer, user_input):
    prompt = f"User: {user_input} Chatbot:"
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    pad_token_id = tokenizer.eos_token_id
    attention_mask = input_ids.ne(pad_token_id).float()

    output = model.generate(input_ids, attention_mask=attention_mask, max_length=50, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7, do_sample=True)
    
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

def main():
    model, tokenizer = load_gpt2_model()

    input=""

    response = generate_response(model, tokenizer, input)
    print(f"{response}")

if __name__ == "__main__":
    main()