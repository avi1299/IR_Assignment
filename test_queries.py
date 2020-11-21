from query_processer import search

# Taking query input
query = input("Type the query: ")
result = search(query, open_web=False, use_zones=False, enable_query_relaxation=False)
print(result)
# search(query, open_web=False, use_zones=True)
