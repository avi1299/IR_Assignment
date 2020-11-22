from query_processer import search

# Taking query input
query = input("Type the query: ")
search(query, open_web=False, use_zones=False, enable_query_relaxation=False)
print('\n')
search(query, open_web=False, use_zones=False, enable_query_relaxation=2)
