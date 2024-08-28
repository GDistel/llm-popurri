def clean_sql_query_fn(query):
    """
    The result from create_sql_query_chain is prefixed with "SQLQuery: "
    whereas it should be just the actual SQL query (see https://github.com/langchain-ai/langchain/issues/12077)
    """
    remove_markdown_sql_starts = ("```sql", "")
    remove_markdown_sql_ends = ("```", "")
    remove_sql_colon = ("SQLQuery: ", "")
    cleaned_query = query.replace(*remove_markdown_sql_starts).replace(*remove_markdown_sql_ends).replace(*remove_sql_colon).strip()
    return cleaned_query