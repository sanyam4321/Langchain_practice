import random

class SampleLLM:
    def __init__(self):
        print("LLM created")

    def predict(self, prompt):
        response_list = [
            'delhi is the capital of india',
            'ipl is a popular cricket league',
            'AI stands for artificial intelligence'
        ]

        return {'response': random.choice(response_list)}
    

class SamplePromptTemplate:
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables
    
    def format(self, input_dict):
        return self.template.format(**input_dict)

class SampleLLMChain:
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt
    
    def run(self, input_dict):

        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)
        return result['response']

      
        
template = SamplePromptTemplate(
    template='Write a {length} poem about a {topic}',
    input_variables=['length', 'topic']
)

llm = SampleLLM()


chain = SampleLLMChain(llm, template)
print(chain.run({'length': 'short', 'topic': 'india'}))
