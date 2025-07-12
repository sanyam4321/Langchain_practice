import random
from abc import ABC, abstractmethod

class Runnable(ABC):

    @abstractmethod
    def invoke(input_data):
        pass


class SampleLLM(Runnable):
    def __init__(self):
        print("LLM created")

    def predict(self, prompt):
        response_list = [
            'delhi is the capital of india',
            'ipl is a popular cricket league',
            'AI stands for artificial intelligence'
        ]

        return {'response': random.choice(response_list)}
    
    def invoke(self, prompt):
        response_list = [
            'delhi is the capital of india',
            'ipl is a popular cricket league',
            'AI stands for artificial intelligence'
        ]

        return {'response': random.choice(response_list)}
    

class SamplePromptTemplate(Runnable):
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables
    
    def format(self, input_dict):
        return self.template.format(**input_dict)
    
    def invoke(self, input_dict):
        return self.template.format(**input_dict)

class SampleLLMChain:
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt
    
    def run(self, input_dict):

        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)
        return result['response']

class SampleStrOutputParser(Runnable):

    def __init__(self):
        pass

    def invoke(self, input_data):
        return input_data['response']     

class RunnableConnector(Runnable):
    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):
        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)
        return input_data
    

        
template = SamplePromptTemplate(
    template='Write a {length} poem about a {topic}',
    input_variables=['length', 'topic']
)

llm = SampleLLM()
parser = SampleStrOutputParser()

chain = RunnableConnector([template, llm, parser])
print(chain.invoke({
    'length': 'long',
    'topic': 'delhi'
}))

