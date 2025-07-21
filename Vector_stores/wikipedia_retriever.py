from langchain_community.retrievers import WikipediaRetriever

# retriever is a runnable
# returns output as LangChain Document Objects
retriever = WikipediaRetriever(top_k_results='2', lang='en')

query = 'how black holes were discovered'
docs = retriever.invoke(query)

for i, doc in enumerate(docs):
    print(f"---Result {i+1}---")
    print(doc.page_content)